from pathlib import Path
import itertools

import pygame

pygame.init()

SPRITE_SIZE = 32


def get_frames(name, orientation=None):
    """ Get list of pygame.Surface objects from image resources
    based on the filename ./images/name_[orientation_]0.png and incrementing digit """
    image_dir = Path("/images")
    sprite_frames = []
    for frame_number in itertools.count(start=0):
        if orientation is None:
            filename = image_dir / f"{name}_{frame_number}.png"
        else:
            filename = image_dir / f"{name}_{orientation}_{frame_number}.png"
        if filename.is_file():
            frame = pygame.image.load(filename).convert_alpha()
            sprite_frames.append(frame)
        else:
            return sprite_frames


def split_spritesheet(
    filename_game,
    rows=6,
    columns=10,
    sprite_height_size_h=SPRITE_SIZE,
    sprite_width_size_w=SPRITE_SIZE,
):
    """
    Convert a sprite sheet into an array of sprites
    filename: file to load
    rows: int number of rows of sprites down the sheet
    columns: int number of columns of sprites along the sheet
    size: pixel size of sprites in height and width (SpBm_Width, SpBm_Height)
    """
    spritesheet = pygame.image.load(filename_game).convert_alpha()

    sprites = [
        spritesheet
    ]  # Sprites are 1 indexed for no reason so I put the whole spritesheet in [0] for debugigng
    i = 1
    for row in range(rows):
        for col in range(columns):
            left = col * sprite_width_size_w
            top = row * sprite_height_size_h
            sprite = pygame.Surface(
                (sprite_width_size_w, sprite_height_size_h), pygame.SRCALPHA
            )
            sprite.blit(
                spritesheet,
                (0, 0),
                (left, top, sprite_width_size_w, sprite_height_size_h),
            )
            sprites.append(sprite)
            i += 1
    return sprites


