import copy

import sprites

class LevelInfo:
    def __init__(self, number, title, hint, author, difficulty, playfield):
        self.number = number
        self.title = title
        self.hint = hint
        self.author = author
        self.difficulty = difficulty
        self.playfield = playfield

class GameBoard:
    SIZE = 16
    def __init__(self):
        sprites.LTSprite.gameboard = self
        self.terrain = [[None for x in range(self.SIZE)] for y in range(self.SIZE)]
        self.items = [[None for x in range(self.SIZE)] for y in range(self.SIZE)]
        self.tank = sprites.Tank(position=(7, 15), direction=1)
        self.laser = sprites.Laser()
        self.sliding_items = []
        self.moves_history = []

    def setup(self, playfield):
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                terrain_str, item_str = playfield[x][y]
                self.terrain[x][y] = sprites.map_strings_to_objects(terrain_str, (x,y))
                self.items[x][y] = sprites.map_strings_to_objects(item_str, (x, y))

    def start_sliding(self, item):
        if item not in self.sliding_items:
            self.sliding_items.append(item)

    def is_within_board(self, position):
        """ Is this square still within the confines of the board? """
        x, y = position
        return 0 <= x < self.SIZE and 0 <= y < self.SIZE

    def get_laser(self):
        return self.laser

    def get_tank(self):
        return self.laser

    def get_item(self, position):
        x, y = position
        return self.items[x][y]

    def put_item(self, position, item):
        x, y = position
        self.items[x][y] = item

    def destroy_item(self, position):
        x, y = position
        self.items[x][y] = sprites.Empty(position)

    def get_terrain(self, position):
        x, y = position
        return self.terrain[x][y]

    def put_terrain(self, position, terrain):
        x, y = position
        self.terrain[x][y] = terrain

    def is_square_empty(self, position):
        x, y = position
        return isinstance(self.items[x][y], sprites.Empty)

    def can_move_into(self, position):
        """ Can an item move into this square? or Is this square on the board and empty? """
        if self.is_within_board(position):
            return self.is_square_empty(position)
        else:
            return False  # Off gameboard

    def setup(self, item_ids, terrain_ids):
        for position, x, y in [((x,y), x, y) for x in range(self.SIZE) for y in range(self.SIZE)]:
            unplaced_item = sprites.get_item_from_id(item_ids[x][y])
            self.put_item(position, unplaced_item(position))
            unplaced_terrain = sprites.get_terrain_from_id(terrain_ids[x][y])
            self.put_terrain(position, unplaced_terrain(position))


class GameState:
    def __init__(self):
        self.level_data = LevelInfo()
        self.gameboard = GameBoard()
        self.input_buffer = []
        self.speed_counter = 0
        self.history = []
        self.add_undo()

    def add_undo(self):
        self.history.append(copy.deepcopy(self.gameboard))

    def queue_event(self, event):
        pass

    def is_not_solved(self):
        pass

    def update(self):
        try:
            if gameboard.players_turn():
                self.gameboard.next_move(self.input_buffer.pop(0))
            else:
                self.gameboard.ai_turn()
        except Solved:
            pass
        except GameOver:
            pass




def run(gamestate, input_engine, render_engine):
    while gamestate.is_not_solved():
        for event in input_engine.get_input():
            if event == "quit":
                return "quit"
            elif event in ["up", "down", "left", "right", "shoot"]:
                gamestate.queue_event(event)
            else:
                print(f"Unhandled input: {event}")
        gamestate.update()
        render_engine(gamestate)
    return "solved"

if __name__ == "__main__":
    from old_LTank2 import LevelLoader
    level_loader = LevelLoader()

    level_info = load_level()
    gamestate(level_info)
    graphics.render_frame(level.info)
    graphics.render(gamestate)
    run(gamestate, input_engine, graphics)