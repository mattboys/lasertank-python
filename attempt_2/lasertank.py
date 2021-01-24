import json
import time
from typing import List

from attempt_2 import sprites
from attempt_2.constants import *


class Board:
    def __init__(self, packed_board=None):
        if packed_board is None:
            packed_board = {}

        def unpack_grid(packed_grid):
            return [
                [sprites.unpack(packed_gameobj=packed_grid[y][x]) for y in range(GAMEBOARD_SIZE)]
                for x in range(GAMEBOARD_SIZE)
            ]

        terrain_packed_default = [[DEFAULT_TERRAIN for y in range(GAMEBOARD_SIZE)] for x in range(GAMEBOARD_SIZE)]
        # noinspection PyTypeChecker
        self.board_terrain: List[List[sprites.Terrain]] = unpack_grid(
            packed_board.get("terrain_packed", terrain_packed_default))
        items_packed_default = [[DEFAULT_ITEM for y in range(GAMEBOARD_SIZE)] for x in range(GAMEBOARD_SIZE)]
        # noinspection PyTypeChecker
        self.board_items: List[List[sprites.Item]] = unpack_grid(packed_board.get("items_packed", items_packed_default))
        self.board_tank = sprites.unpack(packed_board.get("tank_packed", DEFAULT_TANK))
        self.board_laser = sprites.unpack(packed_board.get("laser_packed", DEFAULT_LASER))

        self.sliding_items = []
        for sliding_square in packed_board.get("sliding_packed", []):
            self.start_sliding(self.get_item(sliding_square))

        # Give all sprites a reference to this gameboard
        sprites.LaserTankObject._gameboard = self

    def pack_board(self):
        def pack_grid(grid):
            return [
                [
                    self.board_terrain[y][x].pack() for y in range(GAMEBOARD_SIZE)
                ] for x in range(GAMEBOARD_SIZE)
            ]

        return {
            "terrain_packed": pack_grid(self.board_terrain),
            "items_packed": pack_grid(self.board_items),
            "tank_packed": self.board_tank.pack(),
            "laser_packed": self.board_laser.pack(),
            "sliding_packed": [item.position for item in self.sliding_items],
        }

    def resolve_momenta(self):
        """ Resolve new positions of each item with momentum such as those sliding on ice. """
        for item in reversed(self.sliding_items):
            if not isinstance(item, sprites.Tank):
                item.resolve_momentum()
        # Tank momentum is resolved after all items
        if self.board_tank in self.sliding_items:
            self.board_tank.resolve_momentum()

        self.sliding_items = [
            item for item in self.sliding_items if item.momentum != attempt_2.Direction.NONE
        ]

    def start_sliding(self, item: sprites.Item):
        if item not in self.sliding_items:
            self.sliding_items.append(item)

    def is_sliding(self, item: sprites.Item):
        return item in self.sliding_items

    def is_within_board(self, position: (int, int)) -> bool:
        """ Is this square still within the confines of the board? """
        x, y = position
        return 0 <= x < GAMEBOARD_SIZE and 0 <= y < GAMEBOARD_SIZE

    def get_laser(self) -> sprites.Laser:
        return self.board_laser

    def get_tank(self) -> sprites.Tank:
        return self.board_tank

    def get_item(self, position: (int, int)) -> sprites.Item:
        x, y = position
        return self.board_items[y][x]

    def get_tank_or_item(self, position: (int, int)) -> sprites.Item:
        if self.board_tank.position == position:
            return self.board_tank
        else:
            return self.get_item(position)

    def put_item(self, position: (int, int), item: sprites.Item):
        x, y = position
        self.board_items[y][x] = item

    def destroy_item(self, position: (int, int)):
        x, y = position
        self.board_items[y][x] = sprites.Empty(position)

    def get_terrain(self, position: (int, int)):
        x, y = position
        return self.board_terrain[y][x]

    def put_terrain(self, position: (int, int), terrain: sprites.Terrain):
        x, y = position
        self.board_terrain[y][x] = terrain

    def is_square_empty(self, position):
        x, y = position
        return isinstance(self.board_items[y][x], sprites.Empty)

    def is_tank_in_square(self, position: (int, int)):
        return self.board_tank.position == position

    def can_move_into(self, position: (int, int)):
        """ Can an item move into this square? or Is this square on the board and empty? """
        if self.is_within_board(position):
            return self.is_square_empty(position)
        else:
            return False  # Off gameboard

    def get_tunnels(self, tunnel_id):
        found_set = []
        for x in range(GAMEBOARD_SIZE):
            for y in range(GAMEBOARD_SIZE):
                terrain_obj = self.get_terrain((x, y))
                if isinstance(terrain_obj, sprites.Tunnel) and terrain_obj.tunnel_id == tunnel_id:
                    found_set.append(terrain_obj)
        return found_set


