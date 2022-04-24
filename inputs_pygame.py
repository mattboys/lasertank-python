import pygame
import pygame.locals
import constants as const


class InputEngine:
    def __init__(self):
        pygame.init()

    def get_inputs(self):
        # Get inputs
        translated_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_ESCAPE
            ):
                return [const.K_QUIT]
            elif (
                    event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_UP
            ):
                translated_events.append(const.K_UP)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_DOWN
            ):
                translated_events.append(const.K_DOWN)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_LEFT
            ):
                translated_events.append(const.K_LEFT)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_RIGHT
            ):
                translated_events.append(const.K_RIGHT)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_SPACE
            ):
                translated_events.append(const.K_SHOOT)
            elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_u:
                translated_events.append(const.K_UNDO)
            elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_r:
                return [const.K_RESET]
            elif event.type == pygame.locals.KEYDOWN and (event.key == pygame.locals.K_PAGEDOWN or event.key ==
                                                          pygame.locals.K_p):
                return [const.K_LVL_PRE]
            elif event.type == pygame.locals.KEYDOWN and (event.key == pygame.locals.K_PAGEUP or event.key ==
                                                          pygame.locals.K_s):
                return [const.K_LVL_NXT]

        return translated_events

    def wait_for_anykey(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                        event.type == pygame.locals.KEYDOWN
                        and event.key == pygame.locals.K_ESCAPE
                ):
                    return [const.K_QUIT]
                elif event.type == pygame.locals.KEYDOWN:
                    return []
