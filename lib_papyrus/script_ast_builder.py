import ast as python_ast
import dataclasses
from pathlib import Path
from typing import Any, List

import antlr4

from .parser.PapyrusLexer import PapyrusLexer
from .parser.PapyrusParser import PapyrusParser
from .parser.PapyrusParserVisitor import PapyrusParserVisitor

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



class Visitor(PapyrusParserVisitor):
    """
    Converts various "parser rule contexts" from the Antlr parse tree to
    our own AST dataclass objects
    """

    def visitPapyrusFile(self, ctx: PapyrusParser.PapyrusFileContext) -> script_ast.AST:
        return script_ast.AST(self.visit(ctx.statements()))


    def visitStatements(self, ctx: PapyrusParser.StatementsContext) -> List[script_ast.ASTStatement]:
        return [b for b in (self.visit(a) for a in ctx.statement()) if b is not None]


    def visitSingleLineStatement(self, ctx: PapyrusParser.SingleLineStatementContext) -> script_ast.ASTSingleLineStatement:
        line = self.visit(ctx.standaloneLine())
        if line is None:  # (blank line)
            return None
        elif isinstance(line, script_ast.ASTSetLine):
            return convert_dataclass_to_subclass(line, script_ast.ASTSetStatement)
        elif isinstance(line, script_ast.ASTDeleteLine):
            return convert_dataclass_to_subclass(line, script_ast.ASTDeleteStatement)
        elif isinstance(line, script_ast.ASTRunLine):
            return convert_dataclass_to_subclass(line, script_ast.ASTRunStatement)
        else:
            raise ValueError(f'Unexpected line in single-line statement on line {ctx.start.line}: {line!r}')


    def visitBlockStatement(self, ctx: PapyrusParser.BlockStatementContext) -> script_ast.ASTBlockStatement:
        header = self.visit(ctx.blockStartingLine())
        if isinstance(header, script_ast.ASTAddLine):
            stat = convert_dataclass_to_subclass(header, script_ast.ASTAddStatement)
        elif isinstance(header, script_ast.ASTUpdateLine):
            stat = convert_dataclass_to_subclass(header, script_ast.ASTUpdateStatement)
        else:
            raise ValueError(f'Unexpected header line in block statement on line {ctx.start.line}: {header!r}')

        block = ctx.blockLines()
        if block:
            stat.body_lines.extend(self.visit(line) for line in block.standaloneLine())

        return stat


    def visitBlockLines(self, ctx: PapyrusParser.BlockLinesContext) -> List[script_ast.ASTLine]:
        return [self.visit(a) for a in ctx.standaloneLine()]


    def visitSetLine(self, ctx: PapyrusParser.SetLineContext) -> script_ast.ASTSetLine:
        name = self.visit(ctx.attributeName())
        value = self.visit(ctx.setLineValue())
        return script_ast.ASTSetLine(ctx.start.line, name, value)


    def visitAddLine(self, ctx: PapyrusParser.AddLineContext) -> script_ast.ASTAddLine:
        type_name = self.visit(ctx.typeName())
        object_name = ctx.objectName()
        if object_name is not None:
            object_name = self.visit(object_name)
        initial_data = ctx.bytesLiteral()
        if initial_data is not None:
            initial_data = self.visit(initial_data)
        return script_ast.ASTAddLine(ctx.start.line, type_name, object_name, initial_data)


    def visitDeleteLine(self, ctx: PapyrusParser.DeleteLineContext) -> script_ast.ASTDeleteLine:
        type_name = self.visit(ctx.typeName())
        obj_name_searchable = self.visit(ctx.objectNameSearchable())
        return script_ast.ASTDeleteLine(ctx.start.line, type_name, obj_name_searchable)


    def visitUpdateLine(self, ctx: PapyrusParser.UpdateLineContext) -> script_ast.ASTUpdateLine:
        type_name = self.visit(ctx.typeName())
        obj_name_searchable = self.visit(ctx.objectNameSearchable())
        return script_ast.ASTUpdateLine(ctx.start.line, type_name, object_name, initial_data)


    def visitRunLine(self, ctx: PapyrusParser.RunLineContext) -> script_ast.ASTRunLine:
        macro = self.visit(ctx.macro())
        return script_ast.ASTRunLine(ctx.start.line, macro)


    def visitBoolLiteral(self, ctx:PapyrusParser.BoolLiteralContext):
        return ctx.start.text == 'true'


    def visitIntLiteral(self, ctx:PapyrusParser.IntLiteralContext):
        return int(ctx.start.text, 0)


    def visitStringLiteral(self, ctx:PapyrusParser.StringLiteralContext):
        return python_ast.literal_eval(ctx.start.text)


    def visitBytesLiteral(self, ctx:PapyrusParser.BytesLiteralContext):
        return bytes.fromhex(ctx.start.text.strip(' []'))


    def visitName(self, ctx: PapyrusParser.NameContext) -> script_ast.ASTName:
        return script_ast.ASTName(ctx.start.line, ctx.start.text)



def load_from_file(path: Path) -> script_ast.AST:
    """
    Convert a path pointing to a script file to an AST object.
    """
    input_stream = antlr4.FileStream(path)
    lexer = PapyrusLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = PapyrusParser(stream)

    # (note: the line below is where most of the performance hit is)
    tree = parser.papyrusFile()
    return Visitor().visit(tree)
