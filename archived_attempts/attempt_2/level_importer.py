import struct

from constants import *

# See LTANK.H for C-structs
# See https://docs.python.org/3/library/struct.html#struct-format-strings
decode_table = {
    0: ((GRASS,), (EMPTY,)),
    1: ((GRASS,), (TANK, {"direction": DIRECTION_N, })),
    2: ((FLAG,), (EMPTY,)),
    3: ((WATER,), (EMPTY,)),
    4: ((GRASS,), (SOLID,)),
    5: ((GRASS,), (BLOCK,)),
    6: ((GRASS,), (WALL,)),
    7: ((GRASS,), (ANTITANK, {"direction": DIRECTION_N, })),
    8: ((GRASS,), (ANTITANK, {"direction": DIRECTION_E, })),
    9: ((GRASS,), (ANTITANK, {"direction": DIRECTION_S, })),
    10: ((GRASS,), (ANTITANK, {"direction": DIRECTION_W, })),
    11: ((GRASS,), (MIRROR, {"direction": DIRECTION_N, })),
    12: ((GRASS,), (MIRROR, {"direction": DIRECTION_E, })),
    13: ((GRASS,), (MIRROR, {"direction": DIRECTION_S, })),
    14: ((GRASS,), (MIRROR, {"direction": DIRECTION_W, })),
    15: ((CONVEYOR, {"direction": DIRECTION_N, }), (EMPTY,)),
    16: ((CONVEYOR, {"direction": DIRECTION_E, }), (EMPTY,)),
    17: ((CONVEYOR, {"direction": DIRECTION_S, }), (EMPTY,)),
    18: ((CONVEYOR, {"direction": DIRECTION_W, }), (EMPTY,)),
    19: ((GRASS,), (GLASS,)),
    20: ((GRASS,), (ROTMIRROR, {"direction": DIRECTION_N, })),
    21: ((GRASS,), (ROTMIRROR, {"direction": DIRECTION_E, })),
    22: ((GRASS,), (ROTMIRROR, {"direction": DIRECTION_S, })),
    23: ((GRASS,), (ROTMIRROR, {"direction": DIRECTION_W, })),
    24: ((ICE,), (EMPTY,)),
    25: ((THINICE,), (EMPTY,)),
    64: ((TUNNEL, {"id": 0, }), (EMPTY,)),
    66: ((TUNNEL, {"id": 1, }), (EMPTY,)),
    68: ((TUNNEL, {"id": 2, }), (EMPTY,)),
    70: ((TUNNEL, {"id": 3, }), (EMPTY,)),
    72: ((TUNNEL, {"id": 4, }), (EMPTY,)),
    74: ((TUNNEL, {"id": 5, }), (EMPTY,)),
    76: ((TUNNEL, {"id": 6, }), (EMPTY,)),
    78: ((TUNNEL, {"id": 7, }), (EMPTY,)),
}


def import_legacy_lvl(level_number=1, filename="legacy_resources/Files/LaserTank.lvl"):
    """ Read a .lvl level file created by the original LaserTank 4.1.2 """
    if level_number < 1:
        level_number = 1
    struct_format = "<256s31s256s31sH"  # tLevel C structure
    chunk_size = struct.calcsize(struct_format)  # 576
    byte_offset = chunk_size * (level_number - 1)
    with open(filename, "rb") as f:
        f.seek(byte_offset, 0)  # Seek to byte offset relative to start of file
        chunk = f.read(chunk_size)
        if not chunk:
            return None
    playfield_ints, title, hint, author, difficulty_int = struct.unpack(struct_format, chunk)

    def convert_str(in_bytes):
        return in_bytes.rstrip(b"\x00").decode("mbcs")

    title = convert_str(title)
    hint = convert_str(hint)
    author = convert_str(author)

    DIFFICULTY_TEXTS = {
        1: DIFFICULTY_KIDS,
        2: DIFFICULTY_EASY,
        4: DIFFICULTY_MEDIUM,
        8: DIFFICULTY_HARD,
        16: DIFFICULTY_DEADLY,
    }
    difficulty = DIFFICULTY_TEXTS.get(difficulty_int, DIFFICULTY_TEXTS[1])

    board_items = [[None for x in range(GAMEBOARD_SIZE)] for y in range(GAMEBOARD_SIZE)]
    board_terrain = [[None for x in range(GAMEBOARD_SIZE)] for y in range(GAMEBOARD_SIZE)]
    tank = (TANK,)

    def inject_position(packed_gameobj, position=None):
        obj_name = packed_gameobj[0]
        attributes = packed_gameobj[1] if len(packed_gameobj) > 1 else {}
        # Inject position attribute if provided
        if position is not None:
            attributes.update({"position": position})
        return obj_name, attributes

    for col in range(GAMEBOARD_SIZE):
        for row in range(GAMEBOARD_SIZE):
            # Note that lvl files are saved in columns and playfield is in [y][x]
            x = col
            y = row
            i = int(playfield_ints[row + col * GAMEBOARD_SIZE])
            terrain, item = decode_table[i]
            if item[0] == TANK:
                tank = inject_position(item, position=(x, y))
                item = (EMPTY,)
            terrain = inject_position(terrain, position=(x, y))
            item = inject_position(item, position=(x, y))

            board_items[y][x] = item
            board_terrain[y][x] = terrain

    return {
        "level_info": {
            "number": level_number,
            "title": title,
            "hint": hint,
            "author": author,
            "difficulty": difficulty,
        },
        "packed_board": {
            "terrain_packed": board_terrain,
            "items_packed": board_items,
            "tank_packed": tank
        }
    }


if __name__ == "__main__":
    level_number = 1

    level_data = import_legacy_lvl(level_number=level_number)
    import json

    print(json.dumps(level_data))

    # while True:
    #     level_data = import_legacy_lvl(level_number=level_number)
    #     if level_data is None:
    #         break
    #     print(f"{level_data['number']}" + "\t" +
    #           f"{level_data['title']}" + "\t" +
    #           f"{level_data['author']}" + "\t" +
    #           f"{level_data['difficulty']}" + "\t" +
    #           f"{level_data['hint']}")
    #     level_number += 1
