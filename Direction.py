N = "N"
E = "E"
S = "S"
W = "W"
SHOOT = "F"
NONE = "0"


def get_opposite(direction):
    lookup = {
        N: S,
        S: N,
        E: W,
        W: E,
        NONE: NONE,
    }
    return lookup[direction]


def get_clockwise(direction):
    lookup = {
        N: E,
        E: S,
        S: W,
        W: N,
    }
    return lookup[direction]


def get_xy(direction):
    lookup = {
        N: (0, -1),
        E: (1, 0),
        S: (0, 1),
        W: (-1, 0),
        NONE: (0, 0),
    }
    return lookup[direction]


def reflection_angle_to_dirs(direction):
    lookup = {
        N: (W, N),
        E: (N, E),
        S: (E, S),
        W: (S, W),
    }
    return lookup[direction]


def vec_add(a, b):
    return a[0] + b[0], a[1] + b[1]
