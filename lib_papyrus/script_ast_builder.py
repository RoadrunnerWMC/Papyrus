import ast as python_ast
import dataclasses
import functools
from pathlib import Path
from typing import Any, List

USE_STANDALONE = False

if USE_STANDALONE:
    from .parser.papyrus_parser_standalone import Lark_StandAlone, Indenter, Transformer
else:
    from lark import Lark, Transformer, Tree, Token
    from lark.visitors import Discard
    from lark.indenter import Indenter
    from lark.tree import Meta

from . import script_ast


def convert_dataclass_to_subclass(instance: dataclasses.dataclass, subclass: type) -> dataclasses.dataclass:
    """
    Convert a dataclass instance to an instance of some subclass of its type
    """
    # NOTE: we can't use dataclasses.asdict() because it's recursive
    d = {}
    for field in dataclasses.fields(instance):
        d[field.name] = getattr(instance, field.name)

    return subclass(**d)


class PapyrusIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4


def do_discard() -> Discard:
    """
    Either return or raise Discard (to smooth over a recent Lark API change)
    """
    # This is a really dumb way of detecting it, but I don't know how else
    try:
        issubclass(Discard, Exception)
        # <= 0.12.0
        raise Discard
    except TypeError:
        # > 0.12.0
        return Discard


def filter_none(f):
    @functools.wraps(f)
    def wrapper(self, data: List[Any]) -> List[Any]:
        return f(self, [x for x in data if x is not None])

    return wrapper


def passthrough(self, data: Any) -> Any:
    return data


