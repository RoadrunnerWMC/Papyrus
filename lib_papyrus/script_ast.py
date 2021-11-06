import dataclasses
from typing import Dict, List, Optional, Tuple, Union


dataclass = dataclasses.dataclass


@dataclass
class ASTNode:
    line_no: int


@dataclass
class ASTName(ASTNode):
    value: str


ASTLiteral = Union[bool, int, str, bytes, ASTName]


@dataclass
class ASTObjectAttribute(ASTNode):
    object_name: ASTName
    attribute_name: ASTName


@dataclass
class ASTMacro(ASTNode):
    name: ASTName
    positional_args: List[ASTLiteral] = dataclasses.field(default_factory=list)
    keyword_args: List[Tuple[ASTName, ASTLiteral]] = dataclasses.field(default_factory=list)


ASTObjectNameSearchable = Union[ASTName, ASTMacro]


@dataclass
class ASTLine(ASTNode):
    pass


@dataclass
class ASTSetLine(ASTLine):
    name: ASTName
    value: Union[ASTLiteral, ASTObjectAttribute, ASTMacro]


@dataclass
class ASTAddLine(ASTLine):
    type_name: ASTName
    object_name: Optional[ASTName]
    initial_data: Optional[bytes]


@dataclass
class ASTDeleteLine(ASTLine):
    type_name: ASTName
    object_name_searchable: ASTObjectNameSearchable


@dataclass
class ASTUpdateLine(ASTLine):
    type_name: ASTName
    object_name_searchable: ASTObjectNameSearchable


@dataclass
class ASTRunLine(ASTLine):
    macro: ASTMacro



@dataclass
class ASTStatement(ASTNode):
    pass


@dataclass
class ASTSingleLineStatement(ASTStatement):
    pass


@dataclass
class ASTBlockStatement(ASTStatement):
    body_lines: List[ASTLine] = dataclasses.field(default_factory=list)


@dataclass
class ASTSetStatement(ASTSingleLineStatement, ASTSetLine):
    pass


@dataclass
class ASTAddStatement(ASTBlockStatement, ASTAddLine):
    body_lines: List[ASTSetLine] = dataclasses.field(default_factory=list)


@dataclass
class ASTDeleteStatement(ASTSingleLineStatement, ASTDeleteLine):
    pass


@dataclass
class ASTUpdateStatement(ASTBlockStatement, ASTUpdateLine):
    body_lines: List[ASTSetLine] = dataclasses.field(default_factory=list)


@dataclass
class ASTRunStatement(ASTSingleLineStatement, ASTRunLine):
    pass



@dataclass
class AST:
    statements: List[ASTStatement] = dataclasses.field(default_factory=list)



def perform_ast_semantic_checks(ast: AST) -> None:
    """
    Perform some semantic checks on the AST
    """
    # TODO: implement
    # - update statements must have at least one body line
    # - all block-type statements must only have set lines as body lines
    # - positional macro args must come before keyword args
