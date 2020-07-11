from pathlib import Path
from enum import Enum

import pygame

import lasertank
import sprites

files = {
        "Grass": ["grass_0.png",],
        "Flag": ["flag_0.png","flag_1.png","flag_2.png",],
        "Water": ["water_0.png","water_1.png","water_2.png",],
        "Conveyor_N": ["conveyor_N_0.png","conveyor_N_1.png","conveyor_N_2.png",],
        "Conveyor_S": ["conveyor_S_0.png","conveyor_S_1.png","conveyor_S_2.png",],
        "Conveyor_E": ["conveyor_E_0.png","conveyor_E_1.png","conveyor_E_2.png",],
        "Conveyor_W": ["conveyor_W_0.png","conveyor_W_1.png","conveyor_W_2.png",],
        "Ice": ["ice_0.png",],
        "ThinIce": ["ice_thin_0.png",],
        "Bridge": ["bridge_0.png",],
        "Tunnel_0": ["tunnel_a_0.png",],
        "Tunnel_1": ["tunnel_b_0.png",],
        "Tunnel_2": ["tunnel_c_0.png",],
        "Tunnel_3": ["tunnel_d_0.png",],
        "Tunnel_4": ["tunnel_e_0.png",],
        "Tunnel_5": ["tunnel_f_0.png",],
        "Tunnel_6": ["tunnel_g_0.png",],
        "Tunnel_7": ["tunnel_h_0.png",],
        "Tunnel_8": ["tunnel_a_0.png",],
        "Tunnel_9": ["tunnel_a_0.png",],
        "Tank_N": ["tank_N_0.png",],
        "Tank_S": ["tank_S_0.png",],
        "Tank_E": ["tank_E_0.png",],
        "Tank_W": ["tank_W_0.png",],
        "Solid": ["solid_0.png",],
        "Block": ["block_0.png"],
        "Wall": ["wall_0.png",],
        "Antitank_N": ["antitank_N_0.png", "antitank_N_1.png", "antitank_N_2.png"],
        "Antitank_S": ["antitank_S_0.png", "antitank_S_1.png", "antitank_S_2.png"],
        "Antitank_E": ["antitank_E_0.png", "antitank_E_1.png", "antitank_E_2.png"],
        "Antitank_W": ["antitank_W_0.png", "antitank_W_1.png", "antitank_W_2.png"],
        "DeadAntitank_N": ["antitank_dead_N_0.png"],
        "DeadAntitank_S": ["antitank_dead_S_0.png"],
        "DeadAntitank_E": ["antitank_dead_E_0.png"],
        "DeadAntitank_W": ["antitank_dead_W_0.png"],
        "Mirror_NW": ["mirror_NW_0.png",],
        "Mirror_NE": ["mirror_NE_0.png",],
        "Mirror_SE": ["mirror_SE_0.png",],
        "Mirror_SW": ["mirror_SW_0.png",],
        "Glass_none": ["glass_0.png"],
        "Glass_red": ["glass_red_0.png"],
        "Glass_green": ["glass_green_0.png"],
        "RotMirror_NW": ["rotmirror_NW_0.png",],
        "RotMirror_NE": ["rotmirror_NE_0.png",],
        "RotMirror_SE": ["rotmirror_SE_0.png",],
        "RotMirror_SW": ["rotmirror_SW_0.png",],
    }


class Graphics:
    SPRITE_SIZE = 32
    GAMEBOARD_OFFSET_X = 0
    GAMEBOARD_OFFSET_Y = 0
    ANIMATION_SPEED = 8
    MAX_FRAMES_LCM = 3
    FPS = 2

    frames = {}  # Same structure as files but with pygame.Surface objects

    def __init__(self, image_dir="images"):
        image_dir = Path(image_dir)
        if not image_dir.is_dir():
            image_dir = Path.cwd() / image_dir

        pygame.init()
        pygame.display.set_mode()
        self.clock = pygame.time.Clock()

        DISPLAY_SIZE = (self.GAMEBOARD_OFFSET_X * 2 + self.SPRITE_SIZE * 16,
                             self.GAMEBOARD_OFFSET_Y * 2 +self.SPRITE_SIZE * 16)
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.screen.fill(pygame.Color('white'))
        # Populate frames dir with the image files from files
        for obj_name, file_list in files.items():
            for image_file in file_list:
                if obj_name not in self.frames:
                    self.frames[obj_name] = []
                image_filename = image_dir / image_file
                if not image_filename.is_file():
                    print(f'Could not load frame from {image_filename.resolve()}')
                try:
                    frame = pygame.image.load(str(image_filename)).convert_alpha()
                    self.frames[obj_name].append(frame)
                except pygame.error:
                    print(f'Could not load frame from {image_filename.resolve()}')
        self.animation_frame_number = 0
        self.frame_speed_counter = 0

    def render(self, game: lasertank.GameState):
        self.frame_speed_counter += 1
        if self.frame_speed_counter >= self.ANIMATION_SPEED:
            self.frame_speed_counter = 0
            self.animation_frame_number = (self.animation_frame_number + 1) % self.MAX_FRAMES_LCM

        for y in range(game.GAMEBOARD_SIZE):
            for x in range(game.GAMEBOARD_SIZE):
                position = (x, y)
                self.draw(game.get_terrain(position))
                self.draw(game.get_item(position))
        self.draw(game.get_tank())
        self.draw_laser(game.get_laser())

        pygame.display.update()

        self.clock.tick(self.FPS)

    def draw(self, game_object: sprites.LaserTankObject):
        obj_name = type(game_object).__name__
        position_x, position_y = game_object.position
        location = (self.GAMEBOARD_OFFSET_X + self.SPRITE_SIZE * position_x,
                    self.GAMEBOARD_OFFSET_Y + self.SPRITE_SIZE * position_y)
        if obj_name == "Empty":
            return
        for attribute in ['colour', 'dir', 'angle', 'tunnel_id']:
            if hasattr(game_object, attribute):
                # TODO: Remove reliance on checking if Enum
                value = getattr(game_object, attribute)
                if isinstance(value, Enum):
                    value = value.value
                obj_name = obj_name + "_" + str(value)
        frame_list = self.frames[obj_name]
        current_fame = frame_list[self.animation_frame_number % len(frame_list)]

        self.screen.blit(current_fame, location)



    def draw_laser(self, laser: sprites.Laser):
        pass


