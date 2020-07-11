import copy

import sprites

class GameState:
    GAMEBOARD_SIZE = 16

    def __init__(self, number, title, hint, author, difficulty, playfield):
        self.lvl_number = number
        self.lvl_title = title
        self.lvl_hint = hint
        self.lvl_author = author
        self.lvl_difficulty = difficulty

        sprites.LaserTankObject.gameboard = self
        self.board_terrain = [[sprites.Grass((x, y)) for x in range(self.GAMEBOARD_SIZE)] for y in range(self.GAMEBOARD_SIZE)]
        self.board_items = [[sprites.Empty((x, y)) for x in range(self.GAMEBOARD_SIZE)] for y in range(self.GAMEBOARD_SIZE)]
        self.board_tank = sprites.Tank(position=(7, 15), direction=1)
        self.board_laser = sprites.Laser()
        self.sliding_items = []
        self.moves_history = []
        self.moves_buffer = []

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


    # def add_undo(self):
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
            self.board_tank.shoot()
            self.moves_history.append(sprites.Direction.SHOOT)
        else:
            move_dir = move_direction_mapping[move]
            if self.board_tank.dir == move_dir:
                self.board_tank.move(move_dir)
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
                if isinstance(maybe_antitank,
                              sprites.Antitank) and maybe_antitank.dir == sprites.Direction.get_opposite(
                        check_dir) and check_pos != self.board_tank.position:
                    maybe_antitank.shoot()  # allow the found antitank to shoot
                    return  # Only one antitank gets a chance to fire

    def resolve_momenta(self):
        """ Resolve new positions of each item with momentum such as those sliding on ice. """
        for item in reversed(self.sliding_items):
            item.resolve_momentum()
        self.sliding_items = [
            item for item in self.sliding_items if item.momentum != sprites.Direction.NONE
        ]

    def start_sliding(self, item: sprites.Item):
        if item not in self.sliding_items:
            self.sliding_items.append(item)

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

    def update(self):
        try:
            self.laser_update()
            if self.is_players_turn() and len(self.moves_buffer)>0:
                self.next_move(self.moves_buffer.pop(0))
            self.resolve_momenta()
            self.ai_move()
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
            elif event in ["up", "down", "left", "right", "shoot", "undo", "reset"]:
                gamestate.queue_event(event)
            else:
                print(f"Unhandled input: {event}")
        render_engine.render(gamestate)
    return "solved or game over"


if __name__ == "__main__":
    from level_importer import import_legacy_lvl
    from graphics_pygame import Graphics
    from inputs_pygame import InputEngine

    level_dict = import_legacy_lvl(level_number=1)
    game = GameState(**level_dict)

    # graphics.render_frame(level.info)
    graphics = Graphics()
    inputs = InputEngine()

    run(game, inputs, graphics)