class ImageLoader:
    frames = {
        "grass": [],
        "flag": [],
        "water": [],
        "ice": [],
        "ice_thin": [],
        "bridge": [],
        "solid": [],
        "block": [],
        "wall": [],
        "glass": {"plain": [], "glow_green": [], "glow_red": []},
        "tank": {"N": [], "S": [], "E": [], "W": []},
        "antitank": {
            "N": [],
            "S": [],
            "E": [],
            "W": [],
        },
        "antitank_dead": {
            "N": [],
            "S": [],
            "E": [],
            "W": [],
        },
        "conveyor": {
            "N": [],
            "S": [],
            "E": [],
            "W": [],
        },
        "laser": {
            "red": {"N": [], "S": [], "E": [], "W": []},
            "green": {
                "N": [],
                "S": [],
                "E": [],
                "W": [],
            },
            "outline": {
                "N": [],
                "S": [],
                "E": [],
                "W": [],
            },
        },
        "mirror": {"NE": [], "NW": [], "SE": [], "SW": []},
        "rotmirror": {"NE": [], "NW": [], "SE": [], "SW": []},
        "tunnel": {
            "a": [],
            "b": [],
            "c": [],
            "d": [],
            "e": [],
            "f": [],
            "g": [],
            "h": [],
        },
    }

    def __init__(self):
        pass

    def load_from_spritesheet_png(self, spritesheet_filename="images/all.png"):
        spritelist = split_spritesheet(spritesheet_filename)

        ImageLoader.frames["flag"] = [spritelist[6], spritelist[7], spritelist[8]]
        ImageLoader.frames["water"] = [spritelist[9], spritelist[10], spritelist[11]]
        ImageLoader.frames["ice"] = [spritelist[56]]
        ImageLoader.frames["ice_thin"] = [spritelist[57]]
        ImageLoader.frames["bridge"] = [spritelist[19]]
        ImageLoader.frames["solid"] = [spritelist[13]]
        ImageLoader.frames["block"] = [spritelist[14]]
        ImageLoader.frames["wall"] = [spritelist[15]]

        ImageLoader.frames["glass"]["plain"] = [spritelist[45]]
        ImageLoader.frames["glass"]["green"] = [spritelist[46]]
        ImageLoader.frames["glass"]["red"] = [spritelist[51]]

        ImageLoader.frames["tank"]["N"] = [spritelist[2]]
        ImageLoader.frames["tank"]["S"] = [spritelist[4]]
        ImageLoader.frames["tank"]["E"] = [spritelist[3]]
        ImageLoader.frames["tank"]["W"] = [spritelist[5]]

        ImageLoader.frames["antitank"]["N"] = [
            spritelist[16],
            spritelist[17],
            spritelist[18],
        ]
        ImageLoader.frames["antitank"]["S"] = [
            spritelist[39],
            spritelist[40],
            spritelist[41],
        ]
        ImageLoader.frames["antitank"]["E"] = [
            spritelist[36],
            spritelist[37],
            spritelist[38],
        ]
        ImageLoader.frames["antitank"]["W"] = [
            spritelist[42],
            spritelist[43],
            spritelist[44],
        ]

        ImageLoader.frames["antitank_dead"]["N"] = [spritelist[54]]
        ImageLoader.frames["antitank_dead"]["S"] = [spritelist[12]]
        ImageLoader.frames["antitank_dead"]["E"] = [spritelist[52]]
        ImageLoader.frames["antitank_dead"]["W"] = [spritelist[53]]

        ImageLoader.frames["conveyor"]["N"] = [
            spritelist[24],
            spritelist[25],
            spritelist[26],
        ]
        ImageLoader.frames["conveyor"]["S"] = [
            spritelist[30],
            spritelist[31],
            spritelist[32],
        ]
        ImageLoader.frames["conveyor"]["E"] = [
            spritelist[27],
            spritelist[28],
            spritelist[29],
        ]
        ImageLoader.frames["conveyor"]["W"] = [
            spritelist[33],
            spritelist[34],
            spritelist[35],
        ]

        ImageLoader.frames["mirror"]["NE"] = [spritelist[21]]
        ImageLoader.frames["mirror"]["NW"] = [spritelist[20]]
        ImageLoader.frames["mirror"]["SE"] = [spritelist[22]]
        ImageLoader.frames["mirror"]["SW"] = [spritelist[23]]

        ImageLoader.frames["rotmirror"]["NE"] = [spritelist[48]]
        ImageLoader.frames["rotmirror"]["NW"] = [spritelist[47]]
        ImageLoader.frames["rotmirror"]["SE"] = [spritelist[49]]
        ImageLoader.frames["rotmirror"]["SW"] = [spritelist[50]]

        def draw_laser(direction, colour_name):
            beam_thickness = int(SPRITE_SIZE / 8)

            if direction == "N":
                beam = pygame.Rect(
                    (SPRITE_SIZE - beam_thickness) / 2,
                    0,
                    beam_thickness,
                    SPRITE_SIZE / 2,
                )
            elif direction == "S":
                beam = pygame.Rect(
                    (SPRITE_SIZE - beam_thickness) / 2,
                    SPRITE_SIZE / 2,
                    beam_thickness,
                    SPRITE_SIZE / 2,
                )
            elif direction == "E":
                beam = pygame.Rect(
                    SPRITE_SIZE / 2,
                    (SPRITE_SIZE - beam_thickness) / 2,
                    SPRITE_SIZE / 2,
                    beam_thickness,
                )
            elif direction == "W":
                beam = pygame.Rect(
                    0,
                    (SPRITE_SIZE - beam_thickness) / 2,
                    SPRITE_SIZE / 2,
                    beam_thickness,
                )

            if colour_name == "outline":
                colour = (0, 0, 0, 255)
                thickness = 3
            elif colour_name == "red":
                colour = (255, 0, 0, 255)
                thickness = 0
            elif colour_name == "green":
                colour = (0, 255, 0, 255)
                thickness = 0

            frame = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(frame, colour, beam, thickness)
            return frame

        ImageLoader.frames["laser"]["red"]["N"] = draw_laser("N", "red")
        ImageLoader.frames["laser"]["red"]["S"] = draw_laser("S", "red")
        ImageLoader.frames["laser"]["red"]["E"] = draw_laser("E", "red")
        ImageLoader.frames["laser"]["red"]["W"] = draw_laser("W", "red")
        ImageLoader.frames["laser"]["green"]["N"] = draw_laser(
            "N", "green"
        )
        ImageLoader.frames["laser"]["green"]["S"] = draw_laser(
            "S", "green"
        )
        ImageLoader.frames["laser"]["green"]["E"] = draw_laser(
            "E", "green"
        )
        ImageLoader.frames["laser"]["green"]["W"] = draw_laser(
            "W", "green"
        )
        ImageLoader.frames["laser"]["outline"]["N"] = draw_laser(
            "N", "outline"
        )
        ImageLoader.frames["laser"]["outline"]["S"] = draw_laser(
            "S", "outline"
        )
        ImageLoader.frames["laser"]["outline"]["E"] = draw_laser(
            "E", "outline"
        )
        ImageLoader.frames["laser"]["outline"]["W"] = draw_laser(
            "W", "outline"
        )

        uncoloured_tunnel = spritelist[55]

        def colour_tunnel(colour_name):
            id_colours = {
                "a": pygame.Color(0xFF0000FF),
                "b": pygame.Color(0x00FF00FF),
                "c": pygame.Color(0x0000FFFF),
                "d": pygame.Color(0x00FFFFFF),
                "e": pygame.Color(0x00FFFFFF),
                "f": pygame.Color(0xFF00FFFF),
                "g": pygame.Color(0xFFFFFFFF),
                "h": pygame.Color(0x808080FF),
            }
            colour = id_colours[colour_name]
            coloured_sprite = pygame.Surface.copy(uncoloured_tunnel)
            coloured_sprite.fill(colour)
            coloured_sprite.blit(uncoloured_tunnel, (0, 0))
            return coloured_sprite

        ImageLoader.frames["tunnel"]["a"] = colour_tunnel("a")
        ImageLoader.frames["tunnel"]["b"] = colour_tunnel("b")
        ImageLoader.frames["tunnel"]["c"] = colour_tunnel("c")
        ImageLoader.frames["tunnel"]["d"] = colour_tunnel("d")
        ImageLoader.frames["tunnel"]["e"] = colour_tunnel("e")
        ImageLoader.frames["tunnel"]["f"] = colour_tunnel("f")
        ImageLoader.frames["tunnel"]["g"] = colour_tunnel("g")
        ImageLoader.frames["tunnel"]["h"] = colour_tunnel("h")

    def load_from_img_dir(self):
        image_dir = Path("/images")

        def get_frames_filename(basename):
            filename = image_dir / f"{basename}.png"
            if filename.is_file():
                print(filename)
                return [filename]
            else:
                all_frames = []
                for frame_number in itertools.count(start=0):
                    filename = image_dir / f"{basename}_{frame_number}.png"
                    if filename.is_file():
                        all_frames.append(filename)
                    else:
                        print(all_frames)
                        return all_frames

        ImageLoader.frames["flag"] = get_frames_filename("flag")
        ImageLoader.frames["water"] = get_frames_filename("water")
        ImageLoader.frames["ice"] = get_frames_filename("ice")
        ImageLoader.frames["ice_thin"] = get_frames_filename("ice_thin")
        ImageLoader.frames["bridge"] = get_frames_filename("bridge")
        ImageLoader.frames["solid"] = get_frames_filename("solid")
        ImageLoader.frames["block"] = get_frames_filename("block")
        ImageLoader.frames["wall"] = get_frames_filename("wall")
        ImageLoader.frames["glass"]["plain"] = get_frames_filename("glass_plain")
        ImageLoader.frames["glass"]["green"] = get_frames_filename("glass_green")
        ImageLoader.frames["glass"]["red"] = get_frames_filename("glass_red")
        ImageLoader.frames["tank"]["N"] = get_frames_filename("tank_N")
        ImageLoader.frames["tank"]["S"] = get_frames_filename("tank_S")
        ImageLoader.frames["tank"]["E"] = get_frames_filename("tank_E")
        ImageLoader.frames["tank"]["W"] = get_frames_filename("tank_W")
        ImageLoader.frames["antitank"]["N"] = get_frames_filename("antitank_N")
        ImageLoader.frames["antitank"]["S"] = get_frames_filename("antitank_S")
        ImageLoader.frames["antitank"]["E"] = get_frames_filename("antitank_E")
        ImageLoader.frames["antitank"]["W"] = get_frames_filename("antitank_W")
        ImageLoader.frames["antitank_dead"]["N"] = get_frames_filename("antitank_dead_N")
        ImageLoader.frames["antitank_dead"]["S"] = get_frames_filename("antitank_dead_S")
        ImageLoader.frames["antitank_dead"]["E"] = get_frames_filename("antitank_dead_E")
        ImageLoader.frames["antitank_dead"]["W"] = get_frames_filename("antitank_dead_W")
        ImageLoader.frames["conveyor"]["N"] = get_frames_filename("conveyor_N")
        ImageLoader.frames["conveyor"]["S"] = get_frames_filename("conveyor_S")
        ImageLoader.frames["conveyor"]["E"] = get_frames_filename("conveyor_E")
        ImageLoader.frames["conveyor"]["W"] = get_frames_filename("conveyor_W")
        ImageLoader.frames["mirror"]["NE"] = get_frames_filename("mirror_NE")
        ImageLoader.frames["mirror"]["NW"] = get_frames_filename("mirror_NW")
        ImageLoader.frames["mirror"]["SE"] = get_frames_filename("mirror_SE")
        ImageLoader.frames["mirror"]["SW"] = get_frames_filename("mirror_SW")
        ImageLoader.frames["rotmirror"]["NE"] = get_frames_filename("rotmirror_NE")
        ImageLoader.frames["rotmirror"]["NW"] = get_frames_filename("rotmirror_NW")
        ImageLoader.frames["rotmirror"]["SE"] = get_frames_filename("rotmirror_SE")
        ImageLoader.frames["rotmirror"]["SW"] = get_frames_filename("rotmirror_SW")
        ImageLoader.frames["laser"]["red"]["N"] = get_frames_filename("laser_red_N")
        ImageLoader.frames["laser"]["red"]["S"] = get_frames_filename("laser_red_S")
        ImageLoader.frames["laser"]["red"]["E"] = get_frames_filename("laser_red_E")
        ImageLoader.frames["laser"]["red"]["W"] = get_frames_filename("laser_red_W")
        ImageLoader.frames["laser"]["green"]["N"] = get_frames_filename("laser_green_N")
        ImageLoader.frames["laser"]["green"]["S"] = get_frames_filename("laser_green_S")
        ImageLoader.frames["laser"]["green"]["E"] = get_frames_filename("laser_green_E")
        ImageLoader.frames["laser"]["green"]["W"] = get_frames_filename("laser_green_W")
        ImageLoader.frames["laser"]["outline"]["N"] = get_frames_filename("laser_outline_N")
        ImageLoader.frames["laser"]["outline"]["S"] = get_frames_filename("laser_outline_S")
        ImageLoader.frames["laser"]["outline"]["E"] = get_frames_filename("laser_outline_E")
        ImageLoader.frames["laser"]["outline"]["W"] = get_frames_filename("laser_outline_W")


