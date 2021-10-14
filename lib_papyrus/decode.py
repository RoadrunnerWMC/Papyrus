import dataclasses
import datetime
import enum
from pathlib import Path
from typing import Any, BinaryIO, List, Literal, Optional

import nsmbpy2
import nsmbpy2.level
import nsmbpy2.u8

from . import TOOL_NAME, VERSION_NAME, BLOCK_ITEM_NAMES


@dataclasses.dataclass
class DecodingConfig:
    """
    CLI options regarding decoding.
    """
    game: Optional[nsmbpy2.Game]
    input_file: Path
    output_file: Path
    file_format_version: str
    display_fields: Literal['none', 'nonempty', 'all']


def autodetect_game_for_binary_level(file: BinaryIO) -> nsmbpy2.Game:
    """
    Auto-detect which game this is a level for
    """
    # NSMBW
    file.seek(0)
    if file.read(4) == nsmbpy2.u8.U8_MAGIC:
        return nsmbpy2.Game.NEW_SUPER_MARIO_BROS_WII

    raise ValueError('Unable to identify input file type')


def spritedata_style_bytes_hex_string(data: bytes) -> str:
    """
    Generate a hex string in Reggie spritedata style -- XXXX XXXX XXXX ...
    """
    raw_data_str_1 = data.hex()
    raw_data_str_2 = ''
    while raw_data_str_1:
        raw_data_str_2 += raw_data_str_1[:4] + ' '
        raw_data_str_1 = raw_data_str_1[4:]
    return raw_data_str_2.rstrip()


def convert_field_value_to_str(item_type_name: str, field_name: str, field_value: Any, config: DecodingConfig) -> str:
    """
    Decide on the ideal way to represent this field value as a string
    """

    if item_type_name.startswith('area_settings') and field_name.startswith('initial_event_ids_'):
        return hex(field_value)

    elif item_type_name.startswith('background_layer_') and field_name.startswith('file_id_'):
        # most similar representation to the Object folder filenames
        return f'0x{field_value:04X}'

    elif field_name == 'flags':
        return hex(field_value)

    elif isinstance(field_value, (bytes, bytearray)):
        return f'[{spritedata_style_bytes_hex_string(field_value)}]'

    elif isinstance(field_value, bool):
        return 'true' if field_value else 'false'

    elif isinstance(field_value, enum.IntEnum):
        field_value_str = field_value.name

        semantic_value = None
        if hasattr(field_value, 'semantic_value') and field_value.semantic_value is not None:
            semantic_value = field_value.semantic_value

        if semantic_value is None:
            field_value_str += f'  # ({field_value.value})'
        else:
            field_value_str += f'  # ({field_value.value}: {field_value.semantic_value})'

        return field_value_str

    elif isinstance(field_value, str):
        if field_value == '':
            # don't encode this field
            return None
        return f'"{field_value}"'

    else:
        return str(field_value)


def decode_struct_as_lines(item_type_name: str, item: 'BaseStruct', config: DecodingConfig) -> List[str]:
    """
    Create a textual representation of the provided struct.
    """
    lines = []

    lines.append(f'{item_type_name}: [{spritedata_style_bytes_hex_string(bytes(item))}]')

    if config.display_fields != 'none':
        for field_name, field in item.fields.items():
            field_value = item.get(field_name)

            if config.display_fields == 'nonempty' and field_value == field.empty_value():
                # make an exception for fields named "id", since 0 is
                # obviously still a useful value to display for such fields
                if field_name != 'id':
                    continue

            field_value_str = convert_field_value_to_str(item_type_name, field_name, field_value, config)
            if field_value_str is not None:
                lines.append(f'    {field_name}: {field_value_str}')

    return lines


def convert_level_to_text(api: 'LevelAPI', level: 'Level', config: DecodingConfig) -> str:
    """
    Handles the actual text generation stuff
    """
    lines = []
    lines.append(f'# Converted by {TOOL_NAME} {VERSION_NAME} from {config.input_file.name} at {datetime.datetime.now().isoformat()}')
    lines.append('')
    lines.append(f'set game {api.game.value}')
    lines.append(f'set file_format_version {api.api_version}')
    lines.append('')

    for area_num, area in enumerate(level.areas):
        lines.append('')
        lines.append(f'set area {area_num+1}')

        if area.metadata:
            lines.append(f'set area_metadata [{spritedata_style_bytes_hex_string(area.metadata)}]')

        for layer_num in sorted(area.layers):
            layer = area.layers[layer_num]

            lines.append('')
            lines.append(f'set layer {layer_num}')

            for obj in layer:
                lines.append('')
                lines.extend(decode_struct_as_lines('object', obj, config))

        for block_num, (item_name, block) in enumerate(zip(BLOCK_ITEM_NAMES[api.game], area.blocks)):
            if isinstance(block, list):
                for item in block:
                    lines.append('')
                    lines.extend(decode_struct_as_lines(item_name, item, config))
            else:
                lines.append('')
                lines.extend(decode_struct_as_lines(item_name, block, config))

    lines.append('')
    return '\n'.join(lines)


def decode(config: DecodingConfig) -> None:
    """
    Main function for decoding a level.
    """
    if config.game is None:
        with config.input_file.open('rb') as f:
            config.game = autodetect_game_for_binary_level(f)

    api = nsmbpy2.level.get(config.game, config.file_format_version)
    level = api.Level.load_from_file(config.input_file)

    level_txt = convert_level_to_text(
        api, level, config)
    with config.output_file.open('w', encoding='utf-8') as f:
        f.write(level_txt)
