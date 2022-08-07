import datastructures
from datastructures import *
from engine import Game
import constants as const


class Graphics:
    def draw(self, game: Game):
        state = game.state
        state_sprites = self.get_sprites(state)
        self.draw_grid_with_coordinates(state_sprites)
        print("Loading")

    @staticmethod
    def draw_grid_with_coordinates(squares_list: list[str]):
        print(
            "     "
            + "\t".join(
                [Graphics.coordinate(x=x) for x in range(c.PLAYFIELD_SIZE)]
            )
        )
        for y in range(c.PLAYFIELD_SIZE):
            print(
                Graphics.coordinate(y=y)
                + " : "
                + "\t".join(
                    [
                        squares_list[Square(x, y)]
                        for x in range(c.PLAYFIELD_SIZE)
                    ]
                )
            )

    @staticmethod
    def get_sprites(state: GameState):
        return [Graphics.draw_square(state, s) for s in SQUARES]

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

        if state.laser_live and state.laser.sq == sq:
            if state.laser.dir_front == datastructures.UP:
                return "↑"
            elif state.laser.dir_front == datastructures.RIGHT:
                return "→"
            elif state.laser.dir_front == datastructures.DOWN:
                return "↓"
            elif state.laser.dir_front == datastructures.LEFT:
                return "←"
        elif state.tank.sq == sq:
            if state.tank.direction == datastructures.UP:
                return "⮝"
            elif state.tank.direction == datastructures.RIGHT:
                return "⮞"
            elif state.tank.direction == datastructures.DOWN:
                return "⮟"
            elif state.tank.direction == datastructures.LEFT:
                return "⮜"
        elif item == const.SOLID:
            return "■"
        elif item == const.BLOCK:
            return "□"
        elif item == const.WALL:
            return "▤"
        elif item == const.ANTITANK_LEFT:
            return "⮘"
        elif item == const.ANTITANK_RIGHT:
            return "⮚"
        elif item == const.ANTITANK_DOWN:
            return "⮛"
        elif item == const.ANTITANK_UP:
            return "⮙"
        elif item == const.MIRROR_LEFT_UP:
            return "◿"
        elif item == const.MIRROR_UP_RIGHT:
            return "◺"
        elif item == const.MIRROR_RIGHT_DOWN:
            return "◸"
        elif item == const.MIRROR_DOWN_LEFT:
            return "◹"
        elif item == const.DEADANTITANK_UP or item == const.DEADANTITANK_RIGHT or item == const.DEADANTITANK_DOWN or item == const.DEADANTITANK_LEFT:
            return "X"
        elif item == const.GLASS:
            return "⬚"
        elif item == const.ROTMIRROR_LEFT_UP:
            return "◢"
        elif item == const.ROTMIRROR_UP_RIGHT:
            return "◣"
        elif item == const.ROTMIRROR_RIGHT_DOWN:
            return "◤"
        elif item == const.ROTMIRROR_DOWN_LEFT:
            return "◥"

        elif terrain == const.FLAG:
            return "F"
        elif terrain == const.WATER:
            return "~"
        elif terrain == const.CONVEYOR_UP:
            return "⮅"
        elif terrain == const.CONVEYOR_RIGHT:
            return "⮆"
        elif terrain == const.CONVEYOR_DOWN:
            return "⮇"
        elif terrain == const.CONVEYOR_LEFT:
            return "⮄"
        elif terrain == const.ICE:
            return "_"
        elif terrain == const.THINICE:
            return "﹍"
        elif terrain == const.BRIDGE:
            return "="
        elif terrain == const.TUNNEL_0_RED or terrain == const.TUNNEL_0_RED_WAITING:
            return "①"
        elif terrain == const.TUNNEL_1_GREEN or terrain == const.TUNNEL_1_GREEN_WAITING:
            return "②"
        elif terrain == const.TUNNEL_2_BLUE or terrain == const.TUNNEL_2_BLUE_WAITING:
            return "③"
        elif terrain == const.TUNNEL_3_CYAN or terrain == const.TUNNEL_3_CYAN_WAITING:
            return "④"
        elif terrain == const.TUNNEL_4_YELLOW or terrain == const.TUNNEL_4_YELLOW_WAITING:
            return "⑤"
        elif terrain == const.TUNNEL_5_PINK or terrain == const.TUNNEL_5_PINK_WAITING:
            return "⑥"
        elif terrain == const.TUNNEL_6_WHITE or terrain == const.TUNNEL_6_WHITE_WAITING:
            return "⑦"
        elif terrain == const.TUNNEL_7_GREY or terrain == const.TUNNEL_7_GREY_WAITING:
            return "⑧"
        elif terrain == const.GRASS:
            return " "

        return "?"


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
