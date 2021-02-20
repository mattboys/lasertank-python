def PlaySound(a, b, c):
	print("PlaySound() not implemented")

def LockResource(a):
	print("LockResource() not implemented")

def MessageBox(a, b, c, d):
	print("MessageBox() not implemented")

def LoadResource(a, b):
	print("LoadResource() not implemented")
	return 0

def FindResource(a, b, c):
	print("FindResource() not implemented")
	return None

def SetWindowText(*args):
	"""
	Changes the text of the specified window's title bar (if it has one). If the specified window is a control, the text of the control is changed. However, SetWindowText cannot change the text of a control in another application.
	"""
	print("SetWindowText() not implemented")
	return None

MB_ICONERROR = "ICONERROR"
MB_ICONHAND = "ICONHAND"
MB_ICONINFORMATION = "ICONINFORMATION"
MB_ICONQUESTION = "ICONQUESTION"
MB_OK = "OK"
MB_OKCANCEL = "OKCANCEL"
MB_SP = "SP"
MB_TOS = "TOS"
MB_YESNO = "YESNO"
MB_YESNOCANCEL = "YESNOCANCEL"

RT_RCDATA = "Application-defined resource (raw data)."

# lt32l_us.h
"""******************************************************
 **             LaserTank ver 4.1.1                   **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2005 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 ******************************************************"""
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

#
# ID of Dialogs
# Text values and old ID are in comments
#

# This is the Button Function ID number
ButID1 = 110
ButID2 = 111
ButID3 = 112
ButID4 = 101
ButID5 = 119
ButID6 = 107
ButID7 = 301
ButID8 = 105
ButID9 = 106

# number of linesof each sections in the Language File
SIZE_BUTTON = 9
SIZE_TEXT = 48
SIZE_MMENU = 49
SIZE_EMENU = 24
SIZE_DIALOGS =(4 + 3 + 9 + 9 + 7 + 3 + 14 + 1 + 4 + 3 + 9 + 4 + 7 + 3 + 10 + 6) # 96
SIZE_ABOUTMSG = 14
SIZE_ALL = (SIZE_BUTTON + SIZE_TEXT + SIZE_MMENU + SIZE_EMENU + SIZE_ABOUTMSG + SIZE_DIALOGS)

# Start LINES in the Language File
START_MMENU = 0
START_EMENU =(START_MMENU + SIZE_MMENU)
START_BUTTON =(START_EMENU + SIZE_EMENU)
START_TEXT =(START_BUTTON + SIZE_BUTTON)
START_DIALOGS =(START_TEXT + SIZE_TEXT)
# START_ABOUTMSG =(START_ABOUTMSG + SIZE_ABOUTMSG)

# Start LINES in the LANGText[]
OFFSET_TEXT = SIZE_BUTTON
OFFSET_DIALOGS =(OFFSET_TEXT + SIZE_TEXT)
OFFSET_ABOUTMSG =(OFFSET_DIALOGS + SIZE_DIALOGS)

LANGText = ["language not loaded" for i in range(SIZE_ALL) ] # All lines of Language.dat

ButText1 = LANGText[0]
ButText2 = LANGText[1]
ButText3 = LANGText[2]
ButText4 = LANGText[3]
ButText5 = LANGText[4]
ButText6 = LANGText[5]
ButText7 = LANGText[6]
ButText8 = LANGText[7]
ButText9 = LANGText[8]

txt001 = LANGText[OFFSET_TEXT + 0]
txt002 = LANGText[OFFSET_TEXT + 1]
txt003 = None
txt004 = LANGText[OFFSET_TEXT + 2]
txt005 = LANGText[OFFSET_TEXT + 3]
txt006 = LANGText[OFFSET_TEXT + 4]
txt007 = LANGText[OFFSET_TEXT + 5]
txt008 = LANGText[OFFSET_TEXT + 6]
txt009 = LANGText[OFFSET_TEXT + 7]
txt010 = LANGText[OFFSET_TEXT + 8]
txt011 = LANGText[OFFSET_TEXT + 9]
txt012 = LANGText[OFFSET_TEXT + 10]
txt013 = LANGText[OFFSET_TEXT + 11]
txt014 = LANGText[OFFSET_TEXT + 12]
txt015 = LANGText[OFFSET_TEXT + 13]
txt016 = LANGText[OFFSET_TEXT + 14]
txt017 = LANGText[OFFSET_TEXT + 15]
txt018 = LANGText[OFFSET_TEXT + 16]
txt019 = LANGText[OFFSET_TEXT + 17]
txt020 = LANGText[OFFSET_TEXT + 18]
txt021 = LANGText[OFFSET_TEXT + 19]
txt022 = LANGText[OFFSET_TEXT + 20]
txt023 = LANGText[OFFSET_TEXT + 21]
txt024 = LANGText[OFFSET_TEXT + 22]
txt025 = LANGText[OFFSET_TEXT + 23]
txt026 = LANGText[OFFSET_TEXT + 24]
txt027 = LANGText[OFFSET_TEXT + 25]
txt028 = LANGText[OFFSET_TEXT + 26]
txt029 = LANGText[OFFSET_TEXT + 27]
txt030 = None
txt031 = LANGText[OFFSET_TEXT + 28]
txt032 = LANGText[OFFSET_TEXT + 29]
txt033 = LANGText[OFFSET_TEXT + 30]
txt034 = LANGText[OFFSET_TEXT + 31]
txt035 = LANGText[OFFSET_TEXT + 32]
txt036 = LANGText[OFFSET_TEXT + 33]
txt037 = LANGText[OFFSET_TEXT + 34]
txt038 = LANGText[OFFSET_TEXT + 35]
txt039 = LANGText[OFFSET_TEXT + 36]
txt040 = LANGText[OFFSET_TEXT + 37]
txt041 = LANGText[OFFSET_TEXT + 38]
txt042 = LANGText[OFFSET_TEXT + 39]
txt043 = LANGText[OFFSET_TEXT + 40]
txt044 = LANGText[OFFSET_TEXT + 41]
txt045 = LANGText[OFFSET_TEXT + 42]
REC_Title = LANGText[OFFSET_TEXT + 43]

help01 = LANGText[OFFSET_TEXT + 44]
help02 = LANGText[OFFSET_TEXT + 45]
help03 = LANGText[OFFSET_TEXT + 46]
HelpFileName = LANGText[OFFSET_TEXT + 47]

# This Id is used By Load, HighScore & Global High Score ListBoxs
ID_LISTBOX = 801

# Others IDs
IDM_ABOUTBOX_00 = "About Laser Tank"
IDM_ABOUTBOX_01 = "&Ok"
IDM_ABOUTBOX_04 = "By Jim Kindley"
IDM_ABOUTBOX_06 = "Version"
IDM_ABOUTBOX_02 = "Title"
IDM_ABOUTBOX_03 = "Ver Info"
IDM_ABOUTBOX_05 = "©2002, JEK Software"
ID_ABOUTBOX_00 =(OFFSET_DIALOGS + 0)
ID_ABOUTBOX_OK =(OFFSET_DIALOGS + 1)
ID_ABOUTBOX_04 =(OFFSET_DIALOGS + 2)
ID_ABOUTBOX_06 =(OFFSET_DIALOGS + 3)
ID_ABOUTBOX_02 = 801
ID_ABOUTBOX_03 = 802
ID_ABOUTBOX_05 = 803
ID_ABOUTBOX_07 = 804

IDM_DEADBOX_00 = "&Undo Last Move"
IDM_DEADBOX_01 = "YOU ARE DEAD ! ! !"
IDM_DEADBOX_02 = "&ReStart"
ID_DEADBOX_UNDO =(OFFSET_DIALOGS + 4)
ID_DEADBOX_DEAD =(OFFSET_DIALOGS + 5)
ID_DEADBOX_RESTART =(OFFSET_DIALOGS + 6)
"""
IDM_DIFFBOX_00 =     "Game Difficulty"
IDM_DIFFBOX_01 =     "&Ok"
IDM_DIFFBOX_02 =     "&Kids"
IDM_DIFFBOX_03 =     "&Easy"
IDM_DIFFBOX_04 =     "&Medium"
IDM_DIFFBOX_05 =     "&Hard"
IDM_DIFFBOX_06 =     "&Deadly"
IDM_DIFFBOX_07 =     "&All"
IDM_DIFFBOX_08 =     "Select"
"""
ID_DIFFBOX_00 =(OFFSET_DIALOGS + 7)
ID_DIFFBOX_01 =(OFFSET_DIALOGS + 8)
ID_DIFFBOX_02 =(OFFSET_DIALOGS + 9)
ID_DIFFBOX_03 =(OFFSET_DIALOGS + 10)
ID_DIFFBOX_04 =(OFFSET_DIALOGS + 11)
ID_DIFFBOX_05 =(OFFSET_DIALOGS + 12)
ID_DIFFBOX_06 =(OFFSET_DIALOGS + 13)
ID_DIFFBOX_07 =(OFFSET_DIALOGS + 14)
ID_DIFFBOX_08 =(OFFSET_DIALOGS + 15)

"""
IDM_GRAPHBOX_00 =    "Select Graphics Set"
IDM_GRAPHBOX_01 =    "Select One"
IDM_GRAPHBOX_02 =    "&Internal Graphics"
IDM_GRAPHBOX_03 =    "&User Graphics "
IDM_GRAPHBOX_04 =    "&Close"
IDM_GRAPHBOX_05 =    "Author :"
IDM_GRAPHBOX_06 =    "Laser Tank Graphic Set Description"
IDM_GRAPHBOX_07 =    "&View Opening Screen "
IDM_GRAPHBOX_08 =    "Change &Directory"
"""
ID_GRAPHBOX_00 =(OFFSET_DIALOGS + 16)
ID_GRAPHBOX_01 =(OFFSET_DIALOGS + 17)
ID_GRAPHBOX_02 =(OFFSET_DIALOGS + 18)
ID_GRAPHBOX_03 =(OFFSET_DIALOGS + 19)
ID_GRAPHBOX_04 =(OFFSET_DIALOGS + 20)
ID_GRAPHBOX_05 =(OFFSET_DIALOGS + 21)
ID_GRAPHBOX_06 =(OFFSET_DIALOGS + 22)
ID_GRAPHBOX_07 = 801
ID_GRAPHBOX_08 =(OFFSET_DIALOGS + 23)
ID_GRAPHBOX_09 =(OFFSET_DIALOGS + 24)
ID_GRAPHBOX_10 = 802
ID_GRAPHBOX_11 = 803

"""
IDM_LOADLEV_00 =     "Pick Level to Load"
IDM_LOADLEV_01 =     "&Cancel"
IDM_LOADLEV_03 =     "&Filter"
IDM_LOADLEV_04 =     "File:"
IDM_LOADLEV_05 =     "- File Loading Error -"
IDM_LOADLEV_06 =     "Lev#   Name                           Author"
IDM_LOADLEV_07 =     "or Direct Level Number Entry >>"
"""
ID_LOADLEV_00 =(OFFSET_DIALOGS + 25)
ID_LOADLEV_01 =(OFFSET_DIALOGS + 26)
ID_LOADLEV_02 = 802
ID_LOADLEV_03 =(OFFSET_DIALOGS + 27)
ID_LOADLEV_04 =(OFFSET_DIALOGS + 28)
ID_LOADLEV_05 =(OFFSET_DIALOGS + 29)
ID_LOADLEV_06 =(OFFSET_DIALOGS + 30)
ID_LOADLEV_07 =(OFFSET_DIALOGS + 31)
ID_LOADLEV_08 = ID_LISTBOX
"""
IDM_HINTBOX_00 =     "Modify Hint"
IDM_HINTBOX_01 =     "&Ok"
IDM_HINTBOX_02 =     "&Cancel"
"""
ID_HINTBOX_00 =(OFFSET_DIALOGS + 32)
ID_HINTBOX_01 =(OFFSET_DIALOGS + 33)
ID_HINTBOX_02 =(OFFSET_DIALOGS + 34)
ID_HINTBOX_03 = 801
"""
IDM_SEARCH_00 =      "Filter Level Data"
IDM_SEARCH_01 =      "Enter Search String :"
IDM_SEARCH_02 =      "Search By"
IDM_SEARCH_03 =      "&Title"
IDM_SEARCH_04 =      "&Author"
IDM_SEARCH_05 =      "&Cancel"
IDM_SEARCH_06 =      "&Ok"
IDM_SEARCH_07 =      "ICON1"
IDM_SEARCH_08 =      "&Only Unsolved Levels"
IDM_SEARCH_09 =      "&Filter by Difficulty"
IDM_SEARCH_10 =      "Kids"
IDM_SEARCH_11 =      "Easy"
IDM_SEARCH_12 =      "Medium"
IDM_SEARCH_13 =      "Hard"
IDM_SEARCH_14 =      "Deadly"
"""
ID_SEARCH_00 =(OFFSET_DIALOGS + 35)
ID_SEARCH_01 =(OFFSET_DIALOGS + 36)
ID_SEARCH_02 =(OFFSET_DIALOGS + 37)
ID_SEARCH_03 =(OFFSET_DIALOGS + 38)
ID_SEARCH_04 =(OFFSET_DIALOGS + 39)
ID_SEARCH_05 =(OFFSET_DIALOGS + 40)
ID_SEARCH_06 =(OFFSET_DIALOGS + 41)
ID_SEARCH_07 = 801
ID_SEARCH_08 =(OFFSET_DIALOGS + 42)
ID_SEARCH_09 =(OFFSET_DIALOGS + 43)
ID_SEARCH_10 =(OFFSET_DIALOGS + 44)
ID_SEARCH_11 =(OFFSET_DIALOGS + 45)
ID_SEARCH_12 =(OFFSET_DIALOGS + 46)
ID_SEARCH_13 =(OFFSET_DIALOGS + 47)
ID_SEARCH_14 =(OFFSET_DIALOGS + 48)
"""
IDM_RETBOX_00 =      "&Return to Game"
"""
ID_RETBOX_00 =(OFFSET_DIALOGS + 49)
"""
IDM_WINBOX_00 =      "&Ok"
IDM_WINBOX_01 =      "You Won ! ! !"
IDM_WINBOX_02 =      "File :"
IDM_WINBOX_03 =      "- Error -"
"""
ID_WINBOX_00 =(OFFSET_DIALOGS + 50)
ID_WINBOX_01 =(OFFSET_DIALOGS + 51)
ID_WINBOX_02 =(OFFSET_DIALOGS + 52)
ID_WINBOX_03 =(OFFSET_DIALOGS + 53)
ID_WINBOX_04 = 801
ID_WINBOX_05 = 802
ID_WINBOX_06 = 803
"""
IDM_LOADTID_00 =     "Pick Tunnel ID #"
IDM_LOADTID_03 =     "&Ok"
IDM_LOADTID_04 =     "Enter the ID Number for this Tunnel"
"""
ID_LOADTID_00 =(OFFSET_DIALOGS + 54)
ID_LOADTID_01 = 801
ID_LOADTID_02 = 802
ID_LOADTID_03 =(OFFSET_DIALOGS + 55)
ID_LOADTID_04 =(OFFSET_DIALOGS + 56)
"""
IDM_HIGHBOX_00 =     "! New High Score !"
IDM_HIGHBOX_01 =     "&Ok"
IDM_HIGHBOX_02 =     "Level Number :"
IDM_HIGHBOX_03 =     "Level Name :"
IDM_HIGHBOX_04 =     "Moves :"
IDM_HIGHBOX_05 =     "Shots :"
IDM_HIGHBOX_06 =     "0"
IDM_HIGHBOX_07 =     "0"
IDM_HIGHBOX_08 =     "0"
IDM_HIGHBOX_09 =     " "
IDM_HIGHBOX_10 =     "Initials :"
IDM_HIGHBOX_12 =     "Global HS :"
IDM_HIGHBOX_13 =     "- No Data -"
"""
ID_HIGHBOX_00 =(OFFSET_DIALOGS + 57)
ID_HIGHBOX_01 =(OFFSET_DIALOGS + 58)
ID_HIGHBOX_02 =(OFFSET_DIALOGS + 59)
ID_HIGHBOX_03 =(OFFSET_DIALOGS + 60)
ID_HIGHBOX_04 =(OFFSET_DIALOGS + 61)
ID_HIGHBOX_05 =(OFFSET_DIALOGS + 62)
ID_HIGHBOX_06 = 103
ID_HIGHBOX_07 = 104
ID_HIGHBOX_08 = ID_LISTBOX
ID_HIGHBOX_09 = 102
ID_HIGHBOX_10 =(OFFSET_DIALOGS + 63)
ID_HIGHBOX_12 =(OFFSET_DIALOGS + 64)
ID_HIGHBOX_13 =(OFFSET_DIALOGS + 65)
ID_HIGHBOX_14 = 105
ID_HIGHBOX_15 = 106
"""
IDM_HIGHLIST_00 =    "High Scores"
IDM_HIGHLIST_01 =    "&Ok"
IDM_HIGHLIST_02 =    "- File Loading Error -"
IDM_HIGHLIST_03 =    "Lev#  Name                          Moves  Shots  Initials"
"""
ID_HIGHLIST_00 =(OFFSET_DIALOGS + 66)
ID_HIGHLIST_01 =(OFFSET_DIALOGS + 67)
ID_HIGHLIST_02 =(OFFSET_DIALOGS + 68)
ID_HIGHLIST_03 =(OFFSET_DIALOGS + 69)
"""
IDM_GHIGHLIST_00 =   "Global High Scores"
IDM_GHIGHLIST_01 =   "&Ok"
IDM_GHIGHLIST_02 =   "Lev#  Name                             M      S   Init   M     S  Init"
IDM_GHIGHLIST_03 =   "Global"
IDM_GHIGHLIST_04 =   "Local"
IDM_GHIGHLIST_05 =   "- No Data -"
IDM_GHIGHLIST_06 =   "&Beat"
"""
ID_GHIGHLIST_00 =(OFFSET_DIALOGS + 70)
ID_GHIGHLIST_01 =(OFFSET_DIALOGS + 71)
ID_GHIGHLIST_02 =(OFFSET_DIALOGS + 72)
ID_GHIGHLIST_03 =(OFFSET_DIALOGS + 73)
ID_GHIGHLIST_04 =(OFFSET_DIALOGS + 74)
ID_GHIGHLIST_05 =(OFFSET_DIALOGS + 75)
ID_GHIGHLIST_06 =(OFFSET_DIALOGS + 76)
"""
IDM_RECBOX_00 =      "Recording Game"
IDM_RECBOX_01 =      "Please Enter Your Name"
IDM_RECBOX_02 =      "&Ok"
"""
ID_RECBOX_00 =(OFFSET_DIALOGS + 77)
ID_RECBOX_01 =(OFFSET_DIALOGS + 78)
ID_RECBOX_02 =(OFFSET_DIALOGS + 79)
ID_RECBOX_03 = 101
"""
IDM_PLAYBOX_00 =     "Playback Game"
IDM_PLAYBOX_01 =     "&Close"
IDM_PLAYBOX_02 =     "&Play"
IDM_PLAYBOX_03 =     "&Reset"
IDM_PLAYBOX_04 =     "&Fast"
IDM_PLAYBOX_05 =     "&Slow"
IDM_PLAYBOX_06 =     "S&tep"
IDM_PLAYBOX_07 =     "Step :"
IDM_PLAYBOX_08 =     "of"
IDM_PLAYBOX_09 =     "0"
IDM_PLAYBOX_10 =     "0"
IDM_PLAYBOX_11 =     "Speed"
"""
ID_PLAYBOX_00 =(OFFSET_DIALOGS + 80)
ID_PLAYBOX_01 =(OFFSET_DIALOGS + 81)
ID_PLAYBOX_02 =(OFFSET_DIALOGS + 82)
ID_PLAYBOX_03 =(OFFSET_DIALOGS + 83)
ID_PLAYBOX_04 =(OFFSET_DIALOGS + 84)
ID_PLAYBOX_05 =(OFFSET_DIALOGS + 85)
ID_PLAYBOX_06 =(OFFSET_DIALOGS + 86)
ID_PLAYBOX_07 =(OFFSET_DIALOGS + 87)
ID_PLAYBOX_08 =(OFFSET_DIALOGS + 88)
ID_PLAYBOX_09 = 103
ID_PLAYBOX_10 = 104
ID_PLAYBOX_11 =(OFFSET_DIALOGS + 89)
"""
IDM_PICKLEVEL_00 =   "Save Laser Tank Level"
IDM_PICKLEVEL_01 =   "&Ok"
IDM_PICKLEVEL_02 =   "Enter the Level Number to"
IDM_PICKLEVEL_03 =   "Save :"
IDM_PICKLEVEL_04 =   "0 - 10"
IDM_PICKLEVEL_05 =   "icon1"
IDM_PICKLEVEL_06 =   "= Add"
IDM_PICKLEVEL_07 =   "11"
IDM_PICKLEVEL_08 =   "&Clear High Score"
"""
ID_PICKLEVEL_00 =(OFFSET_DIALOGS + 90)
ID_PICKLEVEL_01 =(OFFSET_DIALOGS + 91)
ID_PICKLEVEL_02 =(OFFSET_DIALOGS + 92)
ID_PICKLEVEL_03 =(OFFSET_DIALOGS + 93)
ID_PICKLEVEL_04 = 103
ID_PICKLEVEL_05 = 101
# MGY - About dialog Bug - 2005/07/08
ID_PICKLEVEL_06 =(OFFSET_DIALOGS + 94)
ID_PICKLEVEL_07 = 104
ID_PICKLEVEL_08 =(OFFSET_DIALOGS + 95)

# lt_sfx.h
"""******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 ******************************************************"""

# This is the header file for the Sound unit of Lasertank

MaxSounds = 20


# LT_Sound_Types(Enum):
S_Bricks = 1
S_Fire = 2
S_Move = 3
S_Head = 4
S_Turn = 5
S_EndLev = 6
S_Die = 7
S_Anti1 = 8
S_Anti2 = 9
S_Deflb = 10
S_LaserHit = 11
S_Push2 = 12
S_Push1 = 13
S_Rotate = 14
S_Push3 = 15
S_Sink = 16


# extern Sound_On

# Function Prototypes

# void SoundPlay(int)
# void SFxInit(void)

# lt_sfx.c
"""******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **                  Sound Unit                       **
 *******************************************************)

	All Sounds are Wav files loaded into the resource file.
	Because lcc-win32 can't handle user defined resources, the wav files
	are converted into a charecter stream and imported as RCData
"""
#include <windows.h>            # required for all Windows applications

#include <mmsystem.h>

#include "lt_sfx.h"            # prototypes specific to this application

# SFx[] 0:BRICKS, 1:FIRE, 2:MOVE, 3:HEAD, 4:TURN, 5:ENDLEV, 6:DIE, 7:ANTI1, 8:ANTI2, 9:DEFLB, 10:LASER2, 11:PUSH2, 12:PUSH1, 13:ROTATE, 14:PUSH3, 15:SINK
SFx = []  # Array of handles to sound resources. Set by SFxInit()->SoundLoad('resource_name')
LastSFWord = 0
SFXError = 0
Sound_On = True  # true when sound is on
# extern HINSTANCE hInst  # Globally Defined Instance

# Declare Local Function
# static void SoundLoad(char * s)

def SoundPlay(sn) :
	if ( not Sound_On) :
		return
	if (SFXError) :
		return
	p = LockResource(SFx[sn])
	PlaySound(p, 0, 5)  # 5 = memory & async


def SoundLoad( s) :
	global SFXError
	global LastSFWord
	global hInst


	if (SFXError) :
		return
	h = LoadResource(hInst, FindResource(hInst, s, RT_RCDATA))
	if h == 0:
		SFXError = LastSFWord + 1
	else :
		LastSFWord += 1
		SFx[LastSFWord] = h  # put resource handle in Sound Array
	


def SFxInit(void) :
	SoundLoad("BRICKS")
	SoundLoad("FIRE")
	SoundLoad("MOVE")
	SoundLoad("HEAD")
	SoundLoad("TURN")
	SoundLoad("ENDLEV")
	SoundLoad("DIE")
	SoundLoad("ANTI1")
	SoundLoad("ANTI2")
	SoundLoad("DEFLB")
	SoundLoad("LASER2")
	SoundLoad("PUSH2")
	SoundLoad("PUSH1")
	SoundLoad("ROTATE")
	SoundLoad("PUSH3")
	SoundLoad("SINK")
	if (SFXError) :
		MessageBox(0, "Loading Error", "SFx Error", MB_OK)


# language.c
"""******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 ******************************************************"""

# Language.c

#include <windows.h>

#include <windowsx.h>

#include <commdlg.h>

#include <string.h>

#include <mmsystem.h>

#include <stdlib.h>

#include <stdio.h>

#include "ltank.h"

LANGText = [] # All lines of Language.dat
LANGFile = ""  # the dynamic file name for Language.dat
szFilterOFN = ""
szFilterPBfn = ""

# ************************************************************************
# These are the originals texts for all messages. Copied into LangText and replaced with lines from Language.dat
# ************************************************************************
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
	"\nCan Not be found in the current level file\n< ",
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

# ************************************************************************
# If Language File, set windowstext with this text
# ************************************************************************
#SetWindowText(GetDlgItem(Dialog,ID_ABOUTBOX_02),App_Title)

def LoadWindowText(hDlg, nIDDlgItem) :
	if (LANGText[nIDDlgItem][0] != '') :
		SetWindowText(GetDlgItem(hDlg, nIDDlgItem), LANGText[nIDDlgItem])

def LoadWindowCaption(hDlg, nIDDlgItem) :
	if (LANGText[nIDDlgItem][0] != '') :
		SetWindowText(hDlg, LANGText[nIDDlgItem])


# ************************************************************************
# Read the language file is exist
# fill the LANGText[],
# update the two menus,
# ************************************************************************
def InitLanguage(MMenu, EMenu) :
	# Initialyse with default values
	for i in range(0,  SIZE_BUTTON + SIZE_TEXT) :
		LANGText[i] = App_Strings[i]

	# Clear default messages dialogs
	for i in range(OFFSET_DIALOGS,OFFSET_ABOUTMSG + SIZE_ABOUTMSG):
		LANGText[i] = ""

	fd = open(LANGFile, "r")  # LANGFile == Setups\US\Language\Language.dat

	if (fd is not None) :
		i = 0
		for szTmp in fd.readlines():
			if szTmp[0] != '' :
				szTmp[len(szTmp) - 1] = ''  # remove the last char
				if ((szTmp[0] != '') and (szTmp[0] != '#')) : # ignore blankc & comment lines and don't increment counter i
					ConvertTabChar(szTmp)  # replace \t and \n

					if ((i >= START_MMENU) and (i < START_MMENU + SIZE_MMENU)): # if 0 <= i < 49 (main menu items)
						ChangeMenuText(MMenu, szTmp)
					elif ((i >= START_EMENU) and (i < START_EMENU + SIZE_EMENU)): # if 49 <= i < 73  (edit menu items)
						ChangeMenuText(EMenu, szTmp)
					elif ((i >= START_BUTTON) and (i < (START_BUTTON + SIZE_BUTTON + SIZE_TEXT + SIZE_ABOUTMSG + SIZE_DIALOGS))) : # if 73 <= i < 240
						LANGText[i - START_BUTTON] = szTmp  # save over LANGText[ 0:167 ] 
					i += 1
				
			
		
		fd.close()
	


# Used by ChangeMenuText() - Converts 00, 01, or  -= 1, to menu level int
def DecodeMenuInt(MenuStr) :
	if (MenuStr[0] == '0'):
		return int(MenuStr[1] - '0')

	if (MenuStr[0] == '1'):
		return int(10 + (MenuStr[1] - '0'))
	else:
		return (-1)


# ************************************************************************
# To change a menu text with this syntax :
# 00,01,02,&Text
#
# ************************************************************************
def ChangeMenuText(hMenu, MenuStr) :
	# MenuStr starts with 3 double digit values showing the position
	# i.e. '00,14, -= 1,Play&back Game...\tF7'
	#.item 00, sub-item 14, sub-sub-item (not), text=Playback Game...  F7 with underline on &b

	if ((len(MenuStr) > 9) and (hMenu != None)) :
		nMenu = DecodeMenuInt((MenuStr + 0))  # Top position
		nMenu1 = DecodeMenuInt((MenuStr + 3))  # Sub menu position
		nMenu2 = DecodeMenuInt((MenuStr + 6))  # Sub-sub menu position
		if (nMenu2 >= 0) :
			#https:#docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsubmenu
			# GetSubMenu(menu handle, position that activates drop down)
			hMenu = GetSubMenu(hMenu, nMenu)
			hMenu = GetSubMenu(hMenu, nMenu1)
			nMenu = nMenu2
		else :
			if (nMenu1 >= 0) :
				hMenu = GetSubMenu(hMenu, nMenu)
				nMenu = nMenu1
			
		

		memset( & ItemInfo, 0, sizeof(MENUITEMINFO))
		ItemInfo.cbSize = sizeof(MENUITEMINFO)
		ItemInfo.fMask = MIIM_TYPE
		GetMenuItemInfo(hMenu, nMenu, True, & ItemInfo)
		if (ItemInfo.fType == MFT_STRING) :
			# Replace menu item.
			ItemInfo.dwTypeData = (MenuStr + 9)
			ItemInfo.cch = lstrlen(ItemInfo.dwTypeData)
			SetMenuItemInfo(hMenu, nMenu, True, & ItemInfo)
		
	


