import pygame

pygame.init()
pygame.display.set_mode()

SPRITE_SIZE = 32

GameBoardOffsetX = 0
GameBoardOffsetY = 0
GameBoardWidth = SPRITE_SIZE * 16 + 2 * GameBoardOffsetX
GameBoardHeight = SPRITE_SIZE * 16 + 2 * GameBoardOffsetY

DIR_UP = 'N'
DIR_RIGHT = 'E'
DIR_DOWN = 'S'
DIR_LEFT = 'W'


def square_to_pixels(square):
    x, y = square
    return (GameBoardOffsetX + x * SPRITE_SIZE, GameBoardOffsetY + y * SPRITE_SIZE)


# def get_sprites_old(
#     filename, rows=6, columns=10, size_h=SPRITE_SIZE, size_w=SPRITE_SIZE
# ):
#     """
#     Convert a sprite sheet into an array of ImageTk.PhotoImage clippings
#     filename: file to load
#     rows: int number of rows of sprites down the sheet
#     columns: int number of columns of sprites along the sheet
#     size: pixel size of sprites in height and width (SpBm_Width, SpBm_Height)
#     """
#     load_image = Image.open(filename)
#
#     sprites = []
#     for row in range(rows):
#         for col in range(columns):
#             left = col * size_w
#             top = row * size_h
#             right = left + size_w
#             bottom = top + size_h
#             sprites.append(
#                 ImageTk.PhotoImage(load_image.crop((left, top, right, bottom)))
#             )
#
#     return sprites


def get_sprites(
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


def init_graphics():
    spritelist = get_sprites("../images/all.png")
    laser_sprites = get_laser_sprites()
    sprites = {
        "grass": spritelist[1],
        "tank_up": spritelist[2],
        "tank_right": spritelist[3],
        "tank_down": spritelist[4],
        "tank_left": spritelist[5],
        "flag_1": spritelist[6],
        "flag_2": spritelist[7],
        "flag_3": spritelist[8],
        "water_1": spritelist[9],
        "water_2": spritelist[10],
        "water_3": spritelist[11],
        "antitank_down_dead": spritelist[12],
        "solid": spritelist[13],
        "block": spritelist[14],
        "wall": spritelist[15],
        "antitank_up_1": spritelist[16],
        "antitank_up_2": spritelist[17],
        "antitank_up_3": spritelist[18],
        "bridge": spritelist[19],
        "mirror_left_up": spritelist[20],
        "mirror_up_right": spritelist[21],
        "mirror_right_down": spritelist[22],
        "mirror_down_left": spritelist[23],
        "conveyor_up_1": spritelist[24],
        "conveyor_up_2": spritelist[25],
        "conveyor_up_3": spritelist[26],
        "conveyor_right_1": spritelist[27],
        "conveyor_right_2": spritelist[28],
        "conveyor_right_3": spritelist[29],
        "conveyor_down_1": spritelist[30],
        "conveyor_down_2": spritelist[31],
        "conveyor_down_3": spritelist[32],
        "conveyor_left_1": spritelist[33],
        "conveyor_left_2": spritelist[34],
        "conveyor_left_3": spritelist[35],
        "antitank_right_1": spritelist[36],
        "antitank_right_2": spritelist[37],
        "antitank_right_3": spritelist[38],
        "antitank_down_1": spritelist[39],
        "antitank_down_2": spritelist[40],
        "antitank_down_3": spritelist[41],
        "antitank_left_1": spritelist[42],
        "antitank_left_2": spritelist[43],
        "antitank_left_3": spritelist[44],
        "glass": spritelist[45],
        "glass_green": spritelist[46],
        "rotmirror_left_up": spritelist[47],
        "rotmirror_up_right": spritelist[48],
        "rotmirror_right_down": spritelist[49],
        "rotmirror_down_left": spritelist[50],
        "glass_red": spritelist[51],
        "antitank_right_dead": spritelist[52],
        "antitank_left_dead": spritelist[53],
        "antitank_up_dead": spritelist[54],
        "teleport": spritelist[55],
        "ice": spritelist[56],
        "ice_thin": spritelist[57],
        "laser": laser_sprites,
    }

    return sprites


def get_laser_sprites():
    """ Laser frames as a dict of laser_sprites[DIR in][DIR our]["colour"] """
    laser_sprites = {}

    directions = [DIR_UP, DIR_DOWN, DIR_RIGHT, DIR_LEFT]
    colours = {"red": (255, 0, 0, 255), "green": (0, 255, 0, 255)}
    BLACK = (0, 0, 0, 255)

    beam_thickness = int(SPRITE_SIZE / 8)

    beam = {}
    beam[DIR_LEFT] = pygame.Rect(
        0, (SPRITE_SIZE - beam_thickness) / 2, SPRITE_SIZE / 2, beam_thickness
    )
    beam[DIR_RIGHT] = pygame.Rect(
        SPRITE_SIZE / 2,
        (SPRITE_SIZE - beam_thickness) / 2,
        SPRITE_SIZE / 2,
        beam_thickness,
    )
    beam[DIR_UP] = pygame.Rect(
        (SPRITE_SIZE - beam_thickness) / 2, 0, beam_thickness, SPRITE_SIZE / 2
    )
    beam[DIR_DOWN] = pygame.Rect(
        (SPRITE_SIZE - beam_thickness) / 2,
        SPRITE_SIZE / 2,
        beam_thickness,
        SPRITE_SIZE / 2,
    )

    for dir1 in directions:
        # if dir1 not in laser_sprites:
        #     laser_sprites[dir1] = {}
        for dir2 in directions:
            # if dir2 not in laser_sprites[dir1]:
            #     laser_sprites[dir1][dir2] = {}
            for colour_name, colour in colours.items():
                frame = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE), pygame.SRCALPHA)
                pygame.draw.rect(frame, BLACK, beam[dir1], 3)
                pygame.draw.rect(frame, BLACK, beam[dir2], 3)
                pygame.draw.rect(frame, colour, beam[dir1])
                pygame.draw.rect(frame, colour, beam[dir2])

                # laser_sprites[dir1][dir2][colour_name] = frame
                laser_sprites[f"laser_{colour_name}_{dir1}{dir2}_0"] = frame
    laser_sprites["laser_blank_0"] = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE), pygame.SRCALPHA)

    return laser_sprites


