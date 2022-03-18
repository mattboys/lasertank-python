######################################################
##             LaserTank ver 4.0                     ##
##               By Jim Kindley                      ##
##               (c) 2001                            ##
##         The Program and Source is Public Domain   ##
#######################################################
##       Release version 2005 by Yves Maingoy        ##
##               ymaingoy@free.fr                    ##
#######################################################

""" LaserTank Ver 4.1 (32Bit) Resource File """

from tkinter import *
import pygame

from Header import *
from menu_commands import *
from language import *

# from LTank2 import *

GameBoardWidth = 32 * 16
GameBoardHeight = 32 * 16

EditorOn = False  # true when in editor mode
QHELP = False  # True when Quick Help is On

# TODO: Load keyboard shortcuts (LoadAccelerators)

# Get filenames for resource files
scriptFile = os.path.dirname(os.path.realpath(__file__))
INIFile = os.path.join(scriptFile, INIFileName)
LANGFile = os.path.join(scriptFile, LANGFileName)
HelpFile = os.path.join(scriptFile, HelpFileName)
# TODO: If running from the command line then load lvl, assign HS file, LoadNextLevel False

# TODO: Set up font

# InitApplication
# Set up window
window_root_MainH = Tk()  # Main window (root)
window_root_MainH.resizable(False, False)  # Can't resize window in x or y
window_root_MainH.title(App_Title)
# TODO: Set icon
window_root_MainH.configure(background="light grey")
# TODO: Set window size

# Set up menu items
window_root_MainH.option_add("*tearOff", False)
menu_main_MMenu = Menu(
    window_root_MainH
)  # Main menu (swapped with Edit Menu when in EditorOn mode)
menu_editor_EMenu = Menu(
    window_root_MainH
)  # Editor menu (swapped with Main Menu when not in EditorOn mode) MENU2

menu_RecordGame_checked = BooleanVar()
menu_OptionsAnimation_checked = BooleanVar()
menu_OptionsSound_checked = BooleanVar()
menu_OptionsRemeberLastLevel_checked = BooleanVar()
menu_OptionsSkipCompletedLevels_checked = BooleanVar()
menu_OptionsAutoRecord_checked = BooleanVar()
menu_OptionsDisableWarnings_checked = BooleanVar()
menu_SizeSmall_checked = BooleanVar()
menu_SizeMedium_checked = BooleanVar()
menu_SizeLarge_checked = BooleanVar()
menu_DifficultyKids_checked = BooleanVar()
menu_DifficultyEasy_checked = BooleanVar()
menu_DifficultyMedium_checked = BooleanVar()
menu_DifficultyHard_checked = BooleanVar()
menu_DifficultyDeadly_checked = BooleanVar()

menu_OptionsAnimation_checked.set(True)
menu_OptionsSound_checked.set(True)
menu_OptionsRemeberLastLevel_checked.set(True)
menu_SizeSmall_checked.set(True)