def ConvertTabChar(szBuffer) :
	P = strchr(szBuffer, '\\')
	while (P) :
		# case of \t
		if ( * (P + 1) == 't') :
			* P += 1 = '\t'
			for (Q = P;* Q != 0; Q += 1)
				*
				Q = * (Q + 1)
		else :
			# case of \n
			if ( * (P + 1) == 'n') :
				* P += 1 = 0x0d
				* P = 0x0a
			else P += 1
		
		# Search the next occurence
		P = strchr(P, '\\')
	



# ************************************************************************
# Load Resource Bitmap or File
# ************************************************************************
def LoadImageFile(hInst, szBitmapRes, szBitmapFile) :
	GetModuleFileName(None, lpszName, MAX_PATH)
	P = strrchr(lpszName, '\\')
	if (P) :
		P += 1
		strcpy(P, TEXT(LANGFilePath))  # add path
		P += strlen(TEXT(LANGFilePath))
		P = szBitmapFile  # add name
	
	hbm = (HBITMAP) LoadImage(None, lpszName, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION)
	if (hbm == None) :
		hbm = LoadBitmap(hInst, szBitmapRes)
	
	return (hbm)


# ltank_d.h
"""******************************************************
 **             Laser Tank ver 3.2a                   **
 **               By Jim Kindley                      **
 **               (c) 2000                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 ******************************************************"""

# Dialog Callback functions
# def AboutBox(, , , )
# def DeadBox(, , , )
# def DiffBox(, , , )
# def RetBox(, , , )
# def LoadBox(, , , )
# def HintBox(, , , )
# def PickBox(, , , )
# def WinBox(, , , )
# def HSBox(, , , )
# def RecordBox(, , , )
# def PBWindow(, , , )
# def HSList(, , , )
# def GHSList(, , , )
# def GraphBox(, , , )
# def LoadTID(, , , )

# def DrawLevels()

# extern FileHand, HSClear
# extern  PlayH, PBCountH

# ltank_d.c
"""******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 **                                                   **
 **   Dialog Code                                     **
 **                                                   **
 *******************************************************
 **       Release version 2005 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 ******************************************************"""
#include <windows.h>

#include <string.h>

#include <stdio.h>

#include <ole2.h>

#include <shlobj.h>

#include "ltank.h"

#include "ltank_d.h"

# PHDC =(pDIS.hDC)
# PRC =(pDIS.rcItem)

DifCList[6] = :
	0x00FFFFFF,
	0x0000FFFF,
	0x00FFFF00,
	0x0000FF00,
	0x00FF00FF,
	0x000000FF
	#Colours for level info text based on difficulty number

# HBRUSH hbrBack
# DRAWITEMSTRUCT FAR * pDIS
# HSClear, LastOfList, DispAll
# THSREC HS, GHS
# TSEARCH SearchRec
#  PBCountH, PlayH
# # extern QHELP
# DWORD OldProcEdit

# Will Set the Starting Directory for the Browsing
# INT CALLBACK BrowseCallBack( hwnd,  uMsg,  lp,  pData) :
# 	if (uMsg == BFFM_INITIALIZED) :
# 		SendMessage(hwnd, BFFM_SETSELECTION, True, () & GraphDN)
# 	return (0)


"""***********************************************************************************
Browse
Action: Uses SHBrowseForFolder to allow the user to browse their shell namespace
Paramaters: hwndOwner - handle to owner window
			 lpszDir - pointer to string that will be filled with the user's selection
					 Assumed to be MAX_PATH
			 lpszTitle - any text that you would like to be displayed in the window
Return value: True if successful, False if there was a problem
***********************************************************************************"""
def Browse(hwndOwner, lpszDir, lpszTitle) :
	OleInitialize(None)

	if (FAILED(SHGetMalloc(pMalloc))):
		return False

	# fill BROWSEINFO struct
	bi.hwndOwner = hwndOwner  # owner window
	bi.pidlRoot = None  # folder to start in - None for My Computer
	bi.pszDisplayName = lpszDir  # pointer to string that gets folder display name
	bi.lpszTitle = lpszTitle  # pointer to text to display in window
	bi.ulFlags = BIF_RETURNONLYFSDIRS  # flags - see API docs for BROWSEINFO
	bi.lpfn = BrowseCallBack  # callback function - usually not needed
	bi.lParam = 0  # parameter to callback function

	pidl = SHBrowseForFolder(bi)

	if (!pidl) :
		return False

	# SHBrowseForFolder filled lpszDir with the name of the chosen item,
	# but it did not give us the full path to it. So, we need to get
	# that using SHGetPathFromIDList.
	if (!SHGetPathFromIDList(pidl, lpszDir)):
		return False
	pMalloc.lpVtbl.Free(pMalloc, pidl)
	pMalloc.lpVtbl.Release(pMalloc)
	return True


# Used By Load, HighScore & Global High Score ListBoxs
def TransListKey(Dialog, Key) :
	if Key ==  VK_HOME:
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, 0, 0)
		break
	elif Key ==  VK_UP:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) - 1
		if (i > -1):
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0)
		break
	elif Key ==  VK_DOWN:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) + 1
		if (i <= LastOfList):
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0)
		break
	elif Key ==  VK_END:
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, LastOfList, 0)
		break
	elif Key ==  VK_PRIOR:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) - 10
		if (i > -1):
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0)
		break
	elif Key ==  VK_NEXT:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) + 10
		if (i <= LastOfList):
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0)
		break
	elif Key ==  VK_ESCAPE:
		EndDialog(Dialog, 0)
	
	return (-2)

#  ++ About Box Dialog Procedure  ++
#  This is an About box with an Edit window that has text in it from the
#  resource file. The text is stored as RCData.
def AboutBox( Dialog,  Message,  wparam,  lparam) :
	char * p
	char AboutMsg[SIZE_ABOUTMSG * MAX_LANG_SIZE + 1]
	i
	HGLOBAL h

	switch0 =  (Message) :
	elif switch0 ==  WM_INITDIALOG:
		# Grab the Text for the About Edit window
		h = LoadResource(hInst, FindResource(hInst, "About", RT_RCDATA))
		if (LANGText[OFFSET_ABOUTMSG][0] != '') :
			AboutMsg[0] = ''
			for i in range(0, SIZE_ABOUTMSG):
				strcat(AboutMsg, LANGText[OFFSET_ABOUTMSG + i])
			p = AboutMsg
		else
			p = LockResource(h)

		LoadWindowCaption(Dialog, ID_ABOUTBOX_00)
		LoadWindowText(Dialog, ID_ABOUTBOX_OK)
		LoadWindowText(Dialog, ID_ABOUTBOX_04)
		LoadWindowText(Dialog, ID_ABOUTBOX_06)

		SetWindowText(GetDlgItem(Dialog, ID_ABOUTBOX_02), App_Title)
		SetWindowText(GetDlgItem(Dialog, ID_ABOUTBOX_03), App_Version)
		SetWindowText(GetDlgItem(Dialog, ID_ABOUTBOX_07), p)
		FreeResource(h)
		return (True)
	elif switch0 ==  WM_COMMAND:
		if (wparam == ID_ABOUTBOX_OK):
			EndDialog(Dialog, 1)
	
	return (0)


#  ++ DeadBox Dialog Procedure  ++
# This dialog Proc is used for the DeadBox dialog.
# It returns the value of the button pressed.
def DeadBox( Dialog,  Message,  wparam,  lparam) :
	switch0 =  (Message) :
	elif switch0 ==  WM_INITDIALOG:
		LoadWindowText(Dialog, ID_DEADBOX_UNDO)
		LoadWindowText(Dialog, ID_DEADBOX_DEAD)
		LoadWindowText(Dialog, ID_DEADBOX_RESTART)
		return (True)  # I need this or I don't kave [tab] key 
	elif switch0 ==  WM_COMMAND:
		if (Game.RecP > 1):
			EndDialog(Dialog, wparam)  # end dialog with button id 
		else:
			EndDialog(Dialog, ID_DEADBOX_RESTART)  # reset if first turn
	
	return (0)


#  ++ RetBox Dialog Procedure  ++
# This dialog Proc is used for "Return to Game".
# It returns the value of the button pressed.
#function DefBox(Dialog: HWnd; Message, WParam: Word;LParam: Longint): Bool; export
def RetBox( Dialog,  Message,  wparam,  lparam) :
	switch0 =  (Message) :
	elif switch0 ==  WM_INITDIALOG:
		LoadWindowText(Dialog, ID_RETBOX_00)
		return (True)  # I need this or I don't kave [tab] key 
	elif switch0 ==  WM_COMMAND:
		if (Game.RecP > 1):
			EndDialog(Dialog, wparam)  # end dialog with button id 
		else:
			EndDialog(Dialog, 2)  # reset if first turn
	
	return (0)


#  ++ Search Box Dialog Procedure  ++
#  The Load Box uses this proc to select a Search term and type
def SearchBox( Dialog,  Message,  wparam,  lparam) :
	if Message ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_SEARCH_00)
		LoadWindowText(Dialog, ID_SEARCH_01)
		LoadWindowText(Dialog, ID_SEARCH_02)
		LoadWindowText(Dialog, ID_SEARCH_03)
		LoadWindowText(Dialog, ID_SEARCH_04)
		LoadWindowText(Dialog, ID_SEARCH_05)
		LoadWindowText(Dialog, ID_SEARCH_06)

		LoadWindowText(Dialog, ID_SEARCH_08)
		LoadWindowText(Dialog, ID_SEARCH_09)
		LoadWindowText(Dialog, ID_SEARCH_10)
		LoadWindowText(Dialog, ID_SEARCH_11)
		LoadWindowText(Dialog, ID_SEARCH_12)
		LoadWindowText(Dialog, ID_SEARCH_13)
		LoadWindowText(Dialog, ID_SEARCH_14)

		SendMessage(GetDlgItem(Dialog, ID_SEARCH_03), BM_SETCHECK, 1, 0)
		SearchRec.mode = 1
		return (True)
	elif Message ==  WM_COMMAND:
		if LOWORD(wparam) ==  ID_SEARCH_06 or LOWORD(wparam) ==  1:
			GetWindowText(GetDlgItem(Dialog, ID_SEARCH_07), SearchRec.data, 60)
			strupr(SearchRec.data)
			if (SendMessage(GetDlgItem(Dialog, ID_SEARCH_03), BM_GETCHECK, 0, 0) != 0):
				SearchRec.mode = 1
			else SearchRec.mode = 2
			if (SendMessage(GetDlgItem(Dialog, ID_SEARCH_09), BM_GETCHECK, 0, 0)) :
				SearchRec.Diff = 0
				if (SendDlgItemMessage(Dialog, ID_SEARCH_10, BM_GETCHECK, 0, 0) == 1):
					SearchRec.Diff += 1
				if (SendDlgItemMessage(Dialog, ID_SEARCH_11, BM_GETCHECK, 0, 0) == 1):
					SearchRec.Diff = SearchRec.Diff + 2
				if (SendDlgItemMessage(Dialog, ID_SEARCH_12, BM_GETCHECK, 0, 0) == 1):
					SearchRec.Diff = SearchRec.Diff + 4
				if (SendDlgItemMessage(Dialog, ID_SEARCH_13, BM_GETCHECK, 0, 0) == 1):
					SearchRec.Diff = SearchRec.Diff + 8
				if (SendDlgItemMessage(Dialog, ID_SEARCH_14, BM_GETCHECK, 0, 0) == 1):
					SearchRec.Diff = SearchRec.Diff + 16
			else SearchRec.Diff = 255
			SearchRec.SkipComp = SendMessage(GetDlgItem(Dialog, 200), BM_GETCHECK, 0, 0)
			EndDialog(Dialog, 1)
			break
		elif LOWORD(wparam) ==  2 or LOWORD(wparam) ==  ID_SEARCH_05:
			EndDialog(Dialog, 2)
			break
		elif LOWORD(wparam) ==  ID_SEARCH_09:
			j = SendMessage(GetDlgItem(Dialog, ID_SEARCH_09), BM_GETCHECK, 0, 0)
			for i in range(ID_SEARCH_10,ID_SEARCH_14+1):
				EnableWindow(GetDlgItem(Dialog, i), j)
		
	
	return (0)


#  ++ Difficulty Box Dialog Procedure  ++
def DiffBox( Dialog,  Message,  wparam,  lparam) :
	if Message ==  WM_INITDIALOG:
		if ((Difficulty & 1) == 1):
			SendDlgItemMessage(Dialog, ID_DIFFBOX_02, BM_SETCHECK, 1, 0)
		if ((Difficulty & 2) == 2):
			SendDlgItemMessage(Dialog, ID_DIFFBOX_03, BM_SETCHECK, 1, 0)
		if ((Difficulty & 4) == 4):
			SendDlgItemMessage(Dialog, ID_DIFFBOX_04, BM_SETCHECK, 1, 0)
		if ((Difficulty & 8) == 8):
			SendDlgItemMessage(Dialog, ID_DIFFBOX_05, BM_SETCHECK, 1, 0)
		if ((Difficulty & 16) == 16):
			SendDlgItemMessage(Dialog, ID_DIFFBOX_06, BM_SETCHECK, 1, 0)

		LoadWindowCaption(Dialog, ID_DIFFBOX_00)
		LoadWindowText(Dialog, ID_DIFFBOX_01)
		LoadWindowText(Dialog, ID_DIFFBOX_02)
		LoadWindowText(Dialog, ID_DIFFBOX_03)
		LoadWindowText(Dialog, ID_DIFFBOX_04)
		LoadWindowText(Dialog, ID_DIFFBOX_05)
		LoadWindowText(Dialog, ID_DIFFBOX_06)
		LoadWindowText(Dialog, ID_DIFFBOX_07)
		LoadWindowText(Dialog, ID_DIFFBOX_08)
		return (True)
	elif Message ==  WM_COMMAND:
		if wparam ==  1 or wparam ==  ID_DIFFBOX_01:
			Difficulty = 0
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_02, BM_GETCHECK, 0, 0) == 1):
				Difficulty += 1
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_03, BM_GETCHECK, 0, 0) == 1):
				Difficulty = Difficulty + 2
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_04, BM_GETCHECK, 0, 0) == 1):
				Difficulty = Difficulty + 4
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_05, BM_GETCHECK, 0, 0) == 1):
				Difficulty = Difficulty + 8
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_06, BM_GETCHECK, 0, 0) == 1):
				Difficulty = Difficulty + 16
			temps = str( Difficulty ) 
			WritePrivateProfileString("DATA", psDiff, temps, INIFile)
			if (Difficulty > 0) EndDialog(Dialog, 0)
			break
		elif wparam ==  ID_DIFFBOX_07:
			SendDlgItemMessage(Dialog, ID_DIFFBOX_02, BM_SETCHECK, 1, 0)
			SendDlgItemMessage(Dialog, ID_DIFFBOX_03, BM_SETCHECK, 1, 0)
			SendDlgItemMessage(Dialog, ID_DIFFBOX_04, BM_SETCHECK, 1, 0)
			SendDlgItemMessage(Dialog, ID_DIFFBOX_05, BM_SETCHECK, 1, 0)
			SendDlgItemMessage(Dialog, ID_DIFFBOX_06, BM_SETCHECK, 1, 0)
		
	
	return (0)


#  ++ Load Box Dialog Procedure  ++
#  List out all levels in the current data file, by number & title.
#  return with the level # + 101 or 0 if canceled
def LoadBox( Dialog,  Message,  wparam,  lparam) :
	TLEVEL TempRecData
	THSREC TempHSData
	char temps[80], t2[90]
	char * P
	i, j

	switch0 =  (Message) :
	elif switch0 ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_LOADLEV_00)
		LoadWindowText(Dialog, ID_LOADLEV_01)
		LoadWindowText(Dialog, ID_LOADLEV_03)
		LoadWindowText(Dialog, ID_LOADLEV_04)
		LoadWindowText(Dialog, ID_LOADLEV_05)
		LoadWindowText(Dialog, ID_LOADLEV_06)
		LoadWindowText(Dialog, ID_LOADLEV_07)
		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
		if (F1 == INVALID_HANDLE_VALUE):
			return (True)  # File NOT Found
		P = strrchr(FileName, '\\')
		if (P == None):
			P = FileName
		else P += 1
		SetWindowText(GetDlgItem(Dialog, ID_LOADLEV_05), P)
		i = SetFilePointer(F1, 0, None, FILE_END) / sizeof(TLEVEL)
		SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_INITSTORAGE, i, 72)
		SetFilePointer(F1, 0, None, FILE_BEGIN)
		i = 1
		ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, None)
		while (BytesMoved == sizeof(TLEVEL)) :
			sprintf(temps, "%4d   %-30.30s %s", i, TempRecData.LName, TempRecData.Author)
			switch1 =  (TempRecData.SDiff) :
			if switch1 ==  1:
				t2[0] = '1'
				break
			elif switch1 ==  2:
				t2[0] = '2'
				break
			elif switch1 ==  4:
				t2[0] = '3'
				break
			elif switch1 ==  8:
				t2[0] = '4'
				break
			elif switch1 ==  16:
				t2[0] = '5'
				break
			default:
				t2[0] = '0'
			
			t2 = t2[0] + temps
			SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_ADDSTRING, 0, () t2)
			i += 1
			ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, None)
		
		LastOfList = i - 2
		CloseHandle(F1)
		SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_SETCURSEL, CurLevel - 1, 0)
		return (True)
	elif switch0 ==  WM_CTLCOLORLISTBOX:
		return ((int) GetStockObject(BLACK_BRUSH))
		break
	elif switch0 ==  WM_MEASUREITEM:
		((MEASUREITEMSTRUCT FAR * ) lparam).itemHeight = 14
		break
	elif switch0 ==  WM_DRAWITEM:
		DrawLevels(lparam)
		return True
	elif switch0 ==  WM_VKEYTOITEM:
		return (TransListKey(Dialog, LOWORD(wparam)))
	elif switch0 ==  WM_COMMAND:
		switch1 =  (LOWORD(wparam)) :
		if switch1 ==  1: # Pressing Enter will get you here
			GetWindowText(GetDlgItem(Dialog, ID_LOADLEV_02), temps, 10)
			i = atoi(temps)
			if (i) :
				EndDialog(Dialog, i + 100)
				break
			
		elif switch1 ==  ID_LOADLEV_08:
			if (((HIWORD(wparam) != LBN_SELCHANGE)) and (wparam != 1)):
				return (0)
			i = SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_GETCURSEL, 0, 0)
			SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_GETTEXT, i, () temps)
			temps[5] = (char) 0
			i = 1
			while (temps[i] == ' '):
				i += 1  # strip leading spaces
			i = atoi( & temps[i])
			EndDialog(Dialog, i + 100)  # Add 100 to the Select #
			break
		elif switch1 ==  ID_LOADLEV_01:
			EndDialog(Dialog, 0)
			break
		elif switch1 ==  ID_LOADLEV_03: # Search
			i = DialogBox(hInst, "Search", Dialog, (DLGPROC) SearchBox)
			if (i == 1): # idOk
				SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_RESETCONTENT, 0, 0)
				F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
					FILE_FLAG_SEQUENTIAL_SCAN, None)
				if (SearchRec.SkipComp):
					F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
				else:
					F2 = INVALID_HANDLE_VALUE
				if (F2 == INVALID_HANDLE_VALUE):
					SearchRec.SkipComp = False
				ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, None)
				LastOfList = -1
				while (BytesMoved == sizeof(TLEVEL)) :
					if (SearchRec.SkipComp):
						ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
					if (BytesMoved < sizeof(THSREC)):
						TempHSData.moves = 0
					if (SearchRec.mode == 1):
						temps = TempRecData.LName
					else:
						temps = TempRecData.Author
					if (TempRecData.SDiff == 0):
						TempRecData.SDiff = 255
					if (strstr(strupr(temps), SearchRec.data) and (TempRecData.SDiff & SearchRec.Diff) and ((SearchRec.SkipComp == 0) or (TempHSData.moves == 0))) :
						sprintf(temps, "%4d   %-30.30s %s", i, TempRecData.LName, TempRecData.Author)
						switch2 =  (TempRecData.SDiff)
						if switch2 ==  1:
							t2[0] = '1'
							break
						elif switch2 ==  2:
							t2[0] = '2'
							break
						elif switch2 ==  4:
							t2[0] = '3'
							break
						elif switch2 ==  8:
							t2[0] = '4'
							break
						elif switch2 ==  16:
							t2[0] = '5'
							break
						else:
							t2[0] = '0'
						
						t2 = t2[0] + temps
						SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_ADDSTRING, 0, () t2)
						LastOfList += 1
					
					i += 1
					ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, None)
				
				CloseHandle(F1)
				if (SearchRec.SkipComp) CloseHandle(F2)
			
		
	
	return (0)


#  ++ Hint Box Dialog Procedure  ++
#  The editor uses this proc to Display & Edit the Hint. If the text is modified
#  the 'Modified' varable is set.
#function HintBox(Dialog: HWnd; Message, WParam: Word; LParam: Longint): Bool; export
def HintBox( Dialog,  Message,  wparam,  lparam) :
	if Message ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_HINTBOX_00)
		LoadWindowText(Dialog, ID_HINTBOX_01)
		LoadWindowText(Dialog, ID_HINTBOX_02)
		SetWindowText(GetDlgItem(Dialog, ID_HINTBOX_03), CurRecData.Hint)
		return (True)
	elif Message ==  WM_COMMAND:
		if wparam ==  1 or wparam ==  ID_HINTBOX_01:
			GetWindowText(GetDlgItem(Dialog, ID_HINTBOX_03), CurRecData.Hint, 255)
			if (SendMessage(GetDlgItem(Dialog, ID_HINTBOX_03), EM_GETMODIFY, 0, 0)) Modified = True
		elif wparam ==  2 or wparam ==  ID_HINTBOX_02:
			EndDialog(Dialog, 2)
		
	
	return (0)


# Dont Process Space key
def EditProc( hwnd,  iMsg,  wParam,  lParam) :
	if ((iMsg == WM_CHAR) and (wParam == VK_SPACE)):
		return (0)
	return (CallWindowProc((WNDPROC) OldProcEdit, hwnd, iMsg, wParam, lParam))


#  ++ Win Box Dialog Procedure  ++
#  This is an Win box with an Edit window that has text in it from the
#  resource file. The text is stored as RCData.
def WinBox( Dialog,  Message,  wparam,  lparam) :
	HGLOBAL H
	char * P
	x, y, i
	RECT Box
	THSREC TempHSData
	char temps[100]
	char AboutMsg[SIZE_ABOUTMSG * MAX_LANG_SIZE + 1]

	switch0 =  (Message) :
	elif switch0 ==  WM_INITDIALOG:
		LoadWindowText(Dialog, ID_WINBOX_00)
		LoadWindowText(Dialog, ID_WINBOX_01)
		LoadWindowText(Dialog, ID_WINBOX_02)
		LoadWindowText(Dialog, ID_WINBOX_03)

		H = LoadResource(hInst, FindResource(hInst, "About", RT_RCDATA))
		if (LANGText[OFFSET_ABOUTMSG][0] != '') :
			AboutMsg[0] = ''
			for i in range(0,SIZE_ABOUTMSG) :
				strcat(AboutMsg, LANGText[OFFSET_ABOUTMSG + i])
			P = AboutMsg
		else
			P = LockResource(H)
		SetWindowText(GetDlgItem(Dialog, ID_WINBOX_06), P)

		P = strrchr(FileName, '\\')
		if (P):
			P += 1
		else P = FileName
		SetWindowText(GetDlgItem(Dialog, ID_WINBOX_03), P)
		FreeResource(H)
		SetFocus(GetDlgItem(Dialog, ID_WINBOX_00))
		F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
		if (F2 == INVALID_HANDLE_VALUE):
			return (True)
		y = 0
		ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
		while (BytesMoved == sizeof(THSREC)) :
			if (TempHSData.moves > 0):
				y += 1
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
		
		CloseHandle(F2)

		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, None)
		x = SetFilePointer(F1, 0, None, FILE_END) / sizeof(TLEVEL)
		CloseHandle(F1)

		sprintf(temps, txt042, y, x)  # "Completed %d of %d levels"
		SetWindowText(GetDlgItem(Dialog, ID_WINBOX_04), temps)
		if ((Difficulty & 0x1F) != 0x1F) :
			temps = txt043  # "Difficulty Set ="
			P = temps + strlen(temps)
			strcat(temps, "         ")
			if ((Difficulty & 1) == 1) :
				P[0] = txt044[0]
				P += 2
			 # txt044="KEMHD"
			if ((Difficulty & 2) == 2) :
				P[0] = txt044[1]
				P += 2
			
			if ((Difficulty & 4) == 4) :
				P[0] = txt044[2]
				P += 2
			
			if ((Difficulty & 8) == 8) :
				P[0] = txt044[3]
				P += 2
			
			if ((Difficulty & 16) == 16) :
				P[0] = txt044[4]
			
			SetWindowText(GetDlgItem(Dialog, ID_WINBOX_05), temps)
		
		return (True)
	elif switch0 ==  WM_ERASEBKGND:
		GetClientRect(Dialog, & Box)
		SelectObject((HDC) wparam, GetStockObject(BLACK_BRUSH))
		Rectangle((HDC) wparam, Box.left, Box.top, Box.right, Box.bottom)
		return (True)
	elif switch0 ==  WM_CTLCOLORSTATIC:
		SetTextColor((HDC) wparam, 0x0000FFFF)
		SetBkColor((HDC) wparam, 0)
		return ((LONG) GetStockObject(BLACK_BRUSH))
	elif switch0 ==  WM_COMMAND:
		if ((wparam == ID_WINBOX_00) or (wparam == 1)):
			EndDialog(Dialog, 1)
	
	return (0)


#  ++ Load Tunnel ID Dialog Procedure  ++
# The editor uses this to pick which level ID number to assign
# to the current tunnel.
def LoadTID( Dialog,  Message,  wparam,  lparam) :
	char temps[40]
	i

	switch0 =  (Message) :
	elif switch0 ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_LOADTID_00)
		LoadWindowText(Dialog, ID_LOADTID_03)
		LoadWindowText(Dialog, ID_LOADTID_04)
		return (True)
	elif switch0 ==  WM_COMMAND:
		if ((wparam == ID_LOADTID_03) or (wparam == 1)): # idOk
			GetWindowText(GetDlgItem(Dialog, ID_LOADTID_01), temps, 10)
			i = atoi(temps)
			if (i > 7):
				i = 0
			EndDialog(Dialog, i)
			return (True)
		
	
	return (0)


#  ++ HS Box Dialog Procedure  ++ HighBox
#  This is the New High Score box
def HSBox( Dialog,  Message,  wparam,  lparam) :
	if Message ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_HIGHBOX_00)
		LoadWindowText(Dialog, ID_HIGHBOX_01)
		LoadWindowText(Dialog, ID_HIGHBOX_02)
		LoadWindowText(Dialog, ID_HIGHBOX_03)
		LoadWindowText(Dialog, ID_HIGHBOX_04)
		LoadWindowText(Dialog, ID_HIGHBOX_05)
		LoadWindowText(Dialog, ID_HIGHBOX_10)
		LoadWindowText(Dialog, ID_HIGHBOX_12)
		LoadWindowText(Dialog, ID_HIGHBOX_13)

		temps = str( CurLevel ) 
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_08), temps)
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_09), CurRecData.LName)
		temps = str( Game.ScoreMove ) 
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_06), temps)
		temps = str( Game.ScoreShot ) 
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_07), temps)
		if (HS.moves > 0) :
			old = txt008
			temps = str( HS.moves ) 
			strcat(old, temps)
			strcat(old, txt010)
			temps = str( HS.shots ) 
			strcat(old, temps)
			strcat(old, txt011)
			strcat(old, HS.name)
			ShowWindow(GetDlgItem(Dialog, ID_HIGHBOX_15), SW_SHOW)
			SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_15), old)
		
		GetPrivateProfileString("DATA", psUser, "", HS.name, 5, INIFile)
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_14), HS.name)
		F3 = CreateFile(GHFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, None)
		SetFilePointer(F3, (CurLevel - 1) * sizeof(GHS), None, FILE_BEGIN)
		ReadFile(F3, & GHS, sizeof(GHS), & BytesMoved, None)
		if (BytesMoved == sizeof(GHS)) :
			if ((GHS.moves == 0) or (Game.ScoreMove < GHS.moves) or ((Game.ScoreMove == GHS.moves) and (Game.ScoreShot < GHS.shots))) :
				SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_13), txt012)
				EnableWindow(GetDlgItem(Dialog, ID_HIGHBOX_13), True)
			else :
				old = txt009
				temps = str( GHS.moves ) 
				strcat(old, temps)
				strcat(old, txt010)
				temps = str( GHS.shots ) 
				strcat(old, temps)
				strcat(old, txt011)
				strcat(old, GHS.name)
				SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_13), old)
			
		
		CloseHandle(F3)
		SetFocus(GetDlgItem(Dialog, ID_HIGHBOX_01))
		return (True)
	elif Message ==  WM_COMMAND:
		if ((wparam == ID_HIGHBOX_01) or (wparam == 1)) :
			GetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_14), temps, 5)
			HS.moves = Game.ScoreMove
			HS.shots = Game.ScoreShot
			if (stricmp(temps, HS.name) != 0) :
				HS.name = temps
				WritePrivateProfileString("DATA", psUser, HS.name, INIFile)
			
			EndDialog(Dialog, 1)
			
	return (0)


