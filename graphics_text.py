from datastructures import *
from engine import Game
import constants as const


class Graphics:
    def draw(self, game: Game):
        self.draw_state(game.state)

    def draw_state(self, state: GameState):
        print(
            "       "
            + "       ".join(
                [self.coordinate(x=x) for x in range(c.PLAYFIELD_SIZE)]
            )
        )
        for y in range(c.PLAYFIELD_SIZE):
            print(
                self.coordinate(y=y)
                + " : "
                + " | ".join(
                    [
                        self.draw_square(state, Square(x, y))
                        for x in range(c.PLAYFIELD_SIZE)
                    ]
                )
            )

    @staticmethod
    def coordinate(x=None, y=None):
        """Translate coordinate to algebraic notation. i.e. (1,2) = 'B03'"""
        x_val = chr(ord("A") + x) if x is not None else ""
        y_val = f"{y + 1:02}" if y is not None else ""
        return f"{x_val}{y_val}"

    @staticmethod
    def draw_square(state: GameState, sq: Square):
        terrain = state.terrain[sq]
        item = state.items[sq]

        if terrain == c.GRASS:
            terrain = " "
        if item == c.EMPTY:
            item = " "
        if state.tank.sq == sq:
            item = "T"
        if state.laser_live and state.laser.sq == sq:
            terrain = "-"

        return f"{terrain: >2}{item: >3}"


class InputEngine:
    def get_inputs(self):
        translated_events = []
        events = input("Enter move (W,A,S,D,space),\n or U: undo, R: reset, N: next, P: prev, Q: exit\n")
        for event in events:
            if event.upper() == "Q":
                return [const.K_QUIT]
            elif event.upper() == "W":
                translated_events.append(const.K_UP)
            elif event.upper() == "S":
                translated_events.append(const.K_DOWN)
            elif event.upper() == "A":
                translated_events.append(const.K_LEFT)
            elif event.upper() == "D":
                translated_events.append(const.K_RIGHT)
            elif event == " ":
                translated_events.append(const.K_SHOOT)
            elif event.upper() == "U":
                translated_events.append(const.K_UNDO)
            elif event.upper() == "R":
                translated_events.append(const.K_RESET)
            elif event.upper() == "N":
                translated_events.append(const.K_LVL_NXT)
            elif event.upper() == "P":
                translated_events.append(const.K_LVL_PRE)
        return translated_events