class GameState:

    def __init__(self, level_info=None, packed_board=None):
        if level_info is None:
            level_info = {}

        self.level_info = {
            "number": 0,
            "title": "",
            "hint": "",
            "author": "",
            "difficulty": DIFFICULTY_KIDS,
        }.update(level_info)

        self.board = Board(packed_board)

        self.moves_history = []
        self.moves_buffer = []

        self.score = {"shots": 0, "moves": 0}

        self.undo_state = []

    def add_undo(self):
        serialized_state = self.serialize_state()
        print(json.dumps(serialized_state))
        self.undo_state.append(serialized_state)  # Save for undos

    #     self.history.append(copy.deepcopy(self.gameboard))

    def queue_event(self, event):
        """ Put move on input buffer. Will be held until player's next turn """
        assert event in ["up", "down", "left", "right", "shoot", "undo", "reset"], "Invalid move!"
        if event in ["up", "down", "left", "right", "shoot"]:
            self.moves_buffer.append(event)
        # TODO: Handle reset board
        # TODO: Handle undo

    def laser_update(self):
        self.board_laser.update()

    def is_players_turn(self):
        """ Can the player execute a move? (nothing moving, laser not moving) """
        return len(self.sliding_items) == 0 and not self.board_laser.exists

    def next_move(self, move):
        move_direction_mapping = {
            "up": attempt_2.Direction.N,
            "down": attempt_2.Direction.S,
            "left": attempt_2.Direction.W,
            "right": attempt_2.Direction.E,
        }
        if move == "shoot":
            self.add_undo()
            self.score["shots"] += 1
            self.board_tank.shoot()
            self.moves_history.append(attempt_2.Direction.SHOOT)
            self.laser_update()  # Laser gets a chance to move immediately after being fired
        else:
            move_dir = move_direction_mapping[move]
            if self.board_tank.direction == move_dir:
                self.add_undo()
                self.score["moves"] += 1
                self.board_tank.move(move_dir)
                self.board_tank.resolve_momentum()
                self.moves_history.append(move_dir)
            else:
                self.board_tank.rotate(move_dir)

    def ai_move(self):
        if not self.board_laser.exists:
            for check_dir in [attempt_2.Direction.E, attempt_2.Direction.W, attempt_2.Direction.S,
                              attempt_2.Direction.N]:
                check_pos = self.board_tank.position
                # Search along direction skipping empty squares
                while self.can_move_into(check_pos):
                    check_pos = sprites.vec_add(check_pos, attempt_2.Direction.get_xy(check_dir))
                if not self.is_within_board(check_pos):
                    continue
                maybe_antitank = self.get_item(check_pos)
                if isinstance(maybe_antitank, sprites.Antitank) \
                        and maybe_antitank.direction == attempt_2.Direction.get_opposite(check_dir) \
                        and check_pos != self.board_tank.position:
                    maybe_antitank.shoot()  # allow the found antitank to shoot
                    self.laser_update()  # Laser gets a chance to move immediately after being fired
                    return  # Only one antitank gets a chance to fire

    def serialize_state(self):
        return self.board.pack_board()

    def load_undo(self):
        """ Pop undo state and deserialize into current state """
        if len(self.undo_state) > 0:
            serialized = self.undo_state.pop()
            self.board = Board(serialized)

    def update(self):
        try:
            self.laser_update()
            if self.is_players_turn() and len(self.moves_buffer) > 0:
                self.next_move(self.moves_buffer.pop(0))
            self.ai_move()
            self.board.resolve_momenta()
            return True
        except sprites.Solved:
            # TODO: Implement game solved
            print("Solved!")
            return False
        except sprites.GameOver:
            # TODO: Implement game over
            print("Game over!")
            return False


def run(gamestate: GameState, input_engine, render_engine):
    while gamestate.update():
        for event in input_engine.get_inputs():
            if event == "quit":
                return "quit"
            elif event == "undo":

                gamestate.load_undo()
            elif event in ["up", "down", "left", "right", "shoot", "reset"]:
                gamestate.queue_event(event)
            else:
                print(f"Unhandled input: {event}")
        render_engine.render(gamestate)
        time.sleep(3)
    return "solved or game over"


if __name__ == "__main__":
    from attempt_2.level_importer import import_legacy_lvl
    from attempt_2.graphics_pygame import Graphics
    from attempt_2.inputs_pygame import InputEngine

    level_dict = import_legacy_lvl(level_number=4, filename="../legacy_resources/Files/Tricks.lvl")
    game = GameState(**level_dict)

    # graphics.render_frame(level.info)
    graphics = Graphics()
    inputs = InputEngine()

    run(game, inputs, graphics)