def DrawLevels( lparam) :
	pDIS = (DRAWITEMSTRUCT FAR * ) lparam

	""" Draw the focus rectangle for an empty list box or an
	empty combo box to indicate that the control has the
	focus
	"""
	if ((int)(pDIS.itemID) < 0) :
		if ((pDIS.itemAction) & (ODA_FOCUS)) DrawFocusRect(PHDC, & PRC)
		return
	

	""" Get the string """
	SendMessage(pDIS.hwndItem, LB_GETTEXT, pDIS.itemID, ()(LPSTR) temps)

	if ((pDIS.itemState) & (ODS_SELECTED))
		""" Set background colors for selected item """
		crBack = 0x00404080
	else
		""" Set background colors for unselected item """
		crBack = 0

	crText = DifCList[0]
	if temps[0] ==  '1':
		crText = DifCList[1]
		break
	elif temps[0] ==  '2':
		crText = DifCList[2]
		break
	elif temps[0] ==  '3':
		crText = DifCList[3]
		break
	elif temps[0] ==  '4':
		crText = DifCList[4]
		break
	elif temps[0] ==  '5':
		crText = DifCList[5]
		break
	

	# Fill item rectangle with background color
	hbrBack = CreateSolidBrush(crBack)
	FillRect(PHDC, & PRC, hbrBack)
	DeleteObject(hbrBack)

	# Set current font, background and text colors
	SetBkColor(PHDC, crBack)
	SetTextColor(PHDC, crText)

	# TextOut uses current background and text colors
	TextOut(PHDC, PRC.left, PRC.top, temps + 1, lstrlen(temps) - 1)

	""" If enabled item has the input focus, call
	DrawFocusRect to set or clear the focus
	rectangle """
	if ((pDIS.itemState) & (ODS_FOCUS)) DrawFocusRect(PHDC, & PRC)


# For :
#  ++ HS List Dialog Procedure  ++
#  ++ Global HS List Dialog Procedure  ++
# So, the ID of the Dialog Item ID_LISTBOX must be the same
# for the two dialogs !!
#
def GetGameLevel( Dialog) :
	i, j
	char temps[100]

	i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0)
	SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETTEXT, i, () temps)
	temps[5] = (char) 0
	i = 1
	while (temps[i] == ' ') i += 1  # strip leading spaces
	j = atoi( & temps[i]) - 1
	if (CurLevel - 1 != j) :
		CurLevel = j
		LoadNextLevel(True, False)
	
	EndDialog(Dialog, 1)


#  ++ HS List Dialog Procedure  ++
#  List out all levels in the current data file, by number ,title, moves, shots & initials
def HSList( Dialog,  Message,  wparam,  lparam) :

	TLEVEL TempRecData
	THSREC TempHSData
	char temps[80], t2[100]
	i, j

	switch0 =  (Message) :
	elif switch0 ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_HIGHLIST_00)
		LoadWindowText(Dialog, ID_HIGHLIST_01)
		LoadWindowText(Dialog, ID_HIGHLIST_02)
		LoadWindowText(Dialog, ID_HIGHLIST_03)

		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
		if (F1 == INVALID_HANDLE_VALUE):
			return (True)  # File NOT Found
		F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
		if (F2 == INVALID_HANDLE_VALUE) :
			CloseHandle(F1)
			return (True)
		
		SetWindowText(GetDlgItem(Dialog, ID_HIGHLIST_02), HFileName)
		i = SetFilePointer(F2, 0, None, FILE_END) / sizeof(THSREC)
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_INITSTORAGE, i, 54)
		SetFilePointer(F2, 0, None, FILE_BEGIN)
		i = 1
		ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
		while (BytesMoved == sizeof(THSREC)) :
			ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, None)
			sprintf(temps, "%4d %-30.30s", i, TempRecData.LName)
			switch0 =  (TempRecData.SDiff) :
			elif switch0 ==  1:
				t2[0] = '1'
				break
			elif switch0 ==  2:
				t2[0] = '2'
				break
			elif switch0 ==  4:
				t2[0] = '3'
				break
			elif switch0 ==  8:
				t2[0] = '4'
				break
			elif switch0 ==  16:
				t2[0] = '5'
				break
			default:
				t2[0] = '0'
			
			t2 = (t2[0] + temps)
			if (TempHSData.moves > 0) :
				sprintf(temps, "%5d  %5d  %s", TempHSData.moves, TempHSData.shots, TempHSData.name)
				strcat(t2, temps)
			
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_ADDSTRING, 0, () t2)
			i += 1
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
		
		LastOfList = i - 2
		CloseHandle(F1)
		CloseHandle(F2)
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, CurLevel - 1, 0)
		OldProcEdit = SetWindowLong(GetDlgItem(Dialog, ID_LISTBOX), GWL_WNDPROC, (LONG)(WNDPROC) EditProc)
		return (True)
	elif switch0 ==  WM_CTLCOLORLISTBOX:
		return ((int) GetStockObject(BLACK_BRUSH))
		break
	elif switch0 ==  WM_MEASUREITEM:
		((MEASUREITEMSTRUCT FAR * ) lparam).itemHeight = 13
		break
	elif switch0 ==  WM_DRAWITEM:
		DrawLevels(lparam)
		return True
	elif switch0 ==  WM_VKEYTOITEM:
		return (TransListKey(Dialog, LOWORD(wparam)))
	elif switch0 ==  WM_COMMAND:
		if ((wparam == ID_HIGHLIST_01) or (wparam == 2)) EndDialog(Dialog, 0)
		if (((LOWORD(wparam) == ID_LISTBOX) and (HIWORD(wparam) == LBN_SELCHANGE)) or
			(wparam == 1)) GetGameLevel(Dialog)
	
	return (0)


def GHSScan( Dialog) :
	TLEVEL TempRecData
	THSREC TempHSData, TempGHSData
	char temps[80], t2[80]
	i, j, BHS

	LastOfList = 0
	F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
	if (F1 == INVALID_HANDLE_VALUE):
		return  # File NOT Found
	F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
	F3 = CreateFile(GHFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
	if (F3 == INVALID_HANDLE_VALUE) :
		CloseHandle(F1)
		if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2)
		return
	
	i = SetFilePointer(F3, 0, None, FILE_END) / sizeof(THSREC)
	SendDlgItemMessage(Dialog, ID_LISTBOX, LB_INITSTORAGE, i, 74)
	SetFilePointer(F3, 0, None, FILE_BEGIN)

	i = 1
	ReadFile(F3, & TempGHSData, sizeof(THSREC), & BytesMoved, None)
	while (BytesMoved == sizeof(THSREC)) :
		ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, None)
		if (F2 != INVALID_HANDLE_VALUE) ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
		BHS = (
			(TempHSData.moves > 0) and (BytesMoved == sizeof(THSREC)) and
			(
				(TempGHSData.moves == 0) or (TempHSData.moves < TempGHSData.moves) or
				((TempHSData.moves == TempGHSData.moves) and (TempHSData.shots < TempGHSData.shots))
			)
		)
		if (DispAll or (!DispAll and BHS)) :
			if (BHS)
				sprintf(temps, "%4d** %-28.28s %5d %5d  %4s>", i, TempRecData.LName, TempGHSData.moves,
					TempGHSData.shots, TempGHSData.name)
			else
				sprintf(temps, "%4d %-30.30s %5d %5d  %4s ", i, TempRecData.LName, TempGHSData.moves,
					TempGHSData.shots, TempGHSData.name)
			switch0 =  (TempRecData.SDiff) :
			elif switch0 ==  1:
				t2[0] = '1'
				break
			elif switch0 ==  2:
				t2[0] = '2'
				break
			elif switch0 ==  4:
				t2[0] = '3'
				break
			elif switch0 ==  8:
				t2[0] = '4'
				break
			elif switch0 ==  16:
				t2[0] = '5'
				break
			default:
				t2[0] = '0'
			
			t2 = t2[0] + temps
			if ((F2 != INVALID_HANDLE_VALUE) and (TempHSData.moves > 0) and (BytesMoved == sizeof(THSREC))) :
				sprintf(temps, "%5d  %5d  %s", TempHSData.moves, TempHSData.shots, TempHSData.name)
				strcat(t2, temps)
			
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_ADDSTRING, 0, () t2)
		
		i += 1
		ReadFile(F3, & TempGHSData, sizeof(THSREC), & BytesMoved, None)
	
	LastOfList = i - 2
	CloseHandle(F1)
	CloseHandle(F2)
	CloseHandle(F3)


#  ++ Global HS List Dialog Procedure  ++
#  List out all levels in the current data file, by number ,title, moves, shots & initials
def GHSList(Dialog, Message, wparam, lparam) :
	switch0 =  (Message) :
	if switch0 ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_GHIGHLIST_00)
		LoadWindowText(Dialog, ID_GHIGHLIST_01)
		LoadWindowText(Dialog, ID_GHIGHLIST_02)
		LoadWindowText(Dialog, ID_GHIGHLIST_03)
		LoadWindowText(Dialog, ID_GHIGHLIST_04)
		LoadWindowText(Dialog, ID_GHIGHLIST_05)
		LoadWindowText(Dialog, ID_GHIGHLIST_06)

		SetWindowText(GetDlgItem(Dialog, ID_GHIGHLIST_05), GHFileName)
		DispAll = True
		GHSScan(Dialog)
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, CurLevel - 1, 0)
		OldProcEdit = SetWindowLong(GetDlgItem(Dialog, ID_LISTBOX), GWL_WNDPROC, (LONG)(WNDPROC) EditProc)
		return (True)
	elif switch0 ==  WM_CTLCOLORLISTBOX:
		return ((int) GetStockObject(BLACK_BRUSH))
	elif switch0 ==  WM_MEASUREITEM:
		((MEASUREITEMSTRUCT FAR * ) lparam).itemHeight = 14
		break
	elif switch0 ==  WM_DRAWITEM:
		DrawLevels(lparam)
		return True
	elif switch0 ==  WM_VKEYTOITEM:
		return (TransListKey(Dialog, LOWORD(wparam)))
	elif switch0 ==  WM_COMMAND:
		if ((wparam == 2) or (wparam == ID_GHIGHLIST_01)):
			EndDialog(Dialog, 0)
		if (
			((LOWORD(wparam) == ID_LISTBOX) or (wparam == 1)) and
			(HIWORD(wparam) == LBN_SELCHANGE)
		):
			if (LastOfList > 0):
				GetGameLevel(Dialog)
		if (wparam == ID_GHIGHLIST_06) :
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_RESETCONTENT, 0, 0)
			DispAll = not DispAll
			GHSScan(Dialog)
			if (DispAll) :
				SetWindowText(GetDlgItem(Dialog, ID_GHIGHLIST_06), txt040)
				SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, CurLevel - 1, 0)
			else:
				SetWindowText(GetDlgItem(Dialog, ID_GHIGHLIST_06), txt041)
		
	
	return (0)


#  ++ Recorder Box Dialog Procedure  ++
#  The Recorder uses this to prompt for the Author's name.
def RecordBox( Dialog,  Message,  wparam,  lparam) :
	if Message ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_RECBOX_00)
		LoadWindowText(Dialog, ID_RECBOX_01)
		LoadWindowText(Dialog, ID_RECBOX_02)

		GetPrivateProfileString("DATA", psPBA, "", PBSRec.Author, 30, INIFile)
		SetWindowText(GetDlgItem(Dialog, ID_RECBOX_03), PBSRec.Author)
		SetFocus(GetDlgItem(Dialog, ID_RECBOX_03))
		break
	elif Message ==  WM_COMMAND:
		if ((wparam == 1) or (wparam == ID_RECBOX_02)) :
			GetWindowText(GetDlgItem(Dialog, ID_RECBOX_03), PBSRec.Author, 31)
			WritePrivateProfileString("DATA", psPBA, PBSRec.Author, INIFile)
			EndDialog(Dialog, 1)
		
	
	return (0)


#  ++ PlayBack Dialog Procedure  ++
#  This is the Playback Control window.
def PBWindow( Dialog,  Message,  wparam,  lparam) :
	# char temps[200]
	# RECT Box
	# char char1

	if Message ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_PLAYBOX_00)
		LoadWindowText(Dialog, ID_PLAYBOX_01)
		LoadWindowText(Dialog, ID_PLAYBOX_02)
		LoadWindowText(Dialog, ID_PLAYBOX_03)
		LoadWindowText(Dialog, ID_PLAYBOX_04)
		LoadWindowText(Dialog, ID_PLAYBOX_05)
		LoadWindowText(Dialog, ID_PLAYBOX_06)
		LoadWindowText(Dialog, ID_PLAYBOX_07)
		LoadWindowText(Dialog, ID_PLAYBOX_08)
		LoadWindowText(Dialog, ID_PLAYBOX_11)

		if (strcmp(CurRecData.LName, PBRec.LName) == 0) :
			SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_10), temps = str( PBRec.Size ) )
			PBCountH = GetDlgItem(Dialog, ID_PLAYBOX_09)
			PlayH = Dialog
			temps = txt013
			strcat(temps, PBRec.LName)
			strcat(temps, txt014)
			strcat(temps, PBRec.Author)

			if Speed ==  1: # Fast
				SendMessage(GetDlgItem(Dialog, ID_PLAYBOX_04), BM_SETCHECK, 1, 0)
			elif Speed ==  2: # Slow
				SendMessage(GetDlgItem(Dialog, ID_PLAYBOX_05), BM_SETCHECK, 1, 0)
			elif Speed ==  3: # Single Step
				SendMessage(GetDlgItem(Dialog, ID_PLAYBOX_06), BM_SETCHECK, 1, 0)
			
			GetWindowRect(MainH, & Box)
			SetWindowPos(Dialog, 0, Box.left + ContXPos + 2, Box.top + 280, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
			if (MessageBox(MainH, temps, App_Title, MB_OKCANCEL | MB_ICONQUESTION) == 2) :
				EndDialog(Dialog, 1)
				return (0)
			
		else EndDialog(Dialog, 1)
		return (0)
	elif Message ==  WM_COMMAND:
		if wparam ==  ID_PLAYBOX_01 or  #Close
				wparam ==  ID_PLAYBOX_11 or  #Speed
				wparam ==  1: # Close Playback Dialog
			if (Game_On and (Game.RecP == PBRec.Size) and
					(MessageBox(Dialog, txt016, App_Title, MB_YESNO | MB_ICONQUESTION) == IDYES)) :
				CheckMenuItem(MMenu, 123, MF_CHECKED)
				EnableMenuItem(MMenu, 117, 0)  # enable Save Recording
				Recording = True
				SetWindowText(MainH, REC_Title)
			
			PlayBack = False
			PBOpen = False
			PBHold = False
			RB_TOS = Game.RecP  #  we stop short
			EndDialog(Dialog, 1)
		elif wparam ==  ID_PLAYBOX_04:
			Speed = 1  # Fast
		elif wparam ==  ID_PLAYBOX_05:
			Speed = 2  # Slow
		elif wparam ==  ID_PLAYBOX_06:
			Speed = 3  # Single Step
		elif wparam ==  ID_PLAYBOX_02:
			if (PlayBack) :
				SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_02), txt017)
				PlayBack = False
			else :
				SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_02), txt018)
				PlayBack = True
			
		elif wparam ==  ID_PLAYBOX_03: #Reset
			PlayBack = False
			SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_02), txt017)
			SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_09), "0")
			SendMessage(MainH, WM_COMMAND, 105, 0)  #ReStart
			Game.RecP = 0
			RB_TOS = PBRec.Size
			PBHold = False
		
	
	return (0)


# static LastLevelNum

#  ++ Pick Box Dialog Procedure  ++
# The editor uses this to pick which level number to save the
# level with. Returns the number.
#function PickBox(Dialog: HWnd; Message, WParam: Word; LParam: Longint): Bool; export
def PickBox( Dialog,  Message,  wparam,  lparam) :
	# char temps[40]
	# i, j
	# TLEVEL TempRecData

	if Message ==  WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_PICKLEVEL_00)
		LoadWindowText(Dialog, ID_PICKLEVEL_01)
		LoadWindowText(Dialog, ID_PICKLEVEL_02)
		LoadWindowText(Dialog, ID_PICKLEVEL_03)
		LoadWindowText(Dialog, ID_PICKLEVEL_06)
		LoadWindowText(Dialog, ID_PICKLEVEL_08)

		i = SetFilePointer(F1, 0, None, FILE_END) / sizeof(TLEVEL)
		sprintf(temps, "1 - %d", i)
		SetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_04), temps)
		i += 1
		LastLevelNum = i  # save Last Level Number to check in exit
		temps = str( i ) 
		SetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_07), temps)
		if (CurLevel < i) temps = str( CurLevel ) 
		SetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_05), temps)
		SendDlgItemMessage(Dialog, ID_PICKLEVEL_08, BM_SETCHECK, 1, 0)
		return (True)
	elif Message ==  WM_COMMAND:
		if ((wparam == 1) or (wparam == ID_PICKLEVEL_01)) :
			GetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_05), temps, 10)
			i = atoi(temps)
			HSClear = SendDlgItemMessage(Dialog, ID_PICKLEVEL_08, BM_GETCHECK, 0, 0) > 0
			if (i <= LastLevelNum) EndDialog(Dialog, i)
			return (True)
		
	
	return (0)


#  ++ Used by Graph Box Dialog Procedure  ++
def SetUpGraphicsBox( d, C101, C102, BU) :
	long DBU
	RECT Box

	SendDlgItemMessage(d, ID_GRAPHBOX_02, BM_SETCHECK, C101, 0)
	#SendDlgItemMessage(d,ID_GRAPHBOX_03,BM_SETCHECK,C102,0)
	DBU = GetDialogBaseUnits()
	GetWindowRect(d, & Box)
	SetWindowPos(d, HWND_TOP, Box.left, Box.top, Box.right - Box.left,
		(BU * HIWORD(DBU)) / 8, SWP_NOZORDER)

	if (GFXOn) GFXKill()
	GFXInit()
	InvalidateRect(MainH, None, True)


#  ++ Used by Graph Box Dialog Procedure  ++
def GetLTGFiles( Dialog, ltgCur) :
	WIN32_FIND_DATA ffdata
	HANDLE ffdH, F1
	TLTGREC ltg

	# Scan for all LTG files
	SetCurrentDirectory(GraphDN)
	ffdH = FindFirstFile("*.ltg", & ffdata)
	if (ffdH) :
		do :
			F1 = CreateFile(ffdata.cFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
				FILE_FLAG_SEQUENTIAL_SCAN, None)
			if (F1 != INVALID_HANDLE_VALUE) :
				if ( not (ReadFile(F1, & ltg, sizeof(TLTGREC), & BytesMoved, None))) FileError()
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_ADDSTRING, 0, () ltg.Name)
				# the next line will help setup the listbox if we are mode 2
				if ((GraphM == 2) and (strcmp(GraphFN, ffdata.cFileName) == 0))
					memcpy(ltgCur, & ltg, sizeof(TLTGREC))
			
			CloseHandle(F1)
		 while (FindNextFile(ffdH, & ffdata))
		FindClose(ffdH)
	


#  ++ Graph Box Dialog Procedure  ++
#  This Dialog is used to change the Graphics Set being used
def GraphBox( Dialog,  Message,  wparam,  lparam) :

	char temps[MAX_PATH]
	TLTGREC ltg, ltgCur
	char Mode2N[40]
	i
	WIN32_FIND_DATA ffdata
	HANDLE ffdH, F1

	if Message ==  WM_INITDIALOG:

		LoadWindowCaption(Dialog, ID_GRAPHBOX_00)
		LoadWindowText(Dialog, ID_GRAPHBOX_01)
		LoadWindowText(Dialog, ID_GRAPHBOX_02)
		#LoadWindowText(Dialog,    ID_GRAPHBOX_03)
		LoadWindowText(Dialog, ID_GRAPHBOX_04)
		LoadWindowText(Dialog, ID_GRAPHBOX_05)
		LoadWindowText(Dialog, ID_GRAPHBOX_06)
		LoadWindowText(Dialog, ID_GRAPHBOX_08)
		LoadWindowText(Dialog, ID_GRAPHBOX_09)

		GetLTGFiles(Dialog, & ltgCur)
		if GraphM ==  1:
			SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_CHECKED, 100)
		elif GraphM ==  2:
			SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_UNCHECKED, 160)
			i = SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_SELECTSTRING, -1, () ltgCur.Name)
			SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_07), ltgCur.Author)
			SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_11), ltgCur.Info)
		else:
			SetUpGraphicsBox(Dialog, BST_CHECKED, BST_UNCHECKED, 100)  # mode 0
		
		return (True)
	elif Message ==  WM_COMMAND:
		switch0 =  (LOWORD(wparam)) :
		if switch0 ==  ID_GRAPHBOX_04 or # Close
				switch0 ==  2: # Cancel
			temps = str( GraphM ) 
			WritePrivateProfileString("SCREEN", psGM, temps, INIFile)
			if (GraphM == 2):
				WritePrivateProfileString("SCREEN", psGFN, GraphFN, INIFile)
			QHELP = False
			InvalidateRect(MainH, None, False)
			EndDialog(Dialog, 1)
		elif switch0 ==  ID_GRAPHBOX_02: # Internal Graphics
			if (GraphM == 2):
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_SETCURSEL, -1, 0)
			GraphM = 0
			SetUpGraphicsBox(Dialog, BST_CHECKED, BST_UNCHECKED, 100)

		# elif switch0 ==  ID_GRAPHBOX_03: # External Graphics
			if (GraphM == 2):
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_SETCURSEL, -1, 0)
			GraphM = 1
			SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_CHECKED, 100)
			if (GraphM == 0) :
				MessageBox(Dialog, txt032, txt007, MB_OK | MB_ICONERROR)
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_02, BM_SETCHECK, BST_CHECKED, 0)
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_03, BM_SETCHECK, BST_UNCHECKED, 0)
			
		elif switch0 ==  ID_GRAPHBOX_10: # Graphics Sets
			i = SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_GETCURSEL, 0, 0)
			if (i == -1):
				break  # Weed out junk ( Don't Ask )
			SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_GETTEXT, i, () Mode2N)
			# Find File Reference
			ffdH = FindFirstFile("*.ltg", & ffdata)
			if (ffdH) :
				do :
					F1 = CreateFile(ffdata.cFileName, GENERIC_READ, FILE_SHARE_READ,
						None, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, None)
					if (F1 != INVALID_HANDLE_VALUE) :
						if ( not (ReadFile(F1, & ltg, sizeof(TLTGREC), & BytesMoved, None))) FileError()
						if (strcmp(Mode2N, ltg.Name) == 0) :
							CloseHandle(F1)
							FindClose(ffdH)
							SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_07), ltg.Author)
							SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_11), ltg.Info)
							GraphFN = ffdata.cFileName
							GraphM = 2
							SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_UNCHECKED, 160)
							return (0)
						
					
					CloseHandle(F1)
				 while (FindNextFile(ffdH, & ffdata))
				FindClose(ffdH)
			
			#We should Never be here
			MessageBox(MainH, txt045, txt007, MB_OK)
		elif switch0 ==  ID_GRAPHBOX_08:
			QHELP = (SendDlgItemMessage(Dialog, ID_GRAPHBOX_08, BM_GETCHECK, 0, 0) > 0)
			InvalidateRect(MainH, None, False)
		elif switch0 ==  ID_GRAPHBOX_09:
			Browse(Dialog, GraphDN, txt037)
			SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_RESETCONTENT, 0, 0)
			GetLTGFiles(Dialog, & ltgCur)
			WritePrivateProfileString("SCREEN", psGDN, GraphDN, INIFile)
		
	return (0)


# ltank.h
"""******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 ******************************************************"""

#include <windows.h>

"""

Obj     BitM  Description
 -= 1-        ++     ++ ++ -= 1-

0       1   Dirt
1       2   Tank Up ( Primary )
-     3   Tank Right
-     4   Tank Down
-     5   Tank left
2     6   Base ( Primary)
-     7   Base Alt ( animation )
-     8   Base Alt2
3     9   Water ( Primary )
-     10    Water Alt
-     11    Water Alt 2
-         12    Blown Up Anti Tank (down)
4     13    Solid Block NOT movable
5     14    Movable Block
6     15    Bricks
7     16    Anti-Tank Gun Up
-     17    Anti-Tank Alt
-     18    Anti-Tank Alt 2
-     19      Movable block after pushing into water
11      20    Mirror Up-Lt
12      21    Mirror Up-Rt
13      22    Mirror Dn-Rt
14      23    Mirror Dn-Lt
15      24    One Way Up (Primary)
-     25    One Way Up Alt
-     26    One Way Up Alt2
16      27    One Way Rt (Primary)
-     28    One Way Rt Alt
-     29    One Way Rt Alt2
17      30    One Way Dn (Primary)
-     31    One Way Dn Alt
-     32    One Way Dn Alt2
18      33    One Way Lt (Primary)
-     34    One Way Lt Alt
-     35    One Way Lt Alt2
8           36      Anti-Tank facing right
-           37
-           38
9         39      Anti-Tank facing down
-         40
-         41
10        42      Anti-Tank facing left
-         43
-         44
19        45      Crystal Block
-         46      Crystal when hit by tank
20      47    Roto Mirror Up-Lt
21      48    Roto Mirror Up-Rt
22      49    Roto Mirror Dn-Rt
23      50    Roto Mirror Dn-Lt
-         51      Crystal when hit by Anti-tank
-         52      Blown Up Anti Tank (right)
-         53      Blown Up Anti Tank (left)
-         54      Blown Up Anti Tank (up)
24      56    Ice
25      57    Thin Ice
01dddddx  55    Worm Hole / Tunnel

"""

# Language Section for Lasertank
# Import this from its own file

#include "lt32l_us.h"

# Game Defaults
LevelData = "LaserTank.lvl" # Default Level Data File
INIFileName = "LaserTank.ini"
# MAX text size for a lang_text
MAX_LANG_SIZE = 300

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

def TPLAYFIELD():  # Matrix of G.O. (Game Object) types
	return [[0 for y in range(16) ] for x in range(16)]

class TLEVEL:   # Level Data from File
	def __init__(self):
		self.PF = TPLAYFIELD()  # Object Grid
		self.LName = ""  # Level Name
		self.Hint = ""  # Hint for this level
		self.Author = ""  # the Author of the Level
		SDiff = 0  # Score Difficulty


class TRECORDREC: # Recording Header
	def __init__(self):
		self.LName = ""  # Level Name
		self.Author = ""  # Author of the recording
		self.Level = 0   # Level Number
		self.Size = -1   # Size of Data  -= 1 Data to fallow


class TSEARCH: # Search Record used in Level Load
	def __init__(self):
		self.mode = 0 # 1=title, 2 = author
		self.SkipComp = False  # True = Skip Completed
		self.Diff = 0  # Difficulty charecter
		self.data = ""  # Search String

class TTANKREC:  # Store the Tank & Laser information
	def __init__(self):
		self.X = 0
		self.Y = 0
		self.Dir = 0
		self.Firing = False
		self.Good= False

class TGAMEREC :
	self.PF = TPLAYFIELD() # Store Game Objects
	self.PF2 = TPLAYFIELD() # Store Objects Under Stuff ( Ground, conveyor)
	self.BMF = TPLAYFIELD() # Bitmaps for Objects
	self.BMF2  = TPLAYFIELD() # Bitmaps for Under Stuff ( Bridges )
	self.ScoreMove = 0 # Move Counter
	self.ScoreShot = 0  # Shot Counter
	self.RecP = 0  # Recording Pointer
	self.Tank = TTANKREC()  # Tank Data

# TGAMEREC, * PGAMEREC

class TXYREC: # Use in BMA
	def __init__(self):
		# X & Y Location in Big Bitmap
		self.X = 0
		self.Y = 0


class TXYZREC: # Use for Mouse Buffer
	def __init__(self):
		self.X = 0
		self.Y = 0
		self.Z = 0

class THSREC: # High Score Record
	def __init__(self):
		self.moves = 0
		self.shots = 0
		self.name = ""  # Initials

class TLTGREC: # Record for LTG graphics
	def __init__(self):
		self.Name = ""  # Name of Graphic Set
		self.Author = ""  # Author of Graphics set
		self.Info = ""  # 3 line Description of Graphics Set
		self.ID = ""  # LTG ID = "LTG1"+0
		self.MaskOffset = 0  # Offset from the biggining of file to Mask Bitmap


