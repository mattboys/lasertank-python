from attempt_1.old_Header import *
from attempt_1.old_Sprites import *
from attempt_1.old_VectorFuncs import *

from functools import partial

# LevelData = 'test.lvl'
# FILENAME_LEVELS = os.path.join('Files', LevelData)

TANK_ID = 1

DIFFICULTY_KIDS = 1
DIFFICULTY_EASY = 2
DIFFICULTY_MEDIUM = 4
DIFFICULTY_HARD = 8
DIFFICULTY_DEADLY = 16
DIFFICULTY_TEXTS = {
    DIFFICULTY_KIDS: "Kids",
    DIFFICULTY_EASY: "Easy",
    DIFFICULTY_MEDIUM: "Medium",
    DIFFICULTY_HARD: "Hard",
    DIFFICULTY_DEADLY: "Deadly",
}

BOARD_SIZE = 16

GAME_SPEED = 1

playfield_int_to_obj = {
    0: (Grass, NoneObject),
    TANK_ID: (Grass, partial(Tank, DIR_UP)),
    2: (Flag, NoneObject),
    3: (Water, NoneObject),
    4: (Grass, Solid),
    5: (Grass, Block),
    6: (Grass, Wall),
    7: (Grass, partial(Antitank, DIR_UP)),
    8: (Grass, partial(Antitank, DIR_RIGHT)),
    9: (Grass, partial(Antitank, DIR_DOWN)),
    10: (Grass, partial(Antitank, DIR_LEFT)),
    11: (Grass, partial(Mirror, ANG_LEFT_UP)),
    12: (Grass, partial(Mirror, ANG_UP_RIGHT)),
    13: (Grass, partial(Mirror, ANG_RIGHT_DOWN)),
    14: (Grass, partial(Mirror, ANG_DOWN_LEFT)),
    15: (partial(Conveyor, DIR_UP), NoneObject),
    16: (partial(Conveyor, DIR_RIGHT), NoneObject),
    17: (partial(Conveyor, DIR_DOWN), NoneObject),
    18: (partial(Conveyor, DIR_LEFT), NoneObject),
    19: (Grass, Glass),
    20: (Grass, partial(RotMirror, ANG_LEFT_UP)),
    21: (Grass, partial(RotMirror, ANG_UP_RIGHT)),
    22: (Grass, partial(RotMirror, ANG_RIGHT_DOWN)),
    23: (Grass, partial(RotMirror, ANG_DOWN_LEFT)),
    24: (Ice, NoneObject),
    25: (ThinIce, NoneObject),
    64: (partial(Tunnel, 0), NoneObject),
    66: (partial(Tunnel, 1), NoneObject),
    68: (partial(Tunnel, 2), NoneObject),
    70: (partial(Tunnel, 3), NoneObject),
    72: (partial(Tunnel, 4), NoneObject),
    74: (partial(Tunnel, 5), NoneObject),
    76: (partial(Tunnel, 6), NoneObject),
    78: (partial(Tunnel, 7), NoneObject),
}


# def empty_array_tPlayField():
#     return [[0 for i in range(16)] for j in range(16)]


class LevelLoader:
    def __init__(self, lvl_number=1, filename=FILENAME_LEVELS):
        self.filename = filename
        self.number = lvl_number
        self.playfield_initial_ints = [[0 for i in range(16)] for j in range(16)]
        self.title = ""
        self.hint = ""
        self.author = ""
        self.difficulty = DIFFICULTY_KIDS
        self.load_level_from_file()

    def load_level_from_file(self):
        if self.number < 1:
            self.number = 1  # First level_inital is numbered 1
        LEVEL_DATA_SIZE = 576
        byte_offset = (self.number - 1) * LEVEL_DATA_SIZE
        with open(self.filename, "rb") as f:
            f.seek(byte_offset, 0)  # Seek to byte offset relative to start of file
            chunk = f.read(LEVEL_DATA_SIZE)
            if chunk:
                playfield_bytes = chunk[0:256]
                self.playfield_initial_ints = [
                    [playfield_bytes[i + (16 * j)] for i in range(16)]
                    for j in range(16)
                ]
                self.title = chunk[256:287].decode("utf-8").rstrip("\x00")
                self.hint = chunk[287:543].decode("utf-8").rstrip("\x00")
                self.author = chunk[543:574].decode("utf-8").rstrip("\x00")
                self.difficulty = int.from_bytes(
                    chunk[574:576], byteorder="little", signed=False
                )
                return True
            else:
                return False

    def next_level(self):
        temp_number = self.number
        self.number += 1
        if self.load_level_from_file():
            return True
        else:
            self.number = temp_number
            return self.load_level_from_file()

    def print_levelinfo(self):
        print(f"Name: {self.title}")
        print(f"Number: {self.number}")
        print(f"Author: {self.author}")
        print(f"Difficulty: {DIFFICULTY_TEXTS[self.difficulty]}")
        for y in range(16):
            print(
                "".join(
                    [
                        "{:3d}".format(self.playfield_initial_ints[x][y])
                        for x in range(16)
                    ]
                )
            )


