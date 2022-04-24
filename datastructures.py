import constants as c

Direction = tuple
UP: Direction = (0, -1)
DOWN: Direction = (0, 1)
LEFT: Direction = (-1, 0)
RIGHT: Direction = (1, 0)
STATIONARY: Direction = (0, 0)


class Square(int):
    def __new__(cls, x, y=None):
        if y is None:
            value = x
        else:
            if not Square.on_board(x, y):
                raise ValueError(f"Square ({x},{y}) is not on the board.")
            value = x + (y * c.PLAYFIELD_SIZE)
        return int.__new__(cls, value)

    @staticmethod
    def on_board(x, y):
        return 0 <= x < c.PLAYFIELD_SIZE and 0 <= y < c.PLAYFIELD_SIZE

    @property
    def coords(self):
        return self.x, self.y

    @property
    def x(self) -> int:
        return self % c.PLAYFIELD_SIZE

    @property
    def y(self) -> int:
        return int(self / c.PLAYFIELD_SIZE)

    def relative(self, direction: Direction):
        """ Return the square one space in the specified direction if on the board, None otherwise """
        x, y = self.coords
        dx, dy = direction
        xp = x + dx
        yp = y + dy
        if not Square.on_board(xp, yp):
            return None
        else:
            return Square(xp, yp)

    def __repr__(self):
        return f"Square({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x},{self.y})"


SQUARES = [Square(x, y) for y in range(c.PLAYFIELD_SIZE) for x in range(c.PLAYFIELD_SIZE)]


class TankRec:
    def __init__(
            self,
            sq: Square,
            direction: Direction,
            on_waiting_tunnel=False,
            is_sliding=False,
            sliding_dr=STATIONARY
    ):
        self.sq: Square = sq
        self.direction: Direction = direction
        self.on_waiting_tunnel = on_waiting_tunnel  # Indicates that tank is on a waiting tunnel
        self.is_sliding = is_sliding
        self.sliding_dr: Direction = sliding_dr

    def __repr__(self):
        return f"TankRec({self.sq}, {self.direction}, {self.on_waiting_tunnel}, {self.is_sliding}, {self.sliding_dr})"


class LaserRec:
    def __init__(
            self,
            sq=Square(5, 10),
            dir_front=UP,
            dir_back=LEFT,
            colour=c.LaserColorR,
    ):
        self.sq: Square = sq
        self.dir_front: Direction = dir_front
        self.dir_back: Direction = dir_back
        self.colour = colour


class LevelInfo:
    def __init__(
            self,
            number: int,
            title: str,
            hint: str,
            author: str,
            difficulty: str,
            filename: str,
    ):
        self.number: int = number
        self.title: str = title
        self.hint: str = hint
        self.author: str = author
        self.difficulty: str = difficulty
        self.filename: str = filename


# class SlidingData:  # Sliding Struct
#     def __init__(
#             self,
#             sq: Square,
#             dr: Direction,
#     ):
#         self.sq: Square = sq  # Last XY position of object to move
#         self.dr: Direction = dr  # Direction to move in Delta Cords


class GameState:
    def __init__(self):
        self.terrain = [c.GRASS for _ in range(c.PLAYFIELD_SIZE ** 2)]
        self.items = [c.EMPTY for _ in range(c.PLAYFIELD_SIZE ** 2)]
        self.tank = TankRec(Square(x=7, y=15), direction=UP)
        self.laser = LaserRec()
        self.laser_live = False
        self.sliding_items: dict[Square, Direction] = {}
        self.score_shots = 0
        self.score_moves = 0
        self.reached_flag = False
        self.player_dead = False