class TICEREC: # Record used for sliding on the Ice
	def __init__(self):
		self.x = 0 # Last XY position of object to move
		self.y = 0
		self.dx = 0  # Direction to move in Delta Cords
		self.dy = 0
		self.s = False  # True if Sliding


#/  ++ ++ ++ MGY  ++ ++ -= 1-
MAX_TICEMEM = 16
class TICEMEM: # Record used for sliding objects on the Ice
	def __init__(self):
		self.Objects = []  # MGY - mem up 16 sliding objects
		self.count = 0  # number of current sliding objects

# extern TICEMEM SlideMem
#/  ++ ++ ++ MGY  ++ ++ -= 1-

# # Extern's  -= 1 Complete Program Defined Global Variables
# extern HINSTANCE hInst  # Globally Defined Instance
# extern char * RecBuffer
# extern GFXOn, Game_On, Sound_On, Ani_On, RLL, ConvMoving, CurLevel, TankDirty, DWarn
# extern AniCount, CurSelBM_L, CurSelBM_R, RB_TOS, PBHold, SpBm_Width, SpBm_Height, ContXPos
# extern ARecord, Difficulty, SkipCL, Recording, PlayBack, EditBMWidth, Speed, SlowPB, RecBufSize
# extern  MainH, Ed1, Ed2, BT1, BT2, BT3, BT4, BT5, BT6, BT7, BT8, BT9
# extern TGAMEREC Game, BackUp, SaveGame
# extern TLEVEL CurRecData
# extern HBRUSH LaserColor, LaserColorG, LaserColorR
# extern HDC gDC  # Use this game dc for all ops
# extern char FileName[], HFileName[], GHFileName[], PBFileName[], GraphFN[], GraphDN[], INIFile[]
# extern HMENU MMenu
# extern Modified, OKtoHS, VHSOn
# extern TRECORDREC PBRec, PBSRec
# extern char HelpFile[]
# extern PGAMEREC UndoBuffer
# extern UndoP, PBOpen
# extern THSREC HS
# extern HDC BuffDC
# extern HBITMAP BuffBMH
# extern TXYREC BMA[MaxBitMaps + 1]  # Bit Map Array
# extern TXYZREC MBuffer[MaxMBuffer]  # Mouse Buffer
# extern MB_TOS, MB_SP  # TOS = Top of Stack ; SP = Stack Pointer
# extern DWORD DEBUG_Time
# extern DWORD DEBUG_Frames
# extern HANDLE F1, F2, F3  # File Handles
# extern DWORD BytesMoved  # use in ReadFile & WriteFile
# extern GraphM, FindTank
# extern TICEREC SlideO, SlideT

# Variables for Language
# extern char LANGText[SIZE_ALL][MAX_LANG_SIZE]  # All lines of Language.dat
# extern char LANGFile[MAX_PATH]  # the dynamic file name for Language.dat
# extern TCHAR szFilterOFN[MAX_PATH]
# extern TCHAR szFilterPBfn[MAX_PATH]

# Global Function Prototypes

# def FileError()
# def GFXInit()  # Load All the Bitmaps
# def GFXKill(void)  # Release All the Bitmaps
# def PutLevel(void)  # Draw Game Board
# def GameOn(int)  # Turns on/off game timer
# def JK3dFrame(HDC, int, int, int, int, int)  # Draw 3D frame
# def JKSelFrame(HDC, int, int, int, int, int)  # Draw Red/Green frame
# def LoadLastLevel()
# BOOL LoadNextLevel(int, int)
# def CheckHighScore(void)  # Compare score to High Score
# def Animate(void)  # Animate all Animated Objects
# def MoveTank(int)
# CheckLoc(int, int)
# def MoveLaser()
# def FireLaser(int, int, int, int)
# def AntiTank()  # Target Anti-Tanks at Tank
# char GetOBM(char)  # Translate Bitmap to Object
# def BuildBMField()  # Convert Objects to bitmaps
# def PutSprite(char, int, int)  # Paint BM at X,Y
# def UpDateSprite(int, int)  # Repaint bitmap at x,y
# def UpDateTank()  # Repaint Tank
# def PutSelectors()  # Editor - paint objects to edit
# def ChangeGO(int, int, int)  # Change Game Object
# def SetGameSize(int)
# def SavePBFile()
# def InitBuffers()
# def KillBuffers()
# def AssignHSFile()
# def UpdateUndo()
# def UndoStep()
# def ResetUndoBuffer()
# MouseOperation(int)  # Process Mouse Input
# def ShowTunnelID()
# def ConvMoveTank(int, int, int)
# def IceMoveT()  # Move an tank on the Ice
# def IceMoveO()  # Move an Object on the Ice
# def AddKBuff(char)

# # Function Prototypes for Language
# def ChangeMenuText(HMENU, char * )
# def InitLanguage(HMENU, HMENU)
# def ConvertTabChar
# HBITMAP LoadImageFile(HINSTANCE, char * , char * )
# def LoadWindowText(, int)
# def LoadWindowCaption(, int)

""" Lets try some Macros """
GetTunnelID =(x, y)((Game.PF[x][y] & 0x0F) >> 1) # 0 - 7

# mgy 18-05-2003 Tunnel is limited to 0-7.
GetTunnelOldID =(x, y)((Game.PF[x][y] & 0x0F) >> 1) # 0 - 7
#GetTunnelOldID =(x,y) ((Game.PF[x][y] & 0x3F)  >> 1)   # 0 - 32

ISTunnel =(x, y)((Game.PF[x][y] & Obj_Tunnel) == Obj_Tunnel)
GameInProg = Game.RecP and (Game.PF[Game.Tank.X][Game.Tank.Y] != 2) and (!DWarn)

# ltank.c
"""******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 ******************************************************"""
#include <windows.h>

#include <string.h>

#include <stdio.h>

#include <mmsystem.h>

#include "ltank.h"

#include "ltank_d.h"

#include "lt_sfx.h"

const GetNextBMArray[MaxObjects + 1] = :
	0,
	1,
	2,
	3,
	4,
	5,
	6,
	8,
	9,
	10,
	7,
	12,
	13,
	14,
	11,
	16,
	17,
	18,
	15,
	19,
	21,
	22,
	23,
	20,
	24

const OpeningBMA[16] = :
	4,
	6,
	1,
	9,
	56,
	57,
	33,
	19,
	16,
	13,
	14,
	45,
	15,
	55,
	21,
	47
	#Bitmap IDs to show on the Quick Help / Welcome screen
EditorOn = False  # true when in editor mode
QHELP = False  # True when Quick Help is On
# extern
# const long DifCList[6]
# HINSTANCE hInst  # Globally Defined Instance
# HBITMAP OpenScreen  # Instruction Bitmap loaded from "control.bmp"
# HFONT MyFont
# FileHand
# RB_TOS  # Rec/Game Buffer pointer to TOP OF STACK
# PBHold
# VHSOn
#  MainH, Ed1, Ed2, BT1, BT2, BT3, BT4, BT5, BT6, BT7, BT8, BT9
# TPLAYFIELD ShiftPF, ShiftBMF
# HMENU EMenu, MMenu
# char PrintJobName[100]
# char HelpFile[MAX_PATH]

# extern Backspace[10]  # Backspace Buffer
# extern BS_SP  # StackPointer for Backspace
# extern OKtoSave

# OPENFILENAME OFN = :
# 	sizeof(OPENFILENAME),
# 	0,
# 	0,
# 	None,
# 	None,
# 	0,
# 	1,
# 	FileName,
# 	MAX_PATH,
# 	None,
# 	0,
# 	None,
# 	txt004,
# 	OFN_HIDEREADONLY,
# 	0,
# 	0,
# 	"lvl"


# OPENFILENAME PBfn = :
# 	sizeof(OPENFILENAME),
# 	0,
# 	0,
# 	None,
# 	None,
# 	0,
# 	1,
# 	PBFileName,
# 	MAX_PATH,
# 	None,
# 	0,
# 	None,
# 	txt005,
# 	OFN_HIDEREADONLY,
# 	0,
# 	0,
# 	"lpb"


# Callback function Declarations
# def WndProc(, , , )
# BOOL InitApplication(HINSTANCE)
# BOOL InitInstance(HINSTANCE, int)
# def EditDiffSet(int)
# BOOL LoadPlayback()
# def VHSPlayback()

# Local Work
def EditDiffSet(t) :
	#lt32l_us.inc
	#POPUP "&Difficulty"
	# BEGIN
	# MENUITEM "&Kids", 701
	# MENUITEM "&Easy", 702
	# MENUITEM "&Medium", 703
	# MENUITEM "&Hard", 704
	# MENUITEM "&Deadly", 705
	# END
	#CheckMenuItem(EMenu, 701, 0)  #Set check mark (menu handle, item ID, unchecked)
	# https:#docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-checkmenuitem
	CheckMenuItem(EMenu, 701, 0)
	CheckMenuItem(EMenu, 702, 0)
	CheckMenuItem(EMenu, 703, 0)
	CheckMenuItem(EMenu, 704, 0)
	CheckMenuItem(EMenu, 705, 0)
	if t ==  1:
		CheckMenuItem(EMenu, 701, MF_CHECKED)
		break
	elif t ==  2:
		CheckMenuItem(EMenu, 702, MF_CHECKED)
		break
	elif t ==  4:
		CheckMenuItem(EMenu, 703, MF_CHECKED)
		break
	elif t ==  8:
		CheckMenuItem(EMenu, 704, MF_CHECKED)
		break
	elif t ==  16:
		CheckMenuItem(EMenu, 705, MF_CHECKED)
	
	CurRecData.SDiff = t


def LoadPlayback() :
	# HANDLE F
	# char temps[200]

	if (Recording):
		SendMessage(MainH, WM_COMMAND, 123, 0)  # Turn Off Recording
	if ((F = CreateFile(PBFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, None)) == INVALID_HANDLE_VALUE):
		return (False)

	PBOpen = True  # this will also tell autorecord not to turn on
	ReadFile(F, & PBRec, sizeof(PBRec), & BytesMoved, None)

	if (RecBufSize <= PBRec.Size) : # RecBuffer needs to be bigger
		RecBufSize = PBRec.Size + 1
		RecBuffer = GlobalReAlloc(RecBuffer, RecBufSize, GMEM_MOVEABLE)
	

	ReadFile(F, RecBuffer, PBRec.Size, & BytesMoved, None)  # Load RecBuffer W data
	CloseHandle(F)
	CurLevel = PBRec.Level - 1

	# Set the current level to match the level in the playback
	# this will error if the levels have moved
	if ((!LoadNextLevel(True, True)) or (strcmp(CurRecData.LName, PBRec.LName) != 0)) :
		# Do a hard file search for the level name
		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, None)
		CurLevel = 0
		ReadFile(F, & CurRecData, sizeof(CurRecData), & BytesMoved, None)
		while ((BytesMoved == sizeof(CurRecData)) and (strcmp(CurRecData.LName, PBRec.LName) != 0)) :
			CurLevel += 1
			ReadFile(F, & CurRecData, sizeof(CurRecData), & BytesMoved, None)
		
		CloseHandle(F1)
		if (BytesMoved == sizeof(CurRecData)) :
			LoadNextLevel(True, True)
		
	
	Game.RecP = 0
	RB_TOS = PBRec.Size
	if (strcmp(CurRecData.LName, PBRec.LName) != 0) :
		# Could not find level from playback in current lvl file
		temps = txt013  # "Playback Level:"
		strcat(temps, PBRec.LName)
		strcat(temps, txt015)  # "\nCan Not be found in the current level file\n<"
		strcat(temps, FileName)
		strcat(temps, " >")
		MessageBox(MainH, temps, txt007, MB_OK | MB_ICONERROR)
		PlayBack = False
		PBOpen = False
		PBHold = False
		SendMessage(MainH, WM_COMMAND, 101, 0)
		return (False)
	
	return (True)


def VHSPlayback() :
	gDC = GetDC(MainH)
	GameOn(False)
	if (FindTank) :
		FindTank = False
		PutLevel()
	
	VHSOn = True
	while (Game.RecP < RB_TOS) :
		if (Game.Tank.Firing) MoveLaser()  # Move laser if one was fired
		# Check Key Press 
		if ( not (Game.Tank.Firing or ConvMoving or SlideO.s or SlideT.s)) :
			switch0 =  (RecBuffer[Game.RecP]) :
			if switch0 ==  VK_UP:
				MoveTank(1)  # Move tank Up one
			elif switch0 ==  VK_RIGHT:
				MoveTank(2)
			elif switch0 ==  VK_DOWN:
				MoveTank(3)
			elif switch0 ==  VK_LEFT:
				MoveTank(4)
			elif switch0 ==  VK_SPACE: :
				UpdateUndo()
				Game.ScoreShot += 1  # do here Not in FireLaser (as FireLaser is also used for antitanks)
				FireLaser(Game.Tank.X, Game.Tank.Y, Game.Tank.Dir, S_Fire)  # Bang
			
			
			Game.RecP += 1  # Point to next charecter
			AntiTank()  # give the Anti-Tanks a turn to play
		
		if (SlideO.s) IceMoveO()
		if (SlideT.s) IceMoveT()
		ConvMoving = False  # used to disable Laser on the conveyor
		switch0 =  (Game.PF[Game.Tank.X][Game.Tank.Y]) :
		if switch0 ==  2:
			if (Game_On): # Reached the Flag
				GameOn(False)
				ReleaseDC(gDC, MainH)
				VHSOn = False
				return  # We shouldn't be here

			
		elif switch0 ==  3:
			PostMessage(MainH, WM_Dead, 0, 0)  # Water
		elif switch0 ==  15:
			if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1)): # Conveyor Up
				ConvMoveTank(0, -1, True)
		elif switch0 ==  16:
			if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y)):
				ConvMoveTank(1, 0, True)
		elif switch0 ==  17:
			if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1)):
				ConvMoveTank(0, 1, True)
		elif switch0 ==  18:
			if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y)):
				ConvMoveTank(-1, 0, True)
		
	
	ReleaseDC(gDC, MainH)
	UpDateTank()
	GameOn(True)
	VHSOn = False


def CancelProc(hdc, nCode) :
	MSG msg

	while (PeekMessage( & msg, None, 0, 0, PM_REMOVE)) :
		TranslateMessage( & msg)
		DispatchMessage( & msg)
	
	return (True)


def Print() :
	PRINTDLG PrintInfo
	char temps[100]
	TEXTMETRIC TextInfo
	XLog, YLog, x, y, ch
	HDC tempDC
	HPALETTE hPal
	LPLOGPALETTE lpLogPal
	BITMAPINFO bmi
	HBITMAP hbm
	LPBYTE pBits
	DIBSECTION ds
	DOCINFO DocInfo = :
		sizeof(DOCINFO),
		0,
		0,
		0,
		0
	

	PrintInfo.hwndOwner = MainH
	PrintInfo.hDevMode = 0
	PrintInfo.hDevNames = 0
	PrintInfo.lStructSize = sizeof(PrintInfo)
	PrintInfo.Flags = PD_RETURNDC | PD_NOPAGENUMS | PD_NOSELECTION | PD_USEDEVMODECOPIES
	if (!PrintDlg( & PrintInfo)):
		return

	UpdateWindow(MainH)  # We need to redraw it first
	gDC = GetDC(MainH)

	ZeroMemory( & bmi, sizeof(bmi))
	bmi.bmiHeader.biSize = sizeof(BITMAPINFOHEADER)
	bmi.bmiHeader.biWidth = 16 * SpBm_Width
	bmi.bmiHeader.biHeight = 16 * SpBm_Height
	bmi.bmiHeader.biPlanes = 1
	bmi.bmiHeader.biBitCount = 24
	bmi.bmiHeader.biCompression = BI_RGB
	# Create intermediate drawing surface
	hbm = CreateDIBSection(gDC, & bmi, DIB_RGB_COLORS, & pBits, None, 0)
	# Prep surface for drawing
	tempDC = CreateCompatibleDC(gDC)
	SelectObject(tempDC, hbm)

	if ((GetDeviceCaps(gDC, RASTERCAPS) & RC_PALETTE)) # Are we Palette Based ?
	:
		# YES we are - Get Palette
		lpLogPal = GlobalAlloc(GPTR, sizeof(LOGPALETTE) + 256 * sizeof(PALETTEENTRY))
		lpLogPal.palVersion = 0x300
		lpLogPal.palNumEntries = 256
		GetSystemPaletteEntries(gDC, 0, 256, (LPPALETTEENTRY)(lpLogPal.palPalEntry))
		hPal = CreatePalette(lpLogPal)
		GlobalFree(lpLogPal)

		# Apply the Palette to Game WIndow
		SelectPalette(gDC, hPal, False)
		RealizePalette(gDC)
		# Apply the Palette to the tempDC
		SelectPalette(tempDC, hPal, False)
		RealizePalette(tempDC)
		DeleteObject(hPal)
	
	# Copy Bits to the memory DC
	BitBlt(tempDC, 0, 0, 16 * SpBm_Width, 16 * SpBm_Height, gDC, XOffset, YOffset, SRCCOPY)
	ReleaseDC(MainH, gDC)

	EnableWindow(MainH, False)
	sprintf(PrintJobName, "%s %d", txt036, CurLevel)
	DocInfo.lpszDocName = PrintJobName
	if (!StartDoc(PrintInfo.hDC, & DocInfo)) return

	SetAbortProc(PrintInfo.hDC, CancelProc)
	StartPage(PrintInfo.hDC)
	GetTextMetrics(PrintInfo.hDC, & TextInfo)
	ch = TextInfo.tmHeight
	XLog = GetDeviceCaps(PrintInfo.hDC, LOGPIXELSX)  # pixles per inch
	YLog = GetDeviceCaps(PrintInfo.hDC, LOGPIXELSY)

	# Now we can start to print
	SetBkMode(PrintInfo.hDC, TRANSPARENT)
	SetTextAlign(PrintInfo.hDC, TA_CENTER)
	TextOut(PrintInfo.hDC, (XLog * 3), (YLog / 2), PrintJobName, strlen(PrintJobName))
	if (CurLevel) # This is if we print the opening Screen
	:
		sprintf(temps, "( %s )", CurRecData.LName)
		TextOut(PrintInfo.hDC, (XLog * 3), (YLog / 2) + ch, temps, strlen(temps))
	
	y = (YLog * 5) + ch
	SetTextAlign(PrintInfo.hDC, TA_LEFT)
	sprintf(temps, "Moves = %d    Shots = %d", Game.ScoreMove, Game.ScoreShot)
	TextOut(PrintInfo.hDC, XLog, y, temps, strlen(temps))

	GetObject(hbm, sizeof(DIBSECTION), & ds)
	StretchDIBits(PrintInfo.hDC, XLog, YLog, XLog * 4, YLog * 4,
		0, 0, (SpBm_Width * 16), (SpBm_Height * 16),
		ds.dsBm.bmBits, (LPBITMAPINFO) & ds.dsBmih, DIB_RGB_COLORS, SRCCOPY)

	EndPage(PrintInfo.hDC)  # Send Page
	EndDoc(PrintInfo.hDC)
	DeleteDC(tempDC)
	DeleteDC(PrintInfo.hDC)
	DeleteObject(hbm)
	EnableWindow(MainH, True)


def ToggleOpt(ID, HMENU Menu, int * Opt, LPCTSTR psText) :
	if (GetMenuState(Menu, ID, 0) & MF_CHECKED) :
		CheckMenuItem(Menu, ID, 0)
		* Opt = False
		WritePrivateProfileString("OPT", psText, "No", INIFile)
	else :
		CheckMenuItem(Menu, ID, MF_CHECKED)
		* Opt = True
		WritePrivateProfileString("OPT", psText, "Yes", INIFile)
	


# Create file name for playback file *_0001.lpb
def BuildPB_Name() :
	char temps[100]
	char * P

	PBSRec.Level = CurLevel
	sprintf(temps, "_%04d.lpb", PBSRec.Level)
	P = strrchr(PBFileName, '_')
	if (P):
		P = temps  # add to name


