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

class LaserRec:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Dir = id.D_UP
        self.Firing = False  # Does it exist on the board?
        self.Good = False
        # Other laser-related fields
        self.oDir = id.D_LEFT
        self.LaserColor = id.LaserColorR
        self.LaserBounceOnIce = False  # If laser bouncing off sliding mirror
        self.ConvMoving = False

class Board:
    def __init__(self):
        self.terrain = [[id.GRASS for y in range(BOARDSIZE)] for x in range(BOARDSIZE)]
        self.items = [[id.EMPTY for y in range(BOARDSIZE)] for x in range(BOARDSIZE)]
        self.tank = TankRec(x=7, y=15, direction=id.D_UP)
        self.laser = LaserRec()

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
                # Tank is not placed in the items array
                if item == id.TANK:
                    self.board.tank = TankRec(x=x, y=y, direction=id.D_UP)
                else:
                    self.board.items[x][y] = item
                self.board.terrain[x][y] = terrain

class Graphics:
    GAMEBOARD_OFFSET_X_PX = 17  # XOffset
    GAMEBOARD_OFFSET_Y_PX = 17  # YOffset
    SPRITE_SIZE = 32  # SpBm_Width, SpBm_Height
    SPRITE_SHEET_ROWS = 6
    SPRITE_SHEET_COLUMNS = 10
    DISPLAY_SIZE = (GAMEBOARD_OFFSET_X_PX * 2 + SPRITE_SIZE * 16,
                    GAMEBOARD_OFFSET_Y_PX * 2 + SPRITE_SIZE * 16)
    TUNNEL_ID_COLOURS = [
        # c: 0x00bbggrr
        # py:0xrrggbbaa
        pygame.Color(0xFF0000FF),
        pygame.Color(0x00FF00FF),
        pygame.Color(0x0000FFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0xFF00FFFF),
        pygame.Color(0xFFFFFFFF),
        pygame.Color(0x808080FF),
    ]

    LASER_COLOURS = {
        id.LaserColorG: pygame.Color(0x00FF00FF),
        id.LaserColorR: pygame.Color(0xFF0000FF),
    }
    LASER_OFFSET = 13  # LaserOffset
    BLACK = pygame.Color(0x000000FF)

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
        self._draw_tank(board.tank.X, board.tank.Y, board.tank.Dir)
        self._draw_laser(board.laser.Dir, board.laser.oDir, board.laser.X, board.laser.Y, board.laser.LaserColor)
        pygame.display.update()
        self._increment_animation_counter()

    def _draw_sprite(self, entity_id, square_x, square_y):
        board_location = (
            self.GAMEBOARD_OFFSET_X_PX + (square_x * self.SPRITE_SIZE),
            self.GAMEBOARD_OFFSET_Y_PX + (square_y * self.SPRITE_SIZE),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE
        )
        if entity_id == id.EMPTY:
            # Don't need to draw empty item squares
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
            self.SPRITE_SIZE * ((bmp_id - 1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE * ((bmp_id - 1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE
        )
        self.screen.blit(self.spritesheet, board_location, sprite_sheet_location)

    def _draw_tank(self, square_x, square_y, direction):
        board_location = (
            self.GAMEBOARD_OFFSET_X_PX + (square_x * self.SPRITE_SIZE),
            self.GAMEBOARD_OFFSET_Y_PX + (square_y * self.SPRITE_SIZE),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE
        )
        bmp_id = id.SPRITE_MAPPING[id.GetTankDirectional[direction]]
        sprite_sheet_location = (
            self.SPRITE_SIZE * ((bmp_id - 1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE * ((bmp_id - 1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE
        )
        self.screen.blit(self.spritesheet, board_location, sprite_sheet_location)

    def _draw_laser(self, direction_a, direction_b, square_x, square_y, laser_colour_id):
        colour = self.LASER_COLOURS[laser_colour_id]
        x = self.GAMEBOARD_OFFSET_X_PX + (square_x * self.SPRITE_SIZE)
        y = self.GAMEBOARD_OFFSET_Y_PX + (square_y * self.SPRITE_SIZE)
        h = self.SPRITE_SIZE / 2
        if direction_a == direction_b:
            # Not deflecting
            if direction_a == id.D_UP or direction_a == id.D_DOWN:
                # Vertical
                beam = pygame.Rect(
                    x + self.LASER_OFFSET,
                    y,
                    self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    self.SPRITE_SIZE
                )
            else:
                # Horizontal
                beam = pygame.Rect(
                    x,
                    y + self.LASER_OFFSET,
                    self.SPRITE_SIZE,
                    self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET
                )
            pygame.draw.rect(self.screen, self.BLACK, beam, 3)
            pygame.draw.rect(self.screen, colour, beam)
        else:
            # Deflecting off mirror
            # Draw two parts of the reflecting laser
            if direction_a == id.D_UP:
                beam_a = pygame.Rect(
                    x + self.LASER_OFFSET,
                    y + h,
                    x + self.SPRITE_SIZE - self.LASER_OFFSET,
                    y + self.SPRITE_SIZE,
                )
            elif direction_a == id.D_RIGHT:
                beam_a = pygame.Rect(
                    x,
                    y + self.LASER_OFFSET,
                    x + h,
                    y + self.SPRITE_SIZE - self.LASER_OFFSET
                )
            elif direction_a == id.D_DOWN:
                beam_a = pygame.Rect(
                    x + self.LASER_OFFSET,
                    y,
                    x + self.SPRITE_SIZE - self.LASER_OFFSET,
                    y + h
                )
            elif direction_a == id.D_LEFT:
                beam_a = pygame.Rect(
                    x + h,
                    y + self.LASER_OFFSET,
                    x + self.SPRITE_SIZE,
                    y + self.SPRITE_SIZE - self.LASER_OFFSET,
                )
            else:
                return

            if direction_b == id.D_UP:
                beam_b = pygame.Rect(
                    x + self.LASER_OFFSET,
                    y,
                    x + self.SPRITE_SIZE - self.LASER_OFFSET,
                    y + h
                )
            elif direction_b == id.D_RIGHT:
                beam_b = pygame.Rect(
                    x + h,
                    y + self.LASER_OFFSET,
                    x + self.SPRITE_SIZE,
                    y + self.SPRITE_SIZE - self.LASER_OFFSET,
                )
            elif direction_b == id.D_DOWN:
                beam_b = pygame.Rect(
                    x + self.LASER_OFFSET,
                    y + h,
                    x + self.SPRITE_SIZE - self.LASER_OFFSET,
                    y + self.SPRITE_SIZE,
                )
            elif direction_b == id.D_LEFT:
                beam_b = pygame.Rect(
                    x,
                    y + self.LASER_OFFSET,
                    x + h,
                    y + self.SPRITE_SIZE - self.LASER_OFFSET
                )
            else:
                return

            pygame.draw.rect(self.screen, self.BLACK, beam_a, 3)
            pygame.draw.rect(self.screen, self.BLACK, beam_b, 3)
            pygame.draw.rect(self.screen, colour, beam_a)
            pygame.draw.rect(self.screen, colour, beam_b)


def colour_helper(c_format_str = '0x00bbggrr'):
    """ Convert a win32 COLORREF value to a hex HTML """
    # c: 0x00bbggrr
    # py:0xrrggbbaa
    a = "FF"
    r = c_format_str[8:10]
    g = c_format_str[6:8]
    b = c_format_str[4:6]
    return f'0x{r}{g}{b}{a}'



if __name__ == '__main__':


    game = GameState()
    graphics = Graphics()

    clock = pygame.time.Clock()

    game.load_level(1)
    while True:
        graphics.draw_board(game.board)
        clock.tick(10)

    pass