GAMEBOARD_SIZE = 16

MOVES_SHOOT = "F"
MOVES_N = "N"
MOVES_S = "S"
MOVES_E = "E"
MOVES_W = "W"

DIRECTION_N = "N"
DIRECTION_S = "S"
DIRECTION_E = "E"
DIRECTION_W = "W"
DIRECTION_NONE = None

DIFFICULTY_KIDS = "Kids"
DIFFICULTY_EASY = "Easy"
DIFFICULTY_MEDIUM = "Medium"
DIFFICULTY_HARD = "Hard"
DIFFICULTY_DEADLY = "Deadly"

# Terrain
GRASS = "Grass"
FLAG = "Flag"
WATER = "Water"
CONVEYOR = "Conveyor"
ICE = "Ice"
THINICE = "ThinIce"
BRIDGE = "Bridge"
TUNNEL = "Tunnel"

# ITEMS
EMPTY = "Empty"
SOLID = "Solid"
BLOCK = "Block"
WALL = "Wall"
ANTITANK = "Antitank"
DEADANTITANK = "DeadAntitank"
MIRROR = "Mirror"
GLASS = "Glass"
ROTMIRROR = "RotMirror"

TANK = "Tank"
LASER = "Laser"

# Defaults
DEFAULT_TANK = (TANK, {"position": (7, 15), "direction": DIRECTION_N})
DEFAULT_LASER = (LASER,)
DEFAULT_ITEM = (EMPTY,)
DEFAULT_TERRAIN = (GRASS,)