#  --- Main Window Procedure ---
# This is used for both the editor and the game 
# function MainWindowProc(Window: HWnd; Message, WParam: Word; LParam: Longint): Longint; export
#https:#docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/ms633573(v%3Dvs.85)
# main game loop main loop
def WndProc( Window,  Message,  wparam,  lparam) :

	switch0 =  (Message) :
	if Message ==  WM_CREATE: # Sent when an application requests that a window be created by calling the CreateWindowEx or CreateWindow function. (The message is sent before the function returns.) The window procedure of the new window receives this message after the window is created, but before the window becomes visible.
		FileName = LevelData  # set up default file name
		Menu = GetMenu(Window)

		# Check INI file for settings and copy into variables
		GetPrivateProfileString("OPT", psAni, psYes, temps, 5, INIFile)
		# Check if Animation is enabled or disabled 
		if (strcmp(temps, psYes)) :
			Ani_On = False
			CheckMenuItem(Menu, 104, 0)  # Yes I Know we should write MF_BYCOMMAND | MF_UNCHECKED
		
		GetPrivateProfileString("OPT", psSound, psYes, temps, 5, INIFile)
		# Check if Sound is enabled or disabled
		if (strcmp(temps, psYes)) :
			Sound_On = False
			CheckMenuItem(Menu, 102, 0)
		
		GetPrivateProfileString("OPT", psSCL, "No", temps, 5, INIFile)
		# Check if Skip Complete Level is enabled or disabled
		if (strcmp(temps, psYes) == 0) :
			CheckMenuItem(Menu, 116, MF_CHECKED)
			SkipCL = True
		
		GetPrivateProfileString("OPT", psARec, "No", temps, 5, INIFile)
		# Check if AutoRecord is enabled or disabled
		if (strcmp(temps, psYes) == 0) :
			CheckMenuItem(Menu, 115, MF_CHECKED)
			ARecord = True
		
		GetPrivateProfileString("OPT", psDW, "No", temps, 5, INIFile)
		# Check if DisableWarnings is enabled or disabled
		if (strcmp(temps, psYes) == 0) :
			CheckMenuItem(Menu, 127, MF_CHECKED)
			DWarn = True
		
		Difficulty = GetPrivateProfileInt("DATA", psDiff, 0, INIFile)
		GetPrivateProfileString("OPT", psRLLOn, psYes, temps, 5, INIFile)
		# Check if Remember Last Level is enabled or disabled
		if (strcmp(temps, psYes)) :
			RLL = False
			CheckMenuItem(Menu, 109, 0)
		else GetPrivateProfileString("DATA", psRLLN, LevelData, FileName, 100, INIFile)
		PBSRec.Author[0] = (char) 0
		LaserColorG = CreateSolidBrush(0x0000FF00)
		LaserColorR = CreateSolidBrush(0x000000FF)
		InitBuffers()
		SFxInit()
		PBHold = False  # used by playback to hold charecters
		VHSOn = False
		AssignHSFile()
		break
	elif Message ==  WM_PAINT:
		pdc = BeginPaint(Window, & PI)
		gDC = pdc  # we use gDC for most graphics stuff
		SelectObject(gDC, MyFont)
		GetClientRect(Window, & Box)

		# draw 3D frames 
		# draw 3D frame around game board inner
		JK3dFrame(pdc, XOffset - 1, YOffset - 1, (SpBm_Width * 16) + XOffset, (SpBm_Height * 16) + YOffset, False)
		JK3dFrame(pdc, XOffset - 2, YOffset - 2, (SpBm_Width * 16) + XOffset + 1, (SpBm_Height * 16) + YOffset + 1, False)
		# draw 3D frame around game board outer (including coordinate labels)
		JK3dFrame(pdc, 1, 1, ContXPos - 5, Box.bottom - 2, True)
		# Draw 3D frame around Level info box
		JK3dFrame(pdc, ContXPos - 1, 1, ContXPos + 181, Box.bottom - 2, True)
		# Draw 3D frame around buttons (only if not in editor mode)
		if (!EditorOn)
			JK3dFrame(pdc, ContXPos + 10, 250, ContXPos + 165, 405, False)

		# Display level information background at (ContXPos,2, 180,245)
		tDC = CreateCompatibleDC(pdc)
		OpenScreen = LoadImageFile(hInst, "CONTROLBM", CONTROL_BMP)
		tBM = SelectObject(tDC, OpenScreen)
		# put up control bitmap  background for level info
		BitBlt(pdc, ContXPos, 2, 180, 245, tDC, 0, 0, SRCCOPY)
		SelectObject(tDC, tBM)
		DeleteObject(OpenScreen)
		SetBkMode(pdc, TRANSPARENT)
		SetTextAlign(pdc, TA_CENTER)
		SetTextColor(pdc, 0x00808080)

		# Draw opening quick help bitmap over the level
		if ((CurLevel == 0) or QHELP) :
			# come here in the beggining before a level is loaded
			OpenScreen = LoadImageFile(hInst, "OPENING", OPENING_BMP)
			tBM = SelectObject(tDC, OpenScreen)
			StretchBlt(gDC, XOffset, YOffset, SpBm_Width * 16, SpBm_Height * 16, tDC, 0, 0, 384, 384, SRCCOPY)
			SelectObject(tDC, tBM)
			DeleteObject(OpenScreen)
			x = XOffset + 3
			y = YOffset + (SpBm_Height * 8)
			j = 1
			for i in range(0, 16) :
				PutSprite(OpeningBMA[i], x, y)
				x += (SpBm_Width * 4)
				j += 1
				if (j > 4) :
					x = XOffset + 3
					y += (SpBm_Height * 2)
					j = 1
				
			
			# desactive  2004/05/09 - mgy
			# TextOut(pdc,(SpBm_Width*13),(SpBm_Height*16),App_Version,strlen(App_Version))
		else :
			# Lable Game Grid
			x = SpBm_Width / 2
			y = (SpBm_Height - 15) / 2
			for i in range(1,17) :
				TextOut(pdc, 8, YOffset + y + ((i - 1) * SpBm_Height), temps = str( i ) , strlen(temps))
				if (i < 10) :
					TextOut(pdc, 8 + XOffset + (16 * SpBm_Width), YOffset + y + ((i - 1) * SpBm_Height), temps = str( i ) , strlen(temps))
				else :
					temps = "1 "
					TextOut(pdc, -1 + 8 + XOffset + (16 * SpBm_Width), YOffset + y + ((i - 1) * SpBm_Height), temps, strlen(temps))
					temps = str( i - 10 ) 
					TextOut(pdc, 3 + 8 + XOffset + (16 * SpBm_Width), YOffset + y + ((i - 1) * SpBm_Height), temps, strlen(temps))
				

				temps = "@"
				temps[0] = temps[0] + i
				TextOut(pdc, XOffset + x + ((i - 1) * SpBm_Width), 1, temps, strlen(temps))
				TextOut(pdc, XOffset + x + ((i - 1) * SpBm_Width), YOffset + 1 + (16 * SpBm_Height), temps, strlen(temps))

			

			PutLevel()  #Draw level
			if (EditorOn) :
				PutSelectors()
				ShowTunnelID()
			else :
				#Draw level info text
				SetTextColor(pdc, DifCList[0])
				temps = str( CurLevel ) 
				switch1 =  (CurRecData.SDiff) # Set text colour and temps text based on level difficulty
				:
				elif switch1 ==  1:
					strcat(temps, txt023)
					SetTextColor(pdc, DifCList[1])
					break
				elif switch1 ==  2:
					strcat(temps, txt024)
					SetTextColor(pdc, DifCList[2])
					break
				elif switch1 ==  4:
					strcat(temps, txt025)
					SetTextColor(pdc, DifCList[3])
					break
				elif switch1 ==  8:
					strcat(temps, txt026)
					SetTextColor(pdc, DifCList[4])
					break
				elif switch1 ==  16:
					strcat(temps, txt027)
					SetTextColor(pdc, DifCList[5])
					break
				
				TextOut(pdc, ContXPos + 91, 43, temps, strlen(temps))
				TextOut(pdc, ContXPos + 91, 100, CurRecData.LName, strlen(CurRecData.LName))
				TextOut(pdc, ContXPos + 91, 150, CurRecData.Author, strlen(CurRecData.Author))
				SetTextColor(pdc, 0x0000FF00)
				TextOut(pdc, ContXPos + 48, 207, temps = str( Game.ScoreMove ) , strlen(temps))
				TextOut(pdc, ContXPos + 134, 207, temps = str( Game.ScoreShot ) , strlen(temps))
			
		
		DeleteDC(tDC)
		EndPaint(Window, & PI)
		return (0)

		# KEY PRESS: if key down event, then add key ID to keyboard buffer (RecBuffer[])
	elif Message ==  WM_KEYDOWN:
		if (!EditorOn) :
			if ((wparam < 32) or (wparam > 40)):
				return (0)  # Must be one of SPACEBAR (32), PAGE UP, PAGE DOWN, END, HOME, LEFT ARROW, UP ARROW, RIGHT ARROW, DOWN ARROW (40)
			if ((RB_TOS > Game.RecP) and (lparam & 0x40000000)):
				return (0)  #If Top Of Stack > Record pointer and Transition is keydown
			AddKBuff(wparam)
			return (0)
		
		break

		# main game logic processing *****************************************
	elif Message ==  WM_TIMER:

		if (QHELP):
			return (0)

		gDC = GetDC(Window)
		SelectObject(gDC, MyFont)

		# If newly loaded level then set up level
		if (FindTank) # Newly loaded level so draw board and turn off FindTank
		:
			FindTank = False
			PutLevel()
			SetTimer(MainH, 1, GameDelay, None)  #Restart the timer for GameDelay (ms). Sends WM_TIMER message when timer up
		

		# Animation: cycle through frames with AniCount += 1
		if (Ani_On):
			AniCount += 1
		if (AniCount == ani_delay):
			Animate()  # Do Animation. Can slow animation frames with ani_delay

		# Move laser
		if (Game.Tank.Firing) :
			MoveLaser()  # Move laser if one was fired

		if (PBOpen) #?If playback is on
		:
			if (Speed == 2) :
				SlowPB += 1
				if (SlowPB == SlowPBSet) SlowPB = 1
			
			if (PlayBack and ( not (ConvMoving or SlideO.s or SlideT.s)) and
				((Speed != 2) or ((Speed == 2) and (SlowPB == 1)))) :
				PBHold = False
				temps = str( Game.RecP ) 
				SendMessage(PBCountH, WM_SETTEXT, 0, (long)(temps))
				if (Speed == 3) SendMessage(PlayH, WM_COMMAND, ID_PLAYBOX_02, 0)
			else PBHold = True
		

		# Check Key Press 
		# PROCESS KEYBOARD INPUT FROM USER
		# python: # if ((Game.RecP < RB_TOS) and ( not (Game.Tank.Firing or ConvMoving or SlideO.s or SlideT.s or PBHold)))
		# if (inputs on stack) and (tank not firing) and (conveyors not moving) and (nothing sliding) and (playback not paused)
		if ((Game.RecP < RB_TOS) and # (speedBug) and
			( not (Game.Tank.Firing or ConvMoving or SlideO.s or SlideT.s or PBHold))) :
			switch2 =  (RecBuffer[Game.RecP]) :
			elif switch2 ==  VK_UP:
				MoveTank(1)  # Move tank Up one
				break
			elif switch2 ==  VK_RIGHT:
				MoveTank(2)
				break
			elif switch2 ==  VK_DOWN:
				MoveTank(3)
				break
			elif switch2 ==  VK_LEFT:
				MoveTank(4)
				break
			elif switch2 ==  VK_SPACE: :
				UpdateUndo()
				Game.ScoreShot += 1  # do here Not in FireLaser
				FireLaser(Game.Tank.X, Game.Tank.Y, Game.Tank.Dir, S_Fire)  # Bang
			
			
			Game.RecP += 1  # Point to next charecter
			AntiTank()  # give the Anti-Tanks a turn to play
		

		# resolve momenta
		if (SlideO.s)
			IceMoveO()
		if (SlideT.s)
			IceMoveT()
		if (TankDirty)
			UpDateTank()  # I know we do this again later.
		ConvMoving = False  # used to disable Laser on the conveyor

		switch3 =  (Game.PF[Game.Tank.X][Game.Tank.Y]) # Check where the tank ended up
		:
		elif switch3 ==  2:
			if (Game_On) # Reached the Flag
			:
				GameOn(False)
				SoundPlay(S_EndLev)
				if (!PBOpen) :
					if (Recording) SendMessage(Window, WM_SaveRec, 0, 0)
					CheckHighScore()
					LoadNextLevel(False, False)
				
			
			break
		elif switch3 ==  3:
			PostMessage(Window, WM_Dead, 0, 0)  # Water
			break
		elif switch3 ==  15:
			if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1)) # Conveyor Up
				ConvMoveTank(0, -1, True)
			break
		elif switch3 ==  16:
			if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y))
				ConvMoveTank(1, 0, True)
			break
		elif switch3 ==  17:
			if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1))
				ConvMoveTank(0, 1, True)
			break
		elif switch3 ==  18:
			if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y))
				ConvMoveTank(-1, 0, True)
		

		# Check the mouse Buffer
		if ((Game.RecP == RB_TOS) and (MB_TOS != MB_SP) and
			( not (Game.Tank.Firing or ConvMoving or SlideO.s or SlideT.s))) :
			if (MouseOperation(MB_SP)) # Turn Mouse Operation into KB chars
			:
				MB_SP += 1
				if (MB_SP == MaxMBuffer) MB_SP = 0
			else :
				MB_SP = MB_TOS  # error so clear the rest
				MessageBeep(0)
			
		
		if (TankDirty)
			UpDateTank()
		ReleaseDC(Window, gDC)
		return (0)

	elif Message ==  WM_GameOver:
		DialogBox(hInst, "WinBox", Window, (DLGPROC) WinBox)
		return (0)

	elif Message ==  WM_NewHS:
		DialogBox(hInst, "HighBox", Window, (DLGPROC) HSBox)
		return (0)

	elif Message ==  WM_SaveRec:
		if (PBSRec.Author[0] == (char) 0)
			DialogBox(hInst, "RecBox", Window, (DLGPROC) RecordBox)
		PBfn.lpstrTitle = txt006
		PBfn.Flags = OFN_HIDEREADONLY | OFN_OVERWRITEPROMPT
		PBSRec.LName = CurRecData.LName
		BuildPB_Name()
		if (GetSaveFileName( & PBfn)) :
			if (strchr(PBFileName, '.') == 0) strcat(PBFileName, ".lpb")
			if (Game.RecP < RecMax) PBSRec.Size = Game.RecP  # Set Playback size
			else PBSRec.Size = RecMax  # WOW Big Level
			SavePBFile()
		
		return (0)

	elif Message ==  WM_Dead:
		GameOn(False)
		if (VHSOn) :
			RB_TOS = Game.RecP
			return (0)
		
		SoundPlay(S_Die)
		i = DialogBox(hInst, "DeadBox", Window, (DLGPROC) DeadBox)
		switch4 =  (i) :
		if switch4 ==  ID_DEADBOX_UNDO:
			SendMessage(Window, WM_COMMAND, 110, 0)
			GameOn(True)
			break
		elif switch4 ==  ID_DEADBOX_RESTART or switch4 ==  2: # Cancel
			UndoStep()  # We have to undo the error first ( inelif switch4 ==  we Restart Undo)
			PostMessage(Window, WM_COMMAND, 105, 0)
		
		return (0)

	elif Message ==  WM_CLOSE:
		if (GameInProg) :
			i = MessageBox(MainH, txt039, txt038, MB_YESNO | MB_ICONQUESTION)
			if (i == IDYES) SendMessage(MainH, WM_SaveRec, 0, 0)
		
		DestroyWindow(Window)
		return (0)

	elif Message ==  WM_DESTROY:
		if (Game_On)
			GameOn(False)  # Kill Timer
		GFXKill()
		KillBuffers()
		DeleteObject(LaserColorR)
		DeleteObject(LaserColorG)
		WinHelp(Window, HelpFile, HELP_QUIT, 0)
		PostQuitMessage(0)
		return (0)

	elif Message ==  WM_MOVE:
		twp.length = sizeof(twp)
		GetWindowPlacement(Window, & twp)
		if (twp.showCmd != SW_SHOWNORMAL) break
		temps = str( twp.rcNormalPosition.top ) 
		WritePrivateProfileString("SCREEN", psYpos, temps, INIFile)
		temps = str( twp.rcNormalPosition.left ) 
		WritePrivateProfileString("SCREEN", psXpos, temps, INIFile)
		break
	elif Message ==  WM_MOUSEMOVE:
		if (EditorOn) # if we are editing then check mouse
		:
			if (( not (wparam & (MK_RBUTTON | MK_LBUTTON))) or
				(wparam & MK_SHIFT)) return (0)  # Mouse Not Down or Shift pressed

			y = ((HIWORD(lparam) - XOffset) / SpBm_Height)
			x = ((LOWORD(lparam) - YOffset) / SpBm_Width)
			if ((x < 0) or (x > 15) or (y < 0) or (y > 15)) return (0)
			if (wparam == MK_LBUTTON) :
				if ((Game.PF[x][y] != CurSelBM_L) and (CurSelBM_L != MaxObjects))
					ChangeGO(x, y, CurSelBM_L)
			else :
				if ((Game.PF[x][y] != CurSelBM_R) and (CurSelBM_R != MaxObjects))
					ChangeGO(x, y, CurSelBM_R)
			
			return (0)
		
		break
	elif Message ==  WM_LBUTTONDOWN:
		if (EditorOn) :
			SetFocus(Window)  # We need to get the focus off of the Edits
			if (LOWORD(lparam) > ContXPos) :
				# we are on the selector window area
				y = (HIWORD(lparam) - 250) / (SpBm_Height + 4)
				x = (LOWORD(lparam) - (ContXPos + 5)) / (SpBm_Width + 4)
				i = x + (y * EditBMWidth)
				if ((i > MaxObjects + 1) or (i < 0)) return (0)
				CurSelBM_L = i
				gDC = GetDC(Window)
				PutSelectors()
				ReleaseDC(Window, gDC)
			else :
				# we are in the Game window area - Edit Mode
				y = ((HIWORD(lparam) - XOffset) / SpBm_Height)
				x = ((LOWORD(lparam) - YOffset) / SpBm_Width)
				if ((x < 0) or (x > 15) or (y < 0) or (y > 15)) return (0)
				if ((wparam & MK_SHIFT) == MK_SHIFT) ChangeGO(x, y, GetNextBMArray[Game.PF[x][y]])  # Rotate Object
				else :
					if (Game.PF[x][y] != CurSelBM_L) ChangeGO(x, y, CurSelBM_L)
				
				Modified = True
			
			return (0)
		else :
			y = ((HIWORD(lparam) - XOffset) / SpBm_Height)
			x = ((LOWORD(lparam) - YOffset) / SpBm_Width)
			if ((x < 0) or (x > 15) or (y < 0) or (y > 15)) return (0)
			MBuffer[MB_TOS].X = x
			MBuffer[MB_TOS].Y = y
			MBuffer[MB_TOS].Z = 1  # 1 = mouse clicked
			MB_TOS += 1
			if (MB_TOS == MaxMBuffer) MB_TOS = 0
		
		break
	elif Message ==  WM_RBUTTONDOWN:
		if (EditorOn) :
			SetFocus(Window)  # We need to get the focus off of the Edits
			if (LOWORD(lparam) > ContXPos) :
				y = (HIWORD(lparam) - 250) / (SpBm_Height + 4)
				x = (LOWORD(lparam) - (ContXPos + 5)) / (SpBm_Width + 4)
				i = x + (y * EditBMWidth)
				if ((i > MaxObjects + 1) or (i < 0)) return (0)
				CurSelBM_R = i
				gDC = GetDC(Window)
				PutSelectors()
				ReleaseDC(Window, gDC)
			else :
				y = ((HIWORD(lparam) - XOffset) / SpBm_Height)
				x = ((LOWORD(lparam) - YOffset) / SpBm_Width)
				if ((x < 0) or (x > 15) or (y < 0) or (y > 15)) return (0)
				if (Game.PF[x][y] != CurSelBM_R) ChangeGO(x, y, CurSelBM_R)
				Modified = True
			
			return (0)
		else :
			# Get the square clicked on (x,y)
			y = ((HIWORD(lparam) - XOffset) / SpBm_Height)
			x = ((LOWORD(lparam) - YOffset) / SpBm_Width)
			if ((x < 0) or (x > 15) or (y < 0) or (y > 15))
				return (0)
			MBuffer[MB_TOS].X = x
			MBuffer[MB_TOS].Y = y
			MBuffer[MB_TOS].Z = 2  # 2 = mouse R clicked
			MB_TOS += 1
			if (MB_TOS == MaxMBuffer)
				MB_TOS = 0
		
		break
	elif Message ==  WM_COMMAND:
		if (!EditorOn) SetFocus(Window)  # We need this for the buttons
		switch5 =  (LOWORD(wparam)) :
		elif switch5 ==  101: # New Game
			LastLevel = CurLevel
			CurLevel = 0
			if (RLL) # Remember Last Level
			:
				GetPrivateProfileString("DATA", psRLLL, "1", temps, 5, INIFile)
				CurLevel = atoi(temps)
				CurLevel -= 1
			
			if (!LoadNextLevel(True, False))
				CurLevel = LastLevel
			return (0)
		elif switch5 ==  102: # Toggle Sound Option
			ToggleOpt(102, MMenu, & Sound_On, psSound)
			return (0)
		elif switch5 ==  103: # Exit
			if (GameInProg) :
				i = MessageBox(MainH, txt039, txt038, MB_YESNO | MB_ICONQUESTION)
				if (i == IDYES) SendMessage(MainH, WM_SaveRec, 0, 0)
			
			DestroyWindow(Window)
			return (0)
		elif switch5 ==  104: # Toggle Animation Option
			ToggleOpt(104, MMenu, & Ani_On, psAni)
			return (0)
		elif switch5 ==  105:
			if (CurLevel > 0) # ReStart
			:
				if (UndoP > 0) UpdateUndo()  # Without this we loose the last move
				memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD))  # Game.PF = CurRecData.PF
				BuildBMField()
				InvalidateRect(Window, None, False)
				GameOn(True)
				Game.RecP = 0
				RB_TOS = 0
				SlideO.s = 0  # stop any sliding
				SlideMem.count = 0  # MGY  -= 1- stop any sliding
				SlideT.s = 0
				# Lets also init the Mouse Buffer
				MB_TOS = MB_SP = 0
			
			return (0)

		elif switch5 ==  106: # Load Level
			x = Game_On
			LastLevel = CurLevel
			GameOn(False)
			i = DialogBox(hInst, "LoadLev", Window, (DLGPROC) LoadBox)
			if (i > 100) :
				CurLevel = i - 101
				if (!LoadNextLevel(True, True)) :
					CurLevel = LastLevel
					GameOn(x)
				
			else
				GameOn(x)
			return (0)

		elif switch5 ==  107: # Skip Level
			LoadNextLevel(False, False)
			return (0)

		elif switch5 ==  108: # Open Data File
			x = Game_On
			GameOn(False)
			OFN.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST
			temps = FileName
			if (GetOpenFileName( & OFN)) :
				AssignHSFile()
				CurLevel = 0
				Backspace[BS_SP] = 0  # Clear Backspace stack
				EnableMenuItem(MMenu, 118, MF_BYCOMMAND | MF_GRAYED)  # Disable Menu Item
				LoadNextLevel(True, False)
			else :
				GameOn(x)
				FileName = temps
			
			return (0)

		elif switch5 ==  109: # Toggle Remember Last Level Option
			ToggleOpt(109, MMenu, & RLL, psRLLOn)
			return (0)

		elif switch5 ==  110: # Undo
			UndoStep()
			if (UndoBuffer[UndoP].Tank.Dir == 0) :
				EnableMenuItem(MMenu, 110, MF_GRAYED)  # disable Undo
				EnableWindow(BT1, SW_HIDE)
			
			InvalidateRect(Window, None, False)
			return (0)
		elif switch5 ==  111: # Save Position
			SaveGame = Game
			EnableMenuItem(MMenu, 112, MF_ENABLED)
			EnableWindow(BT3, SW_SHOWNA)
			return (0)

		elif switch5 ==  112: # Restore Position
			Game = SaveGame
			RB_TOS = Game.RecP  # clear all keys Past this Pos
			MB_TOS = MB_SP = 0  # we need to cancle all mouse inputs
			InvalidateRect(Window, None, False)
			return (0)

		elif switch5 ==  113: # High Score
			DialogBox(hInst, "HighList", Window, (DLGPROC) HSList)
			return (0)

		elif switch5 ==  114: # PlayBack Recording
			BuildPB_Name()
			PBfn.lpstrTitle = txt020
			PBfn.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST
			if (GetOpenFileName( & PBfn)) :
				if (LoadPlayback())
					DialogBox(hInst, "PlayBox", Window, (DLGPROC) PBWindow)
			
			return (0)

		elif switch5 ==  115: # Toggle AutoRecord Option
			if (GetMenuState(MMenu, 115, 0) & MF_CHECKED) :
				CheckMenuItem(MMenu, 115, 0)
				ARecord = False
				WritePrivateProfileString("OPT", psARec, "No", INIFile)
				if (GetMenuState(MMenu, 123, 0) & MF_CHECKED)
					PostMessage(Window, WM_COMMAND, 123, 0)  # Record Off
			else :
				CheckMenuItem(MMenu, 115, MF_CHECKED)
				ARecord = True
				WritePrivateProfileString("OPT", psARec, "Yes", INIFile)
				if ( not (GetMenuState(MMenu, 123, 0) & MF_CHECKED))
					PostMessage(Window, WM_COMMAND, 123, 0)  # Record On
			
			return (0)

		elif switch5 ==  116: # Toggle Skip Complete Levels Option
			ToggleOpt(116, MMenu, & SkipCL, psSCL)
			return (0)

		elif switch5 ==  117:
			if (Recording) PostMessage(Window, WM_SaveRec, 0, 0)  # F6 - Save Rec
			break

		elif switch5 ==  118: # Backspace Level / Last Level Played
			if (Backspace[BS_SP]) :
				Backspace[BS_SP] = 0  # this is so we dont loop around
				BS_SP -= 1
				if (BS_SP < 0)
					BS_SP = 9
				if (Backspace[BS_SP] == 0)
					return (0)  # error
				i = BS_SP - 1
				if (i < 0)
					i = 9
				if (Backspace[i] == 0)
					EnableMenuItem(MMenu, 118, MF_BYCOMMAND | MF_GRAYED)  # Disable Menu Item
				LastLevel = CurLevel
				CurLevel = Backspace[BS_SP] - 1
				if (!LoadNextLevel(True, False))
					CurLevel = LastLevel
			
			return (0)

		elif switch5 ==  119: # Previous Level
			LoadLastLevel()
			return (0)

		elif switch5 ==  120: # small size
			SetGameSize(1)
			InvalidateRect(Window, None, True)
			return (0)

		elif switch5 ==  121: # medium size
			SetGameSize(2)
			InvalidateRect(Window, None, True)
			return (0)

		elif switch5 ==  122: # large size
			SetGameSize(3)
			InvalidateRect(Window, None, True)
			return (0)

		elif switch5 ==  123:
			if (GetMenuState(MMenu, 123, MF_BYCOMMAND) and MF_CHECKED != 0) :
				CheckMenuItem(MMenu, 123, 0)
				Recording = False
				EnableMenuItem(MMenu, 117, MF_GRAYED)
				SetWindowText(MainH, App_Title)
			else :
				CheckMenuItem(MMenu, 123, MF_CHECKED)
				Recording = True
				EnableMenuItem(MMenu, 117, 0)  # enable Save Recording
				SetWindowText(MainH, REC_Title)
			
			return (0)
		elif switch5 ==  124:
			if (CurLevel > 0) # RePlay
			:
				memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD))  # Game.PF = CurRecData.PF
				BuildBMField()
				InvalidateRect(Window, None, False)
				ResetUndoBuffer()  #We don't need the old data
				GameOn(True)
				Game.RecP = 0
			
			return (0)
		elif switch5 ==  125: # Resume Recording
			PBfn.lpstrTitle = txt033
			PBfn.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST
			BuildPB_Name()
			if (GetOpenFileName( & PBfn)) :
				x = LoadPlayback()
				PBOpen = False
				PBHold = False
				if (x) :
					UpdateWindow(Window)
					VHSPlayback()  # Playback File
					SendMessage(MainH, WM_COMMAND, 123, 0)  # Start Recording
				
			
			return (0)
		elif switch5 ==  126: #Print Game Board
			x = Game_On
			GameOn(False)
			Print()
			GameOn(x)
			return (0)
		elif switch5 ==  127: # Disable Warnings
			ToggleOpt(127, MMenu, & DWarn, psDW)
			return (0)
		elif switch5 ==  201: # Editor
			EditorOn = True
			GameOn(False)  # Shut down game engine
			temps = App_Title
			strcat(temps, txt028)
			SetWindowText(Window, temps)  # Change window name
			if (Recording) SendMessage(MainH, WM_COMMAND, 123, 0)
			OKtoHS = False
			SetMenu(Window, EMenu)  # Set up editor menu's
			ShowWindow(BT1, SW_HIDE)
			ShowWindow(BT2, SW_HIDE)
			ShowWindow(BT3, SW_HIDE)
			ShowWindow(BT4, SW_HIDE)
			ShowWindow(BT5, SW_HIDE)
			ShowWindow(BT6, SW_HIDE)
			ShowWindow(BT7, SW_HIDE)
			ShowWindow(BT8, SW_HIDE)
			ShowWindow(BT9, SW_HIDE)
			ShowWindow(Ed1, SW_SHOWNA)  # setup title window
			SetWindowText(Ed1, CurRecData.LName)
			SendMessage(Ed1, EM_SETMODIFY, 0, 0)
			ShowWindow(Ed2, SW_SHOWNA)  # setup Author window
			SendMessage(Ed2, EM_SETMODIFY, 0, 0)
			SetWindowText(Ed2, CurRecData.Author)
			EditDiffSet(CurRecData.SDiff)
			InvalidateRect(Window, None, True)  # redraw in editor mode
			Modified = False
			# Strip off the Tunnel Indexers
			for (x = 0; x < 16; x += 1)
				for (y = 0; y < 16; y += 1)
					if (ISTunnel(x, y)) Game.PF[x][y] &= 0xFE
			if (CurLevel == 0) PostMessage(Window, WM_COMMAND, 601, 0)  # New Level
			return (0)
		elif switch5 ==  225: # Change Difficulty
			x = Game_On
			GameOn(False)
			DialogBox(hInst, "DiffBox", Window, (DLGPROC) DiffBox)
			GameOn(x)
			return (0)
		elif switch5 ==  226: # Graphics Change
			DialogBox(hInst, "GRAPHBOX", Window, (DLGPROC) GraphBox)
			return (0)
		elif switch5 ==  301:
			if (Game_On): # Hint
				GameOn(False)
				if (strlen(CurRecData.Hint) > 0)
					MessageBox(Window, CurRecData.Hint, txt021, MB_OK | MB_ICONINFORMATION)
				else MessageBox(Window, txt035, txt021, MB_OK | MB_ICONHAND)
				GameOn(True)
			
			return (0)
		elif switch5 ==  601: # New Level  [Editor]
			for x in range(0,16):
				for y in range(0,16):
					Game.PF[x][y] = 0
					Game.BMF[x][y] = 1
					Game.BMF2[x][y] = 1
					Game.PF2[x][y] = 0
				
			Game.Tank.X = 7
			Game.Tank.Y = 15
			Game.Tank.Dir = 1
			Game.Tank.Firing = False
			SetWindowText(Ed1, "")
			SendMessage(Ed1, EM_SETMODIFY, 0, 0)
			SetWindowText(Ed2, "")
			SendMessage(Ed2, EM_SETMODIFY, 0, 0)
			CurRecData.Hint[0] = 0  # Clear Out Hint
			InvalidateRect(Window, None, True)
			CurLevel = 1
			Modified = True
			OKtoSave = False
			return (0)
		elif switch5 ==  602: # Load Level [Editor]
			if (SendMessage(Ed1, EM_GETMODIFY, 0, 0) or
				SendMessage(Ed2, EM_GETMODIFY, 0, 0)) Modified = True
			if (Modified)
				if (MessageBox(Window, txt022, txt029, MB_YESNO | MB_ICONQUESTION) == IDYES)
					SendMessage(Window, WM_COMMAND, 603, 0)
			temps = FileName  # Save old name in elif switch5 ==  we cancel
			OFN.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST
			if (GetOpenFileName( & OFN)) :
				i = DialogBox(hInst, "LoadLev", Window, (DLGPROC) LoadBox)
				if (i > 100) :
					i -= 101
					if ( not (F1 := CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
							FILE_FLAG_RANDOM_ACCESS, None))):
						return (0)
					SetFilePointer(F1, i * sizeof(TLEVEL), None, FILE_BEGIN)
					ReadFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, None)
					if (BytesMoved == sizeof(TLEVEL)) :
						SetWindowText(Ed1, CurRecData.LName)
						SendMessage(Ed1, EM_SETMODIFY, 0, 0)
						SetWindowText(Ed2, CurRecData.Author)
						SendMessage(Ed2, EM_SETMODIFY, 0, 0)
						CurLevel = i + 1
						memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD))  # Game.PF = CurRecData.PF
						BuildBMField()
					
					CloseHandle(F1)
					InvalidateRect(Window, None, True)
					OKtoSave = True
				else FileName = temps
			
			return (0)
		elif switch5 ==  603: # Save Level [Editor] 
			if (OKtoSave) :
				F1 = CreateFile(FileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, None, OPEN_ALWAYS,
					FILE_FLAG_RANDOM_ACCESS, None)
				GetWindowText(Ed1, CurRecData.LName, 30)
				GetWindowText(Ed2, CurRecData.Author, 30)
				memcpy(CurRecData.PF, Game.PF, sizeof(TPLAYFIELD))
				CurRecData.PF[Game.Tank.X][Game.Tank.Y] = 1  # save Tank in File
				SetFilePointer(F1, ((CurLevel - 1) * sizeof(TLEVEL)), None, FILE_BEGIN)
				if (WriteFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, None)) :
					Modified = False
					SendMessage(Ed1, EM_SETMODIFY, 0, 0)
					SendMessage(Ed2, EM_SETMODIFY, 0, 0)
				else FileError()
				CloseHandle(F1)
				if (HSClear) :
					AssignHSFile()
					if (F2 = CreateFile(HFileName, GENERIC_WRITE, FILE_SHARE_READ, None, OPEN_EXISTING,
							FILE_FLAG_RANDOM_ACCESS, None)) :
						HS.moves = 0
						SetFilePointer(F2, (CurLevel - 1) * sizeof(THSREC), None, FILE_BEGIN)
						WriteFile(F2, & HS, sizeof(THSREC), & BytesMoved, None)
						CloseHandle(F2)
					
				
			else SendMessage(MainH, WM_COMMAND, 606, 0)  # Save As if new Level
			return (0)
		elif switch5 ==  606: # Save As
			OFN.Flags = OFN_HIDEREADONLY
			if (GetSaveFileName( & OFN)) :
				AssignHSFile()
				F1 = CreateFile(FileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, None, OPEN_ALWAYS,
					FILE_FLAG_RANDOM_ACCESS, None)
				i = DialogBox(hInst, "PickLevel", Window, (DLGPROC) PickBox)
				CloseHandle(F1)
				if (i > 0) :
					CurLevel = i
					OKtoSave = True
					SendMessage(MainH, WM_COMMAND, 603, 0)
				
			
			return (0)
		elif switch5 ==  604: # Leave Editor
			if (SendMessage(Ed1, EM_GETMODIFY, 0, 0) or
				SendMessage(Ed2, EM_GETMODIFY, 0, 0)) Modified = True
			if (Modified)
				if (MessageBox(Window, txt022, txt029, MB_YESNO | MB_ICONQUESTION) == IDYES)
					SendMessage(Window, WM_COMMAND, 603, 0)
			EditorOn = False
			SetWindowText(Window, App_Title)
			SetMenu(Window, MMenu)
			ShowWindow(Ed1, SW_HIDE)
			ShowWindow(Ed2, SW_HIDE)
			ShowWindow(BT1, SW_SHOWNA)
			ShowWindow(BT2, SW_SHOWNA)
			ShowWindow(BT3, SW_SHOWNA)
			ShowWindow(BT4, SW_SHOWNA)
			ShowWindow(BT5, SW_SHOWNA)
			ShowWindow(BT6, SW_SHOWNA)
			ShowWindow(BT7, SW_SHOWNA)
			ShowWindow(BT8, SW_SHOWNA)
			ShowWindow(BT9, SW_SHOWNA)
			memcpy(CurRecData.PF, Game.PF, sizeof(TPLAYFIELD))  # Update CurRec
			CurRecData.PF[Game.Tank.X][Game.Tank.Y] = 1  # save Tank in Playfield's
			InvalidateRect(Window, None, True)
			if (CurLevel > 0) GameOn(True)
			return (0)
		elif switch5 ==  605: # Hint [Editor]
			DialogBox(hInst, "HintBox", Window, (DLGPROC) HintBox)
			return (0)
		elif switch5 ==  701:
			EditDiffSet(1)  # Edit Difficulty Set - Kids
			return (0)
		elif switch5 ==  702:
			EditDiffSet(2)  # Edit Difficulty Set - Easy
			return (0)
		elif switch5 ==  703:
			EditDiffSet(4)  # Edit Difficulty Set - Medium
			return (0)
		elif switch5 ==  704:
			EditDiffSet(8)  # Edit Difficulty Set - Hard
			return (0)
		elif switch5 ==  705:
			EditDiffSet(16)  # Edit Difficulty Set - Deadly
			return (0)
		elif switch5 ==  710: # Shift Game Board Right
			for (x = 1; x < 16; x += 1)
				for (y = 0; y < 16; y += 1) :
					ShiftPF[x][y] = Game.PF[x - 1][y]
					ShiftBMF[x][y] = Game.BMF[x - 1][y]
				
			for (y = 0; y < 16; y += 1) :
				ShiftPF[0][y] = Game.PF[15][y]
				ShiftBMF[0][y] = Game.BMF[15][y]
			
			Game.Tank.X += 1
			if (Game.Tank.X == 16) Game.Tank.X = 0
			Modified = True
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD))  # Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD))  # Update BMF
			InvalidateRect(Window, None, True)
			return (0)
		elif switch5 ==  711: # Shift Game Board Left
			for (x = 0; x < 15; x += 1)
				for (y = 0; y < 16; y += 1) :
					ShiftPF[x][y] = Game.PF[x + 1][y]
					ShiftBMF[x][y] = Game.BMF[x + 1][y]
				
			for (y = 0; y < 16; y += 1) :
				ShiftPF[15][y] = Game.PF[0][y]
				ShiftBMF[15][y] = Game.BMF[0][y]
			
			Game.Tank.X -= 1
			if (Game.Tank.X < 0) Game.Tank.X = 15
			Modified = True
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD))  # Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD))  # Update BMF
			InvalidateRect(Window, None, True)
			return (0)
		elif switch5 ==  712: # Shift Game Board Up
			for (x = 0; x < 16; x += 1)
				for (y = 0; y < 15; y += 1) :
					ShiftPF[x][y] = Game.PF[x][y + 1]
					ShiftBMF[x][y] = Game.BMF[x][y + 1]
				
			for (x = 0; x < 16; x += 1) :
				ShiftPF[x][15] = Game.PF[x][0]
				ShiftBMF[x][15] = Game.BMF[x][0]
			
			Game.Tank.Y -= 1
			if (Game.Tank.Y < 0) Game.Tank.Y = 15
			Modified = True
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD))  # Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD))  # Update BMF
			InvalidateRect(Window, None, True)
			return (0)
		elif switch5 ==  713: # Shift Game Board Down
			for (x = 0; x < 16; x += 1)
				for (y = 1; y < 16; y += 1) :
					ShiftPF[x][y] = Game.PF[x][y - 1]
					ShiftBMF[x][y] = Game.BMF[x][y - 1]
				
			for (x = 0; x < 16; x += 1) :
				ShiftPF[x][0] = Game.PF[x][15]
				ShiftBMF[x][0] = Game.BMF[x][15]
			
			Game.Tank.Y += 1
			if (Game.Tank.Y == 16) Game.Tank.Y = 0
			Modified = True
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD))  # Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD))  # Update BMF
			InvalidateRect(Window, None, True)
			return (0)
		elif switch5 ==  901: # About Box
			x = Game_On
			GameOn(False)
			DialogBox(hInst, "AboutBox", Window, (DLGPROC) AboutBox)
			GameOn(x)
			return (0)
		elif switch5 ==  902: #Help Index 
			WinHelp(Window, HelpFile, HELP_INDEX, 0)
			return (0)
		elif switch5 ==  903: #Help Editor
			WinHelp(Window, HelpFile, HELP_KEY, (DWORD) & help01)
			return (0)
		elif switch5 ==  904: #Revisions History
			WinHelp(Window, HelpFile, HELP_KEY, (long) & help02)
			return (0)
		elif switch5 ==  905: # Help Writing Levels
			WinHelp(Window, HelpFile, HELP_KEY, (long) & help03)
			return (0)
		elif switch5 ==  907: # Quick About Box
			x = Game_On
			GameOn(False)
			QHELP = True
			InvalidateRect(Window, None, False)
			DialogBox(hInst, "RETBOX", Window, (DLGPROC) RetBox)
			QHELP = False
			InvalidateRect(Window, None, False)
			GameOn(x)
			return (0)
		elif switch5 ==  906: #Global high scores list
			DialogBox(hInst, "GHighList", Window, (DLGPROC) GHSList)
			return (0)
		else:
			return (DefWindowProc(Window, Message, wparam, lparam))
		 # Message = (wparam) of WM_COMMAND
	else:
		return (DefWindowProc(Window, Message, wparam, lparam))
	return (0)


