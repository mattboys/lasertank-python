import random

import pygame

from datastructures import *
from engine import Game

DEFAULT_SPRITESHEET_LOC = "./resources/spritesheet.png"


class Graphics:
    MENUBAR_SIZE = 19
    SPRITE_SIZE = 32  # SpBm_Width, SpBm_Height
    SPRITE_SHEET_ROWS = 6
    SPRITE_SHEET_COLUMNS = 10
    SIDEBAR_SIZE = 240
    INFO_HEIGHT = 324
    GAMEBOARD_SIZE = SPRITE_SIZE * c.PLAYFIELD_SIZE
    BOARD_GUTTER = 24
    COODRS_PADDING = 20
    # rect_playfield.left = BOARD_GUTTER  # XOffset
    # OFFSET_TOP = BOARD_GUTTER + MENUBAR_SIZE  # YOffset
    DISPLAY_SIZE = (
        2 * COODRS_PADDING + GAMEBOARD_SIZE + BOARD_GUTTER + SIDEBAR_SIZE,
        2 * COODRS_PADDING + GAMEBOARD_SIZE + BOARD_GUTTER,
    )
    BRICK_SIZE = (13, 7)

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

    FONT_SIZE_COORDS = 13
    FONT_SIZE_INFO_TITLE = 17
    FONT_SIZE_INFO = 15

    BLACK = pygame.Color(0, 0, 0)
    LIGHT_GRAY = pygame.Color(192, 192, 192)
    GRAY = pygame.Color(128, 128, 128)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    RED_BRICK_SPECK = pygame.Color(128, 0, 0)
    BLUE = pygame.Color(0, 0, 255)
    CYAN = pygame.Color(0, 255, 255)
    DARK_YELLOW = pygame.Color(128, 128, 0)
    GREEN = pygame.Color(0, 255, 0)

    def __init__(self, framerate=100):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.framerate = framerate
        self.screen = pygame.display.set_mode(size=self.DISPLAY_SIZE, flags=0)
        # self.screen = pygame.display.set_mode(size=self.DISPLAY_SIZE, flags=pygame.RESIZABLE)
        self.spritesheet = pygame.image.load(DEFAULT_SPRITESHEET_LOC).convert_alpha()
        self.animation_counter = 0
        self.animation_rate_counter = 0
        self.screen.fill(self.LIGHT_GRAY)

        self.font_coords = pygame.font.SysFont("arial", size=self.FONT_SIZE_COORDS)
        self.font_info_title = pygame.font.SysFont("palatinolinotype", size=self.FONT_SIZE_INFO_TITLE)
        self.font_info_title.set_bold(True)
        self.font_info = pygame.font.SysFont("arial", size=self.FONT_SIZE_INFO)

        self.rect_menu = pygame.Rect(0, 0, self.screen.get_width(), self.MENUBAR_SIZE)
        height_remaining = self.screen.get_height() - self.rect_menu.height
        self.rect_playfield_zone = pygame.Rect(0, self.rect_menu.bottom, height_remaining, height_remaining)

        self.rect_playfield = pygame.Rect(0, 0, self.GAMEBOARD_SIZE, self.GAMEBOARD_SIZE)
        self.rect_playfield.center = self.rect_playfield_zone.center

        self.rect_coords = self.rect_playfield.inflate(self.COODRS_PADDING * 2, self.COODRS_PADDING * 2)

        self.rect_info = pygame.Rect(self.rect_coords.right, self.rect_coords.top,
                                     self.DISPLAY_SIZE[0] - self.rect_coords.right - 1, self.INFO_HEIGHT)
        self.rect_buttons = pygame.Rect(self.rect_info.left, self.rect_info.bottom,
                                        self.DISPLAY_SIZE[0] - self.rect_coords.right - 1,
                                        self.DISPLAY_SIZE[1] - self.rect_info.bottom - 1)

        self._draw_menu()
        self._draw_sidebar()
        self._draw_bricks_background()

    def _increment_animation_counter(self):
        self.animation_rate_counter += 1
        if self.animation_rate_counter >= self.ANIMATION_RATE:
            self.animation_rate_counter = 0
            self.animation_counter = (self.animation_counter + 1) % 3

    def _draw_text(self, text, position, colour, background, font):
        rendered_text = font.render(str(text), True, colour, background)
        self.screen.blit(rendered_text, rendered_text.get_rect(center=position))

    # def _draw_embossed(self, rect: pygame.Rect, inner=True, double=False):
    #     if inner:
    #         colour1 = self.WHITE
    #         colour2 = self.GRAY
    #
    #         pygame.draw.line(self.screen, colour1, (rect.left + 1, rect.bottom - 2), (rect.left + 1, rect.top + 1))
    #         pygame.draw.line(self.screen, colour1, (rect.left + 2, rect.top + 1), (rect.right - 3, rect.top + 1))
    #         pygame.draw.line(self.screen, colour2, (rect.left + 2, rect.bottom - 2), (rect.right - 3, rect.bottom - 2))
    #         pygame.draw.line(self.screen, colour2, (rect.right - 2, rect.bottom - 2), (rect.right - 2, rect.top + 1))
    #
    #     else:
    #         colour1 = self.GRAY
    #         colour2 = self.WHITE
    #         pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.bottom), (rect.left - 1, rect.top - 1))
    #         pygame.draw.line(self.screen, colour1, (rect.left, rect.top - 1), (rect.right - 1, rect.top - 1))
    #         pygame.draw.line(self.screen, colour2, (rect.left, rect.bottom), (rect.right, rect.bottom))
    #         pygame.draw.line(self.screen, colour2, (rect.right, rect.bottom - 1), (rect.right, rect.top - 1))
    #         if double:
    #             pygame.draw.line(self.screen, colour1, (rect.left - 2, rect.bottom + 1), (rect.left - 2, rect.top - 2))
    #             pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.top - 2), (rect.right, rect.top - 2))
    #             pygame.draw.line(self.screen, colour2, (rect.left - 1, rect.bottom + 1),
    #                              (rect.right + 1, rect.bottom + 1))
    #             pygame.draw.line(self.screen, colour2, (rect.right + 1, rect.bottom), (rect.right + 1, rect.top - 2))

    def _draw_buttons(self):

        pygame.draw.rect(self.screen, self.CYAN, self.rect_buttons.inflate(-20, -20))

    def _draw_embossed_out(self, rect: pygame.Rect):
        """ Overlays one pixel of embossed-out effect lines on INSIDE of rect """
        colour1 = self.WHITE
        colour2 = self.GRAY

        pygame.draw.line(self.screen, colour1, (rect.left, rect.bottom - 1), (rect.left, rect.top))
        pygame.draw.line(self.screen, colour1, (rect.left + 1, rect.top), (rect.right - 2, rect.top))
        pygame.draw.line(self.screen, colour2, (rect.left + 1, rect.bottom - 1), (rect.right - 2, rect.bottom - 1))
        pygame.draw.line(self.screen, colour2, (rect.right - 1, rect.bottom - 1), (rect.right - 1, rect.top))

    def _draw_embossed_in(self, rect: pygame.Rect):
        """ Overlays one pixel of embossed-in effect lines on INSIDE of rect """
        colour1 = self.GRAY
        colour2 = self.WHITE

        pygame.draw.line(self.screen, colour1, (rect.left, rect.bottom - 1), (rect.left, rect.top))
        pygame.draw.line(self.screen, colour1, (rect.left + 1, rect.top), (rect.right - 2, rect.top))
        pygame.draw.line(self.screen, colour2, (rect.left + 1, rect.bottom - 1), (rect.right - 2, rect.bottom - 1))
        pygame.draw.line(self.screen, colour2, (rect.right - 1, rect.bottom - 1), (rect.right - 1, rect.top))

    def _draw_embossed_in_double(self, rect: pygame.Rect):
        """ Adds two pixels of embossed-in effect lines on OUTSIDE of rect """
        colour1 = self.GRAY
        colour2 = self.WHITE
        pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.bottom), (rect.left - 1, rect.top - 1))
        pygame.draw.line(self.screen, colour1, (rect.left, rect.top - 1), (rect.right - 1, rect.top - 1))
        pygame.draw.line(self.screen, colour2, (rect.left, rect.bottom), (rect.right, rect.bottom))
        pygame.draw.line(self.screen, colour2, (rect.right, rect.bottom - 1), (rect.right, rect.top - 1))

        pygame.draw.line(self.screen, colour1, (rect.left - 2, rect.bottom + 1), (rect.left - 2, rect.top - 2))
        pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.top - 2), (rect.right, rect.top - 2))
        pygame.draw.line(self.screen, colour2, (rect.left - 1, rect.bottom + 1), (rect.right + 1, rect.bottom + 1))
        pygame.draw.line(self.screen, colour2, (rect.right + 1, rect.bottom), (rect.right + 1, rect.top - 2))

    def _draw_board_coords(self):
        for i in range(c.PLAYFIELD_SIZE):
            int_print = str(i + 1)
            x = self.rect_playfield.left - int(self.BOARD_GUTTER / 2) + 1
            y = self.rect_playfield.top + int(self.rect_playfield.height / c.PLAYFIELD_SIZE * (i + 0.5))
            self._draw_text(int_print, (x, y), self.GRAY, self.LIGHT_GRAY, self.font_coords)

            x = self.rect_playfield.right + int(self.BOARD_GUTTER / 2) - 2
            self._draw_text(int_print, (x, y), self.GRAY, self.LIGHT_GRAY, self.font_coords)

            char_print = chr(ord("A") + i)
            x = self.rect_playfield.left + int(self.rect_playfield.width / c.PLAYFIELD_SIZE * (i + 0.5))
            y = self.rect_playfield.top - int(self.BOARD_GUTTER / 2)
            self._draw_text(char_print, (x, y), self.GRAY, self.LIGHT_GRAY, self.font_coords)

            y = self.rect_playfield.bottom + int(self.BOARD_GUTTER / 2) - 3
            self._draw_text(char_print, (x, y), self.GRAY, self.LIGHT_GRAY, self.font_coords)

    def draw(self, game: Game):

        self._draw_board_coords()
        self._draw_embossed_in_double(self.rect_playfield)
        self._draw_embossed_out(self.rect_coords)
        self._draw_level_info()
        self._draw_playfield(game)
        self._draw_buttons()

        pygame.display.update()
        self.clock.tick(self.framerate)

    def _draw_playfield(self, game: Game):
        for sq in SQUARES:
            self._draw_sprite(game.state.terrain[sq], sq)
            self._draw_sprite(game.state.items[sq], sq)
        self._draw_tank(game.state.tank.sq, game.state.tank.direction)
        if game.state.laser_live:
            self._draw_laser(game.state.laser)
        self._increment_animation_counter()

    def _draw_menu(self):
        # pygame.draw.rect(self.screen, self.WHITE, self.rect_menu, width=0, border_radius=0)
        pass

    def _draw_sidebar(self):
        pass
        # sidebar_rect = pygame.Rect(
        #     self.rect_playfield.left + self.GAMEBOARD_SIZE + self.BOARD_GUTTER,
        #     self.MENUBAR_SIZE,
        #     self.SIDEBAR_SIZE,
        #     self.DISPLAY_SIZE[1] - self.MENUBAR_SIZE
        # )
        # pygame.draw.rect(self.screen, self.LIGHT_GRAY, sidebar_rect, width=0, border_radius=0)

    def _draw_info_text_boxed_title(self, text: str, x, y):

        height = 23
        padding = 20

        rendered_text = self.font_info_title.render(text, True, self.BLUE, self.LIGHT_GRAY)
        rendered_text_rect = rendered_text.get_rect()

        background_text = pygame.Rect(0, 0, rendered_text_rect.width + 2 * padding, height)
        background_text.center = (x, y)
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, background_text.inflate(-2, -2))
        self._draw_embossed_out(background_text)
        crop = rendered_text.get_rect(height=height - 6)

        self.screen.blit(rendered_text, rendered_text.get_rect(center=(x, y + 1)), crop)

    def _draw_info_text_boxed_info(self, text: str, width, x, y):

        height = 23

        rendered_text = self.font_info.render(text, True, self.CYAN, self.BLACK)
        rendered_text_rect = rendered_text.get_rect()
        background_text = pygame.Rect(0, 0, width, height)
        background_text.center = (x, y)
        pygame.draw.rect(self.screen, self.BLACK, background_text)
        self._draw_embossed_in_double(background_text)
        crop = rendered_text.get_rect(height=height)

        self.screen.blit(rendered_text, rendered_text.get_rect(center=(x, y - 1)), crop)

    def _draw_text_in_rect(self, text: str, rect: pygame.rect, rect_colour, text_colour, font: pygame.font.Font):
        """ Draw a box at rect with the colour rect_colour and the text centred in the rect """

        rendered_text = font.render(text, True, text_colour, rect_colour)
        rendered_text_rect = rendered_text.get_rect(center=rect.center, height=rect.height)

        pygame.draw.rect(self.screen, rect_colour, rect)

        self.screen.blit(rendered_text, rendered_text_rect)

    def _draw_level_info(self):
        padding_small = 28
        padding_large = 40

        x = self.rect_info.centerx
        y = self.rect_info.top + padding_small

        self._draw_info_text_boxed_title("Level Number", x, y)
        y += padding_small
        self._draw_info_text_boxed_info("1 - Easy", int(self.rect_info.width * 0.6), x, y)
        y += padding_large
        self._draw_info_text_boxed_title("Level Name", x, y)
        y += padding_small
        self._draw_info_text_boxed_info("Boot Camp", int(self.rect_info.width - padding_small), x, y)
        y += padding_large
        self._draw_info_text_boxed_title("Author", x, y)
        y += padding_small
        self._draw_info_text_boxed_info("Jim Kindley", int(self.rect_info.width - padding_small), x, y)

        y += padding_large
        x = self.rect_info.centerx - int(self.rect_info.width / 4) + 5
        moves_rect = pygame.Rect(0, y, 100, 65)
        moves_rect.centerx = x
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, moves_rect)
        self._draw_embossed_out(moves_rect)

        moves_rect_title = pygame.Rect(0, y, 80, 24)
        moves_rect_title.midtop = moves_rect.midtop
        moves_rect_title.y += 3
        self._draw_text_in_rect("Moves", moves_rect_title, self.LIGHT_GRAY, self.DARK_YELLOW, self.font_info_title)

        moves_rect_counter = pygame.Rect(0, y, 80, 24)
        moves_rect_counter.midtop = moves_rect.center
        self._draw_text_in_rect("888", moves_rect_counter, self.BLACK, self.GREEN, self.font_info)
        self._draw_embossed_in_double(moves_rect_counter)

        x = self.rect_info.centerx + int(self.rect_info.width / 4) - 5
        shoot_rect = pygame.Rect(0, y, 100, 65)
        shoot_rect.centerx = x
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, shoot_rect)
        self._draw_embossed_out(shoot_rect)

        shoot_rect_title = pygame.Rect(0, y, 80, 24)
        shoot_rect_title.midtop = shoot_rect.midtop
        shoot_rect_title.y += 3
        self._draw_text_in_rect("Shots", shoot_rect_title, self.LIGHT_GRAY, self.DARK_YELLOW, self.font_info_title)

        shoot_rect_counter = pygame.Rect(0, y, 80, 24)
        shoot_rect_counter.midtop = shoot_rect.center
        self._draw_text_in_rect("555", shoot_rect_counter, self.BLACK, self.GREEN, self.font_info)
        self._draw_embossed_in_double(shoot_rect_counter)

    def _draw_bricks_background(self):
        brick_background_rect = self.rect_info.inflate(-4, -4)
        brick_background = pygame.Surface(brick_background_rect.size)
        wall_bmp = c.SPRITE_MAPPING[c.WALL]
        sprite_sheet_location = (
            self.SPRITE_SIZE * ((wall_bmp - 1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE
            * ((wall_bmp - 1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        brick_rect = pygame.Rect(0, brick_background_rect.height, self.SPRITE_SIZE, self.SPRITE_SIZE)
        # brick_rect.bottomleft = brick_background_rect.
        for col in range(1 + int(brick_background_rect.width / brick_rect.width)):
            for row in range(1 + int(brick_background_rect.height / brick_rect.height)):
                brick_rect.bottom = -1 + brick_background_rect.height - row * brick_rect.height
                brick_rect.left = col * brick_rect.width
                brick_background.blit(self.spritesheet, brick_rect, sprite_sheet_location)
        pygame.draw.line(brick_background, self.BLACK, (brick_background_rect.left, brick_background_rect.bottom - 1),
                         (brick_background_rect.right, brick_background_rect.bottom - 1))
        crop = brick_background.get_rect(width=brick_background_rect.width, height=brick_background_rect.height,
                                         bottomleft=brick_background.get_rect().bottomleft)
        location = crop.copy()
        location.bottomleft = brick_background_rect.bottomleft
        self.screen.blit(brick_background, brick_background_rect, crop)

        self._draw_embossed_out(self.rect_info)

    def _draw_background(self):
        pass

    def _draw_sprite(self, entity_id, square: Square):

        board_location = (
            self.rect_playfield.left + (square.x * self.SPRITE_SIZE),
            self.rect_playfield.top + (square.y * self.SPRITE_SIZE),
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
            self.rect_playfield.left + (square.x * self.SPRITE_SIZE),
            self.rect_playfield.top + (square.y * self.SPRITE_SIZE),
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
        x = self.rect_playfield.left + (laser.sq.x * self.SPRITE_SIZE)
        y = self.rect_playfield.top + (laser.sq.y * self.SPRITE_SIZE)
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
