import struct

import constants

# See LTANK.H for C-structs
# See https://docs.python.org/3/library/struct.html#struct-format-strings

decode_table = {
    0: (constants.Grass, constants.Empty),
    1: (constants.Grass, constants.Tank_N),
    2: (constants.Flag, constants.Empty),
    3: (constants.Water, constants.Empty),
    4: (constants.Grass, constants.Solid),
    5: (constants.Grass, constants.Block),
    6: (constants.Grass, constants.Wall),
    7: (constants.Grass, constants.Antitank_N),
    8: (constants.Grass, constants.Antitank_E),
    9: (constants.Grass, constants.Antitank_S),
    10: (constants.Grass, constants.Antitank_W),
    11: (constants.Grass, constants.Mirror_N),
    12: (constants.Grass, constants.Mirror_E),
    13: (constants.Grass, constants.Mirror_S),
    14: (constants.Grass, constants.Mirror_W),
    15: (constants.Conveyor_N, constants.Empty),
    16: (constants.Conveyor_E, constants.Empty),
    17: (constants.Conveyor_S, constants.Empty),
    18: (constants.Conveyor_W, constants.Empty),
    19: (constants.Grass, constants.Glass),
    20: (constants.Grass, constants.RotMirror_N),
    21: (constants.Grass, constants.RotMirror_E),
    22: (constants.Grass, constants.RotMirror_S),
    23: (constants.Grass, constants.RotMirror_W),
    24: (constants.Ice, constants.Empty),
    25: (constants.ThinIce, constants.Empty),
    64: (constants.Tunnel_0, constants.Empty),
    66: (constants.Tunnel_1, constants.Empty),
    68: (constants.Tunnel_2, constants.Empty),
    70: (constants.Tunnel_3, constants.Empty),
    72: (constants.Tunnel_4, constants.Empty),
    74: (constants.Tunnel_5, constants.Empty),
    76: (constants.Tunnel_6, constants.Empty),
    78: (constants.Tunnel_7, constants.Empty),
}


def import_legacy_lvl(level_number=1, filename="legacy_resources/Files/LaserTank.lvl"):
    """ Read a .lvl level file created by the original LaserTank 4.1.2 """
    BOARDSIZE = 16
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
        1: "Kids",
        2: "Easy",
        4: "Medium",
        8: "Hard",
        16: "Deadly",
    }
    difficulty = DIFFICULTY_TEXTS.get(difficulty_int, DIFFICULTY_TEXTS[1])

    playfield = [[None for x in range(BOARDSIZE)] for y in range(BOARDSIZE)]
    for col in range(BOARDSIZE):
        for row in range(BOARDSIZE):
            # Note that lvl files are saved in columns and playfield is in [y][x]
            x = col
            y = row
            i = int(playfield_ints[row + col * BOARDSIZE])
            terrain, item = decode_table[i]
            playfield[y][x] = (terrain, item)

    return {
        "number": level_number,
        "title": title,
        "hint": hint,
        "author": author,
        "difficulty": difficulty,
        "playfield": playfield,
    }


if __name__ == "__main__":
    level_number = 1
    while True:
        level_data = import_legacy_lvl(level_number=level_number)
        if level_data is None:
            break
        print(f"{level_data['number']}" + "\t" +
              f"{level_data['title']}" + "\t" +
              f"{level_data['author']}" + "\t" +
              f"{level_data['difficulty']}" + "\t" +
              f"{level_data['hint']}")
        level_number += 1
