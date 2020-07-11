import pygame
from pygame.locals import *

class InputEngine:
    def __init__(self):
        pygame.init()

    def get_inputs(self):
        # Get inputs
        translated_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return(["quit"])
            elif event.type == KEYDOWN and event.key == K_UP:
                translated_events.append("up")
            elif event.type == KEYDOWN and event.key == K_DOWN:
                translated_events.append("down")
            elif event.type == KEYDOWN and event.key == K_LEFT:
                translated_events.append("left")
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                translated_events.append("right")
            elif event.type == KEYDOWN and event.key == K_SPACE:
                translated_events.append("shoot")
            # TODO: Undo keys
        return translated_events

