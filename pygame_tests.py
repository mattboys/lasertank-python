import pygame


def display_system_fonts():
    pygame.init()

    SCREEN_HEIGHT = 1000

    FONT_SIZE_COORDS = 16
    LIGHT_GRAY = pygame.Color(192, 192, 192)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, SCREEN_HEIGHT), flags=0)
    screen.fill(LIGHT_GRAY)

    for i, font_name in enumerate(pygame.font.get_fonts()):
        top = (i * 20) % SCREEN_HEIGHT
        left = int((i * 20 / SCREEN_HEIGHT)) * 300
        font = pygame.font.SysFont(font_name, size=FONT_SIZE_COORDS)
        # font.bold = True
        rendered_text = font.render("1 - Easy " + font_name, True, pygame.Color("blue"), LIGHT_GRAY)
        screen.blit(rendered_text, rendered_text.get_rect(top=top, left=left))

    pygame.display.update()
    while True:
        pass


def rounded_key_shape():
    pygame.init()

    LIGHT_GRAY = pygame.Color(192, 192, 192)

    surface = pygame.display.set_mode((500, 500), flags=0)
    surface.fill(pygame.Color("gray 15"))

    position = (10, 10)
    height = 50
    width = 50
    depth = 10
    corner = 5
    border = 3

    rect = pygame.Rect(position[0], position[1], height + depth, width + depth)
    pygame.draw.rect(
        surface,
        pygame.Color("light gray"),
        rect,
        width=0,
        border_radius=7
    )
    pygame.draw.rect(
        surface,
        pygame.Color("black"),
        rect,
        width=2,
        border_radius=7
    )
    rect_top = pygame.Rect(position[0] + int(depth / 2), position[1] + 3, height, width)
    pygame.draw.rect(
        surface,
        pygame.Color("white"),
        rect_top,
        width=0,
        border_radius=corner
    )

    pygame.display.update()
    while True:
        pass


display_system_fonts()
# rounded_key_shape()
