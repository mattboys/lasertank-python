import os
import threading
from tkinter import *
import pygame
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)
from constants import *

# from LTank2 import *

GameBoardWidth = 32 * 16
GameBoardHeight = 32 * 16

SPRITE_SIZE = 32

GameBoardOffsetX = 0
GameBoardOffsetY = 0
GameBoardWidth = SPRITE_SIZE * 16 + 2 * GameBoardOffsetX
GameBoardHeight = SPRITE_SIZE * 16 + 2 * GameBoardOffsetY

EditorOn = False  # true when in editor mode
QHELP = False  # True when Quick Help is On

# TODO: Load keyboard shortcuts (LoadAccelerators)

# Get filenames for resource files
# scriptFile = os.path.dirname(os.path.realpath(__file__))
# INIFile = os.path.join(scriptFile, INIFileName)
# LANGFile = os.path.join(scriptFile, LANGFileName)
# HelpFile = os.path.join(scriptFile, HelpFileName)
# TODO: If running from the command line then load lvl, assign HS file, LoadNextLevel False

# TODO: Set up font

class UI(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.start()

	def run(self):
		# Set up for pygame
		# pygame.init()
		# pygame.display.set_mode()
		self.clock = pygame.time.Clock()

		# InitApplication
		# Set up window
		self.window_root_MainH = Tk()  # Main window (root)
		self.window_root_MainH.resizable(False, False)  # Can't resize window in x or y
		self.window_root_MainH.title(App_Title)
		# TODO: Set icon
		self.window_root_MainH.configure(background="light grey")
		# TODO: Set window size

		# Set up menu items
		self.window_root_MainH.option_add("*tearOff", False)
		self.menu_main_MMenu = Menu(
			self.window_root_MainH
		)  # Main menu (swapped with Edit Menu when in EditorOn mode)
		self.menu_editor_EMenu = Menu(
			self.window_root_MainH
		)  # Editor menu (swapped with Main Menu when not in EditorOn mode) MENU2

		self.menu_RecordGame_checked = BooleanVar()
		self.menu_OptionsAnimation_checked = BooleanVar()
		self.menu_OptionsSound_checked = BooleanVar()
		self.menu_OptionsRemeberLastLevel_checked = BooleanVar()
		self.menu_OptionsSkipCompletedLevels_checked = BooleanVar()
		self.menu_OptionsAutoRecord_checked = BooleanVar()
		self.menu_OptionsDisableWarnings_checked = BooleanVar()
		self.menu_SizeSmall_checked = BooleanVar()
		self.menu_SizeMedium_checked = BooleanVar()
		self.menu_SizeLarge_checked = BooleanVar()
		self.menu_DifficultyKids_checked = BooleanVar()
		self.menu_DifficultyEasy_checked = BooleanVar()
		self.menu_DifficultyMedium_checked = BooleanVar()
		self.menu_DifficultyHard_checked = BooleanVar()
		self.menu_DifficultyDeadly_checked = BooleanVar()

		self.menu_OptionsAnimation_checked.set(True)
		self.menu_OptionsSound_checked.set(True)
		self.menu_OptionsRemeberLastLevel_checked.set(True)
		self.menu_SizeSmall_checked.set(True)

		self.menu_Game = Menu(self.menu_main_MMenu)
		self.menu_Game.add_command(
			label="New", accelerator="F2", command=lambda: self.queue_command("command_New_101"), underline=0
		)
		self.menu_Game.add_command(
			label="Load Level...", accelerator="L", command=lambda: self.queue_command("command_LoadLevel_106"), underline=0
		)
		self.menu_Game.add_command(
			label="Skip Level", accelerator="S", command=lambda: self.queue_command("command_SkipLevel_107"), underline=0
		)
		self.menu_Game.add_command(
			label="Previous Level",
			accelerator="P",
			command=lambda: self.queue_command("command_PreviousLevel_119"),
			underline=0,
		)
		self.menu_Game.add_command(
			label="Last Level Played",
			accelerator="BkSp",
			command=lambda: self.queue_command("command_LastLevelPlayed_118"),
			underline=16,
			state="disabled",
		)
		self.menu_Game.add_separator()
		self.menu_Game.add_command(
			label="Open Data File...",
			accelerator="O",
			command=lambda: self.queue_command("command_OpenDataFile_108"),
			underline=0,
		)
		self.menu_Game.add_separator()
		self.menu_Game.add_command(
			label="View High Scores",
			accelerator="V",
			command=lambda: self.queue_command("command_ViewHighScores_113"),
			underline=0,
		)
		self.menu_Game.add_command(
			label="Global High Score List",
			accelerator="G",
			command=lambda: self.queue_command("command_GlobalHighScoreList_906"),
			underline=0,
		)
		self.menu_Game.add_separator()
		self.menu_Game.add_checkbutton(
			label="Record Game",
			accelerator="F5",
			command=lambda: self.queue_command("command_RecordGame_123"),
			underline=0,
			variable=self.menu_RecordGame_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Game.add_command(
			label="Save Recording",
			accelerator="F6",
			command=lambda: self.queue_command("command_SaveRecording_117"),
			underline=1,
			state="disabled",
		)
		self.menu_Game.add_command(
			label="Resume Recording",
			accelerator="F8",
			command=lambda: self.queue_command("command_ResumeRecording_125"),
			underline=9,
		)
		self.menu_Game.add_command(
			label="Playback Game...",
			accelerator="F7",
			command=lambda: self.queue_command("command_PlaybackGame_114"),
			underline=4,
		)
		self.menu_Game.add_separator()
		self.menu_Game.add_command(
			label="Print GameBoard", command=lambda: self.queue_command("command_PrintGameBoard_126"), underline=2
		)
		self.menu_Game.add_separator()
		self.menu_Game.add_command(label="Exit", command=lambda: self.queue_command("command_Exit_103"), underline=0)
		self.menu_main_MMenu.add_cascade(label="Game", underline=0, menu=self.menu_Game)

		self.menu_Move = Menu(self.menu_main_MMenu)
		self.menu_Move.add_command(
			label="ReStart", accelerator="R", command=lambda: self.queue_command("command_ReStart_105"), underline=0
		)
		self.menu_Move.add_command(
			label="Undo Last Move/Shot",
			accelerator="U",
			command=lambda: self.queue_command("command_UndoLastMoveShot_110"),
			underline=0,
			state="disabled",
		)
		self.menu_Move.add_command(
			label="Save Position",
			accelerator="Ctrl+C",
			command=lambda: self.queue_command("command_SavePosition_111"),
			underline=0,
		)
		self.menu_Move.add_command(
			label="Restore Position",
			accelerator="Crtl+V",
			command=lambda: self.queue_command("command_RestorePosition_112"),
			underline=8,
			state="disabled",
		)
		self.menu_Move.add_command(
			label="RePlay", accelerator="F4", command=lambda: self.queue_command("command_RePlay_124"), underline=5
		)
		self.menu_main_MMenu.add_cascade(label="Move", underline=0, menu=self.menu_Move)

		self.menu_Options = Menu(self.menu_main_MMenu)
		self.menu_Options.add_checkbutton(
			label="Animation",
			accelerator="A",
			command=lambda: self.queue_command("command_Animation_104"),
			underline=0,
			variable=self.menu_OptionsAnimation_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Options.add_checkbutton(
			label="Sound",
			accelerator="N",
			command=lambda: self.queue_command("command_Sound_102"),
			underline=4,
			variable=self.menu_OptionsSound_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Options.add_checkbutton(
			label="Remember Last Level",
			command=lambda: self.queue_command("command_RememberLastLevel_109"),
			underline=0,
			variable=self.menu_OptionsRemeberLastLevel_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Options.add_checkbutton(
			label="Skip Completed Levels",
			command=lambda: self.queue_command("command_SkipCompletedLevels_116"),
			underline=1,
			variable=self.menu_OptionsSkipCompletedLevels_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Options.add_checkbutton(
			label="AutoRecord",
			command=lambda: self.queue_command("command_AutoRecord_115"),
			underline=2,
			variable=self.menu_OptionsAutoRecord_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Options.add_checkbutton(
			label="Disable Warnings",
			command=lambda: self.queue_command("command_DisableWarnings_127"),
			underline=8,
			variable=self.menu_OptionsDisableWarnings_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Options.add_separator()
		self.menu_Size = Menu(self.menu_main_MMenu)
		self.menu_Size.add_checkbutton(
			label="Small",
			command=lambda: self.queue_command("command_SizeSmall_120"),
			underline=0,
			variable=self.menu_SizeSmall_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Size.add_checkbutton(
			label="Medium",
			command=lambda: self.queue_command("command_SizeMedium_121"),
			underline=0,
			variable=self.menu_SizeMedium_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Size.add_checkbutton(
			label="Large",
			command=lambda: self.queue_command("command_SizeLarge_122"),
			underline=0,
			variable=self.menu_SizeLarge_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Options.add_cascade(label="Size", underline=0, menu=self.menu_Size)
		self.menu_Options.add_command(
			label="Change Difficulty...",
			accelerator="D",
			command=lambda: self.queue_command("command_ChangeDifficulty_225"),
			underline=7,
		)
		self.menu_Options.add_command(
			label="Change Graphics ...",
			accelerator="Ctrl+G",
			command=lambda: self.queue_command("command_ChangeGraphics_226"),
			underline=7,
		)
		self.menu_main_MMenu.add_cascade(label="Options", underline=0, menu=self.menu_Options)

		self.menu_main_MMenu.add_command(
			label="Editor [F9]", command=lambda: self.queue_command("command_Editor_201"), underline=0
		)

		self.menu_Help = Menu(self.menu_main_MMenu)
		self.menu_Help.add_command(
			label="Hint", accelerator="H", command=lambda: self.queue_command("command_Hint_301"), underline=0
		)
		self.menu_Help.add_separator()
		self.menu_Help.add_command(label="Index", command=lambda: self.queue_command("command_Index_902"), underline=0)
		self.menu_Help.add_command(
			label="Quick Help", accelerator="F1", command=lambda: self.queue_command("command_QuickHelp_907"), underline=0
		)
		self.menu_Help.add_command(
			label="Revisions (History)", command=lambda: self.queue_command("command_RevisionsHistory_904"), underline=0
		)
		self.menu_Help.add_separator()
		self.menu_Help.add_command(label="About", command=lambda: self.queue_command("command_About_901"), underline=0)
		self.menu_main_MMenu.add_cascade(label="Help", underline=0, menu=self.menu_Help)

		# Editor
		self.menu_Editor = Menu(self.menu_editor_EMenu)
		self.menu_Editor.add_command(
			label="Clear Field",
			accelerator="Ctrl+C",
			command=lambda: self.queue_command("command_EditorClearField_601"),
			underline=0,
		)
		self.menu_Editor.add_command(
			label="Load Level...",
			accelerator="Ctrl+L",
			command=lambda: self.queue_command("command_EditorLoadLevel_602"),
			underline=0,
		)
		self.menu_Editor.add_command(
			label="Save Level",
			accelerator="Ctrl+S",
			command=lambda: self.queue_command("command_EditorSaveLevel_603"),
			underline=0,
		)
		self.menu_Editor.add_command(
			label="Save As...", command=lambda: self.queue_command("command_EditorSaveAs_606"), underline=5
		)
		self.menu_Editor.add_command(label="Exit", command=lambda: self.queue_command("command_Exit_103"), underline=0)
		self.menu_editor_EMenu.add_cascade(label="Editor", underline=0, menu=self.menu_Editor)

		self.menu_editor_EMenu.add_command(label="Hint", command=lambda: self.queue_command("command_EditHint_605"), underline=0)

		self.menu_Shift = Menu(self.menu_editor_EMenu)
		self.menu_Shift.add_command(
			label="Right",
			accelerator="Ctrl+Direction",
			command=lambda: self.queue_command("command_ShiftRight_710"),
			underline=0,
		)
		self.menu_Shift.add_command(label="Left", command=lambda: self.queue_command("command_ShiftLeft_711"), underline=0)
		self.menu_Shift.add_command(label="Up", command=lambda: self.queue_command("command_ShiftUp_712"), underline=0)
		self.menu_Shift.add_command(label="Down", command=lambda: self.queue_command("command_ShiftDown_713"), underline=0)
		self.menu_editor_EMenu.add_cascade(label="Shift", underline=0, menu=self.menu_Shift)

		self.menu_editor_EMenu.add_command(
			label="Close Editor [F9]", command=lambda: self.queue_command("command_CloseEditor_604"), underline=0
		)

		self.menu_Difficulty = Menu(self.menu_editor_EMenu)
		self.menu_Difficulty.add_checkbutton(
			label="Kids",
			command=lambda: self.queue_command("command_EditDifficultyKids_701"),
			underline=0,
			variable=self.menu_DifficultyKids_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Difficulty.add_checkbutton(
			label="Easy",
			command=lambda: self.queue_command("command_EditDifficultyEasy_702"),
			underline=0,
			variable=self.menu_DifficultyEasy_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Difficulty.add_checkbutton(
			label="Medium",
			command=lambda: self.queue_command("command_EditDifficultyMedium_703"),
			underline=0,
			variable=self.menu_DifficultyMedium_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Difficulty.add_checkbutton(
			label="Hard",
			command=lambda: self.queue_command("command_EditDifficultyHard_704"),
			underline=0,
			variable=self.menu_DifficultyHard_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_Difficulty.add_checkbutton(
			label="Deadly",
			command=lambda: self.queue_command("command_EditDifficultyDeadly_705"),
			underline=0,
			variable=self.menu_DifficultyDeadly_checked,
			onvalue=TRUE,
			offvalue=FALSE,
		)
		self.menu_editor_EMenu.add_cascade(label="Difficulty", underline=0, menu=self.menu_Difficulty)

		self.menu_Help = Menu(self.menu_editor_EMenu)
		self.menu_Help.add_command(
			label="Editor", accelerator="F1", command=lambda: self.queue_command("command_HelpEditor_903"), underline=0
		)
		self.menu_Help.add_command(
			label="Writing Levels", command=lambda: self.queue_command("command_HelpWritingLevels_905"), underline=0
		)
		self.menu_Help.add_separator()
		self.menu_Help.add_command(label="About", command=lambda: self.queue_command("command_HelpAbout_901"), underline=0)
		self.menu_editor_EMenu.add_cascade(label="Help", underline=0, menu=self.menu_Help)

		self.window_root_MainH.configure(menu=self.menu_main_MMenu)

		# ContXPos = 419
		# Frames for GUI layout
		# canvas_game = Canvas(width=GameBoardWidth, height=GameBoardHeight, bg='blue')
		self.frame_game = Frame(self.window_root_MainH, width=GameBoardWidth, height=GameBoardHeight, )
		frame_buttons = Frame(width=100, padx=5, pady=5)

		# Edit boxes
		self.lbl_LevelNumber = Label(frame_buttons, text="Level Number")
		self.ent_LevelNumber = Entry(frame_buttons)
		self.lbl_LevelName = Label(frame_buttons, text="Level Name")
		self.ent_LevelName = Entry(frame_buttons)
		self.lbl_LevelAuthor = Label(frame_buttons, text="Author")
		self.ent_LevelAuthor = Entry(frame_buttons)
		self.lbl_Moves = Label(frame_buttons, text="Moves")
		self.ent_Moves = Entry(frame_buttons)
		self.lbl_Shots = Label(frame_buttons, text="Shots")
		self.ent_Shots = Entry(frame_buttons)

		# Buttons
		self.btn1_Undo = Button(
			frame_buttons,
			text=btn1_Undo_text,
			command=lambda: self.queue_command("command_UndoLastMoveShot_110"),
			state="disabled",
		)  # "Undo"
		self.btn2_SavePosition = Button(
			frame_buttons,
			text=btn2_SavePosition_text,
			command=lambda: self.queue_command("command_SavePosition_111"),
			state="disabled",
		)  # "Save Position"
		self.btn3_RestorePosition = Button(
			frame_buttons,
			text=btn3_RestorePosition_text,
			command=lambda: self.queue_command("command_RestorePosition_112"),
			state="disabled",
		)  # "Restore Position"
		self.btn4_New = Button(frame_buttons, text=btn4_New_text, command=lambda: self.queue_command("command_New_101"))  # "New"
		self.btn5_LevelPrev = Button(
			frame_buttons, text=btn5_LevelPrev_text, command=lambda: self.queue_command("command_PreviousLevel_119")
		)  # "<< Level"
		self.btn6_LevelNext = Button(
			frame_buttons, text=btn6_LevelNext_text, command=lambda: self.queue_command("command_SkipLevel_107")
		)  # "Level >>"
		self.btn7_Hint = Button(
			frame_buttons, text=btn7_Hint_text, command=lambda: self.queue_command("command_Hint_301"), state="disabled"
		)  # "Hint"
		self.btn8_Restart = Button(
			frame_buttons, text=btn8_Restart_text, command=lambda: self.queue_command("command_ReStart_105"), state="disabled"
		)  # "Restart"
		self.btn9_LoadLevel = Button(
			frame_buttons, text=btn9_LoadLevel_text, command=lambda: self.queue_command("command_LoadLevel_106")
		)  # "Load Level"

		# Layout
		pad_x = 2
		pad_y = 2

		self.lbl_LevelNumber.grid(row=0, columnspan=2, padx=pad_x, pady=pad_y)
		self.ent_LevelNumber.grid(row=1, columnspan=2, padx=pad_x, pady=pad_y)
		self.lbl_LevelName.grid(row=2, columnspan=2, padx=pad_x, pady=pad_y)
		self.ent_LevelName.grid(row=3, columnspan=2, padx=pad_x, pady=pad_y)
		self.lbl_LevelAuthor.grid(row=4, columnspan=2, padx=pad_x, pady=pad_y)
		self.ent_LevelAuthor.grid(row=5, columnspan=2, padx=pad_x, pady=pad_y)
		self.lbl_Moves.grid(row=6, column=0, padx=pad_x, pady=pad_y)
		self.lbl_Shots.grid(row=6, column=1, padx=pad_x, pady=pad_y)
		self.ent_Moves.grid(row=7, column=0, padx=pad_x, pady=pad_y)
		self.ent_Shots.grid(row=7, column=1, padx=pad_x, pady=pad_y)
		self.btn1_Undo.grid(row=9, column=0, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn7_Hint.grid(row=9, column=1, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn2_SavePosition.grid(row=10, columnspan=2, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn3_RestorePosition.grid(row=11, columnspan=2, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn4_New.grid(row=12, column=0, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn8_Restart.grid(row=12, column=1, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn9_LoadLevel.grid(row=13, columnspan=2, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn5_LevelPrev.grid(row=14, column=0, padx=pad_x, pady=pad_y, sticky=W + E)
		self.btn6_LevelNext.grid(row=14, column=1, padx=pad_x, pady=pad_y, sticky=W + E)

		self.frame_game.pack(fill=BOTH, side=LEFT, expand=TRUE)
		frame_buttons.pack(side=RIGHT, expand=FALSE)

		# Show the window so it's assigned an ID.
		self.window_root_MainH.update()
		# Embed pygame into frame_game
		os.environ["SDL_WINDOWID"] = str(self.frame_game.winfo_id())
		os.environ["SDL_VIDEODRIVER"] = "windib"

		# Usual pygame initialization
		pygame.init()
		pygame.display.init()

		self.screen = pygame.display.set_mode((GameBoardWidth, GameBoardHeight))
		self.screen.fill(pygame.Color(0, 255, 0))

		pygame.display.update()


		# canvas = Canvas(self.window_root_MainH, width=GameBoardWidth, height=GameBoardHeight)
		# canvas.pack()
		# self.window_root_MainH.geometry('1000x1000')

		# Start window
		self.window_root_MainH.after(0, self.update)
		self.window_root_MainH.mainloop()

	def queue_command(self, command):
		print(command)

	def update(self):
		# Get inputs
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				print("quit")
			elif event.type == KEYDOWN and event.key == K_UP:
				print("Key UP")
			elif event.type == KEYDOWN and event.key == K_DOWN:
				print("Key DOWN")
			elif event.type == KEYDOWN and event.key == K_LEFT:
				print("Key LEFT")
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				print("Key RIGHT")
			elif event.type == KEYDOWN and event.key == K_SPACE:
				print("Key SPACE")

		# Update board state
		#game.update()

		# Draw board and animations
		#game.draw(screen)
		pygame.display.update()
		self.clock.tick(60)
		self.window_root_MainH.after(0, self.update)

if __name__ == "__main__":
	ui = UI()
	while True:
		print("looping")
		ui.update()