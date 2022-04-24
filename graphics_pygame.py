import pygame

from datastructures import *
from engine import Game

DEFAULT_SPRITESHEET_LOC = "./resources/spritesheet.png"


class Graphics:
    MENUBAR_SIZE = 19
    SPRITE_SIZE = 32  # SpBm_Width, SpBm_Height
    SPRITE_SHEET_ROWS = 6
    SPRITE_SHEET_COLUMNS = 10
    SIDEBAR_SIZE = 187
    GAMEBOARD_SIZE = SPRITE_SIZE * c.PLAYFIELD_SIZE
    BOARD_GUTTER = 17
    OFFSET_LEFT = BOARD_GUTTER  # XOffset
    OFFSET_TOP = BOARD_GUTTER + MENUBAR_SIZE  # YOffset
    DISPLAY_SIZE = (
        OFFSET_LEFT + GAMEBOARD_SIZE + BOARD_GUTTER + SIDEBAR_SIZE,
        OFFSET_TOP + GAMEBOARD_SIZE + BOARD_GUTTER,
    )

    TUNNEL_ID_COLOURS = [
        # c: 0x00bbggrr
        # py:0xrrggbbaa
        pygame.Color(0xFF_00_00_FF),  # Red
        pygame.Color(0x00_FF_00_FF),  # Green
        pygame.Color(0x00_00_FF_FF),  # Blue
        pygame.Color(0x00_FF_FF_FF),  # Cyan
        pygame.Color(0xFF_FF_00_FF),  # Yellow
        pygame.Color(0xFF_00_FF_FF),  # Magenta
        pygame.Color(0xFF_FF_FF_FF),  # White
        pygame.Color(0x80_80_80_FF),  # Gray
    ]

    LASER_COLOURS = {
        c.LaserColorG: pygame.Color(0x00FF00FF),
        c.LaserColorR: pygame.Color(0xFF0000FF),
    }
    LASER_OFFSET = 13  # LaserOffset
    ANIMATION_RATE = 20

    BLACK = pygame.Color(0, 0, 0)
    LIGHT_GRAY = pygame.Color(192, 192, 192)
    GRAY = pygame.Color(128, 128, 128)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    FONT_SIZE_COORDS = 13

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(size=self.DISPLAY_SIZE, flags=0)
        self.spritesheet = pygame.image.load(DEFAULT_SPRITESHEET_LOC).convert_alpha()
        self.animation_counter = 0
        self.animation_rate_counter = 0
        self.screen.fill(self.LIGHT_GRAY)
        self.font = pygame.font.SysFont("arial", size=self.FONT_SIZE_COORDS)

        self.rect_menu = pygame.Rect(0, 0, self.DISPLAY_SIZE[0], self.MENUBAR_SIZE)
        self.rect_playfield = pygame.Rect(self.OFFSET_LEFT, self.OFFSET_TOP, self.GAMEBOARD_SIZE, self.GAMEBOARD_SIZE)
        self.rect_coords = pygame.Rect(0, self.MENUBAR_SIZE,
                                       self.GAMEBOARD_SIZE + self.BOARD_GUTTER + self.BOARD_GUTTER,
                                       self.GAMEBOARD_SIZE + self.BOARD_GUTTER + self.BOARD_GUTTER)

    def _increment_animation_counter(self):
        self.animation_rate_counter += 1
        if self.animation_rate_counter >= self.ANIMATION_RATE:
            self.animation_rate_counter = 0
            self.animation_counter = (self.animation_counter + 1) % 3

    def _draw_text(self, text, position, colour, background):
        rendered_text = self.font.render(str(text), True, colour, background)
        self.screen.blit(rendered_text, rendered_text.get_rect(center=position))

    def _draw_embossed(self, rect: pygame.Rect, inner=True, double=False):
        if inner:
            colour1 = self.WHITE
            colour2 = self.GRAY

            pygame.draw.line(self.screen, colour1, (rect.left + 1, rect.bottom - 2), (rect.left + 1, rect.top + 1))
            pygame.draw.line(self.screen, colour1, (rect.left + 2, rect.top + 1), (rect.right - 3, rect.top + 1))
            pygame.draw.line(self.screen, colour2, (rect.left + 2, rect.bottom - 2), (rect.right - 3, rect.bottom - 2))
            pygame.draw.line(self.screen, colour2, (rect.right - 2, rect.bottom - 2), (rect.right - 2, rect.top + 1))

        else:
            colour1 = self.GRAY
            colour2 = self.WHITE
            pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.bottom), (rect.left - 1, rect.top - 1))
            pygame.draw.line(self.screen, colour1, (rect.left, rect.top - 1), (rect.right - 1, rect.top - 1))
            pygame.draw.line(self.screen, colour2, (rect.left, rect.bottom), (rect.right, rect.bottom))
            pygame.draw.line(self.screen, colour2, (rect.right, rect.bottom - 1), (rect.right, rect.top - 1))
            if double:
                pygame.draw.line(self.screen, colour1, (rect.left - 2, rect.bottom + 1), (rect.left - 2, rect.top - 2))
                pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.top - 2), (rect.right, rect.top - 2))
                pygame.draw.line(self.screen, colour2, (rect.left - 1, rect.bottom + 1),
                                 (rect.right + 1, rect.bottom + 1))
                pygame.draw.line(self.screen, colour2, (rect.right + 1, rect.bottom), (rect.right + 1, rect.top - 2))

    def _draw_board_coords(self):
        for i in range(c.PLAYFIELD_SIZE):
            int_print = str(i + 1)
            x = self.rect_playfield.left - int(self.BOARD_GUTTER / 2) - 1
            y = self.rect_playfield.top + int(self.rect_playfield.height / c.PLAYFIELD_SIZE * (i + 0.5))
            self._draw_text(int_print, (x, y), self.GRAY, self.LIGHT_GRAY)
            x = self.rect_playfield.right + int(self.BOARD_GUTTER / 2)
            self._draw_text(int_print, (x, y), self.GRAY, self.LIGHT_GRAY)

            char_print = chr(ord("A") + i)
            x = self.rect_playfield.left + int(self.rect_playfield.width / c.PLAYFIELD_SIZE * (i + 0.5))
            y = self.rect_playfield.top - int(self.BOARD_GUTTER / 2)
            self._draw_text(char_print, (x, y), self.GRAY, self.LIGHT_GRAY)
            y = self.rect_playfield.bottom + int(self.BOARD_GUTTER / 2)
            self._draw_text(char_print, (x, y), self.GRAY, self.LIGHT_GRAY)

    def draw_board(self, game: Game):
        self._draw_menu()
        self._draw_sidebar()
        self._draw_background()
        self._draw_board_coords()
        self._draw_embossed(self.rect_playfield, inner=False, double=True)
        self._draw_embossed(self.rect_coords)

        for sq in SQUARES:
            self._draw_sprite(game.state.terrain[sq], sq)
            self._draw_sprite(game.state.items[sq], sq)
        self._draw_tank(game.state.tank.sq, game.state.tank.direction)
        if game.state.laser_live:
            self._draw_laser(game.state.laser)
        pygame.display.update()
        self._increment_animation_counter()

    def _draw_menu(self):
        pygame.draw.rect(self.screen, self.WHITE, self.rect_menu, width=0, border_radius=0)

    def _draw_sidebar(self):
        sidebar_rect = pygame.Rect(
            self.OFFSET_LEFT + self.GAMEBOARD_SIZE + self.BOARD_GUTTER,
            self.MENUBAR_SIZE,
            self.SIDEBAR_SIZE,
            self.DISPLAY_SIZE[1] - self.MENUBAR_SIZE
        )
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, sidebar_rect, width=0, border_radius=0)

    def _draw_background(self):
        pass

    def _draw_sprite(self, entity_id, square: Square):
        board_location = (
            self.OFFSET_LEFT + (square.x * self.SPRITE_SIZE),
            self.OFFSET_TOP + (square.y * self.SPRITE_SIZE),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        if entity_id == c.EMPTY:
            # Don't need to draw empty item squares
            return
        elif entity_id in c.TunnelID:
            colour = self.TUNNEL_ID_COLOURS[c.TunnelID[entity_id]]
            pygame.draw.rect(self.screen, colour, board_location)
            bmp_id = c.BMP_TUNNEL_MASK
        else:
            try:
                bmp_id = c.SPRITE_MAPPING[entity_id]
            except KeyError:
                assert False, f"Cannot draw entity with ID {entity_id}"

        if isinstance(bmp_id, tuple):
            bmp_id = bmp_id[self.animation_counter]
        sprite_sheet_location = (
            self.SPRITE_SIZE * ((bmp_id - 1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE
            * ((bmp_id - 1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        self.screen.blit(self.spritesheet, board_location, sprite_sheet_location)

    def _draw_tank(self, square: Square, direction: Direction):
        board_location = (
            self.OFFSET_LEFT + (square.x * self.SPRITE_SIZE),
            self.OFFSET_TOP + (square.y * self.SPRITE_SIZE),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        TANK_DIRECTION_MAPPING = {
            UP: c.TANK_UP,
            RIGHT: c.TANK_RIGHT,
            DOWN: c.TANK_DOWN,
            LEFT: c.TANK_LEFT,
        }
        bmp_id = c.SPRITE_MAPPING[TANK_DIRECTION_MAPPING[direction]]
        sprite_sheet_location = (
            self.SPRITE_SIZE * ((bmp_id - 1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE
            * ((bmp_id - 1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        self.screen.blit(self.spritesheet, board_location, sprite_sheet_location)

    def _draw_laser(self, laser: LaserRec):
        # if laser.Firing:
        colour = self.LASER_COLOURS[laser.colour]
        x = self.OFFSET_LEFT + (laser.sq.x * self.SPRITE_SIZE)
        y = self.OFFSET_TOP + (laser.sq.y * self.SPRITE_SIZE)
        h = self.SPRITE_SIZE / 2
        if laser.dir_front == laser.dir_back:
            # Not deflecting
            if laser.dir_front == UP or laser.dir_front == DOWN:
                # Vertical
                beam = pygame.Rect(
                    x + self.LASER_OFFSET,
                    y,
                    self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    self.SPRITE_SIZE,
                )
            else:
                # Horizontal
                beam = pygame.Rect(
                    x,
                    y + self.LASER_OFFSET,
                    self.SPRITE_SIZE,
                    self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                )
            pygame.draw.rect(self.screen, colour, beam, width=0, border_radius=2)
            pygame.draw.rect(self.screen, self.BLACK, beam, width=1, border_radius=2)
        else:
            # Deflecting off mirror
            # Draw two parts of the reflecting laser
            def laser_dir_to_rect(direction):
                if direction == UP:
                    return pygame.Rect(
                        x + self.LASER_OFFSET,
                        y,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                        h,
                    )
                elif direction == RIGHT:
                    return pygame.Rect(
                        x + h,
                        y + self.LASER_OFFSET,
                        self.SPRITE_SIZE - h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    )
                elif direction == DOWN:
                    return pygame.Rect(
                        x + self.LASER_OFFSET,
                        y + h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                        self.SPRITE_SIZE - h,
                    )
                elif direction == LEFT:
                    return pygame.Rect(
                        x,
                        y + self.LASER_OFFSET,
                        h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    )

            INVERT_DIRECTION = {
                UP: DOWN,
                RIGHT: LEFT,
                DOWN: UP,
                LEFT: RIGHT,
            }

            beam_a = laser_dir_to_rect(laser.dir_front)
            beam_b = laser_dir_to_rect(INVERT_DIRECTION[laser.dir_back])

            pygame.draw.rect(self.screen, colour, beam_a, width=0, border_radius=2)
            pygame.draw.rect(self.screen, self.BLACK, beam_a, width=1, border_radius=2)

            pygame.draw.rect(self.screen, colour, beam_b, width=0, border_radius=2)
            pygame.draw.rect(self.screen, self.BLACK, beam_b, width=1, border_radius=2)

    @staticmethod
    def colour_helper(c_format_str="0x00bbggrr"):
        """Convert a win32 COLORREF value to a hex HTML"""
        # c: 0x00bbggrr
        # py:0xrrggbbaa
        a = "FF"
        r = c_format_str[8:10]
        g = c_format_str[6:8]
        b = c_format_str[4:6]
        return f"0x{r}{g}{b}{a}"
