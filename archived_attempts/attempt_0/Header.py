import os

LevelData = "LaserTank.lvl"
# LevelData = 'tunnel_test.lvl'

FILENAME_LEVELS = os.path.join("Files", LevelData)


INIFileName = "LaserTank.ini"


# From lt32l_us.inc
App_Title = "LaserTank"
App_Version = "4.1.2"
FILE_VERSION = "4.1.2\0"
PRODUCT_VERSION = "4.1.2\0"

# The name of Language File
LANGFilePath = "Language\\"
LANGFileName = "Language\\Language.dat"
HelpFileName = "LaserTank.hlp"
GAME_BMP = "game.bmp"
MASK_BMP = "mask.bmp"
OPENING_BMP = "opening.bmp"
CONTROL_BMP = "control.bmp"

# number of lines of each sections in the Language File
SIZE_BUTTON = 9
SIZE_TEXT = 48
SIZE_MMENU = 49
SIZE_EMENU = 24
SIZE_DIALOGS = 4 + 3 + 9 + 9 + 7 + 3 + 14 + 1 + 4 + 3 + 9 + 4 + 7 + 3 + 10 + 6
SIZE_ABOUTMSG = 14
SIZE_ALL = (
    SIZE_BUTTON + SIZE_TEXT + SIZE_MMENU + SIZE_EMENU + SIZE_ABOUTMSG + SIZE_DIALOGS
)

# Start LINES in the Language File
START_MMENU = 0
START_EMENU = START_MMENU + SIZE_MMENU
START_BUTTON = START_EMENU + SIZE_EMENU
START_TEXT = START_BUTTON + SIZE_BUTTON
START_DIALOGS = START_TEXT + SIZE_TEXT
START_ABOUTMSG = START_DIALOGS + SIZE_ABOUTMSG