# main app entry for windows
# WinMain is the program entry point. When the program starts, it registers some information about the behavior of the application window. One of the most important items is the address of a function, named WindowProc in this example. This function defines the behavior of the window—its appearance, how it interacts with the user, and so forth.
def WinMain( hInstance,
	 hPrevInstance,
	 lpCmdLine,
	 nCmdShow) :
	# MSG msg
	# HANDLE hAccelTable1, hAccelTable2  # keyboard shortcuts / Accelerator Tables
	# tacc
	# char * P

	# Other instances of app running?
	if (not hPrevInstance) :
		# Initialize shared things
		if (not InitApplication(hInstance)):
			return False  # Exits if unable to initialize
	
	hAccelTable1 = LoadAccelerators(hInst, "ACC1")  # Load keyboard shortcuts from ACC1 ACCELERATORS lines in lt32l_us.inc
	hAccelTable2 = LoadAccelerators(hInst, "ACC2")

	# Create Full INI file name
	# Help file name is created in InitInstance()
	#https:#docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea
	GetModuleFileName(None, INIFile, MAX_PATH)
	#Create files working_dir/INIFile, HelpFile, LangFile using INIFileName, LANGFileName
	HelpFile = INIFile
	P = strrchr(INIFile, '\\')  # Find last occurrence of '\\'
	if (P) :
		P += 1
		P = INIFileName  # add name
		if (GetPrivateProfileInt("DATA", psNET, 0, INIFile) == 1):
			INIFile = INIFileName
		else:
			INIFile = INIFileName  # Error so put in Windows Directory

	LANGFile = INIFile  # *dest, *src.*dest
	P = strrchr(LANGFile, '\\')
	if (P) :
		P += 1
		P = LANGFileName  # add name
	else:
			LANGFile = LANGFileName  # Error so put in Default Directory

	# Perform initializations that apply to a specific instance
	if (not InitInstance(hInstance, nCmdShow)):
		return False
	# Get Command line stuff
	if (lpCmdLine[0] != 0) :
		FileName = lpCmdLine
		if (strstr(strlwr(lpCmdLine), ".lvl")) :
			AssignHSFile()
			CurLevel = 0
			LoadNextLevel(False, False)
		
	
	#  Each time the program calls the DispatchMessage function, it indirectly causes Windows to invoke the WindowProc function, once for each message.
	# Acquire and dispatch messages until a WM_QUIT message is received.
	# BOOL GetMessage(
	#  LPMSG lpMsg, A pointer to an MSG structure that receives message information from the thread's message queue.
	#   hWnd, If hWnd is None, GetMessage retrieves messages for any window that belongs to the current thread, and any messages on the current thread...
	#   wMsgFilterMin,
	#   wMsgFilterMax
	# )  #If the function retrieves the WM_QUIT message, the return value is zero.
	#https:#docs.microsoft.com/en-gb/windows/win32/api/winuser/nf-winuser-getmessage
	while (GetMessage( & msg, None, 0, 0)) : # dont translateAccelerators if editor is on

		if (EditorOn):
			tacc = TranslateAccelerator(msg.hwnd, hAccelTable2, msg)  # Editor Accelerator - converts keyboard shortcuts to menu selections, returns 0 if fails
		else:
			tacc = TranslateAccelerator(msg.hwnd, hAccelTable1, msg)

		if (not tacc) :
			TranslateMessage(msg)  # Translates virtual-key messages into character messages
			DispatchMessage(msg)  # Dispatches a message to a window procedure
		
	
	# Window is quitting
	DestroyMenu(EMenu)
	DeleteObject(MyFont)
	# Returns the value from PostQuitMessage
	return msg.wParam


def InitApplication(hInstance):
	# Initialize the Application ( Only once  )
	WNDCLASS wc
	# Fill in window class structure with parameters that describe the
	# main window.
	# lpszClassName is a string that identifies the window class.
	wc.style = CS_BYTEALIGNWINDOW | CS_SAVEBITS
	wc.lpfnWndProc = (WNDPROC) WndProc  # Window Procedure
	#The window procedure defines most of the behavior of the window.
	wc.cbClsExtra = 0  # No per-class extra data.
	wc.cbWndExtra = 0  # No per-window extra data.
	wc.hInstance = hInstance  # Owner of this class
	#hInstance is the handle to the application instance. Get this value from the hInstance parameter of wWinMain.
	wc.hIcon = LoadIcon(hInstance, "icon1")  # Icon name from .RC
	wc.hCursor = LoadCursor(None, IDC_ARROW)  # Cursor, IDC_ARROW=Standard arrow
	wc.hbrBackground = GetStockObject(LTGRAY_BRUSH)  # Default color
	wc.lpszMenuName = "MAIN"  # Menu name from .RC
	wc.lpszClassName = App_Class  # Name to register as
	# lpszClassName is a string that identifies the window class.
	# Register the window class and return False if unsuccesful.
	if (not RegisterClass(wc)):
		return False
	return True


def InitInstance(hInstance, nCmdShow) :
	#  Window  # Main window handle.
	# xp, yp
	# <LangFile>
	# TCHAR * p
	# TCHAR buffer[50]
	# </LangFile>

	hInst = hInstance  # Store instance handle in our global variable
	xp = GetPrivateProfileInt("SCREEN", psXpos, CW_USEDEFAULT, INIFile)  # Getting from INI file
	yp = GetPrivateProfileInt("SCREEN", psYpos, CW_USEDEFAULT, INIFile)
	# Create a main window for this application instance.
	Window = CreateWindow(App_Class, App_Title,
		WS_OVERLAPPEDWINDOW & ~(WS_SIZEBOX | WS_MAXIMIZEBOX),
		xp, yp, 725, 579, 0, 0, hInst, None)  #className, windowName, windowStyle, 
	#window position xy, width (includes window borders), height, parent, menu, instance, parameter to pass
	if (not Window):
		return False
	MainH = Window
	MMenu = GetMenu(Window)
	OFN.hwndOwner = Window
	PBfn.hwndOwner = Window
	EMenu = LoadMenu(hInst, "MENU2")

	# ************************************************************************
	# Read the language file is exist
	# fill the LANGText[],
	# update the two menus,
	# ************************************************************************
	# <LangFile>
	InitLanguage(MMenu, EMenu)

	# Buit HelpFile file name here, after InitLanguage()
	p = strrchr(HelpFile, '\\')
	if (p) :
		p += 1
		p = HelpFileName  # add name
	else:
		HelpFile = HelpFileName  # Error so put in Default Directory

	# Build up the correct filter strings for OPENFILENAME structure
	p = szFilterOFN
	lstrcpy(buffer, txt002)
	lstrcpy(p, buffer)
	p += lstrlen(buffer) + 1
	lstrcpy(buffer, TEXT("*.LVL"))
	lstrcpy(p, buffer)
	p += lstrlen(buffer) + 1
	strcpy(p, TEXT(""))
	OFN.lpstrFilter = szFilterOFN

	# Build up the correct filter strings for OPENFILENAME structure
	p = szFilterPBfn
	lstrcpy(buffer, txt005)
	lstrcpy(p, buffer)
	p += lstrlen(buffer) + 1
	lstrcpy(buffer, TEXT("*.LPB"))
	lstrcpy(p, buffer)
	p += lstrlen(buffer) + 1
	strcpy(p, TEXT(""))
	PBfn.lpstrFilter = szFilterPBfn
	# </LangFile>

	#############################################################################

	#CREATE MAIN BUTTONS

	#   CreateWindow(
	#  LPCTSTR lpClassName, pointer to registered class name
	#  LPCTSTR lpWindowName,  pointer to window name
	#  DWORD dwStyle,     window style
	#  x,         horizontal position of window
	#  y,         vertical position of window
	#  nWidth,        window width
	#  nHeight,     window height
	#   hWndParent,   handle to parent or owner window
	#  HMENU hMenu,     handle to menu or child-window identifier
	#  HANDLE hInstance,    handle to application instance
	#  LPVOID lpParam     pointer to window-creation data
	#  )
	# https:#docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowa
	############################################################################

	# Title Edit Box - Visable only in Editor Mode
	Ed1 = CreateWindow(
		"EDIT",
		"",
		WS_CHILD | WS_BORDER | ES_LEFT | ES_AUTOHSCROLL,
		418,
		99,
		163,
		20,
		Window,
		(HMENU) 501,
		hInst,
		None)
	# Author Edit Box - Visable only in Editor Mode 
	Ed2 = CreateWindow(
		"EDIT",
		"",
		WS_CHILD | WS_BORDER | ES_LEFT | ES_AUTOHSCROLL,
		418,
		148,
		163,
		20,
		Window,
		(HMENU) 502,
		hInst,
		None)

	BT1 = CreateWindow(
		"BUTTON",
		ButText1,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON | WS_DISABLED,
		418,
		260,
		70,
		20,
		Window,
		(HMENU) ButID1,
		hInst,
		None)
	BT2 = CreateWindow("BUTTON",
		ButText2,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON | WS_DISABLED,
		418,
		280,
		145,
		20,
		Window,
		(HMENU) ButID2,
		hInst,
		None)
	BT3 = CreateWindow("BUTTON",
		ButText3,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON | WS_DISABLED,
		418,
		280,
		145,
		20,
		Window,
		(HMENU) ButID3,
		hInst,
		None)
	BT4 = CreateWindow("BUTTON",
		ButText4,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		418,
		280,
		70,
		20,
		Window,
		(HMENU) ButID4,
		hInst,
		None)

	BT5 = CreateWindow("BUTTON",
		ButText5,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		418,
		280,
		70,
		20,
		Window,
		(HMENU) ButID5,
		hInst,
		None)
	BT6 = CreateWindow("BUTTON",
		ButText6,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		418,
		280,
		70,
		20,
		Window,
		(HMENU) ButID6,
		hInst,
		None)

	BT7 = CreateWindow("BUTTON",
		ButText7,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON | WS_DISABLED,
		418,
		280,
		70,
		20,
		Window,
		(HMENU) ButID7,
		hInst,
		None)
	BT8 = CreateWindow("BUTTON",
		ButText8,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON | WS_DISABLED,
		418,
		280,
		70,
		20,
		Window,
		(HMENU) ButID8,
		hInst,
		None)
	BT9 = CreateWindow("BUTTON",
		ButText9,
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		418,
		280,
		145,
		20,
		Window,
		(HMENU) ButID9,
		hInst,
		None)

	MyFont = CreateFont(16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Arial")
	SetGameSize(GetPrivateProfileInt("SCREEN", psSize, 1, INIFile))
	ShowWindow(Window, nCmdShow)  # Show the window
	UpdateWindow(Window)  # Sends WM_PAINT message
	return True  # We succeeded...



# ltank2.c
"""******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 ******************************************************"""

#include <windows.h>

#include <windowsx.h>

#include <commdlg.h>

#include <string.h>

#include <mmsystem.h>

#include <stdio.h>

#include "ltank.h"

#include "ltank_d.h"

#include "lt_sfx.h"

# Declare the Global Varables

GFXError = 0  # error used for load
GFXOn = False  # True when Graphics are loaded
TankDirty = False  # if true then we need to repaint the tank
NoLevel = True  # if true Main Paint will show Openning
Game_On = False  # true when game is running
Ani_On = True  # true when Animation is On
RLL = True  # remember last level
ConvMoving = False  # true when moving on the conveyor belts
OKtoHS = True  # true if OK to Set HighScore
OKtoSave = False  # true if OK to Set HighScore
Recording = False  # true if Recording
PlayBack = False  # true if PlayBack is recording
PBOpen = False  # true when Playback window is open
ARecord = False  # AutoRecord is On/Off
SkipCL = False  # true if Skip Complete Level is on
DWarn = False  # Disable Warning
CurLevel = 0  # Used to Figure out the Current Level
AniLevel = 0  # Used for Animation Position, Animation frame 0, 1, 2
AniCount = 0  # counter for animation, Counts ticks between animating. When AniCount += 1 reaches ani_delay ticks then animate & AniCount=0
CurSelBM_L = 3  # current selected bm in editor
CurSelBM_R = 0  # current selected bm in editor
SpBm_Width = 32  # Width of Sprite
SpBm_Height = 32  # Height of Sprite
LaserOffset = 10  # Offset of Laser Size
ContXPos = 540  # Position of Control Side
EditBMWidth = 5  # # of bitmaps across edit select area
Speed = 1  # Playback speed
SlowPB = 1  #Delay counter to slow down animation when Speed==2
RecBufSize = 10000  # Size of recording buffer
UndoBufSize = 3200  # Size of Undo Buffer ( * sizeof(TGAMEREC))
Difficulty = 0  # Difficulty Enable ( use Bits )
GraphM = 0  # Graphics Mode 0=int; 1=ext; 2=ltg
FindTank = False  # True when First starting a level, used to draw target lines on tank when first loading level
BlackHole = False  # True if we TunnleTranslae to a Black Hole (no exit found)

# TGAMEREC Game, SaveGame  # The Level Data
# TLEVEL CurRecData
# HBRUSH LaserColor, LaserColorR, LaserColorG
# HDC gDC  # Use this game dc for all ops - set in WM_PAINT gDC = BeginPaint(Window, &PI)
# char FileName[MAX_PATH]  #Default = LevelData = 'LaserTank.lvl' (WM_CREATE)
# char HFileName[MAX_PATH]  #Default = 'LaserTank.hs' (AssignHSFile())
# char GHFileName[MAX_PATH]  #Default = 'LaserTank.ghs' (AssignHSFile())
# char PBFileName[MAX_PATH]  #Default = 'LaserTank_0000.lpb' (AssignHSFile())
# char GraphFN[MAX_PATH], GraphDN[MAX_PATH], INIFile[MAX_PATH]
# Modified
# TICEREC SlideO, SlideT
# TICEMEM SlideMem  # MGY - mem up MAX_TICEMEM sliding objects
# wasIce  # CheckLoc will set this to true if currently on Ice/ThinIce
# WaitToTrans  #Found tunnel output on PF2 (under something)

# # Global Varables

# TXYREC BMA[MaxBitMaps + 1]  # Bit Map Array
# TTANKREC laser
# HDC BuffDC, MaskDC  # used to bitblat all sprites
# HBITMAP BuffBMH, MaskBMH  # Handle to Bitmaps in above DC's
GetOBMArray = [
	1,
	2,
	6,
	9,
	13,
	14,
	15,
	16,
	36,
	39,
	42,
	20,
	21,
	22,
	23,
	24,
	27,
	30,
	33,
	45,
	47,
	48,
	49,
	50,
	56,
	57,
	55,
]

CheckArray = [
	1,
	0,
	1,
	1,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	1,
	1,
	1,
	1,
	0,
	0,
	0,
	0,
	0,
	1,
	1,
]
	#Can tank move into square with this ID?
# Pad the beggining with junk array was [1..MaxBitMaps]
# Flag used in Bliting sprites to show if mask needs to be applied
BMSTA = [
	0,
	0,
	1,
	1,
	1,
	1,
	0,
	0,
	0,
	0,
	0,
	0,
	1,
	0,
	1,
	0,
	1,
	1,
	1,
	0,
	1,
	1,
	1,
	1,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	1,
	1,
	1,
	1,
	1,
	1,
	1,
	1,
	1,
	0,
	0,
	0,
	0,
	0,
	0,
	0,
	1,
	1,
	1,
	0,
	0,
	0,
]

ColorList = [
	0x000000FF,
	0x0000FF00,
	0x00FF0000,
	0x00FFFF00,
	0x00FFFF,
	0x00FF00FF,
	0x00FFFFFF,
	0x00808080,
]

# UndoP
# TRECORDREC PBRec, PBSRec
# char * RecBuffer
# PGAMEREC UndoBuffer
# THSREC HS
# HANDLE F1, F2, F3  #Files created at level load
# DWORD BytesMoved
# TXYZREC MBuffer[MaxMBuffer]
# MB_TOS, MB_SP  # TOS = Top of Stack ; SP = Stack Pointer
# findmap[16][16]

# Backspace[10]  # Backspace Buffer. History of last 10 levels to cycle back to with the backspace key
# BS_SP = 0  # StackPointer for Backspace
# UndoRollOver

# # Local function declaration

# def SetButtons(int)
# def SpriteLoad
static void FindTarget(int, int, int)

#
# Start the code section
#

#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
# Move   a Sliding Object FROM stack
#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
def Mem_to_SlideO(iSlideObj): # MGY
	if (iSlideObj <= SlideMem.count) :
		SlideO.x = SlideMem.Objects[iSlideObj].x
		SlideO.y = SlideMem.Objects[iSlideObj].y
		SlideO.dx = SlideMem.Objects[iSlideObj].dx
		SlideO.dy = SlideMem.Objects[iSlideObj].dy
		SlideO.s = SlideMem.Objects[iSlideObj].s
	


#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
# Move a Sliding Object ON TO stack
# Update SlideMem with an object SlideO
#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
def SlideO_to_Mem(iSlideObj): # MGY
	if (iSlideObj <= SlideMem.count) :
		SlideMem.Objects[iSlideObj].x = SlideO.x
		SlideMem.Objects[iSlideObj].y = SlideO.y
		SlideMem.Objects[iSlideObj].dx = SlideO.dx
		SlideMem.Objects[iSlideObj].dy = SlideO.dy
		SlideMem.Objects[iSlideObj].s = SlideO.s
	


#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
# Add an object in the stack for slidings objects
# But, if this object is already in this stack,
# just change dir and don't increase the counter.
#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
def add_SlideO_to_Mem(): # MGY
	if (SlideMem.count < MAX_TICEMEM - 1) :
		for iSlideObj in range(1,SlideMem.count+1):
			if ((SlideMem.Objects[iSlideObj].x == SlideO.x) and (SlideMem.Objects[iSlideObj].y == SlideO.y)) :
				SlideO_to_Mem(iSlideObj)  # Update the stack
				return  # don't inc the counter
			
		
		# Add this object to the stack
		SlideMem.count += 1
		SlideO_to_Mem(SlideMem.count)
		SlideO.s = (SlideMem.count > 0)
	


#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
# Delete a Sliding Object from stack
#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
def sub_SlideO_from_Mem(iSlideObj): # MGY
	for i in range(iSlideObj,SlideMem.count) :
		Mem_to_SlideO(i + 1)
		SlideO_to_Mem(i)
	
	SlideMem.count -= 1
	SlideO.s = (SlideMem.count > 0)


#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
# If an object is sliding and is hit by a laser,
# delete it from stack. (Done before adding new slide direction to stack.)
#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
def del_SlideO_from_Mem(x, y): # MGY
	for iSlideObj in range(SlideMem.count,0,-1) :
		if ((SlideMem.Objects[iSlideObj].x == x) and (SlideMem.Objects[iSlideObj].y == y)) :
			# remove this object
			sub_SlideO_from_Mem(iSlideObj)
			return  
	SlideO.s = (SlideMem.count > 0)


#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
# Used to handle a bug :  the speed bug
# MGY - 22-nov-2002
# Return True if the tank is on Convoyor.
#  ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ -= 1-
def TestIfConvCanMoveTank() :
	switch0 =  (Game.PF[Game.Tank.X][Game.Tank.Y]) :
	if switch0 ==  15:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1)): # Conveyor Up
			return (True)
	elif switch0 ==  16:
		if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y)):
			return (True)
	elif switch0 ==  17:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1)):
			return (True)
	elif switch0 ==  18:
		if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y)):
			return (True)

	return (False)


def SetButtons(ButtonX) :
	EnableWindow(BT1, (ButtonX & 1) == 1)
	EnableWindow(BT2, (ButtonX & 2) == 2)
	EnableWindow(BT3, (ButtonX & 4) == 4)
	EnableWindow(BT4, (ButtonX & 8) == 8)
	EnableWindow(BT5, (ButtonX & 16) == 16)
	EnableWindow(BT6, (ButtonX & 32) == 32)
	EnableWindow(BT7, (ButtonX & 64) == 64)
	EnableWindow(BT8, (ButtonX & 128) == 128)


def FileError() :
	LPVOID lpMsgBuf

	FormatMessage(
		FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
		None,
		GetLastError(),
		MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), # Default language
		(LPTSTR) & lpMsgBuf,
		0, None)
	# Display the string.
	MessageBox(MainH, lpMsgBuf, "System Error", MB_OK | MB_ICONINFORMATION)
	# Free the buffer.
	LocalFree(lpMsgBuf)


# 32  SPACEBAR
# 33  PAGE UP
# 34  PAGE DOWN
# 35  END
# 36  HOME
# 37  LEFT ARROW
# 38  UP ARROW
# 39  RIGHT ARROW
# 40  DOWN ARROW
def AddKBuff(zz) :
	#Append key number to RecBuffer[] at RB_TOS (top of stack)
	#Increment RB_TOS

	RecBuffer[RB_TOS] = zz
	RB_TOS += 1

	# Top of stack pointer is greater than rec buffer, realloc
	if (RB_TOS >= RecBufSize) :
		i = RecBufSize + RecBufStep
		RecBuffer = GlobalReAlloc(RecBuffer, i, GMEM_MOVEABLE)
		if (RecBuffer == None) : # Recorder Buffer Overflow
			FileError()
			if (Recording):
				SendMessage(MainH, WM_SaveRec, 0, 0)
			RB_TOS = 0
		else:
			RecBufSize = i
	


""" find the shortest path to the target via a fill search algorithm """
def FindTarget(px, py, pathlen) :
	if ((px < 0) or (px > 15) or (py < 0) or (py > 15)):
		return  # outer edges
	# if we hit something AND we are not at the tank then return
	if ((Game.PF[px][py] != 0) and ( not ((Game.Tank.X == px) and (Game.Tank.Y == py)))):
		return  # we hit something - ouch

	if (findmap[px][py] <= pathlen):
		return

	findmap[px][py] = pathlen += 1

	if ((px == Game.Tank.X) and (py == Game.Tank.Y)):
		return  # speed's us up

	FindTarget(px - 1, py, pathlen)
	FindTarget(px + 1, py, pathlen)
	FindTarget(px, py - 1, pathlen)
	FindTarget(px, py + 1, pathlen)


def MouseOperation(sp) :
	dx = MBuffer[sp].X - Game.Tank.X
	dy = MBuffer[sp].Y - Game.Tank.Y
	XBigger = abs(dx) > abs(dy)  # true if x is bigger than y

	if (MBuffer[sp].Z == 1): #Left mouse button clicked
		# Mouse Move
		""" Fill the trace map """
		for cx in range(16):
			for cy in range(16):
				findmap[cx][cy] = BADMOVE
		# We will test the destination manually
		dx = Game.PF[MBuffer[sp].X][MBuffer[sp].Y]  # temp store in dx
		if ( not ((dx < 3) or ((dx > 14) and (dx < 19)) or
				(dx > 23) or ((Obj_Tunnel & dx) == Obj_Tunnel))):
			return (False)
		findmap[MBuffer[sp].X][MBuffer[sp].Y] = 0  # destination
		""" flood fill search to find a shortest path to the push point. """
		FindTarget(MBuffer[sp].X - 1, MBuffer[sp].Y, 1)
		FindTarget(MBuffer[sp].X + 1, MBuffer[sp].Y, 1)
		FindTarget(MBuffer[sp].X, MBuffer[sp].Y - 1, 1)
		FindTarget(MBuffer[sp].X, MBuffer[sp].Y + 1, 1)

		""" if we didn't make it back to the players position, there is no valid path
		 * to that place.
		"""
		if (findmap[Game.Tank.X][Game.Tank.Y] == BADMOVE) :
			return (False)
		else :
			""" we made it back, so let's walk the path we just built up """
			cx = Game.Tank.X
			cy = Game.Tank.Y
			ltdir = Game.Tank.Dir  # we need to keep track of direction
			while (findmap[cx][cy]) :
				if ((cx > 0) and (findmap[cx - 1][cy] == (findmap[cx][cy] - 1))) :
					if (ltdir != 4):
						AddKBuff(VK_LEFT)
					AddKBuff(VK_LEFT)
					cx -= 1
					ltdir = 4
				elif ((cx < 15) and (findmap[cx + 1][cy] == (findmap[cx][cy] - 1))) :
					if (ltdir != 2):
						AddKBuff(VK_RIGHT)
					AddKBuff(VK_RIGHT)
					cx += 1
					ltdir = 2
				elif ((cy > 0) and (findmap[cx][cy - 1] == (findmap[cx][cy] - 1))) :
					if (ltdir != 1):
						AddKBuff(VK_UP)
					AddKBuff(VK_UP)
					cy -= 1
					ltdir = 1
				elif ((cy < 15) and (findmap[cx][cy + 1] == (findmap[cx][cy] - 1))) :
					if (ltdir != 3):
						AddKBuff(VK_DOWN)
					AddKBuff(VK_DOWN)
					cy += 1
					ltdir = 3
				else :
					""" if we get here, something is SERIOUSLY wrong, so we should abort """
					print(" if we get here, something is SERIOUSLY wrong, so we should abort ")
					exit()
	else :
		# Mouse Shot / Right mouse button clicked
		if (XBigger) :
			if (dx > 0) :
				if (Game.Tank.Dir != 2) AddKBuff(VK_RIGHT)  # Turn Right
			 elif (Game.Tank.Dir != 4) AddKBuff(VK_LEFT)  # Turn Left
		else :
			if (dy > 0) :
				if (Game.Tank.Dir != 3) AddKBuff(VK_DOWN)  # Turn Down
			 elif (Game.Tank.Dir != 1) AddKBuff(VK_UP)  # Turn Up
		
		AddKBuff(VK_SPACE)
	
	return (True)


