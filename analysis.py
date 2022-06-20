from copy import deepcopy

from engine import Game
from datastructures import SQUARES, Square


def play_out_state(game: Game, s: Square):
    game.state.tank.sq = s
    game.tick()
    tick_timout = 100
    while True:
        game.tick()
        tick_timout -= 1
        if tick_timout == 0:
            break
        if game.microtick == 0 and not game.is_objects_sliding():
            break
    if game.state.player_dead:
        return "X"
    elif game.state.reached_flag:
        return "!"
    else:
        return "."


def analysis(game: Game):
    return [play_out_state(deepcopy(game), s) for s in SQUARES]


def run_analysis():
    from execution import load_level
    from graphics_text import Graphics

    graphics = Graphics()

    game = load_level(f"resources/levels/standard_levels/LaserTank.lvl", 1)
    game_analysis = analysis(game)

    graphics.draw(game)
    graphics.draw_grid_with_coordinates(game_analysis)


run_analysis()
