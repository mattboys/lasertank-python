from engine import *


class TextGraphics:
    @staticmethod
    def draw_interesting_crop(game: Game):
        x_min = y_min = c.PLAYFIELD_SIZE
        x_max = y_max = 0
        for sq in SQUARES:
            if (
                    game.state.terrain[sq] not in (c.GRASS, c.WATER)
                    or game.state.items[sq] != c.EMPTY
                    or game.state.tank.sq == sq
            ):
                # Square of interest
                x_min = min(x_min, sq.x)
                y_min = min(y_min, sq.y)
                x_max = max(x_max, sq.x)
                y_max = max(y_max, sq.y)
        # print(f"x_min: {x_min},y_min: {y_min},x_max: {x_max},y_max: {y_max}")
        print(
            "       "
            + "       ".join(
                [TextGraphics.coordinate(x=x) for x in range(x_min, x_max + 1)]
            )
        )
        for y in range(y_min, y_max + 1):
            print(
                TextGraphics.coordinate(y=y)
                + " : "
                + " | ".join(
                    [
                        TextGraphics.cell_as_numbers(game, Square(x, y))
                        for x in range(x_min, x_max + 1)
                    ]
                )
            )

    @staticmethod
    def print_directions(moves):
        move_mapping = {
            c.K_SHOOT: "*",
            c.K_LEFT: "⮜",
            c.K_UP: "⮝",
            c.K_RIGHT: "⮞",
            c.K_DOWN: "⮟",
        }
        return "".join(move_mapping[m] for m in moves)

    @staticmethod
    def coordinate(x=None, y=None):
        """Translate coordinate to algebraic notation. i.e. (1,2) = 'B03'"""
        x_val = chr(ord("A") + x) if x is not None else ""
        y_val = f"{y + 1:02}" if y is not None else ""
        return f"{x_val}{y_val}"

    @staticmethod
    def cell_as_numbers(game: Game, sq: Square):
        terrain = game.state.terrain[sq]
        item = game.state.items[sq]
        if terrain == c.GRASS:
            terrain = " "
        if item == c.EMPTY:
            item = " "
        if game.state.tank.sq == sq:
            item = "T"
        if game.state.laser_live and game.state.laser.sq == sq:
            terrain = "-"

        return f"{terrain: >2}{item: >3}"
