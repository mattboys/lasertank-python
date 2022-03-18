App_Title = "LaserTank"
App_Version = "4.1.2"
FILE_VERSION = "4.1.2"
PRODUCT_VERSION = "4.1.2"

# The name of Language File
LANGFilePath = "Language\\"
LANGFileName = "Language\\Language.dat"
GAME_BMP = "game.bmp"
MASK_BMP = "mask.bmp"
OPENING_BMP = "opening.bmp"
CONTROL_BMP = "control.bmp" #Level information background


GAMEBOARD_SIZE = 16

DIFFICULTY_KIDS = 1
DIFFICULTY_EASY = 2
DIFFICULTY_MEDIUM = 4
DIFFICULTY_HARD = 8
DIFFICULTY_DEADLY = 16

OBJ_GRASS = 0
OBJ_TANK_UP = 1
OBJ_FLAG = 2
OBJ_WATER = 3
OBJ_SOLID = 4
OBJ_BLOCK = 5
OBJ_WALL = 6
OBJ_ANTITANK_UP = 7
OBJ_ANTITANK_RIGHT = 8
OBJ_ANTITANK_DOWN = 9
OBJ_ANTITANK_LEFT = 10
OBJ_MIRROR_LEFT_UP = 11
OBJ_MIRROR_UP_RIGHT = 12
OBJ_MIRROR_RIGHT_DOWN = 13
OBJ_MIRROR_DOWN_LEFT = 14
OBJ_CONVEYOR_UP = 15
OBJ_CONVEYOR_RIGHT = 16
OBJ_CONVEYOR_DOWN = 17
OBJ_CONVEYOR_LEFT = 18
OBJ_GLASS = 19
OBJ_ROTMIRROR_LEFT_UP = 20
OBJ_ROTMIRROR_UP_RIGHT = 21
OBJ_ROTMIRROR_RIGHT_DOWN = 22
OBJ_ROTMIRROR_DOWN_LEFT = 23
OBJ_ICE = 24
OBJ_THINICE = 25
OBJ_TUNNEL_0_RED = 64
OBJ_TUNNEL_1_GREEN = 66
OBJ_TUNNEL_2_BLUE = 68
OBJ_TUNNEL_3_CYAN = 70
OBJ_TUNNEL_4_YELLOW = 72
OBJ_TUNNEL_5_PINK = 74
OBJ_TUNNEL_6_WHITE = 76
OBJ_TUNNEL_7_GREY = 78

# Second-state Objects
OBJ_TANK_RIGHT = 30
OBJ_TANK_DOWN = 31
OBJ_TANK_LEFT = 32
OBJ_ANTITANK_DOWN_DEAD = 33
OBJ_BLOCK_SUNK = 34
OBJ_GLASS_GREEN = 35
OBJ_GLASS_RED = 36
OBJ_ANTITANK_RIGHT_DEAD = 37
OBJ_ANTITANK_LEFT_DEAD = 38
OBJ_ANTITANK_UP_DEAD = 39



# Game Defaults
LevelData = "LaserTank.lvl" # Default Level Data File
INIFileName = "LaserTank.ini"
# MAX text size for a lang_text
MAX_LANG_SIZE = 300

WM_USER = 0
MaxObjects = 26 # Maximum number of game objects used
MaxBitMaps = 58 # the maximum number of BitMaps ( + 1 )
XOffset = 17 # Game Board Offset from Left
YOffset = 17 # Game Board Offset from top
ani_delay = 4 # animation Delay in GameDelay units
GameDelay = 50 # Main Operation Loop
WM_GameOver = WM_USER + 1 # Send Message if there are no more levels
WM_Dead = WM_USER + 2 # Send Message when you die
WM_NewHS = WM_USER + 3 # Send to Display New High Score Dialog
WM_SaveRec = WM_USER + 4 # Send to Save Recording
App_Class = "LaserTC2" # The Class Name
UndoBufStep = 200 # Groth Amount of Undo Buffer
UndoMax = 10000 # Max Amount of Undo Buffer
RecBufStep = 10000 # Groth amount of Rec Buffer
RecMax = 65500 # Max recording steps saved to file
SlowPBSet = 5 # Delay of Slow Playback setting
MaxMBuffer = 20 # Size of Mouse Buffer
Obj_Water = 3 # Object Number 3 is water
Obj_Ice = 24 # Ice Object
Obj_ThinIce = 25 # Object Number of Thin Ice
Obj_Tunnel = 0x40 # Object 01dddddX = Tunnel
LTG_ID = "LTG1" # ID field of LTG file

