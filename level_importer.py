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
    11: (constants.Grass, constants.Mirror_NW),
    12: (constants.Grass, constants.Mirror_NE),
    13: (constants.Grass, constants.Mirror_SE),
    14: (constants.Grass, constants.Mirror_SW),
    15: (constants.Conveyor_N, constants.Empty),
    16: (constants.Conveyor_E, constants.Empty),
    17: (constants.Conveyor_S, constants.Empty),
    18: (constants.Conveyor_W, constants.Empty),
    19: (constants.Grass, constants.Glass),
    20: (constants.Grass, constants.RotMirror_NW),
    21: (constants.Grass, constants.RotMirror_NE),
    22: (constants.Grass, constants.RotMirror_SE),
    23: (constants.Grass, constants.RotMirror_SW),
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
    playfiled_ints, title, hint, author, difficulty_int = struct.unpack(struct_format, chunk)

    def convert_str(bytes):
        bytes = bytes.rstrip(b"\x00")
        return "".join([chr(i) for i in bytes])

    #title = title.decode("utf-8").rstrip("\x00")
    #hint = hint.decode("utf-8").rstrip("\x00")
    #author = author.decode("utf-8").rstrip("\x00")

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
    difficulty = DIFFICULTY_TEXTS[difficulty_int]

    playfiled = [[None for x in range(BOARDSIZE)] for y in range(BOARDSIZE)]
    for x in range(BOARDSIZE):
        for y in range(BOARDSIZE):
            i = int(playfiled_ints[x + y * BOARDSIZE])
            terrain, item = decode_table[i]
            playfiled[x][y] = (terrain, item)

    return {
        "number": level_number,
        "title": title,
        "hint": hint,
        "author": author,
        "difficulty": difficulty,
        "playfiled": playfiled
    }

if __name__ == "__main__":
    l = 1
    while True:
        level_data = import_legacy_lvl(level_number=l)
        if level_data is None:
            break
        print(f"{level_data['number']}\t{level_data['title']}\t{level_data['author']}\t{level_data['difficulty']}\t{level_data['hint']}")
        l += 1
