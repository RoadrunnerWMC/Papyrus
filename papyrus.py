import argparse
from pathlib import Path

import nsmbpy2

import lib_papyrus.decode
import lib_papyrus.encode


def main(argv:list=None) -> None:
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description='Papyrus: a text-based level editor for the New Super Mario Bros. series, powered by nsmbpy2')
    parser.add_argument('--game', choices=[m.value for m in nsmbpy2.Game],
        help='the game to work with')
    subparsers = parser.add_subparsers(title='commands',
        description='(run a command with -h for additional help)')

    def handle_decode(p_args: object) -> None:
        """
        Handle the "decode" command.
        """
        game = p_args.game
        input_file = p_args.input_file
        file_format_version = p_args.file_format_version
        display_fields = p_args.display_fields

        output_file = p_args.output_file
        if output_file is None: output_file = input_file.with_suffix('.txt')

        lib_papyrus.decode.decode(game, input_file, output_file, file_format_version, display_fields=display_fields)

    parser_decode = subparsers.add_parser('decode',
        help='convert a level from a binary file to a text file')
    parser_decode.add_argument('input_file', type=Path,
        help='level file')
    parser_decode.add_argument('output_file', nargs='?', type=Path,
        help='output file')
    parser_decode.add_argument('--file-format-version', nargs='?',
        help='file-format version to use (default: latest)')
    parser_decode.add_argument('--display-fields', choices=['none', 'nonempty', 'all'], default='all',
        help='show field values for each item, instead of just the raw hex data (default: all)')
    parser_decode.set_defaults(func=handle_decode)

    def handle_encode(p_args: object) -> None:
        """
        Handle the "encode" command.
        """
        game = p_args.game
        input_files = p_args.input_file

        output_file = p_args.output_file
        # TODO: pick output file extension more appropriately
        if output_file is None: output_file = input_files[0].with_suffix('.bin')

        lib_papyrus.encode.encode(game, input_files, output_file)

    parser_encode = subparsers.add_parser('encode',
        help='convert one or more level files to a binary file')
    parser_encode.add_argument('input_file', nargs='+', type=Path,
        help='level file(s)')
    parser_encode.add_argument('output_file', nargs='?', type=Path,
        help='output file')
    parser_encode.set_defaults(func=handle_encode)

    # Parse args and run appropriate function
    p_args = parser.parse_args(argv)
    if hasattr(p_args, 'func'):
        p_args.func(p_args)
    else:  # this happens if no arguments were specified at all
        parser.print_usage()


if __name__ == '__main__':
    main()