def load_from_img_dir():
    image_dir = Path("images")

    def print_img_path(basename):
        print(basename)
        filename = image_dir / f"{basename}.png"
        if filename.is_file():
            print(f"\t_\t{filename.name}")
        else:
            # Search for files ending in _0, _1, ...
            all_frames = []
            for frame_number in itertools.count(start=0):
                filename = image_dir / f"{basename}_{frame_number}.png"
                if filename.is_file():
                    all_frames.append(filename.name)
                else:
                    if len(all_frames) == 0:
                        print("\tERROR")
                    else:
                        print(f"\t{len(all_frames)}\t{all_frames}")
                    break

    print_img_path("flag")
    print_img_path("water")
    print_img_path("ice")
    print_img_path("ice_thin")
    print_img_path("bridge")
    print_img_path("solid")
    print_img_path("block")
    print_img_path("wall")
    print_img_path("glass_plain")
    print_img_path("glass_green")
    print_img_path("glass_red")
    print_img_path("tank_N")
    print_img_path("tank_S")
    print_img_path("tank_E")
    print_img_path("tank_W")
    print_img_path("antitank_N")
    print_img_path("antitank_S")
    print_img_path("antitank_E")
    print_img_path("antitank_W")
    print_img_path("antitank_dead_N")
    print_img_path("antitank_dead_S")
    print_img_path("antitank_dead_E")
    print_img_path("antitank_dead_W")
    print_img_path("conveyor_N")
    print_img_path("conveyor_S")
    print_img_path("conveyor_E")
    print_img_path("conveyor_W")
    print_img_path("mirror_NE")
    print_img_path("mirror_NW")
    print_img_path("mirror_SE")
    print_img_path("mirror_SW")
    print_img_path("rotmirror_NE")
    print_img_path("rotmirror_NW")
    print_img_path("rotmirror_SE")
    print_img_path("rotmirror_SW")
    print_img_path("laser_red_N")
    print_img_path("laser_red_S")
    print_img_path("laser_red_E")
    print_img_path("laser_red_W")
    print_img_path("laser_green_N")
    print_img_path("laser_green_S")
    print_img_path("laser_green_E")
    print_img_path("laser_green_W")
    print_img_path("laser_outline_N")
    print_img_path("laser_outline_S")
    print_img_path("laser_outline_E")
    print_img_path("laser_outline_W")

if __name__ == "__main__":
    load_from_img_dir()