def InitBuffers() :

	UndoP = 0
	UndoBuffer = GlobalAlloc(GMEM_FIXED, UndoBufSize * sizeof(TGAMEREC))  # Undo Buffer
	RecBuffer = GlobalAlloc(GMEM_FIXED, RecBufSize)  # Recording Buffer
	Backspace[BS_SP] = 0  # Clear Backspace stack
	MB_TOS = MB_SP = 0
	SlideT.s = 0  # nothing sliding
	SlideO.s = 0
	SlideMem.count = 0  # MGY

	UndoRollOver = UndoMax


def ResetUndoBuffer():
	# Reset Undo Buffer to 1 block only; all variable = 0
	UndoBuffer = GlobalReAlloc(UndoBuffer, UndoBufStep * sizeof(TGAMEREC), GMEM_MOVEABLE)
	if (UndoBuffer == None) : # Undo Buffer Allocation Error
		FileError()
	
	UndoBufSize = UndoBufStep
	UndoP = 0
	UndoBuffer.Tank.Dir = 0
	# Lets also init the Mouse Buffer
	MB_TOS = MB_SP = 0


def KillBuffers() :
	GlobalFree(UndoBuffer)
	GlobalFree(RecBuffer)


def UpdateUndo(): # Come here whenever we move or shoot
	
	UndoP += 1
	if (UndoP >= UndoBufSize) :
		if (UndoP >= UndoMax) :
			UndoRollOver = (UndoP - 1)  # Save Where we rolled Over
			UndoP = 0
		else :
			i = UndoBufSize + UndoBufStep
			tmpUndoArray = GlobalReAlloc(UndoBuffer, i * sizeof(TGAMEREC), GMEM_MOVEABLE)
			if (tmpUndoArray == None) : # Undo Buffer Allocation Error
				MessageBox(MainH, txt019, txt007, MB_OK | MB_ICONERROR)
				UndoRollOver = (UndoP - 1)  # Save Where we rolled Over
				UndoP = 0
			else :
				UndoBufSize = i
				UndoBuffer = tmpUndoArray
		
	UndoBuffer[UndoP] = Game
	EnableMenuItem(MMenu, 110, MF_BYCOMMAND | MF_ENABLED)  # enable Undo Command
	EnableWindow(BT1, SW_SHOWNA)


def UndoStep() :
	if (UndoBuffer[UndoP].Tank.Dir == 0):
		return  # out of data
	Game = UndoBuffer[UndoP]
	RB_TOS = Game.RecP  # clear all keys not processed
	SlideT.s = 0  # stop any sliding
	SlideO.s = 0
	SlideMem.count = 0  # MGY
	UndoBuffer[UndoP].Tank.Dir = 0
	UndoP -= 1
	if (UndoP < 0) :
		UndoP = UndoRollOver
	
	MB_TOS = 0
	MB_SP = 0  # we need to cancle all mouse inputs


def PutSprite(bmn, x, y):
	# paint sprite ( bitmap ) at screen location x,y
	# add grass behind if transparent
	if (BMSTA[bmn] == 1) :
		BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, BuffDC, BMA[1].X, BMA[1].Y, SRCCOPY)
		SetTextColor(gDC, RGB(0, 0, 0))
		SetBkColor(gDC, RGB(255, 255, 255))
		BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, MaskDC, BMA[bmn].X, BMA[bmn].Y, SRCAND)
		BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCPAINT)
	else:
		BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCCOPY)


def UpDateSprite(x, y):
	# re-paint sprite at Game Board Location x,y
	
	bmn = Game.BMF[x][y]
	x1 = XOffset + (x * SpBm_Width)
	y1 = YOffset + (y * SpBm_Height)

	# Draw top layer
	if (bmn == 55): # 55 is tunnel
		Bpen = CreateSolidBrush(ColorList[GetTunnelID(x, y)])
		penO = SelectObject(gDC, Bpen)
		Rectangle(gDC, x1, y1, x1 + SpBm_Width, y1 + SpBm_Height)  # Fill cell with coloured rectangle of TunnelID colour
		SetTextColor(gDC, RGB(0, 0, 0))
		SetBkColor(gDC, RGB(255, 255, 255))
		BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, MaskDC, BMA[55].X, BMA[55].Y, SRCAND)  # Draw tunnel with transparency
		BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[55].X, BMA[55].Y, SRCPAINT)
		SelectObject(gDC, penO)
		DeleteObject(Bpen)
	else :
		if (BMSTA[bmn] == 1): # Sprite has a transparency mask
			# Draw bottom layer
			bmn2 = Game.BMF2[x][y]

			if (bmn2 == 55): # 55 is tunnel - If bottom layer is a tunnel
				Bpen = CreateSolidBrush(ColorList[((Game.PF2[x][y] & 0x0F) >> 1)])
				penO = SelectObject(gDC, Bpen)
				Rectangle(gDC, x1, y1, x1 + SpBm_Width, y1 + SpBm_Height)
				SetTextColor(gDC, RGB(0, 0, 0))
				SetBkColor(gDC, RGB(255, 255, 255))
				BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, MaskDC, BMA[55].X, BMA[55].Y, SRCAND)
				BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[55].X, BMA[55].Y, SRCPAINT)
				SelectObject(gDC, penO)
				DeleteObject(Bpen)
			else:
				BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn2].X, BMA[bmn2].Y, SRCCOPY)

			SetTextColor(gDC, RGB(0, 0, 0))
			SetBkColor(gDC, RGB(255, 255, 255))
			BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, MaskDC, BMA[bmn].X, BMA[bmn].Y, SRCAND)  # Draw mask
			BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCPAINT)  # Draw sprite
		else:
			BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCCOPY)  # Draw sprite
	


def UpDateTank():
	# paint mask then tank sprite, we mask the cell so the back ground will show
	TankDirty = False
	SetTextColor(gDC, RGB(0, 0, 0))
	SetBkColor(gDC, RGB(255, 255, 255))
	BitBlt(gDC, XOffset + (Game.Tank.X * SpBm_Width), YOffset + (Game.Tank.Y * SpBm_Height),
		SpBm_Width, SpBm_Height, MaskDC, BMA[1 + Game.Tank.Dir].X, 0, SRCAND)
	BitBlt(gDC, XOffset + (Game.Tank.X * SpBm_Width), YOffset + (Game.Tank.Y * SpBm_Height),
		SpBm_Width, SpBm_Height, BuffDC, BMA[1 + Game.Tank.Dir].X, 0, SRCPAINT)


# Draw laser (not deflecting)
def UpDateLaser():
# paint laser
	
	ob = SelectObject(gDC, LaserColor)
	x = XOffset + (laser.X * SpBm_Width)
	y = YOffset + (laser.Y * SpBm_Height)
	if ((laser.Dir & 1) == 1):
		Rectangle(gDC, x + LaserOffset, y, x + SpBm_Width - LaserOffset, y + SpBm_Height)
	else:
		Rectangle(gDC, x, y + LaserOffset, x + SpBm_Width, y + SpBm_Height - LaserOffset)
	SelectObject(gDC, ob)


# Did laser just hit a moving mirror? Let the laser move again.
LaserBounceOnIce = False

# Draw laser bouncing off a mirror from direction a to direction b. Also set LaserBounceOnIce if object moving
def UpDateLaserBounce(a, b) :
	ob = SelectObject(gDC, LaserColor)
	x = XOffset + (laser.X * SpBm_Width)
	y = YOffset + (laser.Y * SpBm_Height)
	h = SpBm_Width / 2

	# we need to stop advance the LaserShot if sliding on ice & hit
	for (iSlideObj = 1; iSlideObj <= SlideMem.count; iSlideObj += 1) # MGY
		# MGY
		if (SlideMem.Objects[iSlideObj].s and
			(SlideMem.Objects[iSlideObj].x == laser.X) and
			(SlideMem.Objects[iSlideObj].y == laser.Y)) LaserBounceOnIce = True
	#if (SlideO.s and (SlideO.x == laser.X) and (SlideO.y == laser.Y)) LaserBounceOnIce = True

	# Draw two parts of the reflecting laser
	if a ==  1:
		Rectangle(gDC, x + LaserOffset, y + h, x + SpBm_Width - LaserOffset, y + SpBm_Height)
	elif a ==  2:
		Rectangle(gDC, x, y + LaserOffset, x + h, y + SpBm_Height - LaserOffset)
	elif a ==  3:
		Rectangle(gDC, x + LaserOffset, y, x + SpBm_Width - LaserOffset, y + h)
	elif a ==  4:
		Rectangle(gDC, x + h, y + LaserOffset, x + SpBm_Width, y + SpBm_Height - LaserOffset)

	if b ==  1:
		Rectangle(gDC, x + LaserOffset, y, x + SpBm_Width - LaserOffset, y + h)
	elif b ==  2:
		Rectangle(gDC, x + h, y + LaserOffset, x + SpBm_Width, y + SpBm_Height - LaserOffset)
	elif b ==  3:
		Rectangle(gDC, x + LaserOffset, y + h, x + SpBm_Width - LaserOffset, y + SpBm_Height)
	elif b ==  4:
		Rectangle(gDC, x, y + LaserOffset, x + h, y + SpBm_Height - LaserOffset)
	
	SelectObject(gDC, ob)


def PutLevel():
	# paint all game cells and the tank
	
	for y in range(16):
		for x in range(16):
			UpDateSprite(x, y)
	UpDateTank()
	TankDirty = False

	if (FindTank): # Newly loaded level so draw target lines to tank
		# Draws red horizontal and vertical lines from tank when level fir
		ob = SelectObject(gDC, LaserColorR)
		SelectObject(gDC, GetStockObject(None_PEN))
		x = XOffset + (Game.Tank.X * SpBm_Width)
		y = YOffset + (Game.Tank.Y * SpBm_Height)
		Rectangle(gDC, x + LaserOffset, YOffset + 2, x + SpBm_Width - LaserOffset, YOffset + (16 * SpBm_Height))
		Rectangle(gDC, XOffset + 2, y + LaserOffset, XOffset + (16 * SpBm_Width), y + SpBm_Height - LaserOffset)
		SelectObject(gDC, ob)
	


def LoadBitmapFile(dc,FileName):
	# Load a WIndows style Bitmap file

	bm = 0  # set error
	F = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
		FILE_FLAG_SEQUENTIAL_SCAN, None)
	if (F == INVALID_HANDLE_VALUE):
		return (0)  # File not found
	ReadFile(F, Header, sizeof(Header), BytesMoved, None)
	
	if ((BytesMoved != sizeof(Header)) or (Header.bfType != 0x4d42)):
		CloseHandle(F)
		return (bm)


	Size = SetFilePointer(F, 0, None, FILE_END) - sizeof(Header)  # Size = filesize(F) - Sizeof(header)
	SetFilePointer(F, sizeof(Header), None, FILE_BEGIN)  # Reset File Position
	P = GlobalAlloc(GMEM_FIXED, Size)  # Get Big lump of Memory
	
	if (P == 0):
		CloseHandle(F)  # Memory Error
		return (bm)

	# This only works with 32bit LCC if size > 65K
	if ( not (ReadFile(F, P, Size, BytesMoved, None))):
		FileError()

	if (P.bmiHeader.biSize == sizeof(BITMAPINFOHEADER)) :
		n = Header.bfOffBits - sizeof(BITMAPFILEHEADER)  #Compute image Location
		P2 = P + n
		bm = CreateDIBitmap(dc, (LPBITMAPINFOHEADER) P, CBM_INIT, P2, P, DIB_RGB_COLORS)
	
	GlobalFree(P)
	CloseHandle(F)
	return (bm)


def LoadBitmapMem(dc, Header):
# Load a WIndows style Bitmap from a memory block
	
	if (Header.bfType != 0x4d42):
		return (0)

	P = Header + sizeof(BITMAPFILEHEADER)

	if (P.bmiHeader.biSize == sizeof(BITMAPINFOHEADER)) :
		P2 = Header + Header.bfOffBits
		bm = CreateDIBitmap(dc, (LPBITMAPINFOHEADER) P, CBM_INIT, P2, P, DIB_RGB_COLORS)
		return (bm)
	
	return (0)


def LoadLTG(dc, GH, MH, FN) :
	if ((F = CreateFile(FN, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, None)) == INVALID_HANDLE_VALUE):
		return (0)
	LTSize = SetFilePointer(F, 0, None, FILE_END)
	SetFilePointer(F, 0, None, FILE_BEGIN)

	if ( not (ReadFile(F, & tmpLTG, sizeof(TLTGREC), & BytesMoved, None))):
		FileError()
	if (tmpLTG.ID != LTG_ID) :
		MessageBox(MainH, txt031, txt007, MB_OK | MB_ICONERROR)
		return (False)
	
	GSize = tmpLTG.MaskOffset - sizeof(TLTGREC)
	MSize = LTSize - tmpLTG.MaskOffset

	# transfer game bitmap from Filename.GH
	P = GlobalAlloc(GMEM_FIXED, GSize)  # Get Big lump of Memory
	if (P != 0) :
		if ( not (ReadFile(F, P, GSize, & BytesMoved, None))):
			FileError()
		GH = LoadBitmapMem(dc, P)
	
	GlobalFree(P)

	# transfer Mask bitmap from Filename.MH
	P = GlobalAlloc(GMEM_FIXED, MSize)  # Get Big lump of Memory
	if (P != 0) :
		if ( not (ReadFile(F, P, MSize, & BytesMoved, None))):
			FileError()
		MH = LoadBitmapMem(dc, P)
	
	GlobalFree(P)
	CloseHandle(F)
	return (True)


# Load All the Bitmaps
def GFXInit() :
	HDC dc, tdc
	HBITMAP Gh, Mh, xh2
	x, y, i

	SetCurrentDirectory(GraphDN)
	dc = GetDC(MainH)  # Get device context for drawing on

	BuffDC = CreateCompatibleDC(dc)  # DC for All Sprites
	MaskDC = CreateCompatibleDC(dc)  # DC for all Masks  -= 1 same size as Sprites

	tdc = CreateCompatibleDC(dc)  # Temp DC
	# GraphM = Graphics Mode 0=int; 1=ext; 2=ltg
	if (GraphM == 1): # External
		Gh = 0  # need this if error
		Mh = LoadBitmapFile(dc, MASK_BMP)
		if (Mh) Gh = LoadBitmapFile(dc, GAME_BMP)
		if ( not (Mh or Gh)) GraphM = 0  # Error so Set Mode 0 - Internal
	elif (GraphM == 2): # LTG
		if ( not (LoadLTG(dc, & Gh, & Mh, GraphFN))):
			GraphM = 0
	
	if (GraphM == 0): # Internal Graphics are used
		Mh = LoadBitmap(hInst, "MASKBM")
		if (Mh):
			Gh = LoadBitmap(hInst, "GAMEBM")
	
	if ( not (Mh or Gh)): # last chance error check
		GFXError = 1
		if (GFXError != 0):
			MessageBox(0, "Graphics Loading Error", txt007, MB_OK | MB_ICONERROR)
		return
	
	# Create Mask Bitmap; Sized Properly for Screen
	SelectObject(MaskDC, Mh)  # This sets up the B&W
	MaskBMH = CreateCompatibleBitmap(MaskDC, SpBm_Width * 10, SpBm_Height * 6)
	SelectObject(MaskDC, MaskBMH)  # Put New Blank Bitmap in MaskDC
	xh2 = SelectObject(tdc, Mh)  # Hold Old Value
	# Copy Bitmap to new size into MaskDC
	StretchBlt(MaskDC, 0, 0, SpBm_Width * 10, SpBm_Height * 6, tdc, 0, 0, 320, 192, SRCCOPY)
	SelectObject(tdc, xh2)  # Restore Old Value
	DeleteObject(Mh)  # Get Rid of original Bitmap

	# Create Game Bitmap; Sized Properly for Screen
	SelectObject(BuffDC, Gh)  # This sets up the color
	BuffBMH = CreateCompatibleBitmap(BuffDC, SpBm_Width * 10, SpBm_Height * 6)
	SelectObject(BuffDC, BuffBMH)  # Put New Blank Bitmap in GameDC
	xh2 = SelectObject(tdc, Gh)  # Hold Old Value
	# Copy Bitmap to new size into GameDC
	StretchBlt(BuffDC, 0, 0, SpBm_Width * 10, SpBm_Height * 6, tdc, 0, 0, 320, 192, SRCCOPY)
	SelectObject(tdc, xh2)  # Restore Old Value
	DeleteObject(Gh)  # Get Rid of original Bitmap
	x = 0
	y = 0
	for i in range(1, MaxBitMaps + 1):
		BMA[i].X = x
		BMA[i].Y = y
		x += SpBm_Width
		if (x >= (SpBm_Width * 10)) :
			x = 0
			y += SpBm_Height
		
	
	DeleteDC(tdc)
	ReleaseDC(MainH, dc)
	GFXOn = True


def GFXKill() :
	DeleteObject(MaskBMH)
	DeleteObject(BuffBMH)
	DeleteDC(MaskDC)
	DeleteDC(BuffDC)
	GFXOn = False


# Change Game Object
def ChangeGO(x, y, CurSelBM): # Change Game Object
	gDC = GetDC(MainH)
	if (CurSelBM == 1): # Tank
		UpDateSprite(Game.Tank.X, Game.Tank.Y)  # repaint under old tank
		Game.BMF[x][y] = 1
		Game.PF[x][y] = 0
		Game.Tank.X = x
		Game.Tank.Y = y
		UpDateSprite(Game.Tank.X, Game.Tank.Y)  # paint under new tank
		UpDateTank()
	else :
		if (CurSelBM == MaxObjects) :
			# Tunnel
			i = DialogBox(hInst, "LoadTID", MainH, (DLGPROC) LoadTID) << 1
			Game.PF[x][y] = i + 0x40
			Game.BMF[x][y] = 55  # 55 is tunnel
			UpDateSprite(x, y)
			ShowTunnelID()
		else :
			Game.PF[x][y] = CurSelBM
			Game.BMF[x][y] = GetOBM(CurSelBM)
			UpDateSprite(x, y)
		
	ReleaseDC(MainH, gDC)


# Convert Objects to bitmaps
def BuildBMField() :
	Game.Tank.X = 7
	Game.Tank.Y = 15
	Game.Tank.Dir = 1
	Game.Tank.Firing = False
	for x in range(16):
		for y in range(16):
			#  -= 1- mgy 18-05-2003 only legal pieces  -= 1-
			pt = Game.PF[x][y]
			if (pt > 0x19) :
				pt = GetTunnelID(x, y)
				Game.PF[x][y] = (pt << 1) + 0x40
			
			#  -= 1- end of 18-05-2003  -= 1-

			if (Game.PF[x][y] == 1) :
				i = 1
				Game.Tank.X = x
				Game.Tank.Y = y
				Game.PF[x][y] = 0
			else :
				if (Game.PF[x][y] < 64):
					i = GetOBM(Game.PF[x][y])
				elif (ISTunnel(x, y)):
					i = 55  # 55 is tunnel
			
			Game.BMF[x][y] = i
			Game.BMF2[x][y] = 1
			Game.PF2[x][y] = 0
		
	# this is a good place to reset the score counters 
	Game.ScoreMove = 0
	Game.ScoreShot = 0


#Start/stop game timer and set Game_On
def GameOn(b) :
	if (b):
		SetTimer(MainH, 1, GameDelay, None)
	else:
		KillTimer(MainH, 1)
	Game_On = b
	if DEBUG:
		if (b):
			DEBUG_Time = timeGetTime()
		DEBUG_Frames = 0
	


def JK3dFrame(dc, x, y, x2, y2, up) :
	Wpen = CreatePen(PS_SOLID, 1, 0x00FFFFFF)
	Bpen = CreatePen(PS_SOLID, 1, 0x00808080)
	if (up):
		penO = SelectObject(dc, Wpen)
	else:
		penO = SelectObject(dc, Bpen)
	MoveToEx(dc, x, y2, None)
	LineTo(dc, x, y)
	LineTo(dc, x2, y)
	if (up):
		SelectObject(dc, Bpen)
	else:
		SelectObject(dc, Wpen)
	LineTo(dc, x2, y2)
	LineTo(dc, x, y2)
	SelectObject(dc, penO)
	DeleteObject(Bpen)
	DeleteObject(Wpen)


def JKSelFrame(dc, x, y, x2, y2, pnum) :
	
	if (pnum == 1):
		Color = 0x000000FF
	else:
		Color = 0x0000FF00
	Wpen = CreatePen(PS_SOLID, 2, Color)
	penO = SelectObject(dc, Wpen)
	MoveToEx(dc, x + 1, y2, None)
	LineTo(dc, x + 1, y + 1)
	LineTo(dc, x2, y + 1)
	LineTo(dc, x2, y2)
	LineTo(dc, x + 1, y2)
	SelectObject(dc, penO)
	DeleteObject(Wpen)


# Translate Bitmap to Object
def GetOBM(ob) :
	if ((ob > -1) and (ob <= MaxObjects)):
		return (GetOBMArray[ob])
	else:
		return (1)


def LoadLastLevel() :
	
	if (CurLevel < 2):
		return
	GameOn(False)
	F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, None)
	if (F1 == INVALID_HANDLE_VALUE) :
		MessageBox(MainH, txt001, txt007, MB_OK | MB_ICONERROR)
		PostMessage(MainH, WM_COMMAND, 108, 0)
		return
	
	F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, None)
	CurLevel -= 1
	do :
		CurLevel -= 1
		SetFilePointer(F1, CurLevel * sizeof(TLEVEL), None, FILE_BEGIN)
		ReadFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, None)
		if (BytesMoved < sizeof(TLEVEL)) :
			CloseHandle(F1)
			if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2)
			SendMessage(MainH, WM_GameOver, 0, 0)
			return
		
		if (SkipCL and (F2 != INVALID_HANDLE_VALUE)) :
			SetFilePointer(F2, CurLevel * sizeof(THSREC), None, FILE_BEGIN)
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
			if (BytesMoved < sizeof(THSREC)) TempHSData.moves = 0
			if (TempHSData.moves > 0) CurRecData.SDiff = 128  # Error SDiff
		
	 while ((CurLevel > 0) and (CurRecData.SDiff > 0) and ((Difficulty & CurRecData.SDiff) == 0))
	CloseHandle(F1)
	if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2)
	# Load For Real
	LoadNextLevel(True, False)


def LoadNextLevel(DirectLoad, Scanning):
# Directload is true if we shouldn't use difficulties & Completed Level check
# Scanning is true if we are searching and dont want any errors displayed
	if (GameInProg) :
		SavedLevelNum = MessageBox(MainH, txt039, txt038, MB_YESNOCANCEL | MB_ICONQUESTION)  #Game in progress, Do you want to save the game?
		if (SavedLevelNum == IDCANCEL):
			return (False)
		if (SavedLevelNum == IDYES):
			SendMessage(MainH, WM_SaveRec, 0, 0)
	
	GameOn(False)
	SavedLevelNum = CurLevel
	if (Difficulty == 0):
		SendMessage(MainH, WM_COMMAND, 225, 0)  # Set Difficulty Window - Send change difficulty menu command
	if (Recording):
		SendMessage(MainH, WM_COMMAND, 123, 0)  # Turn Off Recording if on
	# Open file "LaserTank.lvl" from: FileName<-LevelData<-"LaserTank.lvl"
	F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, None)
	if (F1 == INVALID_HANDLE_VALUE) :
		MessageBox(MainH, txt001, txt007, MB_OK | MB_ICONERROR)  #The Level file can not be found\nPlease select a new one
		PostMessage(MainH, WM_COMMAND, 108, 0)
		return False
	

	# Open "LaserTank.hs" for local high scores
	F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, None)
	while True :
		SetFilePointer(F1, CurLevel * sizeof(TLEVEL), None, FILE_BEGIN)
		ReadFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, None)
		if (BytesMoved < sizeof(TLEVEL)) :
			CloseHandle(F1)
			if (F2 != INVALID_HANDLE_VALUE):
				CloseHandle(F2)
			CurLevel = SavedLevelNum  # If eof use last Level Number
			if (not Scanning):
				SendMessage(MainH, WM_GameOver, 0, 0)
			return False
		
		if (SkipCL and (F2 != INVALID_HANDLE_VALUE) and (!DirectLoad)) :
			SetFilePointer(F2, CurLevel * sizeof(THSREC), None, FILE_BEGIN)
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, None)
			if (BytesMoved < sizeof(THSREC)):
				TempHSData.moves = 0
			if (TempHSData.moves > 0):
				CurRecData.SDiff = 128  # Error SDiff
		
		CurLevel += 1
		#? Trying to find a level that hasn't been completed?
	 if not ((not DirectLoad) and (CurRecData.SDiff > 0) and ((Difficulty & CurRecData.SDiff) == 0)):
		break

	CloseHandle(F1)
	if (F2 != INVALID_HANDLE_VALUE):
		CloseHandle(F2)
	#Game.PF = CurRecData.PF
	memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD))
	BuildBMField()
	GameOn(True)
	OKtoHS = True
	OKtoSave = True
	EnableMenuItem(MMenu, 110, MF_BYCOMMAND | MF_GRAYED)  # disable Undo
	EnableMenuItem(MMenu, 112, MF_BYCOMMAND | MF_GRAYED)  # disable Restore
	SetButtons(0xFA)
	FindTank = True
	SetTimer(MainH, 1, 700, None)
	InvalidateRect(MainH, None, True)
	ResetUndoBuffer()
	if (RLL) :
		WritePrivateProfileString("DATA", psRLLN, FileName, INIFile)
		WritePrivateProfileString("DATA", psRLLL, str( CurLevel ) , INIFile)
	
	Game.RecP = 0
	RB_TOS = 0
	SlideT.s = 0  # Just incase
	SlideO.s = 0
	SlideMem.count = 0  # MGY
	if (ARecord and (!PBOpen)):
		SendMessage(MainH, WM_COMMAND, 123, 0)
	if (Backspace[BS_SP] != CurLevel): # if CurLevel != LastLevel
		if (Backspace[BS_SP]):
			EnableMenuItem(MMenu, 118, MF_BYCOMMAND)  # Enable Menu Item
		BS_SP += 1
		if (BS_SP > 9):
			BS_SP = 0
		Backspace[BS_SP] = CurLevel  # Add CurLevel to stack
	
	return (True)


def AssignHSFile() :
	GHFileName = FileName
	strcpy(strrchr(GHFileName, '.'), ".ghs")
	HFileName = FileName
	strcpy(strrchr(HFileName, '.'), ".hs")

	# Set up Record Default file name
	PBFileName = FileName
	P = strrchr(PBFileName, '.')  # Set Up to truncate file name
	if (P):
		P[0] = 0  # Set end of string
	strcat(PBFileName, "_0000.lpb")  # add to name


def CheckHighScore() :
	if (not OKtoHS):
		return
	F2 = CreateFile(HFileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, None,
		OPEN_ALWAYS, FILE_FLAG_RANDOM_ACCESS, None)

	if (F2 == INVALID_HANDLE_VALUE):
		FileError()
	# Check if All lower scores are filled in, if not then set levels
	if ((CurLevel * sizeof(THSREC)) > (i = SetFilePointer(F2, 0, None, FILE_END))) :
		HS.moves = 0  # Sets field to blank
		for x in range(i / sizeof(THSREC), CurLevel):
			WriteFile(F2, HS, sizeof(THSREC), BytesMoved, None)
	
	SetFilePointer(F2, (CurLevel - 1) * sizeof(THSREC), None, FILE_BEGIN)
	ReadFile(F2, & HS, sizeof(THSREC), & BytesMoved, None)
	if ((HS.moves == 0) or (Game.ScoreMove < HS.moves) or ((Game.ScoreMove == HS.moves) and (Game.ScoreShot < HS.shots))) :
		SendMessage(MainH, WM_NewHS, 0, 0)
		SetFilePointer(F2, (CurLevel - 1) * sizeof(THSREC), None, FILE_BEGIN)
		WriteFile(F2, & HS, sizeof(THSREC), & BytesMoved, None)
	
	CloseHandle(F2)


