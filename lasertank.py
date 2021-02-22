import time
import json

import sprites


class GameState:
    GAMEBOARD_SIZE = 16

    def __init__(self, number, title, hint, author, difficulty, playfield):
        self.level_info = {"number": number, "title": title, "hint": hint, "difficulty": difficulty, "author": author}

        sprites.LaserTankObject.gameboard = self
        self.board_terrain = [[sprites.Grass((x, y)) for y in range(self.GAMEBOARD_SIZE)] for x in
                              range(self.GAMEBOARD_SIZE)]
        self.board_items = [[sprites.Empty((x, y)) for y in range(self.GAMEBOARD_SIZE)] for x in
                            range(self.GAMEBOARD_SIZE)]
        self.board_tank = sprites.Tank(position=(7, 15), direction=1)
        self.board_laser = sprites.Laser()
        self.sliding_items = []
        self.moves_history = []
        self.moves_buffer = []
        self.score = {"shots": 0, "moves": 0}

        self.undo_state = []

        for y in range(self.GAMEBOARD_SIZE):
            for x in range(self.GAMEBOARD_SIZE):
                terrain_str, item_str = playfield[y][x]
                pos = (x, y)
                self.put_terrain(pos, sprites.map_strings_to_objects(terrain_str, pos))
                item = sprites.map_strings_to_objects(item_str, pos)
                if isinstance(item, sprites.Tank):
                    self.board_tank = item
                else:
                    self.put_item(pos, item)

    def add_undo(self):
        serialized_state = self.serialize_state()
        # print(json.dumps(serialized_state))
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
            "up": sprites.Direction.N,
            "down": sprites.Direction.S,
            "left": sprites.Direction.W,
            "right": sprites.Direction.E,
        }
        if move == "shoot":
            self.add_undo()
            self.score["shots"] += 1
            self.board_tank.shoot()
            self.moves_history.append(sprites.Direction.SHOOT)
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
            for check_dir in [sprites.Direction.E, sprites.Direction.W, sprites.Direction.S, sprites.Direction.N]:
                check_pos = self.board_tank.position
                # Search along direction skipping empty squares
                while self.can_move_into(check_pos):
                    check_pos = sprites.vec_add(check_pos, sprites.Direction.get_xy(check_dir))
                if not self.is_within_board(check_pos):
                    continue
                maybe_antitank = self.get_item(check_pos)
                if isinstance(maybe_antitank, sprites.Antitank) \
                        and maybe_antitank.direction == sprites.Direction.get_opposite(check_dir) \
                        and check_pos != self.board_tank.position:
                    maybe_antitank.shoot()  # allow the found antitank to shoot
                    self.laser_update()  # Laser gets a chance to move immediately after being fired
                    return  # Only one antitank gets a chance to fire

    def resolve_momenta(self):
        """ Resolve new positions of each item with momentum such as those sliding on ice. """
        # TODO: Fix logic to match original
        # IceMoveO()  (move an object on the ice)
        # IceMoveT()  (move tank on the ice)
        # If tank on converyor:
        #     CheckLoc( dest_x, dest_y )
        #     ConvMoveTank( dir_x, dir_y, True )

        for item in reversed(self.sliding_items):
            item.resolve_momentum()
            if not isinstance(item, sprites.Tank):
                item.resolve_momentum()
                self.ai_move()
        # Tank momentum is resolved after all items
        if self.board_tank in self.sliding_items:
            self.board_tank.resolve_momentum()
            self.ai_move()
        # Trim list down to items that still have momentum
        self.sliding_items = [
            item for item in self.sliding_items if item.is_sliding()
        ]

    def start_sliding(self, item: sprites.Item):
        if item not in self.sliding_items:
            self.sliding_items.append(item)

    def is_sliding(self, item: sprites.Item):
        return item in self.sliding_items

    def is_within_board(self, position: (int, int)) -> bool:
        """ Is this square still within the confines of the board? """
        x, y = position
        return 0 <= x < self.GAMEBOARD_SIZE and 0 <= y < self.GAMEBOARD_SIZE

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

    def is_tank_in_square(self, position: (int, int)):
        return self.board_tank.position == position

    def can_move_into(self, position: (int, int)):
        """ Can an item move into this square? or Is this square on the board and empty? """
        if not self.is_within_board(position):
            # Off gameboard
            return False
        else:
            is_empty = isinstance(self.get_item(position),  sprites.Empty)
            is_tank = self.get_tank().position == position
            return is_empty and not is_tank

    def get_tunnels(self, tunnel_id):
        found_set = []
        for x in range(self.GAMEBOARD_SIZE):
            for y in range(self.GAMEBOARD_SIZE):
                terrain_obj = self.get_terrain((x, y))
                if isinstance(terrain_obj, sprites.Tunnel) and terrain_obj.tunnel_id == tunnel_id:
                    found_set.append(terrain_obj)
        return found_set

    def serialize_state(self):
        board_terrain = [[self.get_terrain((x, y)).serialize() for x in range(self.GAMEBOARD_SIZE)] for y in
                         range(self.GAMEBOARD_SIZE)]
        board_items = [[self.get_item((x, y)).serialize() for x in range(self.GAMEBOARD_SIZE)] for y in
                       range(self.GAMEBOARD_SIZE)]
        board_tank = self.get_tank().serialize()
        board_laser = self.get_laser().serialize()
        score = self.score
        return {
            "board_terrain": board_terrain,
            "board_items": board_items,
            "board_tank": board_tank,
            "board_laser": board_laser,
            "score": score,
        }

    def load_undo(self):
        """ Pop undo state and deserialize into current state """
        if len(self.undo_state) > 0:
            serialized = self.undo_state.pop()
            # Deserialize state
            for y in range(self.GAMEBOARD_SIZE):
                for x in range(self.GAMEBOARD_SIZE):
                    position = (x, y)
                    item_name = serialized['board_items'][y][x]
                    self.put_item((x, y), sprites.deserialize(item_name, position))
                    terrain_params = serialized['board_terrain'][y][x]
                    self.put_terrain((x, y), sprites.deserialize(terrain_params, position))

            tank_params = serialized['board_tank']
            self.board_tank = sprites.deserialize_tank(tank_params)
            laser_params = serialized['board_laser']
            self.board_laser = sprites.deserialize_laser(laser_params)
            self.score = serialized["score"]

    def update(self):
        try:
            self.laser_update()
            if self.is_players_turn() and len(self.moves_buffer) > 0:
                self.next_move(self.moves_buffer.pop(0))
            self.ai_move()
            self.resolve_momenta()  # 3108
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
        print(gamestate.serialize_state())
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
        # time.sleep(3)
    return "solved or game over"


if __name__ == "__main__":
    from level_importer import import_legacy_lvl
    from graphics_pygame import Graphics
    from inputs_pygame import InputEngine

    level_dict = import_legacy_lvl(level_number=3, filename="legacy_resources/Files/Tricks.lvl")
    game = GameState(**level_dict)

    # graphics.render_frame(level.info)
    graphics = Graphics()
    inputs = InputEngine()

    run(game, inputs, graphics)

