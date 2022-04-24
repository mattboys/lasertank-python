import struct

from engine import Game
import constants as c


def load_level(filename, level_number):
    game = Game()
    game.load_level(level_number=level_number, filename=filename)
    return game


def load_playback(filename):
    struct_format = "<31s31sHH"  # PBSRec (tRecordRec) C structure
    chunk_size = struct.calcsize(struct_format)  # 66
    with open(filename, "rb") as f:
        info_chunk = f.read(chunk_size)
        if not info_chunk:
            return None
        level_name, player_name, level_number, buffer_size = struct.unpack(
            struct_format, info_chunk
        )
        moves_chunk = f.read(buffer_size)

    def convert_null_terminated_bytes_to_str_helper(in_bytes):
        """Convert null terminated string from bytes to python string"""
        return in_bytes.split(b"\x00")[0].decode("mbcs")

    # Clean up byte data
    level_name = convert_null_terminated_bytes_to_str_helper(level_name)
    player_name = convert_null_terminated_bytes_to_str_helper(player_name)
    playback = []
    for move_byte in moves_chunk:
        if move_byte == 0x20:
            playback.append(c.K_SHOOT)
        elif move_byte == 0x25:
            playback.append(c.K_LEFT)
        elif move_byte == 0x26:
            playback.append(c.K_UP)
        elif move_byte == 0x27:
            playback.append(c.K_RIGHT)
        elif move_byte == 0x28:
            playback.append(c.K_DOWN)
        else:
            break
    return {
        "number": level_number,
        "title": level_name,
        "player_name": player_name,
        "playback": playback,
    }


def execute_playback(inputs: list, game: Game):
    game.queue_new_inputs(inputs)
    while game.running and not game.is_inputs_queued():
        game.tick()
    if game.state.reached_flag:
        return "WIN"
    elif game.state.player_dead:
        return "DEAD"
    else:
        return "UNFINISHED"