def Animate() :
	AniLevel += 1
	AniCount = 0
	if (AniLevel == 3):
		AniLevel = 0

	for x in range(16):
		for y in range(16):
			# Animate Conveyor Belts & Flag if under something
			switch0 =  (Game.PF2[x][y]) :
			if switch0 ==  2:
				Game.BMF2[x][y] = 6 + AniLevel
				UpDateSprite(x, y)
			elif switch0 ==  15:
				Game.BMF2[x][y] = 24 + AniLevel
				UpDateSprite(x, y)
			elif switch0 ==  16:
				Game.BMF2[x][y] = 27 + AniLevel
				UpDateSprite(x, y)
			elif switch0 ==  17:
				Game.BMF2[x][y] = 30 + AniLevel
				UpDateSprite(x, y)
			elif switch0 ==  18:
				Game.BMF2[x][y] = 33 + AniLevel
				UpDateSprite(x, y)
			
			# Now animate all top sprites
			switch1 =  (Game.PF[x][y]) :
			if switch1 ==  2:
				Game.BMF[x][y] = 6 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  3:
				Game.BMF[x][y] = 9 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  7:
				Game.BMF[x][y] = 16 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  8:
				Game.BMF[x][y] = 36 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  9:
				Game.BMF[x][y] = 39 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  10:
				Game.BMF[x][y] = 42 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  15:
				Game.BMF[x][y] = 24 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  16:
				Game.BMF[x][y] = 27 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  17:
				Game.BMF[x][y] = 30 + AniLevel
				UpDateSprite(x, y)
			elif switch1 ==  18:
				Game.BMF[x][y] = 33 + AniLevel
				UpDateSprite(x, y)
	TankDirty = True


#Find the exit to a tunnel with matching ID (scans y:0-15, x:0-15) and set *x, *y to the destination
#sets WaitToTrans to True of exit found in PF2 (under something) and does not change x,y
#sets BlackHole True if no exit found
def TranslateTunnel(x, y) :
	
	bb = Game.PF[x][y]  # bb is ID #
	WaitToTrans = False
	BlackHole = False
	for cy in range(16):
		for cx in range(16):
			if ((Game.PF[cx][cy] == bb) and ( not (( x == cx) and ( y == cy)))) :
				x = cx  # We found an exit YEA !!!
				y = cy
				return
			
	# check for blocked hole - something is over the exit
	# Scan the 2nd layer any matches are blocked holes
	for (cy = 0; cy < 16; cy += 1)
		for (cx = 0; cx < 16; cx += 1)
			if ((Game.PF2[cx][cy] == bb) and ( not (( * x == cx) and ( * y == cy)))) :
				# We found one so we will set the flag
				WaitToTrans = True
				return  # Blocked so no warp
			
	# There is no match, so it is a black hole
	BlackHole = True


def ConvMoveTank(x, y, check) :
	UpDateSprite(Game.Tank.X, Game.Tank.Y)
	Game.Tank.Y += y
	Game.Tank.X += x
	if (ISTunnel(Game.Tank.X, Game.Tank.Y)) :
		TranslateTunnel( & Game.Tank.X, & Game.Tank.Y)  # We moved into a tunnel
		if (BlackHole):
			PostMessage(MainH, WM_Dead, 0, 0)  # The tunnel was a black hole
	
	if (WaitToTrans):
		Game.Tank.Good = True
	TankDirty = True
	ConvMoving = True
	if (wasIce and check) :
		SlideT.x = Game.Tank.X
		SlideT.y = Game.Tank.Y
		SlideT.s = True
		SlideT.dx = x
		SlideT.dy = y
	
	AntiTank()


def UpDateTankPos(x, y) :

	SoundPlay(S_Move)
	UpdateUndo()

	# Update move counter
	Game.ScoreMove += 1
	SetTextAlign(gDC, TA_CENTER)
	SetTextColor(gDC, 0x0000FF00)
	SetBkColor(gDC, 0)
	TextOut(gDC, ContXPos + 48, 207, str( Game.ScoreMove ) , strlen(temps))

	UpDateSprite(Game.Tank.X, Game.Tank.Y)
	Game.Tank.Y += y
	Game.Tank.X += x
	Game.Tank.Good = False  # we need it somewhere if we move off a tunnel
	if (ISTunnel(Game.Tank.X, Game.Tank.Y)) :
		TranslateTunnel( Game.Tank.X, Game.Tank.Y)  # We moved into a tunnel
		if (BlackHole)
			PostMessage(MainH, WM_Dead, 0, 0)  # The tunnel was a black hole
	
	if (WaitToTrans)
		Game.Tank.Good = True
	TankDirty = True


# Set tank direction or move tank in direction if already facing. Then set up SlideT if on ice
def MoveTank(d) :
	if (Game.Tank.Dir != d): # The Tank is Turning
		Game.Tank.Dir = d
		UpDateSprite(Game.Tank.X, Game.Tank.Y)
		TankDirty = True
		SoundPlay(S_Turn)
		return
	
	if d ==  1:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1))
			UpDateTankPos(0, -1)
		else
			SoundPlay(S_Head)  # Ouch we are hitting something hard
		SlideT.dy = -1
		SlideT.dx = 0
	elif d ==  2:
		if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y))
			UpDateTankPos(1, 0)
		else
			SoundPlay(S_Head)
		SlideT.dy = 0
		SlideT.dx = 1
	elif d ==  3:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1))
			UpDateTankPos(0, 1)
		else
			SoundPlay(S_Head)
		SlideT.dy = 1
		SlideT.dx = 0
	elif d ==  4:
		if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y))
			UpDateTankPos(-1, 0)
		else
			SoundPlay(S_Head)
		SlideT.dy = 0
		SlideT.dx = -1
	
	if (wasIce) :
		SlideT.x = Game.Tank.X
		SlideT.y = Game.Tank.Y
		SlideT.s = True
	


def CheckLoc(x, y) :
	# Check if Tank can move
	if ((x < 0) or (x > 15) or (y < 0) or (y > 15))
		return False

	wasIce = ((Game.PF[x][y] == Obj_Ice) or (Game.PF[x][y] == Obj_ThinIce))

	if ((Game.PF[x][y] & Obj_Tunnel) == Obj_Tunnel)
		return True  #Can move into a tunnel square

	return (CheckArray[Game.PF[x][y]])  # Check flags to see if tank can move into this type of square


def MoveObj(x, y, dx, dy, sf):
	# Try to move object on square x,y that was pushed in dir dx,dy then play sound sf
	# Update terrain under object's initial position (x,y)
	#   Also unblock tunnel if Obj blocking tunnel and let other end activate (cx,cy)
	#
	# used by CheckLLoc and IceMoveO
	obt = Game.PF[x][y]  # Get Object type
	bm = Game.BMF[x][y]
	if ((Game.PF2[x][y] & Obj_Tunnel) == Obj_Tunnel): # Check if Tunnel
		# Unblock tunnel

		bb = Game.PF2[x][y] | 1  # bb is ID # w/ 1 set. 1 bit signifies that tunnel has an object on it waiting to be transported
		ok = False
		for cy in range(16):
			for cx in range(16):
				if ((Game.PF2[cx][cy] == bb) and ( not ((x == cx) and (y == cy)))) :
					# Search PF2[y,x] for another covered tunnel with same id (bb) & not same square
					# Search for other end of blocked tunnel
					ok = True
					break
					# Ok if something wants to move here; cx & cy set to orig
			if ok:
				break

		if (ok): # We are Moving an Object
			# Other end of blocked tunnel had an object so move it through now
			#Move object through a tunnel (from xy to cx,cy)
			Game.PF[x][y] = Game.PF[cx][cy]  # Transfer Blocked Object
			Game.BMF[x][y] = Game.BMF[cx][cy]

			Game.PF[cx][cy] = Game.PF2[cx][cy] & 0xFE  # Return Saved State
			Game.PF2[cx][cy] = 0
			Game.BMF[cx][cy] = Game.BMF2[cx][cy]
			UpDateSprite(cx, cy)
		else:
			# Did not find another end of this tunnel with an object on
			# Not Blocked Anymore
			Game.PF[x][y] = Game.PF2[x][y] & 0xFE  # Return Saved State strip
			Game.PF2[x][y] = 0
			Game.BMF[x][y] = Game.BMF2[x][y]

			# We didn't find a match so maybe the tank is it
			if ((Game.PF[Game.Tank.X][Game.Tank.Y] == (bb & 0xFE)) and Game.Tank.Good) :
				Game.ScoreMove -= 1  # MGY - 2003/05/18 - v408b15 -  Bartok Bug.lvl
				UpDateTankPos(0, 0)
				UndoP -= 1
		
		
	else : # If not a tunnel
		#Move terrain from PF2 to PF
		Game.PF[x][y] = Game.PF2[x][y]  # Return Saved State
		Game.PF2[x][y] = 0
		Game.BMF[x][y] = Game.BMF2[x][y]
	

	UpDateSprite(x, y)
	# Source terrain updated

	# Now update destination
	x += dx
	y += dy

	# If destination is a tunnel then set x,y to tunnel's exit
	if (ISTunnel(x, y)) :
		# TranslateTunnel:
		#Find the exit to a tunnel with matching ID (scans y:0-15, x:0-15) and set *x, *y to the destination
		#sets WaitToTrans to True of exit found in PF2 (under something) and does not change x,y
		#sets BlackHole True if no exit found

		TranslateTunnel( & x, & y)  # We moved into a tunnel
		if (BlackHole)
			return  # The tunnel was a black hole
	else
		WaitToTrans = False

	# Move terrain to second layer for dest
	Game.PF2[x][y] = Game.PF[x][y]  # Save Return State

	if (WaitToTrans):
		Game.PF2[x][y] |= 1  # Set bit 1 if we are waiting to transport

	# Also move BMP to second layer
	Game.BMF2[x][y] = Game.BMF[x][y]

	if (Game.PF[x][y] != 3): #Not water terrain
		# Move object to destination square
		Game.PF[x][y] = obt
		Game.BMF[x][y] = bm
	else :
		# Dest square is water (ID=3)
		sf = S_Sink
		if (obt == 5): #If is a block sinking
			#Set id to GRASS and BMP to SUNK_BLOCK
			Game.PF[x][y] = 0
			Game.PF2[x][y] = 0  # Pushing Block into Water 
			Game.BMF[x][y] = 19
			Game.BMF2[x][y] = 19
		
	
	UpDateSprite(x, y)
	if ((x == Game.Tank.X) and (y == Game.Tank.Y)):
		TankDirty = True
	SoundPlay(sf)


def IceMoveT(): # Move the tank on the Ice
	if (Game.PF[SlideT.x][SlideT.y] == Obj_ThinIce) :
		Game.BMF[SlideT.x][SlideT.y] = 9
		Game.PF[SlideT.x][SlideT.y] = Obj_Water  # Ice to Water
		UpDateSprite(SlideT.x, SlideT.y)
	

	if (CheckLoc(SlideT.x + SlideT.dx, SlideT.y + SlideT.dy)) :
		savei = wasIce
		ConvMoveTank(SlideT.dx, SlideT.dy, False)  # use this insted of UpDateTank
	else:
		SlideT.s = False
		return
	

	SlideT.x += SlideT.dx  # Update Position
	SlideT.y += SlideT.dy  # Update Position
	if (not savei):
		SlideT.s = False  # The ride is over


def IceMoveO(): # Move an Object on the Ice
	for iSlideObj in range(SlideMem.count, 0, -1):
		Mem_to_SlideO(iSlideObj)  # Get from memory
		if (iSlideObj <= SlideMem.count): # just in case ... MGY
			if (Game.PF2[SlideO.x][SlideO.y] == Obj_ThinIce) :
				Game.BMF2[SlideO.x][SlideO.y] = 9
				Game.PF2[SlideO.x][SlideO.y] = Obj_Water  # Ice to Water
			if (CheckLoc(SlideO.x + SlideO.dx, SlideO.y + SlideO.dy) and
				( not ((SlideO.x + SlideO.dx == Game.Tank.X) and (SlideO.y + SlideO.dy == Game.Tank.Y)))) :
				savei = wasIce
				MoveObj(SlideO.x, SlideO.y, SlideO.dx, SlideO.dy, S_Push2)
				AntiTank()

				SlideO.x += SlideO.dx  # Update Position
				SlideO.y += SlideO.dy  # Update Position
				if (not savei) :
					SlideO.s = False  # The ride is over
					SlideO_to_Mem(iSlideObj)  # update memory
					sub_SlideO_from_Mem(iSlideObj)
				else:
					SlideO_to_Mem(iSlideObj)  # update memory
				
			else:
				if (Game.PF2[SlideO.x][SlideO.y] == Obj_Water)
					MoveObj(SlideO.x, SlideO.y, 0, 0, 0)  # Drop Object in the water (was thin ice)
				SlideO.s = False
				SlideO_to_Mem(iSlideObj)  # update memory
				sub_SlideO_from_Mem(iSlideObj)
				AntiTank()  # incase an anti-tank is behind a block
				#return  # MGY 

	Mem_to_SlideO(SlideMem.count)  # Get from memory the last object of the list
	SlideO.s = (SlideMem.count > 0)


def KillAtank(x, y, bm):
# used by CheckLLoc
# Kill the AntiTank on square x,y
# Replace bitmap with bm (dead tank bitmap for that dir tank)
# Replace object ID with 4 (solid)
# Play sound S_Anti1
	Game.PF[x][y] = 4  # Solid Object
	Game.BMF[x][y] = bm  # Junk Bitmap
	UpDateSprite(x, y)
	SoundPlay(S_Anti1)


def CheckLLoc(x, y, dx, dy):
# this is were the laser does its damage
# returns true if laser didn't hit anything and still in board

	if ((x < 0) or (x > 15) or (y < 0) or (y > 15)): #Laser out of board
		return (False)
	

	if ((x == Game.Tank.X) and (y == Game.Tank.Y)): #Hit tank
		SendMessage(MainH, WM_Dead, 0, 0)
		return (False)
	

	wasIce = False
	switch0 =  (Game.PF[x][y]) :

	if (switch0 ==  0 or #grass
			switch0 ==  2 or #flag
			switch0 ==  3 or #water
			switch0 ==  15 or #conveyor up
			switch0 ==  16 or #conveyor right
			switch0 ==  17 or #conveyor down
			switch0 ==  18 ): #conveyor left
		return (True)

	elif switch0 ==  4: #solid
		SoundPlay(S_LaserHit)
		

	elif switch0 ==  5: #block
		if (CheckLoc(x + dx, y + dy)) #Can block be moved in direction of laser? Is square free
			MoveObj(x, y, dx, dy, S_Push1)  #Push block
		else
			SoundPlay(S_LaserHit)
		

	elif switch0 ==  6: #wall
		Game.PF[x][y] = 0  #Set this wall object to grass (delete wall)
		Game.BMF[x][y] = 1  #Set this wall object to grass (bitmap)
		UpDateSprite(x, y)
		SoundPlay(S_Bricks)
		

	elif switch0 ==  7: #antitank_up
		if (dy == 1): # Laser hit front of antitank
			KillAtank(x, y, 54)  #Replace antitank with ID=SOLID and frame=54 DEAD ANTITANK
			return (False)
		elif (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  8: #antitank_right
		if (dx == -1) :
			KillAtank(x, y, 52)
			return (False)
		 elif (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  9: #antitank_down
		if (dy == -1) :
			KillAtank(x, y, 12)
			return (False)
		 elif (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  10: #antitank_left
		if (dx == 1) :
			KillAtank(x, y, 53)
			return (False)
		 elif (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  11: #mirror_left_up
		if ((laser.Dir == 2) or (laser.Dir == 3))
			return (True)
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  12: #mirror_up_right
		if ((laser.Dir == 3) or (laser.Dir == 4))
			return (True)
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  13: #mirror_right_down
		if ((laser.Dir == 1) or (laser.Dir == 4))
			return (True)
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  14: #mirror_down_left
		if ((laser.Dir == 1) or (laser.Dir == 2))
			return (True)
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2)
		else
			SoundPlay(S_LaserHit)

	elif switch0 ==  19: #glass
		if (laser.Good)
			# Put green reflecting glass sprite
			PutSprite(46, XOffset + (x * SpBm_Width), YOffset + (y * SpBm_Height))
		else
			# Put red reflecting glass sprite
			PutSprite(51, XOffset + (x * SpBm_Width), YOffset + (y * SpBm_Height))
		return (True)

	elif switch0 ==  20: #rotmirror_left_up
		if ((laser.Dir == 2) or (laser.Dir == 3))
			return (True)
		Game.PF[x][y] = 21  # Replace ID with rotated mirror
		Game.BMF[x][y] = 48  # and replace bitmap
		UpDateSprite(x, y)
		SoundPlay(S_Rotate)
		

	elif switch0 ==  21: #rotmirror_up_right
		if ((laser.Dir == 3) or (laser.Dir == 4))
			return (True)
		Game.PF[x][y] = 22  # Replace ID with rotated mirror
		Game.BMF[x][y] = 49  # and replace bitmap
		UpDateSprite(x, y)
		SoundPlay(S_Rotate)
		

	elif switch0 ==  22: #rotmirror_right_down
		if ((laser.Dir == 1) or (laser.Dir == 4))
			return (True)
		Game.PF[x][y] = 23  # Replace ID with rotated mirror
		Game.BMF[x][y] = 50  # and replace bitmap
		UpDateSprite(x, y)
		SoundPlay(S_Rotate)
		

	elif switch0 ==  23: #rotmirror_down_left
		if ((laser.Dir == 1) or (laser.Dir == 2))
			return (True)
		Game.PF[x][y] = 20  # Replace ID with rotated mirror
		Game.BMF[x][y] = 47  # and replace bitmap
		UpDateSprite(x, y)
		SoundPlay(S_Rotate)
		

	elif (switch0 ==  24 or # Ice
			switch0 ==  25): # thin Ice
		return (True)

	else:
		if (ISTunnel(x, y)):
			return (True)
	

	# If object is moving into an ice square then add it to the Sliding stack
	if (wasIce) :
		# If is already sliding, del it !
		del_SlideO_from_Mem(x, y)
		# and add a new slide in a new direction
		SlideO.x = x + dx
		SlideO.y = y + dy
		SlideO.s = True
		SlideO.dx = dx
		SlideO.dy = dy
		add_SlideO_to_Mem()
	
	# MGY
	else :
		# SlideO.s = False;   # in elif switch0 ==  we side hit off of the ice
		del_SlideO_from_Mem(x, y)
	
	return (False)


def MoveLaser() :

	# LaserMoveJump:
	while True:
		LaserBounceOnIce = False
		x = 0
		y = 0
		if laser.Dir ==  1:
			y = -1
		elif laser.Dir ==  2:
			x = +1
		elif laser.Dir ==  3:
			y = +1
		elif laser.Dir ==  4:
			x = -1
		
		if (CheckLLoc(laser.X + x, laser.Y + y, x, y)): # Check destination square and start objects there moving if needed
		
			# Laser is still on the board

			if (laser.Firing):
				UpDateSprite(laser.X, laser.Y)

			laser.Y += y
			laser.X += x
			if (((Game.PF[laser.X][laser.Y] > 10) and (Game.PF[laser.X][laser.Y] < 15)) or #Is mirror
				((Game.PF[laser.X][laser.Y] > 19) and (Game.PF[laser.X][laser.Y] < 24))): #Is Rotating Mirror
			

				# Reflect off mirror

				oDir = laser.Dir

				# Update laser direction if hitting a mirror
				switch0 =  (Game.PF[laser.X][laser.Y]) :
				if switch0 ==  11 or # mirror_left_up
					switch0 ==  20: # rotmirror_left_up
					if (laser.Dir == 2) laser.Dir = 1
					else laser.Dir = 4
					break

				elif switch0 ==  12: # mirror_up_right
				elif switch0 ==  21:
					if (laser.Dir == 3) laser.Dir = 2
					else laser.Dir = 1
					break

				elif switch0 ==  13: # mirror_right_down
				elif switch0 ==  22:
					if (laser.Dir == 1) laser.Dir = 2
					else laser.Dir = 3
					break

				elif switch0 ==  14: # mirror_down_left
				elif switch0 ==  23:
					if (laser.Dir == 1) laser.Dir = 4
					else laser.Dir = 3
				

				# Draw laser in two halves, original direction and final direction
				UpDateLaserBounce(oDir, laser.Dir)
				SoundPlay(S_Deflb)
			else # Not reflecting
				UpDateLaser()  # Draw laser as rectangle
			laser.Firing = True
		else :
			# Laser is off the board / hit something solid

			Game.Tank.Firing = False
			if (laser.Firing)
				UpDateSprite(laser.X, laser.Y)

			# Antitank turn
			if (Game_On or VHSOn)
				AntiTank()

			# SpeedBug - MGY - 22-11-2002
			if (TestIfConvCanMoveTank())
				ConvMoving = True
		

		# When drawing reflecting laser, LaserBounceOnIce is set to true if in a square with a sliding object
		if (not LaserBounceOnIce):
			break  # goto LaserMoveJump

			

def FireLaser(x, y, d, sf) :
	temps = ""

	Game.Tank.Firing = True

	laser.Dir = d
	laser.X = x
	laser.Y = y
	laser.Firing = False  # true if laser has been moved

	SoundPlay(sf)

	# Update the shot counter text
	SetTextAlign(gDC, TA_CENTER)
	SetTextColor(gDC, 0x0000FF00)
	SetBkColor(gDC, 0)
	temps = str( Game.ScoreShot )   # we incremented it in wm_timer
	TextOut(gDC, ContXPos + 134, 207, temps, strlen(temps))

	if (sf == 2)
		LaserColor = LaserColorG
	else
		LaserColor = LaserColorR
	laser.Good = (sf == 2)
	MoveLaser()


def AntiTank():
	# Look for antitanks on same row/col as tank and let them fire (only if laser not already existing)
	# Order: Right, left, down, above from Tank
	# Program Anti tank seek 

	# Only one laser on board so returns if laser exists
	if (Game.Tank.Firing):
		return

	x = Game.Tank.X  # Look to the right
	while (CheckLoc(x, Game.Tank.Y)) x += 1
	if ((x < 16) and (Game.PF[x][Game.Tank.Y] == 10) and (Game.Tank.X != x)) :
		FireLaser(x, Game.Tank.Y, 4, S_Anti2)
		return
	
	x = Game.Tank.X  # Look to the left
	while (CheckLoc(x, Game.Tank.Y)) x -= 1
	if ((x >= 0) and (Game.PF[x][Game.Tank.Y] == 8) and (Game.Tank.X != x)) :
		FireLaser(x, Game.Tank.Y, 2, S_Anti2)
		return
	
	y = Game.Tank.Y  # Look Down
	while (CheckLoc(Game.Tank.X, y)) y += 1
	if ((y < 16) and (Game.PF[Game.Tank.X][y] == 7) and (Game.Tank.Y != y)) :
		FireLaser(Game.Tank.X, y, 1, S_Anti2)
		return
	
	y = Game.Tank.Y  # Look Up
	while (CheckLoc(Game.Tank.X, y)) y -= 1
	if ((y >= 0) and (Game.PF[Game.Tank.X][y] == 9) and (Game.Tank.Y != y)) :
		FireLaser(Game.Tank.X, y, 3, S_Anti2)
		return
	


def PutSelectors() :
	x, y, i, j

	x = ContXPos + 5
	y = 260
	j = 1
	for i in range(0,MaxObjects+1):
		JK3dFrame(gDC, x - 1, y - 1, x + SpBm_Width, y + SpBm_Height, True)
		if (i == CurSelBM_L) JKSelFrame(gDC, x - 1, y - 1, x + SpBm_Width, y + SpBm_Height, 1)
		if (i == CurSelBM_R) JKSelFrame(gDC, x - 1, y - 1, x + SpBm_Width, y + SpBm_Height, 2)
		PutSprite(GetOBM(i), x, y)
		x += SpBm_Width + 4
		j += 1
		if (j > EditBMWidth) :
			x = ContXPos + 5
			y += SpBm_Height + 4
			j = 1
		
	


def ShowTunnelID() :
	# scan and add Tunnel ID #s
	SetBkMode(gDC, OPAQUE)
	SetTextAlign(gDC, TA_LEFT)
	SetTextColor(gDC, 0)
	for (x = 0; x < 16; x += 1)
		for (y = 0; y < 16; y += 1)
			if (ISTunnel(x, y)) :
				sprintf(temps, "(%1d)", GetTunnelOldID(x, y))
				TextOut(gDC, 22 + (x * SpBm_Width), 20 + (y * SpBm_Height), temps, strlen(temps))
			


def SetGameSize(i):
	CheckMenuItem(MMenu, 120, 0)
	CheckMenuItem(MMenu, 121, 0)
	CheckMenuItem(MMenu, 122, 0)
	CheckMenuItem(MMenu, 119 + i, MF_CHECKED)
	temps = str( i ) 
	WritePrivateProfileString("SCREEN", psSize, temps, INIFile)
	if (GFXOn) GFXKill
	switch0 =  (i) :
	elif switch0 ==  1:
		SpBm_Width = 24
		SpBm_Height = 24
		ContXPos = 419
		EditBMWidth = 6
		SetWindowPos(MainH, 0, 0, 0, ContXPos + 190, 463, SWP_NOMOVE | SWP_NOZORDER)
		LaserOffset = 10
		break

	elif switch0 ==  2:
		SpBm_Width = 32
		SpBm_Height = 32
		ContXPos = 550
		EditBMWidth = 5
		SetWindowPos(MainH, 0, 0, 0, ContXPos + 190, 591, SWP_NOMOVE | SWP_NOZORDER)
		LaserOffset = 13
		break

	elif switch0 ==  3:
		SpBm_Width = 40
		SpBm_Height = 40
		ContXPos = 680
		EditBMWidth = 4
		SetWindowPos(MainH, 0, 0, 0, ContXPos + 190, 719, SWP_NOMOVE | SWP_NOZORDER)
		LaserOffset = 17
		break

	
	SetWindowPos(Ed1, 0, ContXPos + 9, 99, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
	SetWindowPos(Ed2, 0, ContXPos + 9, 148, 0, 0, SWP_NOSIZE | SWP_NOZORDER)

	SetWindowPos(BT1, 0, ContXPos + 15, 255, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
	SetWindowPos(BT2, 0, ContXPos + 15, 280, 0, 0, SWP_NOSIZE | SWP_NOZORDER)

	SetWindowPos(BT3, 0, ContXPos + 15, 305, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
	SetWindowPos(BT4, 0, ContXPos + 15, 330, 0, 0, SWP_NOSIZE | SWP_NOZORDER)

	SetWindowPos(BT5, 0, ContXPos + 15, 380, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
	SetWindowPos(BT6, 0, ContXPos + 90, 380, 0, 0, SWP_NOSIZE | SWP_NOZORDER)

	SetWindowPos(BT7, 0, ContXPos + 90, 255, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
	SetWindowPos(BT8, 0, ContXPos + 90, 330, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
	SetWindowPos(BT9, 0, ContXPos + 15, 355, 0, 0, SWP_NOSIZE | SWP_NOZORDER)
	GraphM = GetPrivateProfileInt("SCREEN", psGM, 0, INIFile)
	if (GraphM == 2)
		GetPrivateProfileString("SCREEN", psGFN, "", GraphFN, MAX_PATH, INIFile)
	GetPrivateProfileString("SCREEN", psGDN, "", GraphDN, MAX_PATH, INIFile)
	if (strlen(GraphDN) == 0) :
		GetCurrentDirectory(MAX_PATH, GraphDN)  #We only do this once
		WritePrivateProfileString("SCREEN", psGDN, GraphDN, INIFile)
	
	GFXInit()


# Write data to .lpb file
# Write PBSRec:
#     char LName[31];       # Level Name
#     char Author[31];      # Author of the recording (player's initals get appended to front with "  -")
#     WORD Level;         # Level Number
#     WORD Size;          # Size of Data
# Write RecBuffer (see AddKBuff(), resizable)
def SavePBFile() :
	HANDLE Book
	char temps[60]
	char SaveAuthor[31]

	# Get Hs.name (player's High Score name)
	GetPrivateProfileString("DATA", psUser, "", temps, 5, INIFile)
	if (stricmp(temps, HS.name) != 0): # String comparison (elif switch0 ==  insensitive)
		HS.name = temps  #strcpy(*dest, *src)
		WritePrivateProfileString("DATA", psUser, HS.name, INIFile)
	

	if (temps[0] != '') :
		# Fill the name with spaces
		strcat(temps, "      ")
		temps[4] = '-'  # FIX: temps[3] = '-'  #temps = "HS - User Name"
		temps[5] = ''
	
	# Add The Author's name
	strcat(temps, PBSRec.Author)
	# Limit the size
	temps[30] = ''

	# temps = "HS  -UserName....."
	# where HS is the palyer's high score initials,
	# and UserName is the name entered when saving, to a total of 30 bytes
	# Save  PBSRec
	SaveAuthor = PBSRec.Author
	PBSRec.Author = temps

	# Write file
	Book = CreateFile(PBFileName, GENERIC_WRITE, 0, None, CREATE_ALWAYS, 0, None)  # Create New PlayBack File
	WriteFile(Book, & PBSRec, sizeof(PBSRec), & BytesMoved, None)  # Save Header Info
	WriteFile(Book, RecBuffer, PBSRec.Size, & BytesMoved, None)  # Data
	CloseHandle(Book)

	# restore   PBSRec
	PBSRec.Author = SaveAuthor