# INI Profile Keys
psRLLOn = "RLL" # Profile String for remember last level
psRLLN = "RLLFilename" # remember last level file name
psRLLL = "RLLLevel" # Level number
psAni = "Animation"
psSound = "Sound"
psSize = "Size" # 1 = small, 3 = large
psXpos = "PosX"
psYpos = "PosY"
psUser = "Player"
psPBA = "Record Author"
psARec = "Auto_Record"
psSCL = "SkipComLev"
psDiff = "Diff_Setting"
psGM = "Graphics_Mode"
psGFN = "Graphics_File"
psGDN = "Graphics_Dir"
psDW = "DisableWarnings"
psYes = "Yes"
psNET = "NETWORK_INI" # 1 = Use INI file from C:\Windows

BADMOVE = 256

App_Strings = [
    # This is the Button Text
    "Undo",
    "Save Position",
    "Restore Position",
    "New",
    "<< Level",
    "Level >>",
    "Hint",
    "Restart",
    "Load Level",
    # This is others texts
    "The Level file can not be found\nPlease select a new one",
    "Level Files (*.LVL)",
    "Pick LaserTank Level File",
    "Playback Files (*.LPB)",
    "Save Playback File",
    "LaserTank Error",
    "Old High Score > M:",
    "M: ",
    " S: ",
    " I: ",
    "Congratulation's You beat it !!",
    "Playback Level : ",
    "\nRecorded by ",
    "\nCan Not be found in the current level_inital file\n< ",
    "Do You want to Continue Recording ?",
    "&Play",
    "&Pause",
    "Out of Memory - Undo Roll Over",
    "Open Playback file",
    "LaserTank Hint",
    "Level NOT Saved, Save Data ?",
    " - Kids",
    " - Easy",
    " - Medium",
    " - Hard",
    " - Deadly",
    " - [Editor]",
    "LaserTank Editor",
    "NOT a Valid LaserTank Graphics Set",
    "game.bmp and/or mask.bmp Not Found",
    "Open Playback file for Resume",
    "Return to Game",
    "< NO HINT SUBMITTED FOR THIS LEVEL >",
    "LaserTank Level #",
    "Select LaserTank Graphics Directory",
    "Game in Progress ...",
    "You will lose game data.\nDo you want to save the game ?",
    "Beat",
    "All",
    "Completed %d of %d levels",
    "Difficulty Set =",
    "KEMHD",
    "LaserTank Graphics file Not Found !",
    "LaserTank *** RECORDING ***",
    "Editor Instructions",
    "Revisions",
    "Writing Your Own Levels",
    "LaserTank.hlp",
]

LANGText = App_Strings  # TODO: Overwrite with lines from language.dat

btn1_Undo_text = LANGText[0]  # "Undo"
btn2_SavePosition_text = LANGText[1]  # "Save Position"
btn3_RestorePosition_text = LANGText[2]  # "Restore Position"
btn4_New_text = LANGText[3]  # "New"
btn5_LevelPrev_text = LANGText[4]  # "<< Level"
btn6_LevelNext_text = LANGText[5]  # "Level >>"
btn7_Hint_text = LANGText[6]  # "Hint"
btn8_Restart_text = LANGText[7]  # "Restart"
btn9_LoadLevel_text = LANGText[8]  # "Load Level"
