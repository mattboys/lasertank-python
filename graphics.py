from pathlib import Path
import itertools

import pygame
pygame.init()

def get_frames(name, orientation=None):
    """ Get list of pygame.Surface objects from image resources
    based on the filename ./images/name_[orientation_]0.png and incrementing digit """
    image_dir = Path("/images")
    sprite_frames = []
    for frame_number in itertools.count(start=0):
        if orientation is None:
            filename = image_dir / f'{name}_{frame_number}.png'
        else:
            filename = image_dir / f'{name}_{orientation}_{frame_number}.png'
        if filename.is_file():
            frame = pygame.image.load(filename).convert_alpha()
            sprite_frames.append(frame)
        else:
            return sprite_frames

class ImageLoader:
    def __init__(self, image_dir_path="/images", file_type="*.png"):
        self.sprite_dict = {}
        self.object_names = {
            ""
        }
        obj_names = {
            "grass": {},
            "flag": {},
            "water": {},
            "conveyor": {"orientation": Direction},
            "ice": {},
            "ice_thin": {},
            "bridge": {},
            "tunnel": {"id": ["a", "b", "c", "d", "e", "f", "g", "h"]},
            "tank": {"orientation": Direction},
            "solid": {},
            "block": {},
            "wall": {},
            "antitank": {"orientation": Direction},
            "antitank_dead": {"orientation": Direction},
            "mirror": {"angle": Angle},
            "glass": {"glow": ["", "green", "red"]},
            "rotmirror": {},
            "laser": {"colour": ["red", "green"], "from_dir": Direction, "to_dir": Direction},
        }

class Graphics:
    # TODO
    pass


