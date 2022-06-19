from execution import load_level
from graphics_text import Graphics, InputEngine


def play_level(level_name, level_number):
    game = load_level(f"resources/levels/{level_name}.lvl", level_number)

    graphics = Graphics()
    inputs = InputEngine()

    graphics.draw(game)

    while game.running:
        game.queue_new_inputs(inputs.get_inputs())
        game.tick()
        graphics.draw(game)

    print(f"End State: {game.state.reached_flag}")


if __name__ == "__main__":
    play_level("standard_levels/LaserTank", 1)
