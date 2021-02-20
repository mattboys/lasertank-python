from constants import *


def print_board(playfield):
        print("     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P")
        for y in range(GAMEBOARD_SIZE):
            print(f"{y: >2}: " + " ".join(f"{playfield[x][y]:02}" for x in range(GAMEBOARD_SIZE))) 



def TPLAYFIELD():  # Matrix of G.O. (Game Object) types
    return [[0 for y in range(16) ] for x in range(16)]


class GameState:
    def __init__(self):
        self.objects = TPLAYFIELD()
        self.objects = TPLAYFIELD()
                


class TLEVEL:   # Level Data from File
    def __init__(self, PF=None, LName="", Hint="", Author="", SDiff = 0):
        if PF is None:
            PF = TPLAYFIELD() 
        self.PF = PF  # Object Grid
        self.LName = LName  # Level Name
        self.Hint = Hint  # Hint for this level
        self.Author = Author  # the Author of the Level
        self.SDiff = SDiff  # Score Difficulty

    def print(self):
        print(f"Level Name: {self.LName}")
        print(f"Author: {self.Author}")
        print(f"Hint:\n{self.Hint}")
        print("Level:")
        print_board(self.PF)


def import_legacy_lvl(level_number=1, filename="legacy_resources/Files/LaserTank.lvl"):
    """ Read a .lvl level file created by the original LaserTank 4.1.2 """

    import struct
    
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
    playfield_ints, title, hint, author, difficulty = struct.unpack(struct_format, chunk)

    def convert_str(in_bytes):
        return in_bytes.rstrip(b"\x00").decode("mbcs")

    title = convert_str(title)
    hint = convert_str(hint)
    author = convert_str(author)

    playfield = [[playfield_ints[y + x * GAMEBOARD_SIZE] for y in range(16) ] for x in range(16)]

    
    return TLEVEL(
        PF = playfield,
        LName = title,
        Hint = hint,
        Author = author,
        SDiff = difficulty,
    )

def main():
    print("Starting up...")
    level1 = import_legacy_lvl(1)
    level1.print()


    from graphics_pygame import Graphics
    from inputs_pygame import InputEngine
    graphics = Graphics()
    inputs = InputEngine()

    game_running = True
    while game_running:
        # Handle events
        for event in input_engine.get_inputs():
            print(event)
            if event == "quit":
                game_running = False





if __name__ == "__main__":
    main()