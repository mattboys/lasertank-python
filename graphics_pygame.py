from pathlib import Path
from enum import Enum

import pygame

import lasertank
import sprites

files = {
    "Grass": ["grass_0.png", ],
    "Flag": ["flag_0.png", "flag_1.png", "flag_2.png", ],
    "Water": ["water_0.png", "water_1.png", "water_2.png", ],
    "Conveyor_N": ["conveyor_N_0.png", "conveyor_N_1.png", "conveyor_N_2.png", ],
    "Conveyor_S": ["conveyor_S_0.png", "conveyor_S_1.png", "conveyor_S_2.png", ],
    "Conveyor_E": ["conveyor_E_0.png", "conveyor_E_1.png", "conveyor_E_2.png", ],
    "Conveyor_W": ["conveyor_W_0.png", "conveyor_W_1.png", "conveyor_W_2.png", ],
    "Ice": ["ice_0.png", ],
    "ThinIce": ["ice_thin_0.png", ],
    "Bridge": ["bridge_0.png", ],
    "Tunnel_0": ["tunnel_0_0.png", ],
    "Tunnel_1": ["tunnel_1_0.png", ],
    "Tunnel_2": ["tunnel_2_0.png", ],
    "Tunnel_3": ["tunnel_3_0.png", ],
    "Tunnel_4": ["tunnel_4_0.png", ],
    "Tunnel_5": ["tunnel_5_0.png", ],
    "Tunnel_6": ["tunnel_6_0.png", ],
    "Tunnel_7": ["tunnel_7_0.png", ],
    "Tunnel_8": ["tunnel_Null_0.png", ],
    "Tunnel_9": ["tunnel_Null_0.png", ],
    "Tank_N": ["tank_N_0.png", ],
    "Tank_S": ["tank_S_0.png", ],
    "Tank_E": ["tank_E_0.png", ],
    "Tank_W": ["tank_W_0.png", ],
    "Solid": ["solid_0.png", ],
    "Block": ["block_0.png"],
    "Wall": ["wall_0.png", ],
    "Antitank_N": ["antitank_N_0.png", "antitank_N_1.png", "antitank_N_2.png"],
    "Antitank_S": ["antitank_S_0.png", "antitank_S_1.png", "antitank_S_2.png"],
    "Antitank_E": ["antitank_E_0.png", "antitank_E_1.png", "antitank_E_2.png"],
    "Antitank_W": ["antitank_W_0.png", "antitank_W_1.png", "antitank_W_2.png"],
    "AntitankDead_N": ["antitank_dead_N_0.png"],
    "AntitankDead_S": ["antitank_dead_S_0.png"],
    "AntitankDead_E": ["antitank_dead_E_0.png"],
    "AntitankDead_W": ["antitank_dead_W_0.png"],
    "Mirror_N": ["mirror_NW_0.png", ],
    "Mirror_E": ["mirror_NE_0.png", ],
    "Mirror_S": ["mirror_SE_0.png", ],
    "Mirror_W": ["mirror_SW_0.png", ],
    "Glass_none": ["glass_0.png"],
    "Glass_red": ["glass_red_0.png"],
    "Glass_green": ["glass_green_0.png"],
    "RotMirror_N": ["rotmirror_NW_0.png", ],
    "RotMirror_E": ["rotmirror_NE_0.png", ],
    "RotMirror_S": ["rotmirror_SE_0.png", ],
    "RotMirror_W": ["rotmirror_SW_0.png", ],
    "laser_green_EE": ["laser_green_EE_0.png", ],
    "laser_green_EW": ["laser_green_EW_0.png", ],
    "laser_green_NE": ["laser_green_NE_0.png", ],
    "laser_green_NN": ["laser_green_NN_0.png", ],
    "laser_green_NS": ["laser_green_NS_0.png", ],
    "laser_green_NW": ["laser_green_NW_0.png", ],
    "laser_green_SE": ["laser_green_SE_0.png", ],
    "laser_green_SS": ["laser_green_SS_0.png", ],
    "laser_green_SW": ["laser_green_SW_0.png", ],
    "laser_green_WW": ["laser_green_WW_0.png", ],
    "laser_red_EE": ["laser_red_EE_0.png", ],
    "laser_red_EW": ["laser_red_EW_0.png", ],
    "laser_red_NE": ["laser_red_NE_0.png", ],
    "laser_red_NN": ["laser_red_NN_0.png", ],
    "laser_red_NS": ["laser_red_NS_0.png", ],
    "laser_red_NW": ["laser_red_NW_0.png", ],
    "laser_red_SE": ["laser_red_SE_0.png", ],
    "laser_red_SS": ["laser_red_SS_0.png", ],
    "laser_red_SW": ["laser_red_SW_0.png", ],
    "laser_red_WW": ["laser_red_WW_0.png", ],
}

class Graphics:
    SPRITE_SIZE = 32
    GAMEBOARD_OFFSET_X = 0
    GAMEBOARD_OFFSET_Y = 0
    ANIMATION_SPEED = 8
    MAX_FRAMES_LCM = 3
    FPS = 60

    frames = {}  # Same structure as files but with pygame.Surface objects

    def __init__(self, image_dir="images"):
        image_dir = Path(image_dir)
        if not image_dir.is_dir():
            image_dir = Path.cwd() / image_dir

        pygame.init()
        pygame.display.set_mode()
        self.clock = pygame.time.Clock()

        DISPLAY_SIZE = (self.GAMEBOARD_OFFSET_X * 2 + self.SPRITE_SIZE * 16,
                        self.GAMEBOARD_OFFSET_Y * 2 + self.SPRITE_SIZE * 16)
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
        for attribute in ['_colour', 'direction', 'angle', 'tunnel_id']:
            if hasattr(game_object, attribute):
                value = getattr(game_object, attribute)
                obj_name = obj_name + "_" + str(value)
        if obj_name not in self.frames:
            print(f"ERROR: Cannot find sprite for object {obj_name}")
            return
        frame_list = self.frames[obj_name]
        current_fame = frame_list[self.animation_frame_number % len(frame_list)]

        self.screen.blit(current_fame, location)

    def draw_laser(self, laser: sprites.Laser):
        if not laser.exists:
            return
        position_x, position_y = laser.position
        location = (self.GAMEBOARD_OFFSET_X + self.SPRITE_SIZE * position_x,
                    self.GAMEBOARD_OFFSET_Y + self.SPRITE_SIZE * position_y)
        # Fix syntax of directions
        dir1 = laser.direction
        if laser.from_direction == sprites.Direction.NONE:
            dir2 = dir1
        else:
            dir2 = laser.from_direction
        obj_name = f"laser_{laser.colour}_{dir1}{dir2}"
        if obj_name not in self.frames:
            obj_name = f"laser_{laser.colour}_{dir2}{dir1}"

        if obj_name not in self.frames:
            print(f"ERROR: Cannot find sprite for object {obj_name}")
            return
        frame_list = self.frames[obj_name]
        current_fame = frame_list[self.animation_frame_number % len(frame_list)]

        self.screen.blit(current_fame, location)
