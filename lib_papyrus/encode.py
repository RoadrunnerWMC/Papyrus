from pathlib import Path
from typing import Any, List

import nsmbpy2

from . import script_ast_builder
from . import script_ast


def encode(game: nsmbpy2.Game, input_files: List[Path], output_file: Path) -> None:
    """
    Main function for encoding a level.
    """
    for fp in input_files:
        ast = script_ast_builder.load_from_file(fp)
        script_ast.perform_ast_semantic_checks(ast)

        print(ast)