def get_laser_frame(from_direction, dir, colour_name):
    DIR_UP = 0
    DIR_RIGHT = 1
    DIR_DOWN = 2
    DIR_LEFT = 3
    DIR_NONE = -1

    COLOURS = {"red": (255, 0, 0, 255), "green": (0, 255, 0, 255)}
    colour = COLOURS[colour_name]
    BLACK = (0, 0, 0, 255)

    beam_thickness = int(SPRITE_SIZE / 8)

    beam = {}
    beam[DIR_LEFT] = pygame.Rect(
        0, (SPRITE_SIZE - beam_thickness) / 2, SPRITE_SIZE / 2, beam_thickness
    )
    beam[DIR_RIGHT] = pygame.Rect(
        SPRITE_SIZE / 2,
        (SPRITE_SIZE - beam_thickness) / 2,
        SPRITE_SIZE / 2,
        beam_thickness,
    )
    beam[DIR_UP] = pygame.Rect(
        (SPRITE_SIZE - beam_thickness) / 2, 0, beam_thickness, SPRITE_SIZE / 2
    )
    beam[DIR_DOWN] = pygame.Rect(
        (SPRITE_SIZE - beam_thickness) / 2,
        SPRITE_SIZE / 2,
        beam_thickness,
        SPRITE_SIZE / 2,
    )

    frame = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE), pygame.SRCALPHA)

    if from_direction == DIR_NONE or dir == DIR_NONE:
        return frame
    else:
        pygame.draw.rect(frame, BLACK, beam[from_direction], 3)
        pygame.draw.rect(frame, BLACK, beam[dir], 3)
        pygame.draw.rect(frame, colour, beam[from_direction])
        pygame.draw.rect(frame, colour, beam[dir])

    return frame


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode()
    sprites = init_graphics()

    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (125, 150, 200)

    screen = pygame.display.set_mode((500, 700))
    screen.fill(pygame.Color(125, 150, 200))

    font = pygame.font.Font("freesansbold.ttf", 10)

    x = 0
    y = 0
    for i, sprite in sprites.items():
        if i == "laser":
            continue
        text = font.render(str(i), True, black, white)
        y += 32
        if y > 20 * 32:
            y = 32
            x += 150
        screen.blit(text, (x, y))
        screen.blit(sprite, (x + 50, y))

    # # TODO: Move the above test into the load sprites code
    # load image files
    # apply mask alphas
    # crop down to individual sprites
    # save into a dict

    # pygame.display.init()
    # pygame.display.update()
    #
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #         pygame.display.update()

    s = get_laser_sprites()
    from pathlib import Path
    for fn, img in s.items():
        pygame.image.save(img, fn + '.png')

    # root = Tk()
    # canvas = Canvas(root, width=1000, height=500)
    #
    #
    # sp = get_sprites(file_game_bmp)
    # row = 50
    # col = 0
    # for s in sp:
    #     canvas.create_image(row, col, image=s, anchor=NW)
    #     row += 50
    #     if row > 1000-50:
    #         row = 50
    #         col += 50
    #
    # frames = [ sp[5], sp[6], sp[7] ]
    # obj = canvas.create_image(3, 3, anchor=NW, image=sp[1])
    #
    # canvas.pack()
    #
    # def animate(obj, frames, frame_no):
    #         print(frame_no)
    #         canvas.itemconfigure(obj, image=frames[frame_no])
    #         next_frame_no = (frame_no+1)%len(frames)
    #         time.sleep(1)
    #         #canvas.update()
    #         canvas.after(1, animate, obj, frames,next_frame_no)
    #
    #
    # canvas.after(3, animate, obj, frames, 0)
    # #canvas.bind("<Button-1>", animate)
    # root.mainloop()