class GameBoard:
    def __init__(self, level_data: LevelLoader):
        LTSprite.gameboard = self  # Let sprites access this GameBoard instance
        self.level_inital = level_data
        self.ground = [[None for i in range(16)] for j in range(16)]
        self.items = [[None for i in range(16)] for j in range(16)]
        self.tank = Tank(position=(7, 15), direction=1)
        self.laser = Laser()
        self.initialise_playfield()
        self.input_buffer = []
        # self.input_enabled = True
        self.sliding_items = []
        self.speed_counter = 0

    def disable_input(self):
        self.input_enabled = False

    def enable_input(self):
        self.input_enabled = True

    def initialise_playfield(self):
        # Initialise to raw level_inital
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                obj_id = self.level_inital.playfield_initial_ints[x][y]
                position = (x, y)
                terrain, item = playfield_int_to_obj[obj_id]
                self.ground[x][y] = terrain(position)
                self.items[x][y] = item(position)
                if obj_id == TANK_ID:
                    self.tank = self.items[x][y]

    def draw(self, surface):
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                self.ground[x][y].draw(surface)
                if self.items[x][y] is not None:
                    self.items[x][y].draw(surface)
        self.tank.draw(surface)
        self.laser.draw(surface)

    def update(self):
        """ Update game board state with keyboard buffer """
        # if self.speed_counter < GAME_SPEED:
        #     self.speed_counter += 1
        #     return
        # else:
        #     self.speed_counter = 0

        # Laser movement
        self.laser.update()

        # Player turn
        if len(self.sliding_items) == 0 and not self.laser.exists:
            if self.input_buffer:
                move = self.input_buffer.pop(0)
                if move == SHOOT:
                    self.tank.shoot()
                else:
                    if self.tank.dir == move:
                        self.tank.push(move)
                    else:
                        self.tank.rotate(move)

        # Update sliding objects list
        for item in reversed(self.sliding_items):
            item.resolve_momentum()
        # Remove stationary object from queue
        self.sliding_items = [
            item for item in self.sliding_items if item.momentum != DIR_NONE
        ]

        # TODO: AntiTank turn
        self._antitank_turn()

    def _antitank_turn(self):
        if not self.laser.exists:
            for check_dir in [DIR_RIGHT, DIR_LEFT, DIR_DOWN, DIR_UP]:
                x, y = self.tank.position
                # Search for
                while self.can_move_into((x, y)):
                    x, y = vec_add((x, y), DIR_TO_XY[check_dir])
                if (
                    self.is_within_board((x, y))
                    and isinstance(self.items[x][y], Antitank)
                    and self.items[x][y].dir == DIR_OPPOSITE[check_dir]
                    and (x, y) != self.tank.position
                    and self.items[x][y].alive
                ):
                    self.items[x][y].shoot()
                    return

    def queue_move(self, move):
        """ Put move on input buffer. Will be held until player's next turn """
        assert move in [DIR_UP, DIR_LEFT, DIR_DOWN, DIR_RIGHT, SHOOT], "Invalid move!"
        self.input_buffer.append(move)

    def destroy_item(self, position):
        x, y = position
        self.items[x][y] = NoneObject(position)

    def game_over(self):
        # TODO
        print("Game Over!")

    def win(self):
        print("Victory!")

    def is_within_board(self, position):
        """ Is this square still within the confines of the board? """
        x, y = position
        if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
            return True
        else:
            return False  # Off gameboard

    def can_move_into(self, position):
        """ Can an item move into this square? or Is this square on the board and empty? """
        if self.is_within_board(position):
            x, y = position
            return self.items[x][y] is None
        else:
            return False  # Off gameboard


#
# def load_level_from_file(level_number):
#     if level_number < 1:
#         level_number = 1  # First level_inital is numbered 1
#     level_data_size = 576
#     byte_offset = (level_number - 1) * level_data_size
#     with open(FILENAME_LEVELS, 'rb') as f:
#         f.seek(byte_offset, 0)  # Seek to byte offset relative to start of file
#         chunk = f.read(level_data_size)
#         if chunk:
#             playfield_bytes = chunk[0:256]
#             playfield_initial_ints = [[playfield_bytes[i + (16 * j)] for i in range(16)] for j in range(16)]
#             level_name = chunk[256:287].decode("utf-8").rstrip('\x00')
#             level_hint = chunk[287:543].decode("utf-8").rstrip('\x00')
#             level_author = chunk[543:574].decode("utf-8").rstrip('\x00')
#             level_difficulty = int.from_bytes(chunk[574:576], byteorder='little', signed=False)
#             return Game(playfield_initial_ints, level_name, level_hint, level_author, level_difficulty, level_number)
#         else:
#             return None


# class game_state:
#     """" Game state and state data """
#
#     def __init__(self):
#         self.playerfield_PF = empty_array_tPlayField()  # Store game items
#         self.ground_PF2 = empty_array_tPlayField()  # Store items under stuff (Ground, conveyor)
#
#         self.Tank = {'X': 0, 'Y': 0, 'Dir': 0, 'Firing': 0, 'Good': 0}  # Tank data
#
#         self.ScoreMove = 0  # Move Counter
#         self.ScoreShot = 0  # Shot counter
#
#         self.RecP = None  # Recording pointer
#
#         self.CurLevel = 0
#
#     def loadNextLevel(self):
#         level_inital = load_level_from_file(self.CurLevel)
#         self.playerfield_PF = level_inital.playerfield_PF


if __name__ == "__main__":
    myLevel = LevelLoader(1)
    myLevel.print_levelinfo()