menu_Game = Menu(menu_main_MMenu)
menu_Game.add_command(
    label="New", accelerator="F2", command=command_New_101, underline=0
)
menu_Game.add_command(
    label="Load Level...", accelerator="L", command=command_LoadLevel_106, underline=0
)
menu_Game.add_command(
    label="Skip Level", accelerator="S", command=command_SkipLevel_107, underline=0
)
menu_Game.add_command(
    label="Previous Level",
    accelerator="P",
    command=command_PreviousLevel_119,
    underline=0,
)
menu_Game.add_command(
    label="Last Level Played",
    accelerator="BkSp",
    command=command_LastLevelPlayed_118,
    underline=16,
    state="disabled",
)
menu_Game.add_separator()
menu_Game.add_command(
    label="Open Data File...",
    accelerator="O",
    command=command_OpenDataFile_108,
    underline=0,
)
menu_Game.add_separator()
menu_Game.add_command(
    label="View High Scores",
    accelerator="V",
    command=command_ViewHighScores_113,
    underline=0,
)
menu_Game.add_command(
    label="Global High Score List",
    accelerator="G",
    command=command_GlobalHighScoreList_906,
    underline=0,
)
menu_Game.add_separator()
menu_Game.add_checkbutton(
    label="Record Game",
    accelerator="F5",
    command=command_RecordGame_123,
    underline=0,
    variable=menu_RecordGame_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Game.add_command(
    label="Save Recording",
    accelerator="F6",
    command=command_SaveRecording_117,
    underline=1,
    state="disabled",
)
menu_Game.add_command(
    label="Resume Recording",
    accelerator="F8",
    command=command_ResumeRecording_125,
    underline=9,
)
menu_Game.add_command(
    label="Playback Game...",
    accelerator="F7",
    command=command_PlaybackGame_114,
    underline=4,
)
menu_Game.add_separator()
menu_Game.add_command(
    label="Print GameBoard", command=command_PrintGameBoard_126, underline=2
)
menu_Game.add_separator()
menu_Game.add_command(label="Exit", command=command_Exit_103, underline=0)
menu_main_MMenu.add_cascade(label="Game", underline=0, menu=menu_Game)

menu_Move = Menu(menu_main_MMenu)
menu_Move.add_command(
    label="ReStart", accelerator="R", command=command_ReStart_105, underline=0
)
menu_Move.add_command(
    label="Undo Last Move/Shot",
    accelerator="U",
    command=command_UndoLastMoveShot_110,
    underline=0,
    state="disabled",
)
menu_Move.add_command(
    label="Save Position",
    accelerator="Ctrl+C",
    command=command_SavePosition_111,
    underline=0,
)
menu_Move.add_command(
    label="Restore Position",
    accelerator="Crtl+V",
    command=command_RestorePosition_112,
    underline=8,
    state="disabled",
)
menu_Move.add_command(
    label="RePlay", accelerator="F4", command=command_RePlay_124, underline=5
)
menu_main_MMenu.add_cascade(label="Move", underline=0, menu=menu_Move)

menu_Options = Menu(menu_main_MMenu)
menu_Options.add_checkbutton(
    label="Animation",
    accelerator="A",
    command=command_Animation_104,
    underline=0,
    variable=menu_OptionsAnimation_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Options.add_checkbutton(
    label="Sound",
    accelerator="N",
    command=command_Sound_102,
    underline=4,
    variable=menu_OptionsSound_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Options.add_checkbutton(
    label="Remember Last Level",
    command=command_RememberLastLevel_109,
    underline=0,
    variable=menu_OptionsRemeberLastLevel_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Options.add_checkbutton(
    label="Skip Completed Levels",
    command=command_SkipCompletedLevels_116,
    underline=1,
    variable=menu_OptionsSkipCompletedLevels_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Options.add_checkbutton(
    label="AutoRecord",
    command=command_AutoRecord_115,
    underline=2,
    variable=menu_OptionsAutoRecord_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Options.add_checkbutton(
    label="Disable Warnings",
    command=command_DisableWarnings_127,
    underline=8,
    variable=menu_OptionsDisableWarnings_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Options.add_separator()
menu_Size = Menu(menu_main_MMenu)
menu_Size.add_checkbutton(
    label="Small",
    command=command_SizeSmall_120,
    underline=0,
    variable=menu_SizeSmall_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Size.add_checkbutton(
    label="Medium",
    command=command_SizeMedium_121,
    underline=0,
    variable=menu_SizeMedium_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Size.add_checkbutton(
    label="Large",
    command=command_SizeLarge_122,
    underline=0,
    variable=menu_SizeLarge_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Options.add_cascade(label="Size", underline=0, menu=menu_Size)
menu_Options.add_command(
    label="Change Difficulty...",
    accelerator="D",
    command=command_ChangeDifficulty_225,
    underline=7,
)
menu_Options.add_command(
    label="Change Graphics ...",
    accelerator="Ctrl+G",
    command=command_ChangeGraphics_226,
    underline=7,
)
menu_main_MMenu.add_cascade(label="Options", underline=0, menu=menu_Options)

menu_main_MMenu.add_command(
    label="Editor [F9]", command=command_Editor_201, underline=0
)

menu_Help = Menu(menu_main_MMenu)
menu_Help.add_command(
    label="Hint", accelerator="H", command=command_Hint_301, underline=0
)
menu_Help.add_separator()
menu_Help.add_command(label="Index", command=command_Index_902, underline=0)
menu_Help.add_command(
    label="Quick Help", accelerator="F1", command=command_QuickHelp_907, underline=0
)
menu_Help.add_command(
    label="Revisions (History)", command=command_RevisionsHistory_904, underline=0
)
menu_Help.add_separator()
menu_Help.add_command(label="About", command=command_About_901, underline=0)
menu_main_MMenu.add_cascade(label="Help", underline=0, menu=menu_Help)

# Editor
menu_Editor = Menu(menu_editor_EMenu)
menu_Editor.add_command(
    label="Clear Field",
    accelerator="Ctrl+C",
    command=command_EditorClearField_601,
    underline=0,
)
menu_Editor.add_command(
    label="Load Level...",
    accelerator="Ctrl+L",
    command=command_EditorLoadLevel_602,
    underline=0,
)
menu_Editor.add_command(
    label="Save Level",
    accelerator="Ctrl+S",
    command=command_EditorSaveLevel_603,
    underline=0,
)
menu_Editor.add_command(
    label="Save As...", command=command_EditorSaveAs_606, underline=5
)
menu_Editor.add_command(label="Exit", command=command_Exit_103, underline=0)
menu_editor_EMenu.add_cascade(label="Editor", underline=0, menu=menu_Editor)

menu_editor_EMenu.add_command(label="Hint", command=command_EditHint_605, underline=0)

menu_Shift = Menu(menu_editor_EMenu)
menu_Shift.add_command(
    label="Right",
    accelerator="Ctrl+Direction",
    command=command_ShiftRight_710,
    underline=0,
)
menu_Shift.add_command(label="Left", command=command_ShiftLeft_711, underline=0)
menu_Shift.add_command(label="Up", command=command_ShiftUp_712, underline=0)
menu_Shift.add_command(label="Down", command=command_ShiftDown_713, underline=0)
menu_editor_EMenu.add_cascade(label="Shift", underline=0, menu=menu_Shift)

menu_editor_EMenu.add_command(
    label="Close Editor [F9]", command=command_CloseEditor_604, underline=0
)

menu_Difficulty = Menu(menu_editor_EMenu)
menu_Difficulty.add_checkbutton(
    label="Kids",
    command=command_EditDifficultyKids_701,
    underline=0,
    variable=menu_DifficultyKids_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Difficulty.add_checkbutton(
    label="Easy",
    command=command_EditDifficultyEasy_702,
    underline=0,
    variable=menu_DifficultyEasy_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Difficulty.add_checkbutton(
    label="Medium",
    command=command_EditDifficultyMedium_703,
    underline=0,
    variable=menu_DifficultyMedium_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Difficulty.add_checkbutton(
    label="Hard",
    command=command_EditDifficultyHard_704,
    underline=0,
    variable=menu_DifficultyHard_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_Difficulty.add_checkbutton(
    label="Deadly",
    command=command_EditDifficultyDeadly_705,
    underline=0,
    variable=menu_DifficultyDeadly_checked,
    onvalue=TRUE,
    offvalue=FALSE,
)
menu_editor_EMenu.add_cascade(label="Difficulty", underline=0, menu=menu_Difficulty)

menu_Help = Menu(menu_editor_EMenu)
menu_Help.add_command(
    label="Editor", accelerator="F1", command=command_HelpEditor_903, underline=0
)
menu_Help.add_command(
    label="Writing Levels", command=command_HelpWritingLevels_905, underline=0
)
menu_Help.add_separator()
menu_Help.add_command(label="About", command=command_HelpAbout_901, underline=0)
menu_editor_EMenu.add_cascade(label="Help", underline=0, menu=menu_Help)

window_root_MainH.configure(menu=menu_main_MMenu)


# ContXPos = 419
# Frames for GUI layout
# canvas_game = Canvas(width=GameBoardWidth, height=GameBoardHeight, bg='blue')
frame_game = Frame(window_root_MainH, width=GameBoardWidth, height=GameBoardHeight,)
frame_buttons = Frame(width=100, padx=5, pady=5)

# Embed pygame into frame_game
os.environ["SDL_WINDOWID"] = str(frame_game.winfo_id())
os.environ["SDL_VIDEODRIVER"] = "windib"
screen = pygame.display.set_mode((GameBoardWidth, GameBoardHeight))
screen.fill(pygame.Color(255, 255, 255))

pygame.display.init()
pygame.display.update()


frame_game.pack(fill=BOTH, side=LEFT, expand=TRUE)
frame_buttons.pack(side=RIGHT, expand=FALSE)


# Edit boxes
lbl_LevelNumber = Label(frame_buttons, text="Level Number")
ent_LevelNumber = Entry(frame_buttons)
lbl_LevelName = Label(frame_buttons, text="Level Name")
ent_LevelName = Entry(frame_buttons)
lbl_LevelAuthor = Label(frame_buttons, text="Author")
ent_LevelAuthor = Entry(frame_buttons)
lbl_Moves = Label(frame_buttons, text="Moves")
ent_Moves = Entry(frame_buttons)
lbl_Shots = Label(frame_buttons, text="Shots")
ent_Shots = Entry(frame_buttons)

# Buttons
btn1_Undo = Button(
    frame_buttons,
    text=btn1_Undo_text,
    command=command_UndoLastMoveShot_110,
    state="disabled",
)  # "Undo"
btn2_SavePosition = Button(
    frame_buttons,
    text=btn2_SavePosition_text,
    command=command_SavePosition_111,
    state="disabled",
)  # "Save Position"
btn3_RestorePosition = Button(
    frame_buttons,
    text=btn3_RestorePosition_text,
    command=command_RestorePosition_112,
    state="disabled",
)  # "Restore Position"
btn4_New = Button(frame_buttons, text=btn4_New_text, command=command_New_101)  # "New"
btn5_LevelPrev = Button(
    frame_buttons, text=btn5_LevelPrev_text, command=command_PreviousLevel_119
)  # "<< Level"
btn6_LevelNext = Button(
    frame_buttons, text=btn6_LevelNext_text, command=command_SkipLevel_107
)  # "Level >>"
btn7_Hint = Button(
    frame_buttons, text=btn7_Hint_text, command=command_Hint_301, state="disabled"
)  # "Hint"
btn8_Restart = Button(
    frame_buttons, text=btn8_Restart_text, command=command_ReStart_105, state="disabled"
)  # "Restart"
btn9_LoadLevel = Button(
    frame_buttons, text=btn9_LoadLevel_text, command=command_LoadLevel_106
)  # "Load Level"


# Layout
pad_x = 2
pad_y = 2

lbl_LevelNumber.grid(row=0, columnspan=2, padx=pad_x, pady=pad_y)
ent_LevelNumber.grid(row=1, columnspan=2, padx=pad_x, pady=pad_y)
lbl_LevelName.grid(row=2, columnspan=2, padx=pad_x, pady=pad_y)
ent_LevelName.grid(row=3, columnspan=2, padx=pad_x, pady=pad_y)
lbl_LevelAuthor.grid(row=4, columnspan=2, padx=pad_x, pady=pad_y)
ent_LevelAuthor.grid(row=5, columnspan=2, padx=pad_x, pady=pad_y)
lbl_Moves.grid(row=6, column=0, padx=pad_x, pady=pad_y)
lbl_Shots.grid(row=6, column=1, padx=pad_x, pady=pad_y)
ent_Moves.grid(row=7, column=0, padx=pad_x, pady=pad_y)
ent_Shots.grid(row=7, column=1, padx=pad_x, pady=pad_y)
btn1_Undo.grid(row=9, column=0, padx=pad_x, pady=pad_y, sticky=W + E)
btn7_Hint.grid(row=9, column=1, padx=pad_x, pady=pad_y, sticky=W + E)
btn2_SavePosition.grid(row=10, columnspan=2, padx=pad_x, pady=pad_y, sticky=W + E)
btn3_RestorePosition.grid(row=11, columnspan=2, padx=pad_x, pady=pad_y, sticky=W + E)
btn4_New.grid(row=12, column=0, padx=pad_x, pady=pad_y, sticky=W + E)
btn8_Restart.grid(row=12, column=1, padx=pad_x, pady=pad_y, sticky=W + E)
btn9_LoadLevel.grid(row=13, columnspan=2, padx=pad_x, pady=pad_y, sticky=W + E)
btn5_LevelPrev.grid(row=14, column=0, padx=pad_x, pady=pad_y, sticky=W + E)
btn6_LevelNext.grid(row=14, column=1, padx=pad_x, pady=pad_y, sticky=W + E)


# Set up canvas

# canvas = Canvas(window_root_MainH, width=WIDTH, height=HEIGHT)
# canvas.pack()
# window_root_MainH.geometry('1000x1000')

# Start window
# window_root_MainH.mainloop()
