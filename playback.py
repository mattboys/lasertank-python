import struct
import constants


def import_legacy_lpb(playback_filename="legacy_resources/Files/Playback_0001.lpb"):
    """ Read a .lvl level file created by the original LaserTank 4.1.2 """

    struct_format = "<31s31sHH"  # tLevel C structure
    chunk_size = struct.calcsize(struct_format)
    with open(playback_filename, "rb") as f:
        info_data = f.read(chunk_size)
        title, player_tag, level_number, moves_number = struct.unpack(struct_format, info_data)
        moves_data = f.read()

    def convert_str(in_bytes):
        return in_bytes.rstrip(b"\x00").decode("mbcs")

    title = convert_str(title)
    player_tag = convert_str(player_tag)
    # player_tag = "UN  -User Name" where UN is the high score initials and User Name is entered at save

    VK_SPACE = 0x20
    VK_LEFT = 0x25
    VK_UP = 0x26
    VK_RIGHT = 0x27
    VK_DOWN = 0x28

    move_conversion = {
        VK_SPACE: constants.MOVES_SHOOT,
        VK_LEFT: constants.MOVES_W,
        VK_UP: constants.MOVES_N,
        VK_RIGHT: constants.MOVES_E,
        VK_DOWN: constants.MOVES_S
    }
    moves = [move_conversion[x] for x in moves_data]

    return {
        "number": level_number,
        "title": title,
        "player": player_tag,
        "moves": moves,
    }
