from setup import *
from LTank2 import *
from Sprites import *

from pygame.locals import *

pygame.init()
pygame.display.set_mode()

clock = pygame.time.Clock()

sprites = init_graphics()

myLevel = LevelLoader()
myLevel.print_levelinfo()

game = GameBoard(myLevel)


pygame.display.init()
game.draw(screen)

while True:

    # Get inputs
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            print("quit")
        elif event.type == KEYDOWN and event.key == K_UP:
            game.queue_move(DIR_UP)
        elif event.type == KEYDOWN and event.key == K_DOWN:
            game.queue_move(DIR_DOWN)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            game.queue_move(DIR_LEFT)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            game.queue_move(DIR_RIGHT)
        elif event.type == KEYDOWN and event.key == K_SPACE:
            game.queue_move(SHOOT)

    # Update board state
    game.update()

    # Draw board and animations
    game.draw(screen)
    pygame.display.update()

    window_root_MainH.update()

    clock.tick(60)