class PapyrusTransformer(Transformer):

    @filter_none
    def statements(self, data: List[Any]) -> List[script_ast.ASTStatement]:
        return data

    @filter_none
    def single_line_statement(self, data: List[Any]) -> script_ast.ASTSingleLineStatement:
        if not data:
            return do_discard()

        line = data[0]
        if line is None:  # (blank line)
            return None
        elif isinstance(line, script_ast.ASTSetLine):
            return convert_dataclass_to_subclass(line, script_ast.ASTSetStatement)
        elif isinstance(line, script_ast.ASTDeleteLine):
            return convert_dataclass_to_subclass(line, script_ast.ASTDeleteStatement)
        elif isinstance(line, script_ast.ASTRunLine):
            return convert_dataclass_to_subclass(line, script_ast.ASTRunStatement)
        else:
            raise ValueError(f'Unexpected line in single-line statement on line {getattr(line, "line", "UNKNOWN")}: {line!r}')

    @filter_none
    def block_statement(self, data: List[Any]) -> script_ast.ASTBlockStatement:
        header, body = data[0], data[1:]

        if isinstance(header, script_ast.ASTAddLine):
            statement = convert_dataclass_to_subclass(header, script_ast.ASTAddStatement)
        elif isinstance(header, script_ast.ASTUpdateLine):
            statement = convert_dataclass_to_subclass(header, script_ast.ASTUpdateStatement)
        else:
            raise ValueError(f'Unexpected header line in block statement on line {ctx.start.line}: {header!r}')

        statement.body_lines = body
        return statement


    block_lines = passthrough


    @filter_none
    def set_line(self, data: List[Any]) -> script_ast.ASTSetLine:
        name, value = data[:2]
        return script_ast.ASTSetLine(name.line_no, name, value)

    @filter_none
    def add_line(self, data: List[Any]) -> script_ast.ASTAddLine:
        type_name = data[0]
        object_name = value = None
        for thing in data[1:]:
            if isinstance(thing, self.AddLineObjectName):
                object_name = thing[0]
            elif isinstance(thing, self.AddLineValue):
                value = thing[0]
            else:
                raise TypeError(thing)
        return script_ast.ASTAddLine(type_name.line_no, type_name, object_name, value)

    class AddLineObjectName(tuple): pass
    class AddLineValue(tuple): pass

    @filter_none
    def add_line_name(self, data: List[Any]) -> AddLineObjectName:
        return self.AddLineObjectName((data[0],))

    @filter_none
    def add_line_value(self, data: List[Any]) -> AddLineValue:
        return self.AddLineValue((data[0],))

    @filter_none
    def delete_line(self, data: List[Any]) -> script_ast.ASTDeleteLine:
        type_name = data[0]
        object_name_searchable = data[1]
        return script_ast.ASTDeleteLine(type_name.line_no, type_name, object_name_searchable)

    @filter_none
    def update_line(self, data: List[Any]) -> script_ast.ASTUpdateLine:
        type_name = data[0]
        object_name_searchable = data[1]
        return script_ast.ASTUpdateLine(type_name.line_no, type_name, object_name_searchable)

    @filter_none
    def run_line(self, data: List[Any]) -> script_ast.ASTRunLine:
        macro = data[0]
        return script_ast.ASTRunLine(macro.line_no, macro)

    @filter_none
    def comment_only_line(self, data: List[Any]) -> Discard:
        return do_discard()


    @filter_none
    def macro(self, data: List[Any]) -> script_ast.ASTMacro:
        if len(data) == 1:
            name, args = data[0], []
        else:
            name, args = data[0], data[1]

        positional_args = []
        keyword_args = []
        for arg in args:
            if isinstance(arg, self.MacroPositionalArg):
                if keyword_args:
                    raise ValueError(f'Positional macro argument after a keyword argument, on line {name.line_no}')
                positional_args.append(arg[0])
            elif isinstance(arg, self.MacroKeywordArg):
                keyword_args.append((arg[0], arg[1]))
            else:
                raise ValueError(arg)

        return script_ast.ASTMacro(name.line_no, name, positional_args, keyword_args)

    macro_args = passthrough

    class MacroPositionalArg(tuple): pass
    class MacroKeywordArg(tuple): pass

    @filter_none
    def macro_positional_arg(self, data: List[Any]) -> MacroPositionalArg:
        return self.MacroPositionalArg((data[0],))

    @filter_none
    def macro_keyword_arg(self, data: List[Any]) -> MacroKeywordArg:
        name, value = data[0], data[1]
        return self.MacroKeywordArg((name, value))


    def bool_literal(self, data: Token) -> bool:
        return data == 'true'

    @filter_none
    def int_literal(self, data: List[Token]) -> int:
        return int(''.join(data), 0)

    @filter_none
    def bytes_literal(self, data: List[Token]) -> bytes:
        return bytes.fromhex(''.join(data))

    def ESCAPED_STRING(self, data: Token) -> str:
        return python_ast.literal_eval(data)

    def NAME(self, data: Token) -> script_ast.ASTName:
        return script_ast.ASTName(data.line, str(data))

    def __default__(self, data: Any, children: List[Any], meta: Meta) -> Any:
        """
        Trying to replicate the behavior of ANTLR's Visitor class, which
        is the only thing that ANTLR does better than Lark
        """
        for child in children:
            if not isinstance(child, (Tree, Token)):
                return child
        return do_discard()


def load_from_file(path: Path) -> script_ast.AST:
    """
    Convert a path pointing to a script file to an AST object.
    """
    SKIP_TREE = False
    if USE_STANDALONE:
        if SKIP_TREE:
            parser = Lark_StandAlone(postlex=PapyrusIndenter(), transformer=PapyrusTransformer())
        else:
            parser = Lark_StandAlone(postlex=PapyrusIndenter())
    else:
        kgjhdskflgjsdfhkl = Path(__file__).parent / 'parser' / 'Papyrus.lark'
        if SKIP_TREE:
            parser = Lark.open(
                kgjhdskflgjsdfhkl,
                parser='lalr',
                postlex=PapyrusIndenter(),
                transformer=PapyrusTransformer())
        else:
            parser = Lark.open(
                kgjhdskflgjsdfhkl,
                parser='lalr',
                postlex=PapyrusIndenter())

    if SKIP_TREE:
        return parser.parse(path.read_text(encoding='utf-8') + '\n')
    else:
        parse_tree = parser.parse(path.read_text(encoding='utf-8') + '\n')
        return PapyrusTransformer().transform(parse_tree)
