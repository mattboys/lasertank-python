import constants as id

import struct

import pygame


BOARDSIZE = 16  # Playfield is 16x16 grid

DEFAULT_LEVEL_LOC = "./resources/LaserTank.lvl"
DEFAULT_SPRITESHEET_LOC = "./resources/spritesheet.png"

class TankRec:
    def __init__(self, x, y, direction):
        self.X = x
        self.Y = y
        self.Dir = direction
        self.Firing = False  # Is laser on the board
        self.Good = False  # Good is used for Tunnel Wait in Game.Tank


class Board:
    def __init__(self):
        self.terrain = [[id.GRASS for y in range(BOARDSIZE)] for x in range(BOARDSIZE)]
        self.items = [[id.EMPTY for y in range(BOARDSIZE)] for x in range(BOARDSIZE)]
        self.tank = TankRec(x=7, y=15, direction=id.D_UP)
        self.laser = TankRec(x=0, y=0, direction=id.D_UP)

class LevelInfo:
    def __init__(self):
        self.name = ""
        self.number = 1


class GameState:
    def __init__(self):
        self.board = Board()
        self.sliding_items = []
        self.moves_history = []
        self.moves_buffer = []
        self.score = {"shots": 0, "moves": 0}
        self.undo_state = []
        self.info = {
            "number": 1,
            "title": "",
            "hint": "",
            "author": "",
            "difficulty": "",
        }

    def load_level(self, level_number, filename=DEFAULT_LEVEL_LOC):
        self.board = Board()
        self.sliding_items = []
        self.moves_history = []
        self.moves_buffer = []
        self.score = {"shots": 0, "moves": 0}
        self.undo_state = []

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
        difficulty = id.DIFFICULTY_TEXTS.get(difficulty_int, id.DIFFICULTY_TEXTS[1])
        self.info = {
            "number": level_number,
            "title":title,
            "hint": hint,
            "author":author,
            "difficulty":difficulty,
                     }

        for x in range(BOARDSIZE):
            for y in range(BOARDSIZE):
                # Note that lvl files are saved in columns and playfield is in [x][y]
                i = int(playfield_ints[y + x * BOARDSIZE])
                terrain, item = id.DECODE_TABLE.get(i, (id.GRASS, id.EMPTY))

                self.board.items[x][y] = item
                self.board.terrain[x][y] = terrain
                if item == id.TANK:
                    self.board.tank = TankRec(x=x, y=y, direction=id.D_UP)

class Graphics:
    GAMEBOARD_OFFSET_X_PX = 0
    GAMEBOARD_OFFSET_Y_PX = 0
    SPRITE_SIZE_PX = 32
    SPRITE_SHEET_ROWS = 6
    SPRITE_SHEET_COLUMNS = 10
    DISPLAY_SIZE = (GAMEBOARD_OFFSET_X_PX * 2 + SPRITE_SIZE_PX * 16,
                    GAMEBOARD_OFFSET_Y_PX * 2 + SPRITE_SIZE_PX * 16)
    TUNNEL_ID_COLOURS = [
        pygame.Color(0xFF0000FF),
        pygame.Color(0x00FF00FF),
        pygame.Color(0x0000FFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0xFF00FFFF),
        pygame.Color(0xFFFFFFFF),
        pygame.Color(0x808080FF),
    ]

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=self.DISPLAY_SIZE, flags=0)
        self.spritesheet = pygame.image.load(DEFAULT_SPRITESHEET_LOC).convert_alpha()
        self.animation_counter = 0

    def _increment_animation_counter(self):
        self.animation_counter = (self.animation_counter + 1) % 3

    def draw_board(self, board: Board):
        for y in range(id.PLAYFIELD_SIZE):
            for x in range(id.PLAYFIELD_SIZE):
                self._draw_sprite(board.terrain[x][y], x, y)
                self._draw_sprite(board.items[x][y], x, y)
        # TODO: Draw tank
        # TODO: Draw tunnel
        pygame.display.update()
        self._increment_animation_counter()

    def _draw_sprite(self, entity_id, square_x, square_y):
        board_location = (
            self.GAMEBOARD_OFFSET_X_PX + (square_x * self.SPRITE_SIZE_PX),
            self.GAMEBOARD_OFFSET_Y_PX + (square_y * self.SPRITE_SIZE_PX),
            self.SPRITE_SIZE_PX,
            self.SPRITE_SIZE_PX
        )
        if entity_id in [id.TANK, id.EMPTY]:
            return
        elif entity_id in id.TunnelID:
            colour = self.TUNNEL_ID_COLOURS[id.TunnelID[entity_id]]
            pygame.draw.rect(self.screen, colour, board_location)
            bmp_id = id.BMP_TUNNEL_MASK
        else:
            try:
                bmp_id = id.SPRITE_MAPPING[entity_id]
            except KeyError:
                assert False, f"Cannot draw entity with ID {entity_id}"

        if isinstance(bmp_id, tuple):
            bmp_id = bmp_id[self.animation_counter]
        sprite_sheet_location = (
            self.SPRITE_SIZE_PX*((bmp_id-1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE_PX*((bmp_id-1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE_PX,
            self.SPRITE_SIZE_PX
        )
        self.screen.blit(self.spritesheet, board_location, sprite_sheet_location)



if __name__ == '__main__':


    game = GameState()
    graphics = Graphics()

    clock = pygame.time.Clock()

    game.load_level(1)
    while True:
        graphics.draw_board(game.board)
        clock.tick(60*10)

    pass