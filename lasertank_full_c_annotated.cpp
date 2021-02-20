// lt32l_us.h
/*******************************************************
 **             LaserTank ver 4.1.1                   **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2005 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 *******************************************************/
#define App_Title "LaserTank"
#define App_Version "4.1.2"
#define FILE_VERSION "4.1.2\0"
#define PRODUCT_VERSION "4.1.2\0"

// The name of Language File
#define LANGFilePath "Language\\"
#define LANGFileName "Language\\Language.dat"
#define GAME_BMP "game.bmp"
#define MASK_BMP "mask.bmp"
#define OPENING_BMP "opening.bmp"
#define CONTROL_BMP "control.bmp" //Level information background

//
// ID of Dialogs
// Text values and old ID are in comments
//

// This is the Button Function ID number
#define ButID1 110
#define ButID2 111
#define ButID3 112
#define ButID4 101
#define ButID5 119
#define ButID6 107
#define ButID7 301
#define ButID8 105
#define ButID9 106

// number of linesof each sections in the Language File
#define SIZE_BUTTON 9
#define SIZE_TEXT 48
#define SIZE_MMENU 49
#define SIZE_EMENU 24
#define SIZE_DIALOGS(4 + 3 + 9 + 9 + 7 + 3 + 14 + 1 + 4 + 3 + 9 + 4 + 7 + 3 + 10 + 6) // 96
#define SIZE_ABOUTMSG 14
#define SIZE_ALL(SIZE_BUTTON + SIZE_TEXT + SIZE_MMENU + SIZE_EMENU + SIZE_ABOUTMSG + SIZE_DIALOGS)

// Start LINES in the Language File
#define START_MMENU 0
#define START_EMENU(START_MMENU + SIZE_MMENU)
#define START_BUTTON(START_EMENU + SIZE_EMENU)
#define START_TEXT(START_BUTTON + SIZE_BUTTON)
#define START_DIALOGS(START_TEXT + SIZE_TEXT)
#define START_ABOUTMSG(START_ABOUTMSG + SIZE_ABOUTMSG)

// Start LINES in the LANGText[]
#define OFFSET_TEXT SIZE_BUTTON
#define OFFSET_DIALOGS(OFFSET_TEXT + SIZE_TEXT)
#define OFFSET_ABOUTMSG(OFFSET_DIALOGS + SIZE_DIALOGS)

#define ButText1 LANGText[0]
#define ButText2 LANGText[1]
#define ButText3 LANGText[2]
#define ButText4 LANGText[3]
#define ButText5 LANGText[4]
#define ButText6 LANGText[5]
#define ButText7 LANGText[6]
#define ButText8 LANGText[7]
#define ButText9 LANGText[8]

#define txt001 LANGText[OFFSET_TEXT + 0]
#define txt002 LANGText[OFFSET_TEXT + 1]
#define txt003 empty
#define txt004 LANGText[OFFSET_TEXT + 2]
#define txt005 LANGText[OFFSET_TEXT + 3]
#define txt006 LANGText[OFFSET_TEXT + 4]
#define txt007 LANGText[OFFSET_TEXT + 5]
#define txt008 LANGText[OFFSET_TEXT + 6]
#define txt009 LANGText[OFFSET_TEXT + 7]
#define txt010 LANGText[OFFSET_TEXT + 8]
#define txt011 LANGText[OFFSET_TEXT + 9]
#define txt012 LANGText[OFFSET_TEXT + 10]
#define txt013 LANGText[OFFSET_TEXT + 11]
#define txt014 LANGText[OFFSET_TEXT + 12]
#define txt015 LANGText[OFFSET_TEXT + 13]
#define txt016 LANGText[OFFSET_TEXT + 14]
#define txt017 LANGText[OFFSET_TEXT + 15]
#define txt018 LANGText[OFFSET_TEXT + 16]
#define txt019 LANGText[OFFSET_TEXT + 17]
#define txt020 LANGText[OFFSET_TEXT + 18]
#define txt021 LANGText[OFFSET_TEXT + 19]
#define txt022 LANGText[OFFSET_TEXT + 20]
#define txt023 LANGText[OFFSET_TEXT + 21]
#define txt024 LANGText[OFFSET_TEXT + 22]
#define txt025 LANGText[OFFSET_TEXT + 23]
#define txt026 LANGText[OFFSET_TEXT + 24]
#define txt027 LANGText[OFFSET_TEXT + 25]
#define txt028 LANGText[OFFSET_TEXT + 26]
#define txt029 LANGText[OFFSET_TEXT + 27]
#define txt030 empty
#define txt031 LANGText[OFFSET_TEXT + 28]
#define txt032 LANGText[OFFSET_TEXT + 29]
#define txt033 LANGText[OFFSET_TEXT + 30]
#define txt034 LANGText[OFFSET_TEXT + 31]
#define txt035 LANGText[OFFSET_TEXT + 32]
#define txt036 LANGText[OFFSET_TEXT + 33]
#define txt037 LANGText[OFFSET_TEXT + 34]
#define txt038 LANGText[OFFSET_TEXT + 35]
#define txt039 LANGText[OFFSET_TEXT + 36]
#define txt040 LANGText[OFFSET_TEXT + 37]
#define txt041 LANGText[OFFSET_TEXT + 38]
#define txt042 LANGText[OFFSET_TEXT + 39]
#define txt043 LANGText[OFFSET_TEXT + 40]
#define txt044 LANGText[OFFSET_TEXT + 41]
#define txt045 LANGText[OFFSET_TEXT + 42]
#define REC_Title LANGText[OFFSET_TEXT + 43]

#define help01 LANGText[OFFSET_TEXT + 44]
#define help02 LANGText[OFFSET_TEXT + 45]
#define help03 LANGText[OFFSET_TEXT + 46]
#define HelpFileName LANGText[OFFSET_TEXT + 47]

// This Id is used By Load, HighScore & Global High Score ListBoxs
#define ID_LISTBOX 801

// Others IDs
#define IDM_ABOUTBOX_00 "About Laser Tank"
#define IDM_ABOUTBOX_01 "&Ok"
#define IDM_ABOUTBOX_04 "By Jim Kindley"
#define IDM_ABOUTBOX_06 "Version"
#define IDM_ABOUTBOX_02 "Title"
#define IDM_ABOUTBOX_03 "Ver Info"
#define IDM_ABOUTBOX_05 "©2002, JEK Software"
#define ID_ABOUTBOX_00(OFFSET_DIALOGS + 0)
#define ID_ABOUTBOX_OK(OFFSET_DIALOGS + 1)
#define ID_ABOUTBOX_04(OFFSET_DIALOGS + 2)
#define ID_ABOUTBOX_06(OFFSET_DIALOGS + 3)
#define ID_ABOUTBOX_02 801
#define ID_ABOUTBOX_03 802
#define ID_ABOUTBOX_05 803
#define ID_ABOUTBOX_07 804

#define IDM_DEADBOX_00 "&Undo Last Move"
#define IDM_DEADBOX_01 "YOU ARE DEAD ! ! !"
#define IDM_DEADBOX_02 "&ReStart"
#define ID_DEADBOX_UNDO(OFFSET_DIALOGS + 4)
#define ID_DEADBOX_DEAD(OFFSET_DIALOGS + 5)
#define ID_DEADBOX_RESTART(OFFSET_DIALOGS + 6)
/*
#define IDM_DIFFBOX_00     "Game Difficulty"
#define IDM_DIFFBOX_01     "&Ok"
#define IDM_DIFFBOX_02     "&Kids"
#define IDM_DIFFBOX_03     "&Easy"
#define IDM_DIFFBOX_04     "&Medium"
#define IDM_DIFFBOX_05     "&Hard"
#define IDM_DIFFBOX_06     "&Deadly"
#define IDM_DIFFBOX_07     "&All"
#define IDM_DIFFBOX_08     "Select"
*/
#define ID_DIFFBOX_00(OFFSET_DIALOGS + 7)
#define ID_DIFFBOX_01(OFFSET_DIALOGS + 8)
#define ID_DIFFBOX_02(OFFSET_DIALOGS + 9)
#define ID_DIFFBOX_03(OFFSET_DIALOGS + 10)
#define ID_DIFFBOX_04(OFFSET_DIALOGS + 11)
#define ID_DIFFBOX_05(OFFSET_DIALOGS + 12)
#define ID_DIFFBOX_06(OFFSET_DIALOGS + 13)
#define ID_DIFFBOX_07(OFFSET_DIALOGS + 14)
#define ID_DIFFBOX_08(OFFSET_DIALOGS + 15)

/*
#define IDM_GRAPHBOX_00    "Select Graphics Set"
#define IDM_GRAPHBOX_01    "Select One"
#define IDM_GRAPHBOX_02    "&Internal Graphics"
#define IDM_GRAPHBOX_03    "&User Graphics "
#define IDM_GRAPHBOX_04    "&Close"
#define IDM_GRAPHBOX_05    "Author :"
#define IDM_GRAPHBOX_06    "Laser Tank Graphic Set Description"
#define IDM_GRAPHBOX_07    "&View Opening Screen "
#define IDM_GRAPHBOX_08    "Change &Directory"
*/
#define ID_GRAPHBOX_00(OFFSET_DIALOGS + 16)
#define ID_GRAPHBOX_01(OFFSET_DIALOGS + 17)
#define ID_GRAPHBOX_02(OFFSET_DIALOGS + 18)
#define ID_GRAPHBOX_03(OFFSET_DIALOGS + 19)
#define ID_GRAPHBOX_04(OFFSET_DIALOGS + 20)
#define ID_GRAPHBOX_05(OFFSET_DIALOGS + 21)
#define ID_GRAPHBOX_06(OFFSET_DIALOGS + 22)
#define ID_GRAPHBOX_07 801
#define ID_GRAPHBOX_08(OFFSET_DIALOGS + 23)
#define ID_GRAPHBOX_09(OFFSET_DIALOGS + 24)
#define ID_GRAPHBOX_10 802
#define ID_GRAPHBOX_11 803

/*
#define IDM_LOADLEV_00     "Pick Level to Load"
#define IDM_LOADLEV_01     "&Cancel"
#define IDM_LOADLEV_03     "&Filter"
#define IDM_LOADLEV_04     "File:"
#define IDM_LOADLEV_05     "- File Loading Error -"
#define IDM_LOADLEV_06     "Lev#   Name                           Author"
#define IDM_LOADLEV_07     "or Direct Level Number Entry >>"
*/
#define ID_LOADLEV_00(OFFSET_DIALOGS + 25)
#define ID_LOADLEV_01(OFFSET_DIALOGS + 26)
#define ID_LOADLEV_02 802
#define ID_LOADLEV_03(OFFSET_DIALOGS + 27)
#define ID_LOADLEV_04(OFFSET_DIALOGS + 28)
#define ID_LOADLEV_05(OFFSET_DIALOGS + 29)
#define ID_LOADLEV_06(OFFSET_DIALOGS + 30)
#define ID_LOADLEV_07(OFFSET_DIALOGS + 31)
#define ID_LOADLEV_08 ID_LISTBOX
/*
#define IDM_HINTBOX_00     "Modify Hint"
#define IDM_HINTBOX_01     "&Ok"
#define IDM_HINTBOX_02     "&Cancel"
*/
#define ID_HINTBOX_00(OFFSET_DIALOGS + 32)
#define ID_HINTBOX_01(OFFSET_DIALOGS + 33)
#define ID_HINTBOX_02(OFFSET_DIALOGS + 34)
#define ID_HINTBOX_03 801
/*
#define IDM_SEARCH_00      "Filter Level Data"
#define IDM_SEARCH_01      "Enter Search String :"
#define IDM_SEARCH_02      "Search By"
#define IDM_SEARCH_03      "&Title"
#define IDM_SEARCH_04      "&Author"
#define IDM_SEARCH_05      "&Cancel"
#define IDM_SEARCH_06      "&Ok"
#define IDM_SEARCH_07      "ICON1"
#define IDM_SEARCH_08      "&Only Unsolved Levels"
#define IDM_SEARCH_09      "&Filter by Difficulty"
#define IDM_SEARCH_10      "Kids"
#define IDM_SEARCH_11      "Easy"
#define IDM_SEARCH_12      "Medium"
#define IDM_SEARCH_13      "Hard"
#define IDM_SEARCH_14      "Deadly"
*/
#define ID_SEARCH_00(OFFSET_DIALOGS + 35)
#define ID_SEARCH_01(OFFSET_DIALOGS + 36)
#define ID_SEARCH_02(OFFSET_DIALOGS + 37)
#define ID_SEARCH_03(OFFSET_DIALOGS + 38)
#define ID_SEARCH_04(OFFSET_DIALOGS + 39)
#define ID_SEARCH_05(OFFSET_DIALOGS + 40)
#define ID_SEARCH_06(OFFSET_DIALOGS + 41)
#define ID_SEARCH_07 801
#define ID_SEARCH_08(OFFSET_DIALOGS + 42)
#define ID_SEARCH_09(OFFSET_DIALOGS + 43)
#define ID_SEARCH_10(OFFSET_DIALOGS + 44)
#define ID_SEARCH_11(OFFSET_DIALOGS + 45)
#define ID_SEARCH_12(OFFSET_DIALOGS + 46)
#define ID_SEARCH_13(OFFSET_DIALOGS + 47)
#define ID_SEARCH_14(OFFSET_DIALOGS + 48)
/*
#define IDM_RETBOX_00      "&Return to Game"
*/
#define ID_RETBOX_00(OFFSET_DIALOGS + 49)
/*
#define IDM_WINBOX_00      "&Ok"
#define IDM_WINBOX_01      "You Won ! ! !"
#define IDM_WINBOX_02      "File :"
#define IDM_WINBOX_03      "- Error -"
*/
#define ID_WINBOX_00(OFFSET_DIALOGS + 50)
#define ID_WINBOX_01(OFFSET_DIALOGS + 51)
#define ID_WINBOX_02(OFFSET_DIALOGS + 52)
#define ID_WINBOX_03(OFFSET_DIALOGS + 53)
#define ID_WINBOX_04 801
#define ID_WINBOX_05 802
#define ID_WINBOX_06 803
/*
#define IDM_LOADTID_00     "Pick Tunnel ID #"
#define IDM_LOADTID_03     "&Ok"
#define IDM_LOADTID_04     "Enter the ID Number for this Tunnel"
*/
#define ID_LOADTID_00(OFFSET_DIALOGS + 54)
#define ID_LOADTID_01 801
#define ID_LOADTID_02 802
#define ID_LOADTID_03(OFFSET_DIALOGS + 55)
#define ID_LOADTID_04(OFFSET_DIALOGS + 56)
/*
#define IDM_HIGHBOX_00     "! New High Score !"
#define IDM_HIGHBOX_01     "&Ok"
#define IDM_HIGHBOX_02     "Level Number :"
#define IDM_HIGHBOX_03     "Level Name :"
#define IDM_HIGHBOX_04     "Moves :"
#define IDM_HIGHBOX_05     "Shots :"
#define IDM_HIGHBOX_06     "0"
#define IDM_HIGHBOX_07     "0"
#define IDM_HIGHBOX_08     "0"
#define IDM_HIGHBOX_09     " "
#define IDM_HIGHBOX_10     "Initials :"
#define IDM_HIGHBOX_12     "Global HS :"
#define IDM_HIGHBOX_13     "- No Data -"
*/
#define ID_HIGHBOX_00(OFFSET_DIALOGS + 57)
#define ID_HIGHBOX_01(OFFSET_DIALOGS + 58)
#define ID_HIGHBOX_02(OFFSET_DIALOGS + 59)
#define ID_HIGHBOX_03(OFFSET_DIALOGS + 60)
#define ID_HIGHBOX_04(OFFSET_DIALOGS + 61)
#define ID_HIGHBOX_05(OFFSET_DIALOGS + 62)
#define ID_HIGHBOX_06 103
#define ID_HIGHBOX_07 104
#define ID_HIGHBOX_08 ID_LISTBOX
#define ID_HIGHBOX_09 102
#define ID_HIGHBOX_10(OFFSET_DIALOGS + 63)
#define ID_HIGHBOX_12(OFFSET_DIALOGS + 64)
#define ID_HIGHBOX_13(OFFSET_DIALOGS + 65)
#define ID_HIGHBOX_14 105
#define ID_HIGHBOX_15 106
/*
#define IDM_HIGHLIST_00    "High Scores"
#define IDM_HIGHLIST_01    "&Ok"
#define IDM_HIGHLIST_02    "- File Loading Error -"
#define IDM_HIGHLIST_03    "Lev#  Name                          Moves  Shots  Initials"
*/
#define ID_HIGHLIST_00(OFFSET_DIALOGS + 66)
#define ID_HIGHLIST_01(OFFSET_DIALOGS + 67)
#define ID_HIGHLIST_02(OFFSET_DIALOGS + 68)
#define ID_HIGHLIST_03(OFFSET_DIALOGS + 69)
/*
#define IDM_GHIGHLIST_00   "Global High Scores"
#define IDM_GHIGHLIST_01   "&Ok"
#define IDM_GHIGHLIST_02   "Lev#  Name                             M      S   Init   M     S  Init"
#define IDM_GHIGHLIST_03   "Global"
#define IDM_GHIGHLIST_04   "Local"
#define IDM_GHIGHLIST_05   "- No Data -"
#define IDM_GHIGHLIST_06   "&Beat"
*/
#define ID_GHIGHLIST_00(OFFSET_DIALOGS + 70)
#define ID_GHIGHLIST_01(OFFSET_DIALOGS + 71)
#define ID_GHIGHLIST_02(OFFSET_DIALOGS + 72)
#define ID_GHIGHLIST_03(OFFSET_DIALOGS + 73)
#define ID_GHIGHLIST_04(OFFSET_DIALOGS + 74)
#define ID_GHIGHLIST_05(OFFSET_DIALOGS + 75)
#define ID_GHIGHLIST_06(OFFSET_DIALOGS + 76)
/*
#define IDM_RECBOX_00      "Recording Game"
#define IDM_RECBOX_01      "Please Enter Your Name"
#define IDM_RECBOX_02      "&Ok"
*/
#define ID_RECBOX_00(OFFSET_DIALOGS + 77)
#define ID_RECBOX_01(OFFSET_DIALOGS + 78)
#define ID_RECBOX_02(OFFSET_DIALOGS + 79)
#define ID_RECBOX_03 101
/*
#define IDM_PLAYBOX_00     "Playback Game"
#define IDM_PLAYBOX_01     "&Close"
#define IDM_PLAYBOX_02     "&Play"
#define IDM_PLAYBOX_03     "&Reset"
#define IDM_PLAYBOX_04     "&Fast"
#define IDM_PLAYBOX_05     "&Slow"
#define IDM_PLAYBOX_06     "S&tep"
#define IDM_PLAYBOX_07     "Step :"
#define IDM_PLAYBOX_08     "of"
#define IDM_PLAYBOX_09     "0"
#define IDM_PLAYBOX_10     "0"
#define IDM_PLAYBOX_11     "Speed"
*/
#define ID_PLAYBOX_00(OFFSET_DIALOGS + 80)
#define ID_PLAYBOX_01(OFFSET_DIALOGS + 81)
#define ID_PLAYBOX_02(OFFSET_DIALOGS + 82)
#define ID_PLAYBOX_03(OFFSET_DIALOGS + 83)
#define ID_PLAYBOX_04(OFFSET_DIALOGS + 84)
#define ID_PLAYBOX_05(OFFSET_DIALOGS + 85)
#define ID_PLAYBOX_06(OFFSET_DIALOGS + 86)
#define ID_PLAYBOX_07(OFFSET_DIALOGS + 87)
#define ID_PLAYBOX_08(OFFSET_DIALOGS + 88)
#define ID_PLAYBOX_09 103
#define ID_PLAYBOX_10 104
#define ID_PLAYBOX_11(OFFSET_DIALOGS + 89)
/*
#define IDM_PICKLEVEL_00   "Save Laser Tank Level"
#define IDM_PICKLEVEL_01   "&Ok"
#define IDM_PICKLEVEL_02   "Enter the Level Number to"
#define IDM_PICKLEVEL_03   "Save :"
#define IDM_PICKLEVEL_04   "0 - 10"
#define IDM_PICKLEVEL_05   "icon1"
#define IDM_PICKLEVEL_06   "= Add"
#define IDM_PICKLEVEL_07   "11"
#define IDM_PICKLEVEL_08   "&Clear High Score"
*/
#define ID_PICKLEVEL_00(OFFSET_DIALOGS + 90)
#define ID_PICKLEVEL_01(OFFSET_DIALOGS + 91)
#define ID_PICKLEVEL_02(OFFSET_DIALOGS + 92)
#define ID_PICKLEVEL_03(OFFSET_DIALOGS + 93)
#define ID_PICKLEVEL_04 103
#define ID_PICKLEVEL_05 101
// MGY - About dialog Bug - 2005/07/08
#define ID_PICKLEVEL_06(OFFSET_DIALOGS + 94)
#define ID_PICKLEVEL_07 104
#define ID_PICKLEVEL_08(OFFSET_DIALOGS + 95)

// lt_sfx.h
/*******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************/

// This is the header file for the Sound unit of Lasertank

#define MaxSounds 20

typedef enum LT_Sound_Types {
	S_Bricks = 1, S_Fire, S_Move, S_Head, S_Turn,
		S_EndLev, S_Die, S_Anti1, S_Anti2, S_Deflb,
		S_LaserHit, S_Push2, S_Push1, S_Rotate, S_Push3,
		S_Sink
};

extern int Sound_On;

// Function Prototypes

void SoundPlay(int);
void SFxInit(void);

// lt_sfx.c
/*******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **                  Sound Unit                       **
 *******************************************************)

  All Sounds are Wav files loaded into the resource file.
  Because lcc-win32 can't handle user defined resources, the wav files
  are converted into a charecter stream and imported as RCData
*/
#include <windows.h>            // required for all Windows applications

#include <mmsystem.h>

#include "lt_sfx.h"            // prototypes specific to this application

// SFx[] 0:BRICKS, 1:FIRE, 2:MOVE, 3:HEAD, 4:TURN, 5:ENDLEV, 6:DIE, 7:ANTI1, 8:ANTI2, 9:DEFLB, 10:LASER2, 11:PUSH2, 12:PUSH1, 13:ROTATE, 14:PUSH3, 15:SINK
HGLOBAL SFx[MaxSounds]; // Array of handles to sound resources. Set by SFxInit()->SoundLoad('resource_name')
int LastSFWord = 0;
int SFXError = 0;
int Sound_On = 1; // true when sound is on
extern HINSTANCE hInst; // Globally Defined Instance

// Declare Local Function
static void SoundLoad(char * s);

void SoundPlay(int sn) {
	char * p;
	if (!Sound_On) return;
	if (SFXError) return;
	p = LockResource(SFx[sn]);
	PlaySound(p, 0, 5); // 5 = memory & async
}

static void SoundLoad(char * s) {
	HGLOBAL h;

	if (SFXError) return;
	h = LoadResource(hInst, FindResource(hInst, s, RT_RCDATA));
	if (h == 0)
		SFXError = LastSFWord + 1;
	else {
		LastSFWord++;
		SFx[LastSFWord] = h; // put resource handle in Sound Array
	}
}

void SFxInit(void) {
	SoundLoad("BRICKS");
	SoundLoad("FIRE");
	SoundLoad("MOVE");
	SoundLoad("HEAD");
	SoundLoad("TURN");
	SoundLoad("ENDLEV");
	SoundLoad("DIE");
	SoundLoad("ANTI1");
	SoundLoad("ANTI2");
	SoundLoad("DEFLB");
	SoundLoad("LASER2");
	SoundLoad("PUSH2");
	SoundLoad("PUSH1");
	SoundLoad("ROTATE");
	SoundLoad("PUSH3");
	SoundLoad("SINK");
	if (SFXError) MessageBox(0, "Loading Error", "SFx Error", MB_OK);
}

// language.c
/*******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 *******************************************************/

// Language.c

#include <windows.h>

#include <windowsx.h>

#include <commdlg.h>

#include <string.h>

#include <mmsystem.h>

#include <stdlib.h>

#include <stdio.h>

#include "ltank.h"

char LANGText[SIZE_ALL][MAX_LANG_SIZE]; // All lines of Language.dat
char LANGFile[MAX_PATH]; // the dynamic file name for Language.dat
TCHAR szFilterOFN[MAX_PATH];
TCHAR szFilterPBfn[MAX_PATH];

// ************************************************************************
// These are the originals texts for all messages. Copied into LangText and replaced with lines from Language.dat
// ************************************************************************
char * App_Strings[SIZE_BUTTON + SIZE_TEXT] = {
	// This is the Button Text
	"Undo",
	"Save Position",
	"Restore Position",
	"New",
	"<< Level",
	"Level >>",
	"Hint",
	"Restart",
	"Load Level",

	// This is others texts
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
	"LaserTank.hlp"
};

// ************************************************************************
// If Language File, set windowstext with this text
// ************************************************************************
//SetWindowText(GetDlgItem(Dialog,ID_ABOUTBOX_02),App_Title);

void LoadWindowText(HWND hDlg, int nIDDlgItem) {
	if (LANGText[nIDDlgItem][0] != '\0')
		SetWindowText(GetDlgItem(hDlg, nIDDlgItem), LANGText[nIDDlgItem]);
}
void LoadWindowCaption(HWND hDlg, int nIDDlgItem) {
	if (LANGText[nIDDlgItem][0] != '\0')
		SetWindowText(hDlg, LANGText[nIDDlgItem]);
}

// ************************************************************************
// Read the language file is exist
// fill the LANGText[],
// update the two menus,
// ************************************************************************
void InitLanguage(HMENU MMenu, HMENU EMenu) {
	int i;
	FILE * fd;
	char szTmp[MAX_LANG_SIZE];

	// Initialyse with default values
	for (i = 0; i < SIZE_BUTTON + SIZE_TEXT; i++)
		strcpy(LANGText[i], App_Strings[i]);

	// Clear default messages dialogs
	for (i = OFFSET_DIALOGS; i < OFFSET_ABOUTMSG + SIZE_ABOUTMSG; i++)
		strcpy(LANGText[i], "\0");

	fd = fopen(LANGFile, "r"); // LANGFile == Setups\US\Language\Language.dat

	if (fd != NULL) {
		i = 0;
		while (!feof(fd)) {
			fgets(szTmp, MAX_LANG_SIZE, fd); // Load lines from Language.dat into szTmp
			if (szTmp[0] != '\0') {
				szTmp[strlen(szTmp) - 1] = '\0'; // remove the last char
				if ((szTmp[0] != '\0') && (szTmp[0] != '#')) // ignore blankc & comment lines and don't increment counter i
				{
					ConvertTabChar(szTmp); // replace \t and \n

					if ((i >= START_MMENU) && (i < START_MMENU + SIZE_MMENU)) // if 0 <= i < 49 (main menu items)
						ChangeMenuText(MMenu, szTmp);

					else if ((i >= START_EMENU) && (i < START_EMENU + SIZE_EMENU)) // if 49 <= i < 73  (edit menu items)
						ChangeMenuText(EMenu, szTmp);

					else if ((i >= START_BUTTON) &&
						(i < (START_BUTTON + SIZE_BUTTON + SIZE_TEXT + SIZE_ABOUTMSG + SIZE_DIALOGS))) // if 73 <= i < 240
						strcpy(LANGText[i - START_BUTTON], szTmp); // save over LANGText[ 0:167 ] 
					i++;
				}
			}
		}
		fclose(fd);
	}
}

// Used by ChangeMenuText() - Converts 00, 01, or --, to menu level int
int DecodeMenuInt(char * MenuStr) {
	if (MenuStr[0] == '0')
		return ((int)(MenuStr[1] - '0'));

	if (MenuStr[0] == '1')
		return ((int)(10 + (MenuStr[1] - '0')));
	else
		return (-1);
}

// ************************************************************************
// To change a menu text with this syntax :
// 00,01,02,&Text
//
// ************************************************************************
void ChangeMenuText(HMENU hMenu, char * MenuStr) {
	// MenuStr starts with 3 double digit values showing the position
	// i.e. '00,14,--,Play&back Game...\tF7'
	// -> item 00, sub-item 14, sub-sub-item (not), text=Playback Game...  F7 with underline on &b

	MENUITEMINFO ItemInfo;
	int nMenu;
	int nMenu1;
	int nMenu2;

	if ((strlen(MenuStr) > 9) && (hMenu != NULL)) {
		nMenu = DecodeMenuInt((char * )(MenuStr + 0)); // Top position
		nMenu1 = DecodeMenuInt((char * )(MenuStr + 3)); // Sub menu position
		nMenu2 = DecodeMenuInt((char * )(MenuStr + 6)); // Sub-sub menu position
		if (nMenu2 >= 0) {
			//https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsubmenu
			// GetSubMenu(menu handle, position that activates drop down)
			hMenu = GetSubMenu(hMenu, nMenu);
			hMenu = GetSubMenu(hMenu, nMenu1);
			nMenu = nMenu2;
		} else {
			if (nMenu1 >= 0) {
				hMenu = GetSubMenu(hMenu, nMenu);
				nMenu = nMenu1;
			}
		}

		memset( & ItemInfo, 0, sizeof(MENUITEMINFO));
		ItemInfo.cbSize = sizeof(MENUITEMINFO);
		ItemInfo.fMask = MIIM_TYPE;
		GetMenuItemInfo(hMenu, nMenu, TRUE, & ItemInfo);
		if (ItemInfo.fType == MFT_STRING) {
			// Replace menu item.
			ItemInfo.dwTypeData = (char * )(MenuStr + 9);
			ItemInfo.cch = lstrlen(ItemInfo.dwTypeData);
			SetMenuItemInfo(hMenu, nMenu, TRUE, & ItemInfo);
		}
	}
}

void ConvertTabChar(char * szBuffer) {
	char * P;
	char * Q;

	P = strchr(szBuffer, '\\');
	while (P) {
		// case of \t
		if ( * (P + 1) == 't') {
			* P++ = '\t';
			for (Q = P;* Q != 0; Q++)
				*
				Q = * (char * )(Q + 1);
		} else {
			// case of \n
			if ( * (P + 1) == 'n') {
				* P++ = 0x0d;
				* P = 0x0a;
			} else P++;
		}
		// Search the next occurence
		P = strchr(P, '\\');
	}

}

// ************************************************************************
// Load Resource Bitmap or File
// ************************************************************************
HBITMAP LoadImageFile(HINSTANCE hInst, char * szBitmapRes, char * szBitmapFile) {

	HBITMAP hbm;
	char * P;
	char lpszName[MAX_PATH];

	GetModuleFileName(NULL, lpszName, MAX_PATH);
	P = strrchr(lpszName, '\\');
	if (P) {
		P++;
		strcpy(P, TEXT(LANGFilePath)); // add path
		P += strlen(TEXT(LANGFilePath));
		strcpy(P, szBitmapFile); // add name
	}
	hbm = (HBITMAP) LoadImage(NULL, lpszName, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION);
	if (hbm == NULL) {
		hbm = LoadBitmap(hInst, szBitmapRes);
	}
	return (hbm);
}

// ltank_d.h
/*******************************************************
 **             Laser Tank ver 3.2a                   **
 **               By Jim Kindley                      **
 **               (c) 2000                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 *******************************************************/

// Dialog Callback functions
LRESULT CALLBACK AboutBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK DeadBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK DiffBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK RetBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK LoadBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK HintBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK PickBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK WinBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK HSBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK RecordBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK PBWindow(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK HSList(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK GHSList(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK GraphBox(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK LoadTID(HWND, UINT, WPARAM, LPARAM);

void DrawLevels(LPARAM);

extern int FileHand, HSClear;
extern HWND PlayH, PBCountH;

// ltank_d.c
/*******************************************************
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
 *******************************************************/
#include <windows.h>

#include <string.h>

#include <stdio.h>

#include <ole2.h>

#include <shlobj.h>

#include "ltank.h"

#include "ltank_d.h"

#define PHDC(pDIS -> hDC)
#define PRC(pDIS -> rcItem)

const long DifCList[6] = {
	0x00FFFFFF,
	0x0000FFFF,
	0x00FFFF00,
	0x0000FF00,
	0x00FF00FF,
	0x000000FF
}; //Colours for level info text based on difficulty number

HBRUSH hbrBack;
DRAWITEMSTRUCT FAR * pDIS;
int HSClear, LastOfList, DispAll;
THSREC HS, GHS;
TSEARCH SearchRec;
HWND PBCountH, PlayH;
extern int QHELP;
DWORD OldProcEdit;

// Will Set the Starting Directory for the Browsing
INT CALLBACK BrowseCallBack(HWND hwnd, UINT uMsg, LPARAM lp, LPARAM pData) {
	if (uMsg == BFFM_INITIALIZED)
		SendMessage(hwnd, BFFM_SETSELECTION, TRUE, (LPARAM) & GraphDN);
	return (0);
}

/************************************************************************************
Browse
Action: Uses SHBrowseForFolder to allow the user to browse their shell namespace
Paramaters: hwndOwner - handle to owner window
		   lpszDir - pointer to string that will be filled with the user's selection
					 Assumed to be MAX_PATH
		   lpszTitle - any text that you would like to be displayed in the window
Return value: TRUE if successful, FALSE if there was a problem
************************************************************************************/
BOOL Browse(HWND hwndOwner, LPTSTR lpszDir, LPCTSTR lpszTitle) {
	BROWSEINFO bi;
	LPITEMIDLIST pidl;
	IMalloc * pMalloc;

	OleInitialize(NULL);

	if (FAILED(SHGetMalloc( & pMalloc))) return FALSE;

	// fill BROWSEINFO struct
	bi.hwndOwner = hwndOwner; // owner window
	bi.pidlRoot = NULL; // folder to start in - NULL for My Computer
	bi.pszDisplayName = lpszDir; // pointer to string that gets folder display name
	bi.lpszTitle = lpszTitle; // pointer to text to display in window
	bi.ulFlags = BIF_RETURNONLYFSDIRS; // flags - see API docs for BROWSEINFO
	bi.lpfn = BrowseCallBack; // callback function - usually not needed
	bi.lParam = 0; // parameter to callback function

	pidl = SHBrowseForFolder( & bi);

	if (!pidl)
		return FALSE;

	// SHBrowseForFolder filled lpszDir with the name of the chosen item,
	// but it did not give us the full path to it. So, we need to get
	// that using SHGetPathFromIDList.
	if (!SHGetPathFromIDList(pidl, lpszDir)) return FALSE;
	pMalloc -> lpVtbl -> Free(pMalloc, pidl);
	pMalloc -> lpVtbl -> Release(pMalloc);
	return TRUE;
}

// Used By Load, HighScore & Global High Score ListBoxs
int TransListKey(HWND Dialog, INT Key) {
	int i;

	switch (Key) {
	case VK_HOME:
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, 0, 0);
		break;
	case VK_UP:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) - 1;
		if (i > -1) SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0);
		break;
	case VK_DOWN:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) + 1;
		if (i <= LastOfList) SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0);
		break;
	case VK_END:
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, LastOfList, 0);
		break;
	case VK_PRIOR:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) - 10;
		if (i > -1) SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0);
		break;
	case VK_NEXT:
		i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0) + 10;
		if (i <= LastOfList) SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, i, 0);
		break;
	case VK_ESCAPE:
		EndDialog(Dialog, 0);
	}
	return (-2);
}
// ---- About Box Dialog Procedure ----
//  This is an About box with an Edit window that has text in it from the
//  resource file. The text is stored as RCData.
LRESULT CALLBACK AboutBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	char * p;
	char AboutMsg[SIZE_ABOUTMSG * MAX_LANG_SIZE + 1];
	int i;
	HGLOBAL h;

	switch (Message) {
	case WM_INITDIALOG:
		// Grab the Text for the About Edit window
		h = LoadResource(hInst, FindResource(hInst, "About", RT_RCDATA));
		if (LANGText[OFFSET_ABOUTMSG][0] != '\0') {
			AboutMsg[0] = '\0';
			for (i = 0; i < SIZE_ABOUTMSG; i++)
				strcat(AboutMsg, LANGText[OFFSET_ABOUTMSG + i]);
			p = AboutMsg;
		} else
			p = LockResource(h);

		LoadWindowCaption(Dialog, ID_ABOUTBOX_00);
		LoadWindowText(Dialog, ID_ABOUTBOX_OK);
		LoadWindowText(Dialog, ID_ABOUTBOX_04);
		LoadWindowText(Dialog, ID_ABOUTBOX_06);

		SetWindowText(GetDlgItem(Dialog, ID_ABOUTBOX_02), App_Title);
		SetWindowText(GetDlgItem(Dialog, ID_ABOUTBOX_03), App_Version);
		SetWindowText(GetDlgItem(Dialog, ID_ABOUTBOX_07), p);
		FreeResource(h);
		return (TRUE);
	case WM_COMMAND:
		if (wparam == ID_ABOUTBOX_OK) EndDialog(Dialog, 1);
	}
	return (0);
}

// ---- DeadBox Dialog Procedure ----
// This dialog Proc is used for the DeadBox dialog.
// It returns the value of the button pressed.}
LRESULT CALLBACK DeadBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowText(Dialog, ID_DEADBOX_UNDO);
		LoadWindowText(Dialog, ID_DEADBOX_DEAD);
		LoadWindowText(Dialog, ID_DEADBOX_RESTART);
		return (TRUE); // I need this or I don't kave [tab] key }
	case WM_COMMAND:
		if (Game.RecP > 1) EndDialog(Dialog, wparam); // end dialog with button id }
		else EndDialog(Dialog, ID_DEADBOX_RESTART); // reset if first turn
	}
	return (0);
}

// ---- RetBox Dialog Procedure ----
// This dialog Proc is used for "Return to Game".
// It returns the value of the button pressed.}
//function DefBox(Dialog: HWnd; Message, WParam: Word;LParam: Longint): Bool; export;
LRESULT CALLBACK RetBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowText(Dialog, ID_RETBOX_00);
		return (TRUE); // I need this or I don't kave [tab] key }
	case WM_COMMAND:
		if (Game.RecP > 1) EndDialog(Dialog, wparam); // end dialog with button id }
		else EndDialog(Dialog, 2); // reset if first turn
	}
	return (0);
}

// ---- Search Box Dialog Procedure ----
//  The Load Box uses this proc to select a Search term and type
LRESULT CALLBACK SearchBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	int i, j;

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_SEARCH_00);
		LoadWindowText(Dialog, ID_SEARCH_01);
		LoadWindowText(Dialog, ID_SEARCH_02);
		LoadWindowText(Dialog, ID_SEARCH_03);
		LoadWindowText(Dialog, ID_SEARCH_04);
		LoadWindowText(Dialog, ID_SEARCH_05);
		LoadWindowText(Dialog, ID_SEARCH_06);

		LoadWindowText(Dialog, ID_SEARCH_08);
		LoadWindowText(Dialog, ID_SEARCH_09);
		LoadWindowText(Dialog, ID_SEARCH_10);
		LoadWindowText(Dialog, ID_SEARCH_11);
		LoadWindowText(Dialog, ID_SEARCH_12);
		LoadWindowText(Dialog, ID_SEARCH_13);
		LoadWindowText(Dialog, ID_SEARCH_14);

		SendMessage(GetDlgItem(Dialog, ID_SEARCH_03), BM_SETCHECK, 1, 0);
		SearchRec.mode = 1;
		return (TRUE);
	case WM_COMMAND:
		switch (LOWORD(wparam)) {
		case ID_SEARCH_06:
		case 1:
			GetWindowText(GetDlgItem(Dialog, ID_SEARCH_07), SearchRec.data, 60);
			strupr(SearchRec.data);
			if (SendMessage(GetDlgItem(Dialog, ID_SEARCH_03), BM_GETCHECK, 0, 0) != 0) SearchRec.mode = 1;
			else SearchRec.mode = 2;
			if (SendMessage(GetDlgItem(Dialog, ID_SEARCH_09), BM_GETCHECK, 0, 0)) {
				SearchRec.Diff = 0;
				if (SendDlgItemMessage(Dialog, ID_SEARCH_10, BM_GETCHECK, 0, 0) == 1) SearchRec.Diff++;
				if (SendDlgItemMessage(Dialog, ID_SEARCH_11, BM_GETCHECK, 0, 0) == 1) SearchRec.Diff = SearchRec.Diff + 2;
				if (SendDlgItemMessage(Dialog, ID_SEARCH_12, BM_GETCHECK, 0, 0) == 1) SearchRec.Diff = SearchRec.Diff + 4;
				if (SendDlgItemMessage(Dialog, ID_SEARCH_13, BM_GETCHECK, 0, 0) == 1) SearchRec.Diff = SearchRec.Diff + 8;
				if (SendDlgItemMessage(Dialog, ID_SEARCH_14, BM_GETCHECK, 0, 0) == 1) SearchRec.Diff = SearchRec.Diff + 16;
			} else SearchRec.Diff = 255;
			SearchRec.SkipComp = SendMessage(GetDlgItem(Dialog, 200), BM_GETCHECK, 0, 0);
			EndDialog(Dialog, 1);
			break;
		case 2:
		case ID_SEARCH_05:
			EndDialog(Dialog, 2);
			break;
		case ID_SEARCH_09:
			j = SendMessage(GetDlgItem(Dialog, ID_SEARCH_09), BM_GETCHECK, 0, 0);
			for (i = ID_SEARCH_10; i <= ID_SEARCH_14; i++) EnableWindow(GetDlgItem(Dialog, i), j);
		}
	}
	return (0);
}

// ---- Difficulty Box Dialog Procedure ----
LRESULT CALLBACK DiffBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	char temps[40];
	switch (Message) {
	case WM_INITDIALOG:
		if ((Difficulty & 1) == 1) SendDlgItemMessage(Dialog, ID_DIFFBOX_02, BM_SETCHECK, 1, 0);
		if ((Difficulty & 2) == 2) SendDlgItemMessage(Dialog, ID_DIFFBOX_03, BM_SETCHECK, 1, 0);
		if ((Difficulty & 4) == 4) SendDlgItemMessage(Dialog, ID_DIFFBOX_04, BM_SETCHECK, 1, 0);
		if ((Difficulty & 8) == 8) SendDlgItemMessage(Dialog, ID_DIFFBOX_05, BM_SETCHECK, 1, 0);
		if ((Difficulty & 16) == 16) SendDlgItemMessage(Dialog, ID_DIFFBOX_06, BM_SETCHECK, 1, 0);

		LoadWindowCaption(Dialog, ID_DIFFBOX_00);
		LoadWindowText(Dialog, ID_DIFFBOX_01);
		LoadWindowText(Dialog, ID_DIFFBOX_02);
		LoadWindowText(Dialog, ID_DIFFBOX_03);
		LoadWindowText(Dialog, ID_DIFFBOX_04);
		LoadWindowText(Dialog, ID_DIFFBOX_05);
		LoadWindowText(Dialog, ID_DIFFBOX_06);
		LoadWindowText(Dialog, ID_DIFFBOX_07);
		LoadWindowText(Dialog, ID_DIFFBOX_08);
		return (TRUE);
	case WM_COMMAND:
		switch (wparam) {
		case 1:
		case ID_DIFFBOX_01:
			Difficulty = 0;
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_02, BM_GETCHECK, 0, 0) == 1) Difficulty++;
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_03, BM_GETCHECK, 0, 0) == 1) Difficulty = Difficulty + 2;
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_04, BM_GETCHECK, 0, 0) == 1) Difficulty = Difficulty + 4;
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_05, BM_GETCHECK, 0, 0) == 1) Difficulty = Difficulty + 8;
			if (SendDlgItemMessage(Dialog, ID_DIFFBOX_06, BM_GETCHECK, 0, 0) == 1) Difficulty = Difficulty + 16;
			itoa(Difficulty, temps, 10);
			WritePrivateProfileString("DATA", psDiff, temps, INIFile);
			if (Difficulty > 0) EndDialog(Dialog, 0);
			break;
		case ID_DIFFBOX_07:
			SendDlgItemMessage(Dialog, ID_DIFFBOX_02, BM_SETCHECK, 1, 0);
			SendDlgItemMessage(Dialog, ID_DIFFBOX_03, BM_SETCHECK, 1, 0);
			SendDlgItemMessage(Dialog, ID_DIFFBOX_04, BM_SETCHECK, 1, 0);
			SendDlgItemMessage(Dialog, ID_DIFFBOX_05, BM_SETCHECK, 1, 0);
			SendDlgItemMessage(Dialog, ID_DIFFBOX_06, BM_SETCHECK, 1, 0);
		}
	}
	return (0);
}

// ---- Load Box Dialog Procedure ----
//  List out all levels in the current data file, by number & title.
//  return with the level # + 101 or 0 if canceled}
LRESULT CALLBACK LoadBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	TLEVEL TempRecData;
	THSREC TempHSData;
	char temps[80], t2[90];
	char * P;
	int i, j;

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_LOADLEV_00);
		LoadWindowText(Dialog, ID_LOADLEV_01);
		LoadWindowText(Dialog, ID_LOADLEV_03);
		LoadWindowText(Dialog, ID_LOADLEV_04);
		LoadWindowText(Dialog, ID_LOADLEV_05);
		LoadWindowText(Dialog, ID_LOADLEV_06);
		LoadWindowText(Dialog, ID_LOADLEV_07);
		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
		if (F1 == INVALID_HANDLE_VALUE) return (TRUE); // File NOT Found
		P = strrchr(FileName, '\\');
		if (P == NULL) P = FileName;
		else P++;
		SetWindowText(GetDlgItem(Dialog, ID_LOADLEV_05), P);
		i = SetFilePointer(F1, 0, NULL, FILE_END) / sizeof(TLEVEL);
		SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_INITSTORAGE, i, 72);
		SetFilePointer(F1, 0, NULL, FILE_BEGIN);
		i = 1;
		ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, NULL);
		while (BytesMoved == sizeof(TLEVEL)) {
			sprintf(temps, "%4d   %-30.30s %s", i, TempRecData.LName, TempRecData.Author);
			switch (TempRecData.SDiff) {
			case 1:
				t2[0] = '1';
				break;
			case 2:
				t2[0] = '2';
				break;
			case 4:
				t2[0] = '3';
				break;
			case 8:
				t2[0] = '4';
				break;
			case 16:
				t2[0] = '5';
				break;
			default:
				t2[0] = '0';
			}
			strcpy(t2 + 1, temps);
			SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_ADDSTRING, 0, (LPARAM) t2);
			i++;
			ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, NULL);
		}
		LastOfList = i - 2;
		CloseHandle(F1);
		SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_SETCURSEL, CurLevel - 1, 0);
		return (TRUE);
	case WM_CTLCOLORLISTBOX:
		return ((int) GetStockObject(BLACK_BRUSH));
		break;
	case WM_MEASUREITEM:
		((MEASUREITEMSTRUCT FAR * ) lparam) -> itemHeight = 14;
		break;
	case WM_DRAWITEM:
		DrawLevels(lparam);
		return TRUE;
	case WM_VKEYTOITEM:
		return (TransListKey(Dialog, LOWORD(wparam)));
	case WM_COMMAND:
		switch (LOWORD(wparam)) {
		case 1: // Pressing Enter will get you here
			GetWindowText(GetDlgItem(Dialog, ID_LOADLEV_02), temps, 10);
			i = atoi(temps);
			if (i) {
				EndDialog(Dialog, i + 100);
				break;
			}
			case ID_LOADLEV_08:
				if (((HIWORD(wparam) != LBN_SELCHANGE)) && (wparam != 1)) return (0);
				i = SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_GETCURSEL, 0, 0);
				SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_GETTEXT, i, (LPARAM) temps);
				temps[5] = (char) 0;
				i = 1;
				while (temps[i] == ' ') i++; // strip leading spaces
				i = atoi( & temps[i]);
				EndDialog(Dialog, i + 100); // Add 100 to the Select #
				break;
			case ID_LOADLEV_01:
				EndDialog(Dialog, 0);
				break;
			case ID_LOADLEV_03: // Search
				i = DialogBox(hInst, "Search", Dialog, (DLGPROC) SearchBox);
				if (i == 1) // idOk
				{
					SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_RESETCONTENT, 0, 0);
					F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
						FILE_FLAG_SEQUENTIAL_SCAN, NULL);
					if (SearchRec.SkipComp) F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
					else F2 = INVALID_HANDLE_VALUE;
					if (F2 == INVALID_HANDLE_VALUE) SearchRec.SkipComp = FALSE;
					ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, NULL);
					LastOfList = -1;
					while (BytesMoved == sizeof(TLEVEL)) {
						if (SearchRec.SkipComp) ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
						if (BytesMoved < sizeof(THSREC)) TempHSData.moves = 0;
						if (SearchRec.mode == 1) strcpy(temps, TempRecData.LName);
						else strcpy(temps, TempRecData.Author);
						if (TempRecData.SDiff == 0) TempRecData.SDiff = 255;
						if (strstr(strupr(temps), SearchRec.data) && (TempRecData.SDiff & SearchRec.Diff) &&
							((SearchRec.SkipComp == 0) || (TempHSData.moves == 0))) {
							sprintf(temps, "%4d   %-30.30s %s", i, TempRecData.LName, TempRecData.Author);
							switch (TempRecData.SDiff) {
							case 1:
								t2[0] = '1';
								break;
							case 2:
								t2[0] = '2';
								break;
							case 4:
								t2[0] = '3';
								break;
							case 8:
								t2[0] = '4';
								break;
							case 16:
								t2[0] = '5';
								break;
							default:
								t2[0] = '0';
							}
							strcpy(t2 + 1, temps);
							SendDlgItemMessage(Dialog, ID_LOADLEV_08, LB_ADDSTRING, 0, (LPARAM) t2);
							LastOfList++;
						}
						i++;
						ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, NULL);
					}
					CloseHandle(F1);
					if (SearchRec.SkipComp) CloseHandle(F2);
				}
		}
	}
	return (0);
}

// ---- Hint Box Dialog Procedure ----
//  The editor uses this proc to Display & Edit the Hint. If the text is modified
//  the 'Modified' varable is set.}
//function HintBox(Dialog: HWnd; Message, WParam: Word; LParam: Longint): Bool; export;
LRESULT CALLBACK HintBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_HINTBOX_00);
		LoadWindowText(Dialog, ID_HINTBOX_01);
		LoadWindowText(Dialog, ID_HINTBOX_02);
		SetWindowText(GetDlgItem(Dialog, ID_HINTBOX_03), CurRecData.Hint);
		return (TRUE);
	case WM_COMMAND:
		switch (wparam) {
		case 1:
		case ID_HINTBOX_01:
			GetWindowText(GetDlgItem(Dialog, ID_HINTBOX_03), CurRecData.Hint, 255);
			if (SendMessage(GetDlgItem(Dialog, ID_HINTBOX_03), EM_GETMODIFY, 0, 0)) Modified = TRUE;
		case 2:
		case ID_HINTBOX_02:
			EndDialog(Dialog, 2);
		}
	}
	return (0);
}

// Dont Process Space key
LRESULT CALLBACK EditProc(HWND hwnd, UINT iMsg, WPARAM wParam, LPARAM lParam) {
	if ((iMsg == WM_CHAR) && (wParam == VK_SPACE)) return (0);
	return (CallWindowProc((WNDPROC) OldProcEdit, hwnd, iMsg, wParam, lParam));
}

// ---- Win Box Dialog Procedure ----
//  This is an Win box with an Edit window that has text in it from the
//  resource file. The text is stored as RCData.}
LRESULT CALLBACK WinBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	HGLOBAL H;
	char * P;
	int x, y, i;
	RECT Box;
	THSREC TempHSData;
	char temps[100];
	char AboutMsg[SIZE_ABOUTMSG * MAX_LANG_SIZE + 1];

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowText(Dialog, ID_WINBOX_00);
		LoadWindowText(Dialog, ID_WINBOX_01);
		LoadWindowText(Dialog, ID_WINBOX_02);
		LoadWindowText(Dialog, ID_WINBOX_03);

		H = LoadResource(hInst, FindResource(hInst, "About", RT_RCDATA));
		if (LANGText[OFFSET_ABOUTMSG][0] != '\0') {
			AboutMsg[0] = '\0';
			for (i = 0; i < SIZE_ABOUTMSG; i++)
				strcat(AboutMsg, LANGText[OFFSET_ABOUTMSG + i]);
			P = AboutMsg;
		} else
			P = LockResource(H);
		SetWindowText(GetDlgItem(Dialog, ID_WINBOX_06), P);

		P = strrchr(FileName, '\\');
		if (P) P++;
		else P = FileName;
		SetWindowText(GetDlgItem(Dialog, ID_WINBOX_03), P);
		FreeResource(H);
		SetFocus(GetDlgItem(Dialog, ID_WINBOX_00));
		F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
		if (F2 == INVALID_HANDLE_VALUE) return (TRUE);
		y = 0;
		ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
		while (BytesMoved == sizeof(THSREC)) {
			if (TempHSData.moves > 0) y++;
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
		}
		CloseHandle(F2);

		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, NULL);
		x = SetFilePointer(F1, 0, NULL, FILE_END) / sizeof(TLEVEL);
		CloseHandle(F1);

		sprintf(temps, txt042, y, x); // "Completed %d of %d levels"
		SetWindowText(GetDlgItem(Dialog, ID_WINBOX_04), temps);
		if ((Difficulty & 0x1F) != 0x1F) {
			strcpy(temps, txt043); // "Difficulty Set ="
			P = temps + strlen(temps);
			strcat(temps, "         ");
			if ((Difficulty & 1) == 1) {
				P[0] = txt044[0];
				P += 2;
			} // txt044="KEMHD"
			if ((Difficulty & 2) == 2) {
				P[0] = txt044[1];
				P += 2;
			}
			if ((Difficulty & 4) == 4) {
				P[0] = txt044[2];
				P += 2;
			}
			if ((Difficulty & 8) == 8) {
				P[0] = txt044[3];
				P += 2;
			}
			if ((Difficulty & 16) == 16) {
				P[0] = txt044[4];
			}
			SetWindowText(GetDlgItem(Dialog, ID_WINBOX_05), temps);
		}
		return (TRUE);
	case WM_ERASEBKGND:
		GetClientRect(Dialog, & Box);
		SelectObject((HDC) wparam, GetStockObject(BLACK_BRUSH));
		Rectangle((HDC) wparam, Box.left, Box.top, Box.right, Box.bottom);
		return (TRUE);
	case WM_CTLCOLORSTATIC:
		SetTextColor((HDC) wparam, 0x0000FFFF);
		SetBkColor((HDC) wparam, 0);
		return ((LONG) GetStockObject(BLACK_BRUSH));
	case WM_COMMAND:
		if ((wparam == ID_WINBOX_00) || (wparam == 1)) EndDialog(Dialog, 1);
	}
	return (0);
}

// ---- Load Tunnel ID Dialog Procedure ----
// The editor uses this to pick which level ID number to assign
// to the current tunnel.
LRESULT CALLBACK LoadTID(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	char temps[40];
	int i;

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_LOADTID_00);
		LoadWindowText(Dialog, ID_LOADTID_03);
		LoadWindowText(Dialog, ID_LOADTID_04);
		return (TRUE);
	case WM_COMMAND:
		if ((wparam == ID_LOADTID_03) || (wparam == 1)) // idOk
		{
			GetWindowText(GetDlgItem(Dialog, ID_LOADTID_01), temps, 10);
			i = atoi(temps);
			if (i > 7) i = 0;
			EndDialog(Dialog, i);
			return (TRUE);
		}
	}
	return (0);
}

// ---- HS Box Dialog Procedure ---- HighBox
//  This is the New High Score box
LRESULT CALLBACK HSBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	char temps[20], old[40];

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_HIGHBOX_00);
		LoadWindowText(Dialog, ID_HIGHBOX_01);
		LoadWindowText(Dialog, ID_HIGHBOX_02);
		LoadWindowText(Dialog, ID_HIGHBOX_03);
		LoadWindowText(Dialog, ID_HIGHBOX_04);
		LoadWindowText(Dialog, ID_HIGHBOX_05);
		LoadWindowText(Dialog, ID_HIGHBOX_10);
		LoadWindowText(Dialog, ID_HIGHBOX_12);
		LoadWindowText(Dialog, ID_HIGHBOX_13);

		itoa(CurLevel, temps, 10);
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_08), temps);
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_09), CurRecData.LName);
		itoa(Game.ScoreMove, temps, 10);
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_06), temps);
		itoa(Game.ScoreShot, temps, 10);
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_07), temps);
		if (HS.moves > 0) {
			strcpy(old, txt008);
			itoa(HS.moves, temps, 10);
			strcat(old, temps);
			strcat(old, txt010);
			itoa(HS.shots, temps, 10);
			strcat(old, temps);
			strcat(old, txt011);
			strcat(old, HS.name);
			ShowWindow(GetDlgItem(Dialog, ID_HIGHBOX_15), SW_SHOW);
			SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_15), old);
		}
		GetPrivateProfileString("DATA", psUser, "", HS.name, 5, INIFile);
		SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_14), HS.name);
		F3 = CreateFile(GHFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, NULL);
		SetFilePointer(F3, (CurLevel - 1) * sizeof(GHS), NULL, FILE_BEGIN);
		ReadFile(F3, & GHS, sizeof(GHS), & BytesMoved, NULL);
		if (BytesMoved == sizeof(GHS)) {
			if ((GHS.moves == 0) || (Game.ScoreMove < GHS.moves) ||
				((Game.ScoreMove == GHS.moves) && (Game.ScoreShot < GHS.shots))) {
				SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_13), txt012);
				EnableWindow(GetDlgItem(Dialog, ID_HIGHBOX_13), TRUE);
			} else {
				strcpy(old, txt009);
				itoa(GHS.moves, temps, 10);
				strcat(old, temps);
				strcat(old, txt010);
				itoa(GHS.shots, temps, 10);
				strcat(old, temps);
				strcat(old, txt011);
				strcat(old, GHS.name);
				SetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_13), old);
			}
		}
		CloseHandle(F3);
		SetFocus(GetDlgItem(Dialog, ID_HIGHBOX_01));
		return (TRUE);
	case WM_COMMAND:
		if ((wparam == ID_HIGHBOX_01) || (wparam == 1)) {
			GetWindowText(GetDlgItem(Dialog, ID_HIGHBOX_14), temps, 5);
			HS.moves = Game.ScoreMove;
			HS.shots = Game.ScoreShot;
			if (stricmp(temps, HS.name) != 0) {
				strcpy(HS.name, temps);
				WritePrivateProfileString("DATA", psUser, HS.name, INIFile);
			}
			EndDialog(Dialog, 1);
		}
	}
	return (0);
}

void DrawLevels(LPARAM lparam) {
	int crBack, crText;
	char temps[100];

	pDIS = (DRAWITEMSTRUCT FAR * ) lparam;

	/* Draw the focus rectangle for an empty list box or an
	empty combo box to indicate that the control has the
	focus
	*/
	if ((int)(pDIS -> itemID) < 0) {
		if ((pDIS -> itemAction) & (ODA_FOCUS)) DrawFocusRect(PHDC, & PRC);
		return;
	}

	/* Get the string */
	SendMessage(pDIS -> hwndItem, LB_GETTEXT, pDIS -> itemID, (LPARAM)(LPSTR) temps);

	if ((pDIS -> itemState) & (ODS_SELECTED))
		/* Set background colors for selected item */
		crBack = 0x00404080;
	else
		/* Set background colors for unselected item */
		crBack = 0;

	crText = DifCList[0];
	switch (temps[0]) {
	case '1':
		crText = DifCList[1];
		break;
	case '2':
		crText = DifCList[2];
		break;
	case '3':
		crText = DifCList[3];
		break;
	case '4':
		crText = DifCList[4];
		break;
	case '5':
		crText = DifCList[5];
		break;
	}

	// Fill item rectangle with background color
	hbrBack = CreateSolidBrush(crBack);
	FillRect(PHDC, & PRC, hbrBack);
	DeleteObject(hbrBack);

	// Set current font, background and text colors
	SetBkColor(PHDC, crBack);
	SetTextColor(PHDC, crText);

	// TextOut uses current background and text colors
	TextOut(PHDC, PRC.left, PRC.top, temps + 1, lstrlen(temps) - 1);

	/* If enabled item has the input focus, call
	DrawFocusRect to set or clear the focus
	rectangle */
	if ((pDIS -> itemState) & (ODS_FOCUS)) DrawFocusRect(PHDC, & PRC);
}

// For :
// ---- HS List Dialog Procedure ----
// ---- Global HS List Dialog Procedure ----
// So, the ID of the Dialog Item ID_LISTBOX must be the same
// for the two dialogs !!
//
void GetGameLevel(HWND Dialog) {
	int i, j;
	char temps[100];

	i = SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETCURSEL, 0, 0);
	SendDlgItemMessage(Dialog, ID_LISTBOX, LB_GETTEXT, i, (LPARAM) temps);
	temps[5] = (char) 0;
	i = 1;
	while (temps[i] == ' ') i++; // strip leading spaces
	j = atoi( & temps[i]) - 1;
	if (CurLevel - 1 != j) {
		CurLevel = j;
		LoadNextLevel(TRUE, FALSE);
	}
	EndDialog(Dialog, 1);
}

// ---- HS List Dialog Procedure ----
//  List out all levels in the current data file, by number ,title, moves, shots & initials
LRESULT CALLBACK HSList(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {

	TLEVEL TempRecData;
	THSREC TempHSData;
	char temps[80], t2[100];
	int i, j;

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_HIGHLIST_00);
		LoadWindowText(Dialog, ID_HIGHLIST_01);
		LoadWindowText(Dialog, ID_HIGHLIST_02);
		LoadWindowText(Dialog, ID_HIGHLIST_03);

		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
		if (F1 == INVALID_HANDLE_VALUE) return (TRUE); // File NOT Found
		F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
		if (F2 == INVALID_HANDLE_VALUE) {
			CloseHandle(F1);
			return (TRUE);
		}
		SetWindowText(GetDlgItem(Dialog, ID_HIGHLIST_02), HFileName);
		i = SetFilePointer(F2, 0, NULL, FILE_END) / sizeof(THSREC);
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_INITSTORAGE, i, 54);
		SetFilePointer(F2, 0, NULL, FILE_BEGIN);
		i = 1;
		ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
		while (BytesMoved == sizeof(THSREC)) {
			ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, NULL);
			sprintf(temps, "%4d %-30.30s", i, TempRecData.LName);
			switch (TempRecData.SDiff) {
			case 1:
				t2[0] = '1';
				break;
			case 2:
				t2[0] = '2';
				break;
			case 4:
				t2[0] = '3';
				break;
			case 8:
				t2[0] = '4';
				break;
			case 16:
				t2[0] = '5';
				break;
			default:
				t2[0] = '0';
			}
			strcpy(t2 + 1, temps);
			if (TempHSData.moves > 0) {
				sprintf(temps, "%5d  %5d  %s", TempHSData.moves, TempHSData.shots, TempHSData.name);
				strcat(t2, temps);
			}
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_ADDSTRING, 0, (LPARAM) t2);
			i++;
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
		}
		LastOfList = i - 2;
		CloseHandle(F1);
		CloseHandle(F2);
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, CurLevel - 1, 0);
		OldProcEdit = SetWindowLong(GetDlgItem(Dialog, ID_LISTBOX), GWL_WNDPROC, (LONG)(WNDPROC) EditProc);
		return (TRUE);
	case WM_CTLCOLORLISTBOX:
		return ((int) GetStockObject(BLACK_BRUSH));
		break;
	case WM_MEASUREITEM:
		((MEASUREITEMSTRUCT FAR * ) lparam) -> itemHeight = 13;
		break;
	case WM_DRAWITEM:
		DrawLevels(lparam);
		return TRUE;
	case WM_VKEYTOITEM:
		return (TransListKey(Dialog, LOWORD(wparam)));
	case WM_COMMAND:
		if ((wparam == ID_HIGHLIST_01) || (wparam == 2)) EndDialog(Dialog, 0);
		if (((LOWORD(wparam) == ID_LISTBOX) && (HIWORD(wparam) == LBN_SELCHANGE)) ||
			(wparam == 1)) GetGameLevel(Dialog);
	}
	return (0);
}

void GHSScan(HWND Dialog) {
	TLEVEL TempRecData;
	THSREC TempHSData, TempGHSData;
	char temps[80], t2[80];
	int i, j, BHS;

	LastOfList = 0;
	F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
	if (F1 == INVALID_HANDLE_VALUE) return; // File NOT Found
	F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
	F3 = CreateFile(GHFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
	if (F3 == INVALID_HANDLE_VALUE) {
		CloseHandle(F1);
		if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2);
		return;
	}
	i = SetFilePointer(F3, 0, NULL, FILE_END) / sizeof(THSREC);
	SendDlgItemMessage(Dialog, ID_LISTBOX, LB_INITSTORAGE, i, 74);
	SetFilePointer(F3, 0, NULL, FILE_BEGIN);

	i = 1;
	ReadFile(F3, & TempGHSData, sizeof(THSREC), & BytesMoved, NULL);
	while (BytesMoved == sizeof(THSREC)) {
		ReadFile(F1, & TempRecData, sizeof(TLEVEL), & BytesMoved, NULL);
		if (F2 != INVALID_HANDLE_VALUE) ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
		BHS = (
			(TempHSData.moves > 0) && (BytesMoved == sizeof(THSREC)) &&
			(
				(TempGHSData.moves == 0) || (TempHSData.moves < TempGHSData.moves) ||
				((TempHSData.moves == TempGHSData.moves) && (TempHSData.shots < TempGHSData.shots))
			)
		);
		if (DispAll || (!DispAll && BHS)) {
			if (BHS)
				sprintf(temps, "%4d** %-28.28s %5d %5d  %4s>", i, TempRecData.LName, TempGHSData.moves,
					TempGHSData.shots, TempGHSData.name);
			else
				sprintf(temps, "%4d %-30.30s %5d %5d  %4s ", i, TempRecData.LName, TempGHSData.moves,
					TempGHSData.shots, TempGHSData.name);
			switch (TempRecData.SDiff) {
			case 1:
				t2[0] = '1';
				break;
			case 2:
				t2[0] = '2';
				break;
			case 4:
				t2[0] = '3';
				break;
			case 8:
				t2[0] = '4';
				break;
			case 16:
				t2[0] = '5';
				break;
			default:
				t2[0] = '0';
			}
			strcpy(t2 + 1, temps);
			if ((F2 != INVALID_HANDLE_VALUE) && (TempHSData.moves > 0) &&
				(BytesMoved == sizeof(THSREC))) {
				sprintf(temps, "%5d  %5d  %s", TempHSData.moves, TempHSData.shots, TempHSData.name);
				strcat(t2, temps);
			}
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_ADDSTRING, 0, (LPARAM) t2);
		}
		i++;
		ReadFile(F3, & TempGHSData, sizeof(THSREC), & BytesMoved, NULL);
	}
	LastOfList = i - 2;
	CloseHandle(F1);
	CloseHandle(F2);
	CloseHandle(F3);
}

// ---- Global HS List Dialog Procedure ----
//  List out all levels in the current data file, by number ,title, moves, shots & initials
LRESULT CALLBACK GHSList(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_GHIGHLIST_00);
		LoadWindowText(Dialog, ID_GHIGHLIST_01);
		LoadWindowText(Dialog, ID_GHIGHLIST_02);
		LoadWindowText(Dialog, ID_GHIGHLIST_03);
		LoadWindowText(Dialog, ID_GHIGHLIST_04);
		LoadWindowText(Dialog, ID_GHIGHLIST_05);
		LoadWindowText(Dialog, ID_GHIGHLIST_06);

		SetWindowText(GetDlgItem(Dialog, ID_GHIGHLIST_05), GHFileName);
		DispAll = TRUE;
		GHSScan(Dialog);
		SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, CurLevel - 1, 0);
		OldProcEdit = SetWindowLong(GetDlgItem(Dialog, ID_LISTBOX), GWL_WNDPROC, (LONG)(WNDPROC) EditProc);
		return (TRUE);
	case WM_CTLCOLORLISTBOX:
		return ((int) GetStockObject(BLACK_BRUSH));
	case WM_MEASUREITEM:
		((MEASUREITEMSTRUCT FAR * ) lparam) -> itemHeight = 14;
		break;
	case WM_DRAWITEM:
		DrawLevels(lparam);
		return TRUE;
	case WM_VKEYTOITEM:
		return (TransListKey(Dialog, LOWORD(wparam)));
	case WM_COMMAND:
		if ((wparam == 2) || (wparam == ID_GHIGHLIST_01)) EndDialog(Dialog, 0);
		if (
			((LOWORD(wparam) == ID_LISTBOX) || (wparam == 1)) &&
			(HIWORD(wparam) == LBN_SELCHANGE)
		)
			if (LastOfList > 0) GetGameLevel(Dialog);
		if (wparam == ID_GHIGHLIST_06) {
			SendDlgItemMessage(Dialog, ID_LISTBOX, LB_RESETCONTENT, 0, 0);
			DispAll = !DispAll;
			GHSScan(Dialog);
			if (DispAll) {
				SetWindowText(GetDlgItem(Dialog, ID_GHIGHLIST_06), txt040);
				SendDlgItemMessage(Dialog, ID_LISTBOX, LB_SETCURSEL, CurLevel - 1, 0);
			} else SetWindowText(GetDlgItem(Dialog, ID_GHIGHLIST_06), txt041);
		}
	}
	return (0);
}

// ---- Recorder Box Dialog Procedure ----
//  The Recorder uses this to prompt for the Author's name.
LRESULT CALLBACK RecordBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_RECBOX_00);
		LoadWindowText(Dialog, ID_RECBOX_01);
		LoadWindowText(Dialog, ID_RECBOX_02);

		GetPrivateProfileString("DATA", psPBA, "", PBSRec.Author, 30, INIFile);
		SetWindowText(GetDlgItem(Dialog, ID_RECBOX_03), PBSRec.Author);
		SetFocus(GetDlgItem(Dialog, ID_RECBOX_03));
		break;
	case WM_COMMAND:
		if ((wparam == 1) || (wparam == ID_RECBOX_02)) {
			GetWindowText(GetDlgItem(Dialog, ID_RECBOX_03), PBSRec.Author, 31);
			WritePrivateProfileString("DATA", psPBA, PBSRec.Author, INIFile);
			EndDialog(Dialog, 1);
		}
	}
	return (0);
}

// ---- PlayBack Dialog Procedure ----
//  This is the Playback Control window.
LRESULT CALLBACK PBWindow(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	char temps[200];
	RECT Box;
	char char1;

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_PLAYBOX_00);
		LoadWindowText(Dialog, ID_PLAYBOX_01);
		LoadWindowText(Dialog, ID_PLAYBOX_02);
		LoadWindowText(Dialog, ID_PLAYBOX_03);
		LoadWindowText(Dialog, ID_PLAYBOX_04);
		LoadWindowText(Dialog, ID_PLAYBOX_05);
		LoadWindowText(Dialog, ID_PLAYBOX_06);
		LoadWindowText(Dialog, ID_PLAYBOX_07);
		LoadWindowText(Dialog, ID_PLAYBOX_08);
		LoadWindowText(Dialog, ID_PLAYBOX_11);

		if (strcmp(CurRecData.LName, PBRec.LName) == 0) {
			SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_10), itoa(PBRec.Size, temps, 10));
			PBCountH = GetDlgItem(Dialog, ID_PLAYBOX_09);
			PlayH = Dialog;
			strcpy(temps, txt013);
			strcat(temps, PBRec.LName);
			strcat(temps, txt014);
			strcat(temps, PBRec.Author);

			switch (Speed) {
			case 1: // Fast
				SendMessage(GetDlgItem(Dialog, ID_PLAYBOX_04), BM_SETCHECK, 1, 0);
				break;
			case 2: // Slow
				SendMessage(GetDlgItem(Dialog, ID_PLAYBOX_05), BM_SETCHECK, 1, 0);
				break;
			case 3: // Single Step
				SendMessage(GetDlgItem(Dialog, ID_PLAYBOX_06), BM_SETCHECK, 1, 0);
				break;
			}
			GetWindowRect(MainH, & Box);
			SetWindowPos(Dialog, 0, Box.left + ContXPos + 2, Box.top + 280, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
			if (MessageBox(MainH, temps, App_Title, MB_OKCANCEL | MB_ICONQUESTION) == 2) {
				EndDialog(Dialog, 1);
				return (0);
			}
		} else EndDialog(Dialog, 1);
		return (0);
	case WM_COMMAND:
		switch (wparam) {
		case ID_PLAYBOX_01: //Close
		case ID_PLAYBOX_11: //Speed
		case 1: // Close Playback Dialog
			if (Game_On && (Game.RecP == PBRec.Size) &&
				(MessageBox(Dialog, txt016, App_Title, MB_YESNO | MB_ICONQUESTION) == IDYES)) {
				CheckMenuItem(MMenu, 123, MF_CHECKED);
				EnableMenuItem(MMenu, 117, 0); // enable Save Recording
				Recording = TRUE;
				SetWindowText(MainH, REC_Title);
			}
			PlayBack = FALSE;
			PBOpen = FALSE;
			PBHold = FALSE;
			RB_TOS = Game.RecP; // incase we stop short
			EndDialog(Dialog, 1);
			break;
		case ID_PLAYBOX_04:
			Speed = 1; // Fast
			break;
		case ID_PLAYBOX_05:
			Speed = 2; // Slow
			break;
		case ID_PLAYBOX_06:
			Speed = 3; // Single Step
			break;
		case ID_PLAYBOX_02:
			if (PlayBack) {
				SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_02), txt017);
				PlayBack = FALSE;
			} else {
				SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_02), txt018);
				PlayBack = TRUE;
			}
			break;
		case ID_PLAYBOX_03: //Reset
			PlayBack = FALSE;
			SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_02), txt017);
			SetWindowText(GetDlgItem(Dialog, ID_PLAYBOX_09), "0");
			SendMessage(MainH, WM_COMMAND, 105, 0); //ReStart
			Game.RecP = 0;
			RB_TOS = PBRec.Size;
			PBHold = FALSE;
		}
	}
	return (0);
}

static int LastLevelNum;

// ---- Pick Box Dialog Procedure ----
// The editor uses this to pick which level number to save the
// level with. Returns the number.}
//function PickBox(Dialog: HWnd; Message, WParam: Word; LParam: Longint): Bool; export;
LRESULT CALLBACK PickBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {
	char temps[40];
	int i, j;
	TLEVEL TempRecData;

	switch (Message) {
	case WM_INITDIALOG:
		LoadWindowCaption(Dialog, ID_PICKLEVEL_00);
		LoadWindowText(Dialog, ID_PICKLEVEL_01);
		LoadWindowText(Dialog, ID_PICKLEVEL_02);
		LoadWindowText(Dialog, ID_PICKLEVEL_03);
		LoadWindowText(Dialog, ID_PICKLEVEL_06);
		LoadWindowText(Dialog, ID_PICKLEVEL_08);

		i = SetFilePointer(F1, 0, NULL, FILE_END) / sizeof(TLEVEL);
		sprintf(temps, "1 - %d", i);
		SetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_04), temps);
		i++;
		LastLevelNum = i; // save Last Level Number to check in exit
		itoa(i, temps, 10);
		SetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_07), temps);
		if (CurLevel < i) itoa(CurLevel, temps, 10);
		SetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_05), temps);
		SendDlgItemMessage(Dialog, ID_PICKLEVEL_08, BM_SETCHECK, 1, 0);
		return (TRUE);
	case WM_COMMAND:
		if ((wparam == 1) || (wparam == ID_PICKLEVEL_01)) {
			GetWindowText(GetDlgItem(Dialog, ID_PICKLEVEL_05), temps, 10);
			i = atoi(temps);
			HSClear = SendDlgItemMessage(Dialog, ID_PICKLEVEL_08, BM_GETCHECK, 0, 0) > 0;
			if (i <= LastLevelNum) EndDialog(Dialog, i);
			return (TRUE);
		}
	}
	return (0);
}

// ---- Used by Graph Box Dialog Procedure ----
void SetUpGraphicsBox(HWND d, int C101, int C102, int BU) {
	long DBU;
	RECT Box;

	SendDlgItemMessage(d, ID_GRAPHBOX_02, BM_SETCHECK, C101, 0);
	//SendDlgItemMessage(d,ID_GRAPHBOX_03,BM_SETCHECK,C102,0);
	DBU = GetDialogBaseUnits();
	GetWindowRect(d, & Box);
	SetWindowPos(d, HWND_TOP, Box.left, Box.top, Box.right - Box.left,
		(BU * HIWORD(DBU)) / 8, SWP_NOZORDER);

	if (GFXOn) GFXKill();
	GFXInit();
	InvalidateRect(MainH, NULL, TRUE);
}

// ---- Used by Graph Box Dialog Procedure ----
void GetLTGFiles(HWND Dialog, TLTGREC * ltgCur) {
	WIN32_FIND_DATA ffdata;
	HANDLE ffdH, F1;
	TLTGREC ltg;

	// Scan for all LTG files
	SetCurrentDirectory(GraphDN);
	ffdH = FindFirstFile("*.ltg", & ffdata);
	if (ffdH) {
		do {
			F1 = CreateFile(ffdata.cFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
				FILE_FLAG_SEQUENTIAL_SCAN, NULL);
			if (F1 != INVALID_HANDLE_VALUE) {
				if (!(ReadFile(F1, & ltg, sizeof(TLTGREC), & BytesMoved, NULL))) FileError();
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_ADDSTRING, 0, (LPARAM) ltg.Name);
				// the next line will help setup the listbox if we are mode 2
				if ((GraphM == 2) && (strcmp(GraphFN, ffdata.cFileName) == 0))
					memcpy(ltgCur, & ltg, sizeof(TLTGREC));
			}
			CloseHandle(F1);
		} while (FindNextFile(ffdH, & ffdata));
		FindClose(ffdH);
	}
}

// ---- Graph Box Dialog Procedure ----
//  This Dialog is used to change the Graphics Set being used
LRESULT CALLBACK GraphBox(HWND Dialog, UINT Message, WPARAM wparam, LPARAM lparam) {

	char temps[MAX_PATH];
	TLTGREC ltg, ltgCur;
	char Mode2N[40];
	int i;
	WIN32_FIND_DATA ffdata;
	HANDLE ffdH, F1;

	switch (Message) {
	case WM_INITDIALOG:

		LoadWindowCaption(Dialog, ID_GRAPHBOX_00);
		LoadWindowText(Dialog, ID_GRAPHBOX_01);
		LoadWindowText(Dialog, ID_GRAPHBOX_02);
		//LoadWindowText(Dialog,    ID_GRAPHBOX_03);
		LoadWindowText(Dialog, ID_GRAPHBOX_04);
		LoadWindowText(Dialog, ID_GRAPHBOX_05);
		LoadWindowText(Dialog, ID_GRAPHBOX_06);
		LoadWindowText(Dialog, ID_GRAPHBOX_08);
		LoadWindowText(Dialog, ID_GRAPHBOX_09);

		GetLTGFiles(Dialog, & ltgCur);
		switch (GraphM) {
		case 1:
			SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_CHECKED, 100);
			break;
		case 2:
			SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_UNCHECKED, 160);
			i = SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_SELECTSTRING, -1, (LPARAM) ltgCur.Name);
			SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_07), ltgCur.Author);
			SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_11), ltgCur.Info);
			break;
		default:
			SetUpGraphicsBox(Dialog, BST_CHECKED, BST_UNCHECKED, 100); // mode 0
		}
		return (TRUE);
	case WM_COMMAND:
		switch (LOWORD(wparam)) {
		case ID_GRAPHBOX_04: // Close
		case 2: // Cancel
			itoa(GraphM, temps, 10);
			WritePrivateProfileString("SCREEN", psGM, temps, INIFile);
			if (GraphM == 2) WritePrivateProfileString("SCREEN", psGFN, GraphFN, INIFile);
			QHELP = FALSE;
			InvalidateRect(MainH, NULL, FALSE);
			EndDialog(Dialog, 1);
			break;
		case ID_GRAPHBOX_02: // Internal Graphics
			if (GraphM == 2) SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_SETCURSEL, -1, 0);
			GraphM = 0;
			SetUpGraphicsBox(Dialog, BST_CHECKED, BST_UNCHECKED, 100);

			break;
		case ID_GRAPHBOX_03: // External Graphics
			if (GraphM == 2) SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_SETCURSEL, -1, 0);
			GraphM = 1;
			SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_CHECKED, 100);
			if (GraphM == 0) {
				MessageBox(Dialog, txt032, txt007, MB_OK | MB_ICONERROR);
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_02, BM_SETCHECK, BST_CHECKED, 0);
				SendDlgItemMessage(Dialog, ID_GRAPHBOX_03, BM_SETCHECK, BST_UNCHECKED, 0);
			}
			break;
		case ID_GRAPHBOX_10: // Graphics Sets
			i = SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_GETCURSEL, 0, 0);
			if (i == -1) break; // Weed out junk ( Don't Ask )
			SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_GETTEXT, i, (LPARAM) Mode2N);
			// Find File Reference
			ffdH = FindFirstFile("*.ltg", & ffdata);
			if (ffdH) {
				do {
					F1 = CreateFile(ffdata.cFileName, GENERIC_READ, FILE_SHARE_READ,
						NULL, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);
					if (F1 != INVALID_HANDLE_VALUE) {
						if (!(ReadFile(F1, & ltg, sizeof(TLTGREC), & BytesMoved, NULL))) FileError();
						if (strcmp(Mode2N, ltg.Name) == 0) {
							CloseHandle(F1);
							FindClose(ffdH);
							SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_07), ltg.Author);
							SetWindowText(GetDlgItem(Dialog, ID_GRAPHBOX_11), ltg.Info);
							strcpy(GraphFN, ffdata.cFileName);
							GraphM = 2;
							SetUpGraphicsBox(Dialog, BST_UNCHECKED, BST_UNCHECKED, 160);
							return (0);
						}
					}
					CloseHandle(F1);
				} while (FindNextFile(ffdH, & ffdata));
				FindClose(ffdH);
			}
			//We should Never be here
			MessageBox(MainH, txt045, txt007, MB_OK);
			break;
		case ID_GRAPHBOX_08:
			QHELP = (SendDlgItemMessage(Dialog, ID_GRAPHBOX_08, BM_GETCHECK, 0, 0) > 0);
			InvalidateRect(MainH, NULL, FALSE);
			break;
		case ID_GRAPHBOX_09:
			Browse(Dialog, GraphDN, txt037);
			SendDlgItemMessage(Dialog, ID_GRAPHBOX_10, LB_RESETCONTENT, 0, 0);
			GetLTGFiles(Dialog, & ltgCur);
			WritePrivateProfileString("SCREEN", psGDN, GraphDN, INIFile);
			break;
		}
	}
	return (0);
}

// ltank.h
/*******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 *******************************************************/

#include <windows.h>

/*

Obj			BitM	Description
---     	----    -----------

0 			1		Dirt
1 			2		Tank Up ( Primary )
-			3		Tank Right
-			4		Tank Down
-			5		Tank left
2			6		Base ( Primary)
-			7		Base Alt ( animation )
-			8		Base Alt2
3			9		Water ( Primary )
-			10		Water Alt
-			11		Water Alt 2
-       	12  	Blown Up Anti Tank (down)
4			13		Solid Block NOT movable
5			14		Movable Block
6			15		Bricks
7			16		Anti-Tank Gun Up
-			17		Anti-Tank Alt
-			18		Anti-Tank Alt 2
-			19	    Movable block after pushing into water
11			20		Mirror Up-Lt
12			21		Mirror Up-Rt
13			22		Mirror Dn-Rt
14			23		Mirror Dn-Lt
15			24		One Way Up (Primary)
-			25		One Way Up Alt
-			26		One Way Up Alt2
16			27		One Way Rt (Primary)
-			28		One Way Rt Alt
-			29		One Way Rt Alt2
17			30		One Way Dn (Primary)
-			31		One Way Dn Alt
-			32		One Way Dn Alt2
18			33		One Way Lt (Primary)
-			34		One Way Lt Alt
-			35		One Way Lt Alt2
8 	      	36      Anti-Tank facing right
- 	      	37
- 	      	38
9       	39      Anti-Tank facing down
-       	40
-       	41
10      	42      Anti-Tank facing left
-       	43
-       	44
19      	45      Crystal Block
-       	46      Crystal when hit by tank
20			47		Roto Mirror Up-Lt
21			48		Roto Mirror Up-Rt
22			49		Roto Mirror Dn-Rt
23			50		Roto Mirror Dn-Lt
-       	51      Crystal when hit by Anti-tank
-       	52      Blown Up Anti Tank (right)
-       	53      Blown Up Anti Tank (left)
-       	54      Blown Up Anti Tank (up)
24			56		Ice
25			57		Thin Ice
01dddddx	55		Worm Hole / Tunnel

*/

// Language Section for Lasertank
// Import this from its own file

#include "lt32l_us.h"

// Game Defaults
#define LevelData "LaserTank.lvl" // Default Level Data File
#define INIFileName "LaserTank.ini"
// MAX text size for a lang_text
#define MAX_LANG_SIZE 300

#define MaxObjects 26 // Maximum number of game objects used
#define MaxBitMaps 58 // the maximum number of BitMaps ( + 1 )
#define XOffset 17 // Game Board Offset from Left
#define YOffset 17 // Game Board Offset from top
#define ani_delay 4 // animation Delay in GameDelay units
#define GameDelay 50 // Main Operation Loop
#define WM_GameOver WM_USER + 1 // Send Message if there are no more levels
#define WM_Dead WM_USER + 2 // Send Message when you die
#define WM_NewHS WM_USER + 3 // Send to Display New High Score Dialog
#define WM_SaveRec WM_USER + 4 // Send to Save Recording
#define App_Class "LaserTC2" // The Class Name
#define UndoBufStep 200 // Groth Amount of Undo Buffer
#define UndoMax 10000 // Max Amount of Undo Buffer
#define RecBufStep 10000 // Groth amount of Rec Buffer
#define RecMax 65500 // Max recording steps saved to file
#define SlowPBSet 5 // Delay of Slow Playback setting
#define MaxMBuffer 20 // Size of Mouse Buffer
#define Obj_Water 3 // Object Number 3 is water
#define Obj_Ice 24 // Ice Object
#define Obj_ThinIce 25 // Object Number of Thin Ice
#define Obj_Tunnel 0x40 // Object 01dddddX = Tunnel
#define LTG_ID "LTG1" // ID field of LTG file
#define psRLLOn "RLL" // Profile String for remember last level
#define psRLLN "RLLFilename" // remember last level file name
#define psRLLL "RLLLevel" // Level number
#define psAni "Animation"
#define psSound "Sound"
#define psSize "Size" // 1 = small, 3 = large
#define psXpos "PosX"
#define psYpos "PosY"
#define psUser "Player"
#define psPBA "Record Author"
#define psARec "Auto_Record"
#define psSCL "SkipComLev"
#define psDiff "Diff_Setting"
#define psGM "Graphics_Mode"
#define psGFN "Graphics_File"
#define psGDN "Graphics_Dir"
#define psDW "DisableWarnings"
#define psYes "Yes"
#define psNET "NETWORK_INI" // 1 = Use INI file from C:\Windows
#define BADMOVE 256

typedef char TPLAYFIELD[16][16]; // Matrix of G.O. types

typedef struct tLevel // Level Data from File
{
	TPLAYFIELD PF; // Object Grid
	char LName[31]; // Level Name
	char Hint[256]; // Hint for this level
	char Author[31]; // the Author of the Level
	WORD SDiff; // Score Difficulty
}
TLEVEL;

typedef struct tRecordRec // Recording Header
{
	char LName[31]; // Level Name
	char Author[31]; // Author of the recording
	WORD Level; // Level Number
	WORD Size; // Size of Data -- Data to fallow
}
TRECORDREC;

typedef struct tSearch // Search Record used in Level Load
{
	int mode, // 1=title, 2 = author
	SkipComp; // True = Skip Completed
	WORD Diff; // Difficulty charecter
	char data[61]; // Search String
}
TSEARCH;

typedef struct tTankRec // Store the Tank & Laser information
{
	int X, Y, Dir, Firing, Good; // Good is used for Tunnel Wait in Game.Tank
}
TTANKREC;

typedef struct tGameRec {
	TPLAYFIELD PF, // Store Game Objects
	PF2, // Store Objects Under Stuff ( Ground, conveyor)
	BMF, // Bitmaps for Objects
	BMF2; // Bitmaps for Under Stuff ( Bridges )
	WORD ScoreMove, // Move Counter
	ScoreShot; // Shot Counter
	DWORD RecP; // Recording Pointer
	TTANKREC Tank; // Tank Data
}
TGAMEREC, * PGAMEREC;

typedef struct tXYRec // Use in BMA
{
	int X, Y; // X & Y Location in Big Butmap
}
TXYREC;

typedef struct tXYZRec // Use for Mouse Buffer
{
	int X, Y, Z;
}
TXYZREC;

typedef struct tHSRec // High Score Record
{
	WORD moves, shots;
	char name[6]; // Initials
}
THSREC;

typedef struct tLTGRec // Record for LTG graphics
{
	char Name[40]; // Name of Graphic Set
	char Author[30]; // Author of Graphics set
	char Info[245]; // 3 line Description of Graphics Set
	char ID[5]; // LTG ID = "LTG1"+0
	DWORD MaskOffset; // Offset from the biggining of file to Mask Bitmap
}
TLTGREC;

typedef struct tIceRec // Record used for sliding on the Ice
{
	int x, y, // Last XY position of object to move
	dx, dy, // Direction to move in Delta Cords
	s; // True if Sliding

}
TICEREC;

/// ------------ MGY -----------
#define MAX_TICEMEM 16
typedef struct tIceMem // Record used for sliding objects on the Ice
{
	TICEREC Objects[MAX_TICEMEM]; // MGY - mem up 16 sliding objects
	int count; // number of current sliding objects
}
TICEMEM;
extern TICEMEM SlideMem;
/// ------------ MGY -----------

// Extern's -- Complete Program Defined Global Variables
extern HINSTANCE hInst; // Globally Defined Instance
extern char * RecBuffer;
extern int GFXOn, Game_On, Sound_On, Ani_On, RLL, ConvMoving, CurLevel, TankDirty, DWarn;
extern int AniCount, CurSelBM_L, CurSelBM_R, RB_TOS, PBHold, SpBm_Width, SpBm_Height, ContXPos;
extern int ARecord, Difficulty, SkipCL, Recording, PlayBack, EditBMWidth, Speed, SlowPB, RecBufSize;
extern HWND MainH, Ed1, Ed2, BT1, BT2, BT3, BT4, BT5, BT6, BT7, BT8, BT9;
extern TGAMEREC Game, BackUp, SaveGame;
extern TLEVEL CurRecData;
extern HBRUSH LaserColor, LaserColorG, LaserColorR;
extern HDC gDC; // Use this game dc for all ops
extern char FileName[], HFileName[], GHFileName[], PBFileName[], GraphFN[], GraphDN[], INIFile[];
extern HMENU MMenu;
extern int Modified, OKtoHS, VHSOn;
extern TRECORDREC PBRec, PBSRec;
extern char HelpFile[];
extern PGAMEREC UndoBuffer;
extern int UndoP, PBOpen;
extern THSREC HS;
extern HDC BuffDC;
extern HBITMAP BuffBMH;
extern TXYREC BMA[MaxBitMaps + 1]; // Bit Map Array
extern TXYZREC MBuffer[MaxMBuffer]; // Mouse Buffer
extern int MB_TOS, MB_SP; // TOS = Top of Stack ; SP = Stack Pointer
extern DWORD DEBUG_Time;
extern DWORD DEBUG_Frames;
extern HANDLE F1, F2, F3; // File Handles
extern DWORD BytesMoved; // use in ReadFile & WriteFile
extern int GraphM, FindTank;
extern TICEREC SlideO, SlideT;

// Variables for Language
extern char LANGText[SIZE_ALL][MAX_LANG_SIZE]; // All lines of Language.dat
extern char LANGFile[MAX_PATH]; // the dynamic file name for Language.dat
extern TCHAR szFilterOFN[MAX_PATH];
extern TCHAR szFilterPBfn[MAX_PATH];

// Global Function Prototypes

void FileError();
void GFXInit(); // Load All the Bitmaps
void GFXKill(void); // Release All the Bitmaps
void PutLevel(void); // Draw Game Board
void GameOn(int); // Turns on/off game timer
void JK3dFrame(HDC, int, int, int, int, int); // Draw 3D frame
void JKSelFrame(HDC, int, int, int, int, int); // Draw Red/Green frame
void LoadLastLevel();
BOOL LoadNextLevel(int, int);
void CheckHighScore(void); // Compare score to High Score
void Animate(void); // Animate all Animated Objects
void MoveTank(int);
int CheckLoc(int, int);
void MoveLaser();
void FireLaser(int, int, int, int);
void AntiTank(); // Target Anti-Tanks at Tank
char GetOBM(char); // Translate Bitmap to Object
void BuildBMField(); // Convert Objects to bitmaps
void PutSprite(char, int, int); // Paint BM at X,Y
void UpDateSprite(int, int); // Repaint bitmap at x,y
void UpDateTank(); // Repaint Tank
void PutSelectors(); // Editor - paint objects to edit
void ChangeGO(int, int, int); // Change Game Object
void SetGameSize(int);
void SavePBFile();
void InitBuffers();
void KillBuffers();
void AssignHSFile();
void UpdateUndo();
void UndoStep();
void ResetUndoBuffer();
int MouseOperation(int); // Process Mouse Input
void ShowTunnelID();
void ConvMoveTank(int, int, int);
void IceMoveT(); // Move an tank on the Ice
void IceMoveO(); // Move an Object on the Ice
void AddKBuff(char);

// Function Prototypes for Language
void ChangeMenuText(HMENU, char * );
void InitLanguage(HMENU, HMENU);
void ConvertTabChar(char * );
HBITMAP LoadImageFile(HINSTANCE, char * , char * );
void LoadWindowText(HWND, int);
void LoadWindowCaption(HWND, int);

/* Lets try some Macros */
#define GetTunnelID(x, y)((Game.PF[x][y] & 0x0F) >> 1) // 0 - 7

// mgy 18-05-2003 Tunnel is limited to 0-7.
#define GetTunnelOldID(x, y)((Game.PF[x][y] & 0x0F) >> 1) // 0 - 7
//#define GetTunnelOldID(x,y) ((Game.PF[x][y] & 0x3F)  >> 1)		// 0 - 32

#define ISTunnel(x, y)((Game.PF[x][y] & Obj_Tunnel) == Obj_Tunnel)
#define GameInProg Game.RecP && (Game.PF[Game.Tank.X][Game.Tank.Y] != 2) && (!DWarn)

// ltank.c
/*******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 *******************************************************/
#include <windows.h>

#include <string.h>

#include <stdio.h>

#include <mmsystem.h>

#include "ltank.h"

#include "ltank_d.h"

#include "lt_sfx.h"

const int GetNextBMArray[MaxObjects + 1] = {
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
};
const int OpeningBMA[16] = {
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
}; //Bitmap IDs to show on the Quick Help / Welcome screen
int EditorOn = FALSE; // true when in editor mode
int QHELP = FALSE; // True when Quick Help is On
extern
const long DifCList[6];
HINSTANCE hInst; // Globally Defined Instance
HBITMAP OpenScreen; // Instruction Bitmap loaded from "control.bmp"
HFONT MyFont;
int FileHand;
int RB_TOS; // Rec/Game Buffer pointer to TOP OF STACK
int PBHold;
int VHSOn;
HWND MainH, Ed1, Ed2, BT1, BT2, BT3, BT4, BT5, BT6, BT7, BT8, BT9;
TPLAYFIELD ShiftPF, ShiftBMF;
HMENU EMenu, MMenu;
char PrintJobName[100];
char HelpFile[MAX_PATH];

extern int Backspace[10]; // Backspace Buffer
extern int BS_SP; // StackPointer for Backspace
extern int OKtoSave;

OPENFILENAME OFN = {
	sizeof(OPENFILENAME),
	0,
	0,
	NULL,
	NULL,
	0,
	1,
	FileName,
	MAX_PATH,
	NULL,
	0,
	NULL,
	txt004,
	OFN_HIDEREADONLY,
	0,
	0,
	"lvl"
};

OPENFILENAME PBfn = {
	sizeof(OPENFILENAME),
	0,
	0,
	NULL,
	NULL,
	0,
	1,
	PBFileName,
	MAX_PATH,
	NULL,
	0,
	NULL,
	txt005,
	OFN_HIDEREADONLY,
	0,
	0,
	"lpb"
};

// Callback function Declarations
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);
BOOL InitApplication(HINSTANCE);
BOOL InitInstance(HINSTANCE, int);
void EditDiffSet(int);
BOOL LoadPlayback();
void VHSPlayback();

// Local Work
void EditDiffSet(int t) {
	//lt32l_us.inc
	//POPUP "&Difficulty"
	//	BEGIN
	//	MENUITEM "&Kids", 701
	//	MENUITEM "&Easy", 702
	//	MENUITEM "&Medium", 703
	//	MENUITEM "&Hard", 704
	//	MENUITEM "&Deadly", 705
	//	END
	//CheckMenuItem(EMenu, 701, 0); //Set check mark (menu handle, item ID, unchecked)
	// https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-checkmenuitem
	CheckMenuItem(EMenu, 701, 0);
	CheckMenuItem(EMenu, 702, 0);
	CheckMenuItem(EMenu, 703, 0);
	CheckMenuItem(EMenu, 704, 0);
	CheckMenuItem(EMenu, 705, 0);
	switch (t) {
	case 1:
		CheckMenuItem(EMenu, 701, MF_CHECKED);
		break;
	case 2:
		CheckMenuItem(EMenu, 702, MF_CHECKED);
		break;
	case 4:
		CheckMenuItem(EMenu, 703, MF_CHECKED);
		break;
	case 8:
		CheckMenuItem(EMenu, 704, MF_CHECKED);
		break;
	case 16:
		CheckMenuItem(EMenu, 705, MF_CHECKED);
	}
	CurRecData.SDiff = t;
}

BOOL LoadPlayback() {
	HANDLE F;
	char temps[200];

	if (Recording)
		SendMessage(MainH, WM_COMMAND, 123, 0); // Turn Off Recording
	if ((F = CreateFile(PBFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, NULL)) == INVALID_HANDLE_VALUE)
		return (FALSE);

	PBOpen = TRUE; // this will also tell autorecord not to turn on
	ReadFile(F, & PBRec, sizeof(PBRec), & BytesMoved, NULL);

	if (RecBufSize <= PBRec.Size) { // RecBuffer needs to be bigger
		RecBufSize = PBRec.Size + 1;
		RecBuffer = GlobalReAlloc(RecBuffer, RecBufSize, GMEM_MOVEABLE);
	}

	ReadFile(F, RecBuffer, PBRec.Size, & BytesMoved, NULL); // Load RecBuffer W data
	CloseHandle(F);
	CurLevel = PBRec.Level - 1;

	// Set the current level to match the level in the playback
	// this will error if the levels have moved
	if ((!LoadNextLevel(TRUE, TRUE)) || (strcmp(CurRecData.LName, PBRec.LName) != 0)) {
		// Do a hard file search for the level name
		F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, NULL);
		CurLevel = 0;
		ReadFile(F, & CurRecData, sizeof(CurRecData), & BytesMoved, NULL);
		while ((BytesMoved == sizeof(CurRecData)) && (strcmp(CurRecData.LName, PBRec.LName) != 0)) {
			CurLevel++;
			ReadFile(F, & CurRecData, sizeof(CurRecData), & BytesMoved, NULL);
		}
		CloseHandle(F1);
		if (BytesMoved == sizeof(CurRecData)) {
			LoadNextLevel(TRUE, TRUE);
		}
	}
	Game.RecP = 0;
	RB_TOS = PBRec.Size;
	if (strcmp(CurRecData.LName, PBRec.LName) != 0) {
		// Could not find level from playback in current lvl file
		strcpy(temps, txt013); // "Playback Level:"
		strcat(temps, PBRec.LName);
		strcat(temps, txt015); // "\nCan Not be found in the current level file\n<"
		strcat(temps, FileName);
		strcat(temps, " >");
		MessageBox(MainH, temps, txt007, MB_OK | MB_ICONERROR);
		PlayBack = FALSE;
		PBOpen = FALSE;
		PBHold = FALSE;
		SendMessage(MainH, WM_COMMAND, 101, 0);
		return (FALSE);
	}
	return (TRUE);
}

void VHSPlayback() {
	gDC = GetDC(MainH);
	GameOn(FALSE);
	if (FindTank) {
		FindTank = FALSE;
		PutLevel();
	}
	VHSOn = TRUE;
	while (Game.RecP < RB_TOS) {
		if (Game.Tank.Firing) MoveLaser(); // Move laser if one was fired
		// Check Key Press }
		if (!(Game.Tank.Firing || ConvMoving || SlideO.s || SlideT.s)) {
			switch (RecBuffer[Game.RecP]) {
			case VK_UP:
				MoveTank(1); // Move tank Up one
				break;
			case VK_RIGHT:
				MoveTank(2);
				break;
			case VK_DOWN:
				MoveTank(3);
				break;
			case VK_LEFT:
				MoveTank(4);
				break;
			case VK_SPACE: {
				UpdateUndo();
				Game.ScoreShot++; // do here Not in FireLaser (as FireLaser is also used for antitanks)
				FireLaser(Game.Tank.X, Game.Tank.Y, Game.Tank.Dir, S_Fire); // Bang
			}
			}
			Game.RecP++; // Point to next charecter
			AntiTank(); // give the Anti-Tanks a turn to play
		}
		if (SlideO.s) IceMoveO();
		if (SlideT.s) IceMoveT();
		ConvMoving = FALSE; // used to disable Laser on the conveyor
		switch (Game.PF[Game.Tank.X][Game.Tank.Y]) {
		case 2:
			if (Game_On) // Reached the Flag
			{
				GameOn(FALSE);
				ReleaseDC(gDC, MainH);
				VHSOn = FALSE;
				return; // We shouldn't be here

			}
			break;
		case 3:
			PostMessage(MainH, WM_Dead, 0, 0); // Water
			break;
		case 15:
			if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1)) // Conveyor Up
				ConvMoveTank(0, -1, TRUE);
			break;
		case 16:
			if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y))
				ConvMoveTank(1, 0, TRUE);
			break;
		case 17:
			if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1))
				ConvMoveTank(0, 1, TRUE);
			break;
		case 18:
			if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y))
				ConvMoveTank(-1, 0, TRUE);
		}
	}
	ReleaseDC(gDC, MainH);
	UpDateTank();
	GameOn(TRUE);
	VHSOn = FALSE;
}

BOOL CALLBACK CancelProc(HDC hdc, int nCode) {
	MSG msg;

	while (PeekMessage( & msg, NULL, 0, 0, PM_REMOVE)) {
		TranslateMessage( & msg);
		DispatchMessage( & msg);
	}
	return (TRUE);
}

void Print() {
	PRINTDLG PrintInfo;
	char temps[100];
	TEXTMETRIC TextInfo;
	int XLog, YLog, x, y, ch;
	HDC tempDC;
	HPALETTE hPal;
	LPLOGPALETTE lpLogPal;
	BITMAPINFO bmi;
	HBITMAP hbm;
	LPBYTE pBits;
	DIBSECTION ds;
	DOCINFO DocInfo = {
		sizeof(DOCINFO),
		0,
		0,
		0,
		0
	};

	PrintInfo.hwndOwner = MainH;
	PrintInfo.hDevMode = 0;
	PrintInfo.hDevNames = 0;
	PrintInfo.lStructSize = sizeof(PrintInfo);
	PrintInfo.Flags = PD_RETURNDC | PD_NOPAGENUMS | PD_NOSELECTION | PD_USEDEVMODECOPIES;
	if (!PrintDlg( & PrintInfo)) return;

	UpdateWindow(MainH); // We need to redraw it first
	gDC = GetDC(MainH);

	ZeroMemory( & bmi, sizeof(bmi));
	bmi.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
	bmi.bmiHeader.biWidth = 16 * SpBm_Width;
	bmi.bmiHeader.biHeight = 16 * SpBm_Height;
	bmi.bmiHeader.biPlanes = 1;
	bmi.bmiHeader.biBitCount = 24;
	bmi.bmiHeader.biCompression = BI_RGB;
	// Create intermediate drawing surface
	hbm = CreateDIBSection(gDC, & bmi, DIB_RGB_COLORS, & pBits, NULL, 0);
	// Prep surface for drawing
	tempDC = CreateCompatibleDC(gDC);
	SelectObject(tempDC, hbm);

	if ((GetDeviceCaps(gDC, RASTERCAPS) & RC_PALETTE)) // Are we Palette Based ?
	{
		// YES we are - Get Palette
		lpLogPal = GlobalAlloc(GPTR, sizeof(LOGPALETTE) + 256 * sizeof(PALETTEENTRY));
		lpLogPal -> palVersion = 0x300;
		lpLogPal -> palNumEntries = 256;
		GetSystemPaletteEntries(gDC, 0, 256, (LPPALETTEENTRY)(lpLogPal -> palPalEntry));
		hPal = CreatePalette(lpLogPal);
		GlobalFree(lpLogPal);

		// Apply the Palette to Game WIndow
		SelectPalette(gDC, hPal, FALSE);
		RealizePalette(gDC);
		// Apply the Palette to the tempDC
		SelectPalette(tempDC, hPal, FALSE);
		RealizePalette(tempDC);
		DeleteObject(hPal);
	}
	// Copy Bits to the memory DC
	BitBlt(tempDC, 0, 0, 16 * SpBm_Width, 16 * SpBm_Height, gDC, XOffset, YOffset, SRCCOPY);
	ReleaseDC(MainH, gDC);

	EnableWindow(MainH, FALSE);
	sprintf(PrintJobName, "%s %d", txt036, CurLevel);
	DocInfo.lpszDocName = PrintJobName;
	if (!StartDoc(PrintInfo.hDC, & DocInfo)) return;

	SetAbortProc(PrintInfo.hDC, CancelProc);
	StartPage(PrintInfo.hDC);
	GetTextMetrics(PrintInfo.hDC, & TextInfo);
	ch = TextInfo.tmHeight;
	XLog = GetDeviceCaps(PrintInfo.hDC, LOGPIXELSX); // pixles per inch
	YLog = GetDeviceCaps(PrintInfo.hDC, LOGPIXELSY);

	// Now we can start to print
	SetBkMode(PrintInfo.hDC, TRANSPARENT);
	SetTextAlign(PrintInfo.hDC, TA_CENTER);
	TextOut(PrintInfo.hDC, (XLog * 3), (YLog / 2), PrintJobName, strlen(PrintJobName));
	if (CurLevel) // This is if we print the opening Screen
	{
		sprintf(temps, "( %s )", CurRecData.LName);
		TextOut(PrintInfo.hDC, (XLog * 3), (YLog / 2) + ch, temps, strlen(temps));
	}
	y = (YLog * 5) + ch;
	SetTextAlign(PrintInfo.hDC, TA_LEFT);
	sprintf(temps, "Moves = %d    Shots = %d", Game.ScoreMove, Game.ScoreShot);
	TextOut(PrintInfo.hDC, XLog, y, temps, strlen(temps));

	GetObject(hbm, sizeof(DIBSECTION), & ds);
	StretchDIBits(PrintInfo.hDC, XLog, YLog, XLog * 4, YLog * 4,
		0, 0, (SpBm_Width * 16), (SpBm_Height * 16),
		ds.dsBm.bmBits, (LPBITMAPINFO) & ds.dsBmih, DIB_RGB_COLORS, SRCCOPY);

	EndPage(PrintInfo.hDC); // Send Page
	EndDoc(PrintInfo.hDC);
	DeleteDC(tempDC);
	DeleteDC(PrintInfo.hDC);
	DeleteObject(hbm);
	EnableWindow(MainH, TRUE);
}

void ToggleOpt(int ID, HMENU Menu, int * Opt, LPCTSTR psText) {
	if (GetMenuState(Menu, ID, 0) & MF_CHECKED) {
		CheckMenuItem(Menu, ID, 0);
		* Opt = FALSE;
		WritePrivateProfileString("OPT", psText, "No", INIFile);
	} else {
		CheckMenuItem(Menu, ID, MF_CHECKED);
		* Opt = TRUE;
		WritePrivateProfileString("OPT", psText, "Yes", INIFile);
	}
}

// Create file name for playback file *_0001.lpb
void BuildPB_Name() {
	char temps[100];
	char * P;

	PBSRec.Level = CurLevel;
	sprintf(temps, "_%04d.lpb", PBSRec.Level);
	P = strrchr(PBFileName, '_');
	if (P) strcpy(P, temps); // add to name
}

// --- Main Window Procedure --- }
// This is used for both the editor and the game }
// function MainWindowProc(Window: HWnd; Message, WParam: Word; LParam: Longint): Longint; export;
//https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/ms633573(v%3Dvs.85)
// main game loop main loop
LRESULT CALLBACK WndProc(HWND Window, UINT Message, WPARAM wparam, LPARAM lparam) {
	char temps[100];
	HDC tDC, pdc;
	HBITMAP tBM;
	RECT Box;
	HMENU Menu;
	PAINTSTRUCT PI;
	int i, j, x, y, LastLevel;
	char * P;
	WINDOWPLACEMENT twp;

	switch (Message) {
	case WM_CREATE: // Sent when an application requests that a window be created by calling the CreateWindowEx or CreateWindow function. (The message is sent before the function returns.) The window procedure of the new window receives this message after the window is created, but before the window becomes visible.
		strcpy(FileName, LevelData); // set up default file name
		Menu = GetMenu(Window);

		// Check INI file for settings and copy into variables
		GetPrivateProfileString("OPT", psAni, psYes, temps, 5, INIFile);
		// Check if Animation is enabled or disabled }
		if (strcmp(temps, psYes)) {
			Ani_On = FALSE;
			CheckMenuItem(Menu, 104, 0); // Yes I Know we should write MF_BYCOMMAND | MF_UNCHECKED
		}
		GetPrivateProfileString("OPT", psSound, psYes, temps, 5, INIFile);
		// Check if Sound is enabled or disabled
		if (strcmp(temps, psYes)) {
			Sound_On = FALSE;
			CheckMenuItem(Menu, 102, 0);
		}
		GetPrivateProfileString("OPT", psSCL, "No", temps, 5, INIFile);
		// Check if Skip Complete Level is enabled or disabled
		if (strcmp(temps, psYes) == 0) {
			CheckMenuItem(Menu, 116, MF_CHECKED);
			SkipCL = TRUE;
		}
		GetPrivateProfileString("OPT", psARec, "No", temps, 5, INIFile);
		// Check if AutoRecord is enabled or disabled
		if (strcmp(temps, psYes) == 0) {
			CheckMenuItem(Menu, 115, MF_CHECKED);
			ARecord = TRUE;
		}
		GetPrivateProfileString("OPT", psDW, "No", temps, 5, INIFile);
		// Check if DisableWarnings is enabled or disabled
		if (strcmp(temps, psYes) == 0) {
			CheckMenuItem(Menu, 127, MF_CHECKED);
			DWarn = TRUE;
		}
		Difficulty = GetPrivateProfileInt("DATA", psDiff, 0, INIFile);
		GetPrivateProfileString("OPT", psRLLOn, psYes, temps, 5, INIFile);
		// Check if Remember Last Level is enabled or disabled
		if (strcmp(temps, psYes)) {
			RLL = FALSE;
			CheckMenuItem(Menu, 109, 0);
		} else GetPrivateProfileString("DATA", psRLLN, LevelData, FileName, 100, INIFile);
		PBSRec.Author[0] = (char) 0;
		LaserColorG = CreateSolidBrush(0x0000FF00);
		LaserColorR = CreateSolidBrush(0x000000FF);
		InitBuffers();
		SFxInit();
		PBHold = FALSE; // used by playback to hold charecters
		VHSOn = FALSE;
		AssignHSFile();
		break;
	case WM_PAINT:
		pdc = BeginPaint(Window, & PI);
		gDC = pdc; // we use gDC for most graphics stuff
		SelectObject(gDC, MyFont);
		GetClientRect(Window, & Box);

		// draw 3D frames }
		// draw 3D frame around game board inner
		JK3dFrame(pdc, XOffset - 1, YOffset - 1, (SpBm_Width * 16) + XOffset, (SpBm_Height * 16) + YOffset, FALSE);
		JK3dFrame(pdc, XOffset - 2, YOffset - 2, (SpBm_Width * 16) + XOffset + 1, (SpBm_Height * 16) + YOffset + 1, FALSE);
		// draw 3D frame around game board outer (including coordinate labels)
		JK3dFrame(pdc, 1, 1, ContXPos - 5, Box.bottom - 2, TRUE);
		// Draw 3D frame around Level info box
		JK3dFrame(pdc, ContXPos - 1, 1, ContXPos + 181, Box.bottom - 2, TRUE);
		// Draw 3D frame around buttons (only if not in editor mode)
		if (!EditorOn)
			JK3dFrame(pdc, ContXPos + 10, 250, ContXPos + 165, 405, FALSE);

		// Display level information background at (ContXPos,2, 180,245)
		tDC = CreateCompatibleDC(pdc);
		OpenScreen = LoadImageFile(hInst, "CONTROLBM", CONTROL_BMP);
		tBM = SelectObject(tDC, OpenScreen);
		// put up control bitmap } background for level info
		BitBlt(pdc, ContXPos, 2, 180, 245, tDC, 0, 0, SRCCOPY);
		SelectObject(tDC, tBM);
		DeleteObject(OpenScreen);
		SetBkMode(pdc, TRANSPARENT);
		SetTextAlign(pdc, TA_CENTER);
		SetTextColor(pdc, 0x00808080);

		// Draw opening quick help bitmap over the level
		if ((CurLevel == 0) || QHELP) {
			// come here in the beggining before a level is loaded
			OpenScreen = LoadImageFile(hInst, "OPENING", OPENING_BMP);
			tBM = SelectObject(tDC, OpenScreen);
			StretchBlt(gDC, XOffset, YOffset, SpBm_Width * 16, SpBm_Height * 16, tDC, 0, 0, 384, 384, SRCCOPY);
			SelectObject(tDC, tBM);
			DeleteObject(OpenScreen);
			x = XOffset + 3;
			y = YOffset + (SpBm_Height * 8);
			j = 1;
			for (i = 0; i < 16; i++) {
				PutSprite(OpeningBMA[i], x, y);
				x += (SpBm_Width * 4);
				j++;
				if (j > 4) {
					x = XOffset + 3;
					y += (SpBm_Height * 2);
					j = 1;
				}
			}
			// desactive  2004/05/09 - mgy
			// TextOut(pdc,(SpBm_Width*13),(SpBm_Height*16),App_Version,strlen(App_Version));
		} else {
			// Label Game Grid
			x = SpBm_Width / 2;
			y = (SpBm_Height - 15) / 2;
			for (i = 1; i < 17; i++) {
				TextOut(pdc, 8, YOffset + y + ((i - 1) * SpBm_Height), itoa(i, temps, 10), strlen(temps));
				if (i < 10) {
					TextOut(pdc, 8 + XOffset + (16 * SpBm_Width), YOffset + y + ((i - 1) * SpBm_Height), itoa(i, temps, 10), strlen(temps));
				} else {
					strcpy(temps, "1 ");
					TextOut(pdc, -1 + 8 + XOffset + (16 * SpBm_Width), YOffset + y + ((i - 1) * SpBm_Height), temps, strlen(temps));
					itoa(i - 10, temps, 10);
					TextOut(pdc, 3 + 8 + XOffset + (16 * SpBm_Width), YOffset + y + ((i - 1) * SpBm_Height), temps, strlen(temps));
				}

				strcpy(temps, "@");
				temps[0] = temps[0] + i;
				TextOut(pdc, XOffset + x + ((i - 1) * SpBm_Width), 1, temps, strlen(temps));
				TextOut(pdc, XOffset + x + ((i - 1) * SpBm_Width), YOffset + 1 + (16 * SpBm_Height), temps, strlen(temps));

			}

			PutLevel(); //Draw level
			if (EditorOn) {
				PutSelectors();
				ShowTunnelID();
			} else {
				//Draw level info text
				SetTextColor(pdc, DifCList[0]);
				itoa(CurLevel, temps, 10);
				switch (CurRecData.SDiff) // Set text colour and temps text based on level difficulty
				{
				case 1:
					strcat(temps, txt023);
					SetTextColor(pdc, DifCList[1]);
					break;
				case 2:
					strcat(temps, txt024);
					SetTextColor(pdc, DifCList[2]);
					break;
				case 4:
					strcat(temps, txt025);
					SetTextColor(pdc, DifCList[3]);
					break;
				case 8:
					strcat(temps, txt026);
					SetTextColor(pdc, DifCList[4]);
					break;
				case 16:
					strcat(temps, txt027);
					SetTextColor(pdc, DifCList[5]);
					break;
				}
				TextOut(pdc, ContXPos + 91, 43, temps, strlen(temps));
				TextOut(pdc, ContXPos + 91, 100, CurRecData.LName, strlen(CurRecData.LName));
				TextOut(pdc, ContXPos + 91, 150, CurRecData.Author, strlen(CurRecData.Author));
				SetTextColor(pdc, 0x0000FF00);
				TextOut(pdc, ContXPos + 48, 207, itoa(Game.ScoreMove, temps, 10), strlen(temps));
				TextOut(pdc, ContXPos + 134, 207, itoa(Game.ScoreShot, temps, 10), strlen(temps));
			}
		}
		DeleteDC(tDC);
		EndPaint(Window, & PI);
		return (0);

		// KEY PRESS: if key down event, then add key ID to keyboard buffer (RecBuffer[])
	case WM_KEYDOWN:
		if (!EditorOn) {
			if ((wparam < 32) || (wparam > 40)) return (0); // Must be one of SPACEBAR (32), PAGE UP, PAGE DOWN, END, HOME, LEFT ARROW, UP ARROW, RIGHT ARROW, DOWN ARROW (40)
			if ((RB_TOS > Game.RecP) && (lparam & 0x40000000)) return (0); //If Top Of Stack > Record pointer && Transition is keydown
			AddKBuff(wparam);
			return (0);
		}
		break;

	// main game logic processing *****************************************
	case WM_TIMER:

		if (QHELP) return (0);

		gDC = GetDC(Window);
		SelectObject(gDC, MyFont);

		// If newly loaded level then set up level
		if (FindTank) // Newly loaded level so draw board and turn off FindTank
		{
			FindTank = FALSE;
			PutLevel();
			SetTimer(MainH, 1, GameDelay, NULL); //Restart the timer for GameDelay (ms). Sends WM_TIMER message when timer up
		}

		// Animation: cycle through frames with AniCount++
		if (Ani_On) AniCount++;
		if (AniCount == ani_delay) Animate(); // Do Animation. Can slow animation frames with ani_delay

		// Move laser
		if (Game.Tank.Firing)
			MoveLaser(); // Move laser if one was fired

		if (PBOpen) //?If playback is on
		{
			if (Speed == 2) {
				SlowPB++;
				if (SlowPB == SlowPBSet) SlowPB = 1;
			}
			if (PlayBack && (!(ConvMoving || SlideO.s || SlideT.s)) &&
				((Speed != 2) || ((Speed == 2) && (SlowPB == 1)))) {
				PBHold = FALSE;
				itoa(Game.RecP, temps, 10);
				SendMessage(PBCountH, WM_SETTEXT, 0, (long)(temps));
				if (Speed == 3) SendMessage(PlayH, WM_COMMAND, ID_PLAYBOX_02, 0);
			} else PBHold = TRUE;
		}

		// Check Key Press }
		// PROCESS KEYBOARD INPUT FROM USER
		// python: # if ((Game.RecP < RB_TOS) && (!(Game.Tank.Firing || ConvMoving || SlideO.s || SlideT.s || PBHold)))
		// if (inputs on stack) && (tank not firing) && (conveyors not moving) && (nothing sliding) && (playback not paused)
		if ((Game.RecP < RB_TOS) && // (speedBug) &&
			(!(Game.Tank.Firing || ConvMoving || SlideO.s || SlideT.s || PBHold))) {
			switch (RecBuffer[Game.RecP]) {
				case VK_UP:
					MoveTank(1); // Move tank Up one
					break;
				case VK_RIGHT:
					MoveTank(2);
					break;
				case VK_DOWN:
					MoveTank(3);
					break;
				case VK_LEFT:
					MoveTank(4);
					break;
				case VK_SPACE:
				{
					UpdateUndo();
					Game.ScoreShot++; // do here Not in FireLaser
					FireLaser(Game.Tank.X, Game.Tank.Y, Game.Tank.Dir, S_Fire); // Bang
				}
			}
			Game.RecP++; // Point to next charecter
			AntiTank(); // give the Anti-Tanks a turn to play
		}

		// resolve momenta
		if (SlideO.s)
			IceMoveO();
		if (SlideT.s)
			IceMoveT();
		if (TankDirty)
			UpDateTank(); // I know we do this again later.
		ConvMoving = FALSE; // used to disable Laser on the conveyor


		switch (Game.PF[Game.Tank.X][Game.Tank.Y]) // Check where the tank ended up
		{
			case 2:
				if (Game_On) // Reached the Flag
				{
					GameOn(FALSE);
					SoundPlay(S_EndLev);
					if (!PBOpen) {
						if (Recording) SendMessage(Window, WM_SaveRec, 0, 0);
						CheckHighScore();
						LoadNextLevel(FALSE, FALSE);
					}
				}
				break;
			case 3:
				PostMessage(Window, WM_Dead, 0, 0); // Water
				break;
			case 15:
				if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1)) // Conveyor Up
					ConvMoveTank(0, -1, TRUE);
				break;
			case 16:
				if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y))
					ConvMoveTank(1, 0, TRUE);
				break;
			case 17:
				if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1))
					ConvMoveTank(0, 1, TRUE);
				break;
			case 18:
				if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y))
					ConvMoveTank(-1, 0, TRUE);
		}

		// Check the mouse Buffer
		if ((Game.RecP == RB_TOS) && (MB_TOS != MB_SP) &&
			(!(Game.Tank.Firing || ConvMoving || SlideO.s || SlideT.s))) {
			if (MouseOperation(MB_SP)) // Turn Mouse Operation into KB chars
			{
				MB_SP++;
				if (MB_SP == MaxMBuffer) MB_SP = 0;
			} else {
				MB_SP = MB_TOS; // error so clear the rest
				MessageBeep(0);
			}
		}
		if (TankDirty)
			UpDateTank();
		ReleaseDC(Window, gDC);
		return (0);

	case WM_GameOver:
		DialogBox(hInst, "WinBox", Window, (DLGPROC) WinBox);
		return (0);

	case WM_NewHS:
		DialogBox(hInst, "HighBox", Window, (DLGPROC) HSBox);
		return (0);

	case WM_SaveRec:
		if (PBSRec.Author[0] == (char) 0)
			DialogBox(hInst, "RecBox", Window, (DLGPROC) RecordBox);
		PBfn.lpstrTitle = txt006;
		PBfn.Flags = OFN_HIDEREADONLY | OFN_OVERWRITEPROMPT;
		strcpy(PBSRec.LName, CurRecData.LName);
		BuildPB_Name();
		if (GetSaveFileName( & PBfn)) {
			if (strchr(PBFileName, '.') == 0) strcat(PBFileName, ".lpb");
			if (Game.RecP < RecMax) PBSRec.Size = Game.RecP; // Set Playback size
			else PBSRec.Size = RecMax; // WOW Big Level
			SavePBFile();
		}
		return (0);

	case WM_Dead:
		GameOn(FALSE);
		if (VHSOn) {
			RB_TOS = Game.RecP;
			return (0);
		}
		SoundPlay(S_Die);
		i = DialogBox(hInst, "DeadBox", Window, (DLGPROC) DeadBox);
		switch (i) {
		case ID_DEADBOX_UNDO:
			SendMessage(Window, WM_COMMAND, 110, 0);
			GameOn(TRUE);
			break;
		case ID_DEADBOX_RESTART:
		case 2: // Cancel
			UndoStep(); // We have to undo the error first ( incase we Restart Undo)
			PostMessage(Window, WM_COMMAND, 105, 0);
		}
		return (0);

	case WM_CLOSE:
		if (GameInProg) {
			i = MessageBox(MainH, txt039, txt038, MB_YESNO | MB_ICONQUESTION);
			if (i == IDYES) SendMessage(MainH, WM_SaveRec, 0, 0);
		}
		DestroyWindow(Window);
		return (0);

	case WM_DESTROY:
		if (Game_On)
			GameOn(FALSE); // Kill Timer
		GFXKill();
		KillBuffers();
		DeleteObject(LaserColorR);
		DeleteObject(LaserColorG);
		WinHelp(Window, HelpFile, HELP_QUIT, 0);
		PostQuitMessage(0);
		return (0);

	case WM_MOVE:
		twp.length = sizeof(twp);
		GetWindowPlacement(Window, & twp);
		if (twp.showCmd != SW_SHOWNORMAL) break;
		itoa(twp.rcNormalPosition.top, temps, 10);
		WritePrivateProfileString("SCREEN", psYpos, temps, INIFile);
		itoa(twp.rcNormalPosition.left, temps, 10);
		WritePrivateProfileString("SCREEN", psXpos, temps, INIFile);
		break;
	case WM_MOUSEMOVE:
		if (EditorOn) // if we are editing then check mouse
		{
			if ((!(wparam & (MK_RBUTTON | MK_LBUTTON))) ||
				(wparam & MK_SHIFT)) return (0); // Mouse Not Down or Shift pressed

			y = ((HIWORD(lparam) - XOffset) / SpBm_Height);
			x = ((LOWORD(lparam) - YOffset) / SpBm_Width);
			if ((x < 0) || (x > 15) || (y < 0) || (y > 15)) return (0);
			if (wparam == MK_LBUTTON) {
				if ((Game.PF[x][y] != CurSelBM_L) && (CurSelBM_L != MaxObjects))
					ChangeGO(x, y, CurSelBM_L);
			} else {
				if ((Game.PF[x][y] != CurSelBM_R) && (CurSelBM_R != MaxObjects))
					ChangeGO(x, y, CurSelBM_R);
			}
			return (0);
		}
		break;
	case WM_LBUTTONDOWN:
		if (EditorOn) {
			SetFocus(Window); // We need to get the focus off of the Edits
			if (LOWORD(lparam) > ContXPos) {
				// we are on the selector window area
				y = (HIWORD(lparam) - 250) / (SpBm_Height + 4);
				x = (LOWORD(lparam) - (ContXPos + 5)) / (SpBm_Width + 4);
				i = x + (y * EditBMWidth);
				if ((i > MaxObjects + 1) || (i < 0)) return (0);
				CurSelBM_L = i;
				gDC = GetDC(Window);
				PutSelectors();
				ReleaseDC(Window, gDC);
			} else {
				// we are in the Game window area - Edit Mode
				y = ((HIWORD(lparam) - XOffset) / SpBm_Height);
				x = ((LOWORD(lparam) - YOffset) / SpBm_Width);
				if ((x < 0) || (x > 15) || (y < 0) || (y > 15)) return (0);
				if ((wparam & MK_SHIFT) == MK_SHIFT) ChangeGO(x, y, GetNextBMArray[Game.PF[x][y]]); // Rotate Object
				else {
					if (Game.PF[x][y] != CurSelBM_L) ChangeGO(x, y, CurSelBM_L);
				}
				Modified = TRUE;
			}
			return (0);
		} else {
			y = ((HIWORD(lparam) - XOffset) / SpBm_Height);
			x = ((LOWORD(lparam) - YOffset) / SpBm_Width);
			if ((x < 0) || (x > 15) || (y < 0) || (y > 15)) return (0);
			MBuffer[MB_TOS].X = x;
			MBuffer[MB_TOS].Y = y;
			MBuffer[MB_TOS].Z = 1; // 1 = mouse clicked
			MB_TOS++;
			if (MB_TOS == MaxMBuffer) MB_TOS = 0;
		}
		break;
	case WM_RBUTTONDOWN:
		if (EditorOn) {
			SetFocus(Window); // We need to get the focus off of the Edits
			if (LOWORD(lparam) > ContXPos) {
				y = (HIWORD(lparam) - 250) / (SpBm_Height + 4);
				x = (LOWORD(lparam) - (ContXPos + 5)) / (SpBm_Width + 4);
				i = x + (y * EditBMWidth);
				if ((i > MaxObjects + 1) || (i < 0)) return (0);
				CurSelBM_R = i;
				gDC = GetDC(Window);
				PutSelectors();
				ReleaseDC(Window, gDC);
			} else {
				y = ((HIWORD(lparam) - XOffset) / SpBm_Height);
				x = ((LOWORD(lparam) - YOffset) / SpBm_Width);
				if ((x < 0) || (x > 15) || (y < 0) || (y > 15)) return (0);
				if (Game.PF[x][y] != CurSelBM_R) ChangeGO(x, y, CurSelBM_R);
				Modified = TRUE;
			}
			return (0);
		} else {
			// Get the square clicked on (x,y)
			y = ((HIWORD(lparam) - XOffset) / SpBm_Height);
			x = ((LOWORD(lparam) - YOffset) / SpBm_Width);
			if ((x < 0) || (x > 15) || (y < 0) || (y > 15))
				return (0);
			MBuffer[MB_TOS].X = x;
			MBuffer[MB_TOS].Y = y;
			MBuffer[MB_TOS].Z = 2; // 2 = mouse R clicked
			MB_TOS++;
			if (MB_TOS == MaxMBuffer)
				MB_TOS = 0;
		}
		break;
	case WM_COMMAND:
		if (!EditorOn) SetFocus(Window); // We need this for the buttons
		switch (LOWORD(wparam)) {
		case 101: // New Game
			LastLevel = CurLevel;
			CurLevel = 0;
			if (RLL) // Remember Last Level
			{
				GetPrivateProfileString("DATA", psRLLL, "1", temps, 5, INIFile);
				CurLevel = atoi(temps);
				CurLevel--;
			}
			if (!LoadNextLevel(TRUE, FALSE))
				CurLevel = LastLevel;
			return (0);
		case 102: // Toggle Sound Option
			ToggleOpt(102, MMenu, & Sound_On, psSound);
			return (0);
		case 103: // Exit
			if (GameInProg) {
				i = MessageBox(MainH, txt039, txt038, MB_YESNO | MB_ICONQUESTION);
				if (i == IDYES) SendMessage(MainH, WM_SaveRec, 0, 0);
			}
			DestroyWindow(Window);
			return (0);
		case 104: // Toggle Animation Option
			ToggleOpt(104, MMenu, & Ani_On, psAni);
			return (0);
		case 105:
			if (CurLevel > 0) // ReStart
			{
				if (UndoP > 0) UpdateUndo(); // Without this we loose the last move
				memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD)); // Game.PF = CurRecData.PF;
				BuildBMField();
				InvalidateRect(Window, NULL, FALSE);
				GameOn(TRUE);
				Game.RecP = 0;
				RB_TOS = 0;
				SlideO.s = 0; // stop any sliding
				SlideMem.count = 0; // MGY --- stop any sliding
				SlideT.s = 0;
				// Lets also init the Mouse Buffer
				MB_TOS = MB_SP = 0;
			}
			return (0);

		case 106: // Load Level
			x = Game_On;
			LastLevel = CurLevel;
			GameOn(FALSE);
			i = DialogBox(hInst, "LoadLev", Window, (DLGPROC) LoadBox);
			if (i > 100) {
				CurLevel = i - 101;
				if (!LoadNextLevel(TRUE, TRUE)) {
					CurLevel = LastLevel;
					GameOn(x);
				}
			} else
				GameOn(x);
			return (0);

		case 107: // Skip Level
			LoadNextLevel(FALSE, FALSE);
			return (0);

		case 108: // Open Data File
			x = Game_On;
			GameOn(FALSE);
			OFN.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST;
			strcpy(temps, FileName);
			if (GetOpenFileName( & OFN)) {
				AssignHSFile();
				CurLevel = 0;
				Backspace[BS_SP] = 0; // Clear Backspace stack
				EnableMenuItem(MMenu, 118, MF_BYCOMMAND | MF_GRAYED); // Disable Menu Item
				LoadNextLevel(TRUE, FALSE);
			} else {
				GameOn(x);
				strcpy(FileName, temps);
			}
			return (0);

		case 109: // Toggle Remember Last Level Option
			ToggleOpt(109, MMenu, & RLL, psRLLOn);
			return (0);

		case 110: // Undo
			UndoStep();
			if (UndoBuffer[UndoP].Tank.Dir == 0) {
				EnableMenuItem(MMenu, 110, MF_GRAYED); // disable Undo
				EnableWindow(BT1, SW_HIDE);
			}
			InvalidateRect(Window, NULL, FALSE);
			return (0);
		case 111: // Save Position
			SaveGame = Game;
			EnableMenuItem(MMenu, 112, MF_ENABLED);
			EnableWindow(BT3, SW_SHOWNA);
			return (0);

		case 112: // Restore Position
			Game = SaveGame;
			RB_TOS = Game.RecP; // clear all keys Past this Pos
			MB_TOS = MB_SP = 0; // we need to cancle all mouse inputs
			InvalidateRect(Window, NULL, FALSE);
			return (0);

		case 113: // High Score
			DialogBox(hInst, "HighList", Window, (DLGPROC) HSList);
			return (0);

		case 114: // PlayBack Recording
			BuildPB_Name();
			PBfn.lpstrTitle = txt020;
			PBfn.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST;
			if (GetOpenFileName( & PBfn)) {
				if (LoadPlayback())
					DialogBox(hInst, "PlayBox", Window, (DLGPROC) PBWindow);
			}
			return (0);

		case 115: // Toggle AutoRecord Option
			if (GetMenuState(MMenu, 115, 0) & MF_CHECKED) {
				CheckMenuItem(MMenu, 115, 0);
				ARecord = FALSE;
				WritePrivateProfileString("OPT", psARec, "No", INIFile);
				if (GetMenuState(MMenu, 123, 0) & MF_CHECKED)
					PostMessage(Window, WM_COMMAND, 123, 0); // Record Off
			} else {
				CheckMenuItem(MMenu, 115, MF_CHECKED);
				ARecord = TRUE;
				WritePrivateProfileString("OPT", psARec, "Yes", INIFile);
				if (!(GetMenuState(MMenu, 123, 0) & MF_CHECKED))
					PostMessage(Window, WM_COMMAND, 123, 0); // Record On
			}
			return (0);

		case 116: // Toggle Skip Complete Levels Option
			ToggleOpt(116, MMenu, & SkipCL, psSCL);
			return (0);

		case 117:
			if (Recording) PostMessage(Window, WM_SaveRec, 0, 0); // F6 - Save Rec
			break;

		case 118: // Backspace Level / Last Level Played
			if (Backspace[BS_SP]) {
				Backspace[BS_SP] = 0; // this is so we dont loop around
				BS_SP--;
				if (BS_SP < 0)
					BS_SP = 9;
				if (Backspace[BS_SP] == 0)
					return (0); // error
				i = BS_SP - 1;
				if (i < 0)
					i = 9;
				if (Backspace[i] == 0)
					EnableMenuItem(MMenu, 118, MF_BYCOMMAND | MF_GRAYED); // Disable Menu Item
				LastLevel = CurLevel;
				CurLevel = Backspace[BS_SP] - 1;
				if (!LoadNextLevel(TRUE, FALSE))
					CurLevel = LastLevel;
			}
			return (0);

		case 119: // Previous Level
			LoadLastLevel();
			return (0);

		case 120: // small size
			SetGameSize(1);
			InvalidateRect(Window, NULL, TRUE);
			return (0);

		case 121: // medium size
			SetGameSize(2);
			InvalidateRect(Window, NULL, TRUE);
			return (0);

		case 122: // large size
			SetGameSize(3);
			InvalidateRect(Window, NULL, TRUE);
			return (0);
			
		case 123: // Turn Off Recording if on
			if (GetMenuState(MMenu, 123, MF_BYCOMMAND) && MF_CHECKED != 0) {
				CheckMenuItem(MMenu, 123, 0);
				Recording = FALSE;
				EnableMenuItem(MMenu, 117, MF_GRAYED);
				SetWindowText(MainH, App_Title);
			} else {
				CheckMenuItem(MMenu, 123, MF_CHECKED);
				Recording = TRUE;
				EnableMenuItem(MMenu, 117, 0); // enable Save Recording
				SetWindowText(MainH, REC_Title);
			}
			return (0);
		case 124:
			if (CurLevel > 0) // RePlay
			{
				memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD)); // Game.PF = CurRecData.PF;
				BuildBMField();
				InvalidateRect(Window, NULL, FALSE);
				ResetUndoBuffer(); //We don't need the old data
				GameOn(TRUE);
				Game.RecP = 0;
			}
			return (0);
		case 125: // Resume Recording
			PBfn.lpstrTitle = txt033;
			PBfn.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST;
			BuildPB_Name();
			if (GetOpenFileName( & PBfn)) {
				x = LoadPlayback();
				PBOpen = FALSE;
				PBHold = FALSE;
				if (x) {
					UpdateWindow(Window);
					VHSPlayback(); // Playback File
					SendMessage(MainH, WM_COMMAND, 123, 0); // Start Recording
				}
			}
			return (0);
		case 126: //Print Game Board
			x = Game_On;
			GameOn(FALSE);
			Print();
			GameOn(x);
			return (0);
		case 127: // Disable Warnings
			ToggleOpt(127, MMenu, & DWarn, psDW);
			return (0);
		case 201: // Editor
			EditorOn = TRUE;
			GameOn(FALSE); // Shut down game engine
			strcpy(temps, App_Title);
			strcat(temps, txt028);
			SetWindowText(Window, temps); // Change window name
			if (Recording) SendMessage(MainH, WM_COMMAND, 123, 0);
			OKtoHS = FALSE;
			SetMenu(Window, EMenu); // Set up editor menu's
			ShowWindow(BT1, SW_HIDE);
			ShowWindow(BT2, SW_HIDE);
			ShowWindow(BT3, SW_HIDE);
			ShowWindow(BT4, SW_HIDE);
			ShowWindow(BT5, SW_HIDE);
			ShowWindow(BT6, SW_HIDE);
			ShowWindow(BT7, SW_HIDE);
			ShowWindow(BT8, SW_HIDE);
			ShowWindow(BT9, SW_HIDE);
			ShowWindow(Ed1, SW_SHOWNA); // setup title window
			SetWindowText(Ed1, CurRecData.LName);
			SendMessage(Ed1, EM_SETMODIFY, 0, 0);
			ShowWindow(Ed2, SW_SHOWNA); // setup Author window
			SendMessage(Ed2, EM_SETMODIFY, 0, 0);
			SetWindowText(Ed2, CurRecData.Author);
			EditDiffSet(CurRecData.SDiff);
			InvalidateRect(Window, NULL, TRUE); // redraw in editor mode
			Modified = FALSE;
			// Strip off the Tunnel Indexers
			for (x = 0; x < 16; x++)
				for (y = 0; y < 16; y++)
					if (ISTunnel(x, y)) Game.PF[x][y] &= 0xFE;
			if (CurLevel == 0) PostMessage(Window, WM_COMMAND, 601, 0); // New Level
			return (0);
		case 225: // Change Difficulty
			x = Game_On;
			GameOn(FALSE);
			DialogBox(hInst, "DiffBox", Window, (DLGPROC) DiffBox);
			GameOn(x);
			return (0);
		case 226: // Graphics Change
			DialogBox(hInst, "GRAPHBOX", Window, (DLGPROC) GraphBox);
			return (0);
		case 301:
			if (Game_On) // Hint
			{
				GameOn(FALSE);
				if (strlen(CurRecData.Hint) > 0)
					MessageBox(Window, CurRecData.Hint, txt021, MB_OK | MB_ICONINFORMATION);
				else MessageBox(Window, txt035, txt021, MB_OK | MB_ICONHAND);
				GameOn(TRUE);
			}
			return (0);
		case 601: // New Level  [Editor]
			for (x = 0; x < 16; x++)
				for (y = 0; y < 16; y++) {
					Game.PF[x][y] = 0;
					Game.BMF[x][y] = 1;
					Game.BMF2[x][y] = 1;
					Game.PF2[x][y] = 0;
				}
			Game.Tank.X = 7;
			Game.Tank.Y = 15;
			Game.Tank.Dir = 1;
			Game.Tank.Firing = FALSE;
			SetWindowText(Ed1, "");
			SendMessage(Ed1, EM_SETMODIFY, 0, 0);
			SetWindowText(Ed2, "");
			SendMessage(Ed2, EM_SETMODIFY, 0, 0);
			CurRecData.Hint[0] = 0; // Clear Out Hint
			InvalidateRect(Window, NULL, TRUE);
			CurLevel = 1;
			Modified = TRUE;
			OKtoSave = FALSE;
			return (0);
		case 602: // Load Level [Editor]
			if (SendMessage(Ed1, EM_GETMODIFY, 0, 0) ||
				SendMessage(Ed2, EM_GETMODIFY, 0, 0)) Modified = TRUE;
			if (Modified)
				if (MessageBox(Window, txt022, txt029, MB_YESNO | MB_ICONQUESTION) == IDYES)
					SendMessage(Window, WM_COMMAND, 603, 0);
			strcpy(temps, FileName); // Save old name in case we cancel
			OFN.Flags = OFN_HIDEREADONLY | OFN_FILEMUSTEXIST;
			if (GetOpenFileName( & OFN)) {
				i = DialogBox(hInst, "LoadLev", Window, (DLGPROC) LoadBox);
				if (i > 100) {
					i -= 101;
					if (!(F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
							FILE_FLAG_RANDOM_ACCESS, NULL))) return (0);
					SetFilePointer(F1, i * sizeof(TLEVEL), NULL, FILE_BEGIN);
					ReadFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, NULL);
					if (BytesMoved == sizeof(TLEVEL)) {
						SetWindowText(Ed1, CurRecData.LName);
						SendMessage(Ed1, EM_SETMODIFY, 0, 0);
						SetWindowText(Ed2, CurRecData.Author);
						SendMessage(Ed2, EM_SETMODIFY, 0, 0);
						CurLevel = i + 1;
						memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD)); // Game.PF = CurRecData.PF;
						BuildBMField();
					}
					CloseHandle(F1);
					InvalidateRect(Window, NULL, TRUE);
					OKtoSave = TRUE;
				} else strcpy(FileName, temps);
			}
			return (0);
		case 603: // Save Level [Editor] }
			if (OKtoSave) {
				F1 = CreateFile(FileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, NULL, OPEN_ALWAYS,
					FILE_FLAG_RANDOM_ACCESS, NULL);
				GetWindowText(Ed1, CurRecData.LName, 30);
				GetWindowText(Ed2, CurRecData.Author, 30);
				memcpy(CurRecData.PF, Game.PF, sizeof(TPLAYFIELD));
				CurRecData.PF[Game.Tank.X][Game.Tank.Y] = 1; // save Tank in File
				SetFilePointer(F1, ((CurLevel - 1) * sizeof(TLEVEL)), NULL, FILE_BEGIN);
				if (WriteFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, NULL)) {
					Modified = FALSE;
					SendMessage(Ed1, EM_SETMODIFY, 0, 0);
					SendMessage(Ed2, EM_SETMODIFY, 0, 0);
				} else FileError();
				CloseHandle(F1);
				if (HSClear) {
					AssignHSFile();
					if (F2 = CreateFile(HFileName, GENERIC_WRITE, FILE_SHARE_READ, NULL, OPEN_EXISTING,
							FILE_FLAG_RANDOM_ACCESS, NULL)) {
						HS.moves = 0;
						SetFilePointer(F2, (CurLevel - 1) * sizeof(THSREC), NULL, FILE_BEGIN);
						WriteFile(F2, & HS, sizeof(THSREC), & BytesMoved, NULL);
						CloseHandle(F2);
					}
				}
			} else SendMessage(MainH, WM_COMMAND, 606, 0); // Save As if new Level
			return (0);
		case 606: // Save As
			OFN.Flags = OFN_HIDEREADONLY;
			if (GetSaveFileName( & OFN)) {
				AssignHSFile();
				F1 = CreateFile(FileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, NULL, OPEN_ALWAYS,
					FILE_FLAG_RANDOM_ACCESS, NULL);
				i = DialogBox(hInst, "PickLevel", Window, (DLGPROC) PickBox);
				CloseHandle(F1);
				if (i > 0) {
					CurLevel = i;
					OKtoSave = TRUE;
					SendMessage(MainH, WM_COMMAND, 603, 0);
				}
			}
			return (0);
		case 604: // Leave Editor
			if (SendMessage(Ed1, EM_GETMODIFY, 0, 0) ||
				SendMessage(Ed2, EM_GETMODIFY, 0, 0)) Modified = TRUE;
			if (Modified)
				if (MessageBox(Window, txt022, txt029, MB_YESNO | MB_ICONQUESTION) == IDYES)
					SendMessage(Window, WM_COMMAND, 603, 0);
			EditorOn = FALSE;
			SetWindowText(Window, App_Title);
			SetMenu(Window, MMenu);
			ShowWindow(Ed1, SW_HIDE);
			ShowWindow(Ed2, SW_HIDE);
			ShowWindow(BT1, SW_SHOWNA);
			ShowWindow(BT2, SW_SHOWNA);
			ShowWindow(BT3, SW_SHOWNA);
			ShowWindow(BT4, SW_SHOWNA);
			ShowWindow(BT5, SW_SHOWNA);
			ShowWindow(BT6, SW_SHOWNA);
			ShowWindow(BT7, SW_SHOWNA);
			ShowWindow(BT8, SW_SHOWNA);
			ShowWindow(BT9, SW_SHOWNA);
			memcpy(CurRecData.PF, Game.PF, sizeof(TPLAYFIELD)); // Update CurRec
			CurRecData.PF[Game.Tank.X][Game.Tank.Y] = 1; // save Tank in Playfield's
			InvalidateRect(Window, NULL, TRUE);
			if (CurLevel > 0) GameOn(TRUE);
			return (0);
		case 605: // Hint [Editor]
			DialogBox(hInst, "HintBox", Window, (DLGPROC) HintBox);
			return (0);
		case 701:
			EditDiffSet(1); // Edit Difficulty Set - Kids
			return (0);
		case 702:
			EditDiffSet(2); // Edit Difficulty Set - Easy
			return (0);
		case 703:
			EditDiffSet(4); // Edit Difficulty Set - Medium
			return (0);
		case 704:
			EditDiffSet(8); // Edit Difficulty Set - Hard
			return (0);
		case 705:
			EditDiffSet(16); // Edit Difficulty Set - Deadly
			return (0);
		case 710: // Shift Game Board Right
			for (x = 1; x < 16; x++)
				for (y = 0; y < 16; y++) {
					ShiftPF[x][y] = Game.PF[x - 1][y];
					ShiftBMF[x][y] = Game.BMF[x - 1][y];
				}
			for (y = 0; y < 16; y++) {
				ShiftPF[0][y] = Game.PF[15][y];
				ShiftBMF[0][y] = Game.BMF[15][y];
			}
			Game.Tank.X++;
			if (Game.Tank.X == 16) Game.Tank.X = 0;
			Modified = TRUE;
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD)); // Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD)); // Update BMF
			InvalidateRect(Window, NULL, TRUE);
			return (0);
		case 711: // Shift Game Board Left
			for (x = 0; x < 15; x++)
				for (y = 0; y < 16; y++) {
					ShiftPF[x][y] = Game.PF[x + 1][y];
					ShiftBMF[x][y] = Game.BMF[x + 1][y];
				}
			for (y = 0; y < 16; y++) {
				ShiftPF[15][y] = Game.PF[0][y];
				ShiftBMF[15][y] = Game.BMF[0][y];
			}
			Game.Tank.X--;
			if (Game.Tank.X < 0) Game.Tank.X = 15;
			Modified = TRUE;
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD)); // Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD)); // Update BMF
			InvalidateRect(Window, NULL, TRUE);
			return (0);
		case 712: // Shift Game Board Up
			for (x = 0; x < 16; x++)
				for (y = 0; y < 15; y++) {
					ShiftPF[x][y] = Game.PF[x][y + 1];
					ShiftBMF[x][y] = Game.BMF[x][y + 1];
				}
			for (x = 0; x < 16; x++) {
				ShiftPF[x][15] = Game.PF[x][0];
				ShiftBMF[x][15] = Game.BMF[x][0];
			}
			Game.Tank.Y--;
			if (Game.Tank.Y < 0) Game.Tank.Y = 15;
			Modified = TRUE;
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD)); // Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD)); // Update BMF
			InvalidateRect(Window, NULL, TRUE);
			return (0);
		case 713: // Shift Game Board Down
			for (x = 0; x < 16; x++)
				for (y = 1; y < 16; y++) {
					ShiftPF[x][y] = Game.PF[x][y - 1];
					ShiftBMF[x][y] = Game.BMF[x][y - 1];
				}
			for (x = 0; x < 16; x++) {
				ShiftPF[x][0] = Game.PF[x][15];
				ShiftBMF[x][0] = Game.BMF[x][15];
			}
			Game.Tank.Y++;
			if (Game.Tank.Y == 16) Game.Tank.Y = 0;
			Modified = TRUE;
			memcpy(Game.PF, ShiftPF, sizeof(TPLAYFIELD)); // Update PF
			memcpy(Game.BMF, ShiftBMF, sizeof(TPLAYFIELD)); // Update BMF
			InvalidateRect(Window, NULL, TRUE);
			return (0);
		case 901: // About Box
			x = Game_On;
			GameOn(FALSE);
			DialogBox(hInst, "AboutBox", Window, (DLGPROC) AboutBox);
			GameOn(x);
			return (0);
		case 902: //Help Index 
			WinHelp(Window, HelpFile, HELP_INDEX, 0);
			return (0);
		case 903: //Help Editor
			WinHelp(Window, HelpFile, HELP_KEY, (DWORD) & help01);
			return (0);
		case 904: //Revisions History
			WinHelp(Window, HelpFile, HELP_KEY, (long) & help02);
			return (0);
		case 905: // Help Writing Levels
			WinHelp(Window, HelpFile, HELP_KEY, (long) & help03);
			return (0);
		case 907: // Quick About Box
			x = Game_On;
			GameOn(FALSE);
			QHELP = TRUE;
			InvalidateRect(Window, NULL, FALSE);
			DialogBox(hInst, "RETBOX", Window, (DLGPROC) RetBox);
			QHELP = FALSE;
			InvalidateRect(Window, NULL, FALSE);
			GameOn(x);
			return (0);
		case 906: //Global high scores list
			DialogBox(hInst, "GHighList", Window, (DLGPROC) GHSList);
			return (0);
		default:
			return (DefWindowProc(Window, Message, wparam, lparam));
		} // switch(wparam) of WM_COMMAND
		default:
			return (DefWindowProc(Window, Message, wparam, lparam));
	} // switch (Message)
	return (0);
}

// main app entry for windows
// WinMain is the program entry point. When the program starts, it registers some information about the behavior of the application window. One of the most important items is the address of a function, named WindowProc in this example. This function defines the behavior of the window—its appearance, how it interacts with the user, and so forth.
int APIENTRY WinMain(HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nCmdShow) {
	MSG msg;
	HANDLE hAccelTable1, hAccelTable2; // keyboard shortcuts / Accelerator Tables
	int tacc;
	char * P;

	// Other instances of app running?
	if (!hPrevInstance) {
		// Initialize shared things
		if (!InitApplication(hInstance)) return FALSE; // Exits if unable to initialize
	}
	hAccelTable1 = LoadAccelerators(hInst, "ACC1"); // Load keyboard shortcuts from ACC1 ACCELERATORS lines in lt32l_us.inc
	hAccelTable2 = LoadAccelerators(hInst, "ACC2");

	// Create Full INI file name
	// Help file name is created in InitInstance()
	//https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea
	GetModuleFileName(NULL, INIFile, MAX_PATH);
	//Create files working_dir/INIFile, HelpFile, LangFile using INIFileName, LANGFileName
	strcpy(HelpFile, INIFile);
	P = strrchr(INIFile, '\\'); // Find last occurrence of '\\'
	if (P) {
		P++;
		strcpy(P, INIFileName); // add name
		if (GetPrivateProfileInt("DATA", psNET, 0, INIFile) == 1) strcpy(INIFile, INIFileName);
	} else strcpy(INIFile, INIFileName); // Error so put in Windows Directory

	strcpy(LANGFile, INIFile); // *dest, *src -> *dest
	P = strrchr(LANGFile, '\\');
	if (P) {
		P++;
		strcpy(P, LANGFileName); // add name
	} else strcpy(LANGFile, LANGFileName); // Error so put in Default Directory

	// Perform initializations that apply to a specific instance
	if (!InitInstance(hInstance, nCmdShow)) return FALSE;
	// Get Command line stuff
	if (lpCmdLine[0] != 0) {
		strcpy(FileName, lpCmdLine);
		if (strstr(strlwr(lpCmdLine), ".lvl")) {
			AssignHSFile();
			CurLevel = 0;
			LoadNextLevel(FALSE, FALSE);
		}
	}
	//  Each time the program calls the DispatchMessage function, it indirectly causes Windows to invoke the WindowProc function, once for each message.
	// Acquire and dispatch messages until a WM_QUIT message is received.
	// BOOL GetMessage(
	//  LPMSG lpMsg, A pointer to an MSG structure that receives message information from the thread's message queue.
	//	HWND  hWnd, If hWnd is NULL, GetMessage retrieves messages for any window that belongs to the current thread, and any messages on the current thread...
	//	UINT  wMsgFilterMin,
	//	UINT  wMsgFilterMax
	//	); //If the function retrieves the WM_QUIT message, the return value is zero.
	//https://docs.microsoft.com/en-gb/windows/win32/api/winuser/nf-winuser-getmessage
	while (GetMessage( & msg, NULL, 0, 0)) { // dont translateAccelerators if editor is on

		if (EditorOn) tacc = TranslateAccelerator(msg.hwnd, hAccelTable2, & msg); // Editor Accelerator - converts keyboard shortcuts to menu selections, returns 0 if fails
		else tacc = TranslateAccelerator(msg.hwnd, hAccelTable1, & msg);

		if (!tacc) {
			TranslateMessage( & msg); // Translates virtual-key messages into character messages
			DispatchMessage( & msg); // Dispatches a message to a window procedure
		}
	}
	// Window is quitting
	DestroyMenu(EMenu);
	DeleteObject(MyFont);
	// Returns the value from PostQuitMessage
	return msg.wParam;
}

BOOL InitApplication(HINSTANCE hInstance)
// Initialize the Application ( Only once  )
{
	WNDCLASS wc;
	// Fill in window class structure with parameters that describe the
	// main window.
	//	lpszClassName is a string that identifies the window class.
	wc.style = CS_BYTEALIGNWINDOW | CS_SAVEBITS;
	wc.lpfnWndProc = (WNDPROC) WndProc; // Window Procedure
	//The window procedure defines most of the behavior of the window.
	wc.cbClsExtra = 0; // No per-class extra data.
	wc.cbWndExtra = 0; // No per-window extra data.
	wc.hInstance = hInstance; // Owner of this class
	//hInstance is the handle to the application instance. Get this value from the hInstance parameter of wWinMain.
	wc.hIcon = LoadIcon(hInstance, "icon1"); // Icon name from .RC
	wc.hCursor = LoadCursor(NULL, IDC_ARROW); // Cursor, IDC_ARROW=Standard arrow
	wc.hbrBackground = GetStockObject(LTGRAY_BRUSH); // Default color
	wc.lpszMenuName = "MAIN"; // Menu name from .RC
	wc.lpszClassName = App_Class; // Name to register as
	//	lpszClassName is a string that identifies the window class.
	// Register the window class and return FALSE if unsuccesful.
	if (!RegisterClass( & wc)) return FALSE;
	return TRUE;
}

BOOL InitInstance(HINSTANCE hInstance, int nCmdShow) {
	HWND Window; // Main window handle.
	int xp, yp;
	// <LangFile>
	TCHAR * p;
	TCHAR buffer[50];
	// </LangFile>

	hInst = hInstance; // Store instance handle in our global variable
	xp = GetPrivateProfileInt("SCREEN", psXpos, CW_USEDEFAULT, INIFile); // Getting from INI file
	yp = GetPrivateProfileInt("SCREEN", psYpos, CW_USEDEFAULT, INIFile);
	// Create a main window for this application instance.
	Window = CreateWindow(App_Class, App_Title,
		WS_OVERLAPPEDWINDOW & ~(WS_SIZEBOX | WS_MAXIMIZEBOX),
		xp, yp, 725, 579, 0, 0, hInst, NULL); //className, windowName, windowStyle, 
	//window position xy, width (includes window borders), height, parent, menu, instance, parameter to pass
	if (!Window) return FALSE;
	MainH = Window;
	MMenu = GetMenu(Window);
	OFN.hwndOwner = Window;
	PBfn.hwndOwner = Window;
	EMenu = LoadMenu(hInst, "MENU2");

	// ************************************************************************
	// Read the language file is exist
	// fill the LANGText[],
	// update the two menus,
	// ************************************************************************
	// <LangFile>
	InitLanguage(MMenu, EMenu);

	// Buit HelpFile file name here, after InitLanguage()
	p = strrchr(HelpFile, '\\');
	if (p) {
		p++;
		strcpy(p, HelpFileName); // add name
	} else strcpy(HelpFile, HelpFileName); // Error so put in Default Directory

	// Build up the correct filter strings for OPENFILENAME structure
	p = szFilterOFN;
	lstrcpy(buffer, txt002);
	lstrcpy(p, buffer);
	p += lstrlen(buffer) + 1;
	lstrcpy(buffer, TEXT("*.LVL"));
	lstrcpy(p, buffer);
	p += lstrlen(buffer) + 1;
	strcpy(p, TEXT("\0"));
	OFN.lpstrFilter = szFilterOFN;

	// Build up the correct filter strings for OPENFILENAME structure
	p = szFilterPBfn;
	lstrcpy(buffer, txt005);
	lstrcpy(p, buffer);
	p += lstrlen(buffer) + 1;
	lstrcpy(buffer, TEXT("*.LPB"));
	lstrcpy(p, buffer);
	p += lstrlen(buffer) + 1;
	strcpy(p, TEXT("\0"));
	PBfn.lpstrFilter = szFilterPBfn;
	// </LangFile>

	//############################################################################

	//CREATE MAIN BUTTONS

	//  HWND CreateWindow(
	//  LPCTSTR lpClassName,	pointer to registered class name
	//  LPCTSTR lpWindowName,	pointer to window name
	//  DWORD dwStyle,		 	window style
	//  int x,		 			horizontal position of window
	//  int y,		 			vertical position of window
	//  int nWidth,				window width
	//  int nHeight,		 	window height
	//  HWND hWndParent,		handle to parent or owner window
	//  HMENU hMenu,			handle to menu or child-window identifier
	//  HANDLE hInstance,		handle to application instance
	//  LPVOID lpParam		 	pointer to window-creation data
	//  );
	// https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowa
	//###########################################################################

	// Title Edit Box - Visable only in Editor Mode
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
		NULL);
	// Author Edit Box - Visable only in Editor Mode }
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
		NULL);

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
		NULL);
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
		NULL);
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
		NULL);
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
		NULL);

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
		NULL);
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
		NULL);

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
		NULL);
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
		NULL);
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
		NULL);

	MyFont = CreateFont(16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Arial");
	SetGameSize(GetPrivateProfileInt("SCREEN", psSize, 1, INIFile));
	ShowWindow(Window, nCmdShow); // Show the window
	UpdateWindow(Window); // Sends WM_PAINT message
	return TRUE; // We succeeded...

}

// ltank2.c
/*******************************************************
 **             LaserTank ver 4.0                     **
 **               By Jim Kindley                      **
 **               (c) 2001                            **
 **         The Program and Source is Public Domain   **
 *******************************************************
 **       Release version 2002 by Yves Maingoy        **
 **               ymaingoy@free.fr                    **
 *******************************************************/

#include <windows.h>

#include <windowsx.h>

#include <commdlg.h>

#include <string.h>

#include <mmsystem.h>

#include <stdio.h>

#include "ltank.h"

#include "ltank_d.h"

#include "lt_sfx.h"

// Declare the Global Varables

int GFXError = 0; // error used for load
int GFXOn = FALSE; // True when Graphics are loaded
int TankDirty = FALSE; // if true then we need to repaint the tank
int NoLevel = TRUE; // if true Main Paint will show Openning
int Game_On = FALSE; // true when game is running
int Ani_On = TRUE; // true when Animation is On
int RLL = TRUE; // remember last level
int ConvMoving = FALSE; // true when moving on the conveyor belts
int OKtoHS = TRUE; // true if OK to Set HighScore
int OKtoSave = FALSE; // true if OK to Set HighScore
int Recording = FALSE; // true if Recording
int PlayBack = FALSE; // true if PlayBack is recording
int PBOpen = FALSE; // true when Playback window is open
int ARecord = FALSE; // AutoRecord is On/Off
int SkipCL = FALSE; // true if Skip Complete Level is on
int DWarn = FALSE; // Disable Warning
int CurLevel = 0; // Used to Figure out the Current Level
int AniLevel = 0; // Used for Animation Position, Animation frame 0, 1, 2
int AniCount = 0; // counter for animation, Counts ticks between animating. When AniCount++ reaches ani_delay ticks then animate & AniCount=0
int CurSelBM_L = 3; // current selected bm in editor
int CurSelBM_R = 0; // current selected bm in editor
int SpBm_Width = 32; // Width of Sprite
int SpBm_Height = 32; // Height of Sprite
int LaserOffset = 10; // Offset of Laser Size
int ContXPos = 540; // Position of Control Side
int EditBMWidth = 5; // # of bitmaps across edit select area
int Speed = 1; // Playback speed
int SlowPB = 1; //Delay counter to slow down animation when Speed==2
int RecBufSize = 10000; // Size of recording buffer
int UndoBufSize = 3200; // Size of Undo Buffer ( * sizeof(TGAMEREC))
int Difficulty = 0; // Difficulty Enable ( use Bits )
int GraphM = 0; // Graphics Mode 0=int; 1=ext; 2=ltg
int FindTank = FALSE; // True when First starting a level, used to draw target lines on tank when first loading level
int BlackHole = FALSE; // True if we TunnleTranslae to a Black Hole (no exit found)

TGAMEREC Game, SaveGame; // The Level Data
TLEVEL CurRecData;
HBRUSH LaserColor, LaserColorR, LaserColorG;
HDC gDC; // Use this game dc for all ops - set in WM_PAINT gDC = BeginPaint(Window, &PI)
char FileName[MAX_PATH]; //Default = LevelData = 'LaserTank.lvl' (WM_CREATE)
char HFileName[MAX_PATH]; //Default = 'LaserTank.hs' (AssignHSFile())
char GHFileName[MAX_PATH]; //Default = 'LaserTank.ghs' (AssignHSFile())
char PBFileName[MAX_PATH]; //Default = 'LaserTank_0000.lpb' (AssignHSFile())
char GraphFN[MAX_PATH], GraphDN[MAX_PATH], INIFile[MAX_PATH];
int Modified;
TICEREC SlideO, SlideT;
TICEMEM SlideMem; // MGY - mem up MAX_TICEMEM sliding objects
int wasIce; // CheckLoc will set this to true if currently on Ice/ThinIce
int WaitToTrans; //Found tunnel output on PF2 (under something)

// Global Varables

TXYREC BMA[MaxBitMaps + 1]; // Bit Map Array
TTANKREC laser;
HDC BuffDC, MaskDC; // used to bitblat all sprites
HBITMAP BuffBMH, MaskBMH; // Handle to Bitmaps in above DC's
const int GetOBMArray[MaxObjects + 1] = {
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
	55
};
const int CheckArray[MaxObjects] = {
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
	1
}; //Can tank move into square with this ID?
// Pad the beggining with junk array was [1..MaxBitMaps]
// Flag used in Bliting sprites to show if mask needs to be applied
const int BMSTA[MaxBitMaps + 1] = {
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
	0
};
const long ColorList[8] = {
	0x000000FF,
	0x0000FF00,
	0x00FF0000,
	0x00FFFF00,
	0x00FFFF,
	0x00FF00FF,
	0x00FFFFFF,
	0x00808080
};
int UndoP;
TRECORDREC PBRec, PBSRec;
char * RecBuffer;
PGAMEREC UndoBuffer;
THSREC HS;
HANDLE F1, F2, F3; //Files created at level load
DWORD BytesMoved;
TXYZREC MBuffer[MaxMBuffer];
int MB_TOS, MB_SP; // TOS = Top of Stack ; SP = Stack Pointer
int findmap[16][16];

int Backspace[10]; // Backspace Buffer. History of last 10 levels to cycle back to with the backspace key
int BS_SP = 0; // StackPointer for Backspace
int UndoRollOver;

// Local function declaration

void SetButtons(int);
void SpriteLoad(char * );
static void FindTarget(int, int, int);

//
// Start the code section
//

// ---------------------------------------------------
// Move   a Sliding Object FROM stack
// ---------------------------------------------------
void Mem_to_SlideO(int iSlideObj) // MGY
{
	if (iSlideObj <= SlideMem.count) {
		SlideO.x = SlideMem.Objects[iSlideObj].x;
		SlideO.y = SlideMem.Objects[iSlideObj].y;
		SlideO.dx = SlideMem.Objects[iSlideObj].dx;
		SlideO.dy = SlideMem.Objects[iSlideObj].dy;
		SlideO.s = SlideMem.Objects[iSlideObj].s;
	}
}

// ---------------------------------------------------
// Move a Sliding Object ON TO stack
// Update SlideMem with an object SlideO
// ---------------------------------------------------
void SlideO_to_Mem(int iSlideObj) // MGY
{
	if (iSlideObj <= SlideMem.count) {
		SlideMem.Objects[iSlideObj].x = SlideO.x;
		SlideMem.Objects[iSlideObj].y = SlideO.y;
		SlideMem.Objects[iSlideObj].dx = SlideO.dx;
		SlideMem.Objects[iSlideObj].dy = SlideO.dy;
		SlideMem.Objects[iSlideObj].s = SlideO.s;
	}
}

// ---------------------------------------------------
// Add an object in the stack for slidings objects
// But, if this object is already in this stack,
// just change dir and don't increase the counter.
// ---------------------------------------------------
void add_SlideO_to_Mem() // MGY
{
	int iSlideObj;

	if (SlideMem.count < MAX_TICEMEM - 1) {
		for (iSlideObj = 1; iSlideObj <= SlideMem.count; iSlideObj++) {
			if ((SlideMem.Objects[iSlideObj].x == SlideO.x) &&
				(SlideMem.Objects[iSlideObj].y == SlideO.y)) {
				SlideO_to_Mem(iSlideObj); // Update the stack
				return; // don't inc the counter
			}
		}
		// Add this object to the stack
		SlideMem.count++;
		SlideO_to_Mem(SlideMem.count);
		SlideO.s = (SlideMem.count > 0);
	}
}

// ---------------------------------------------------
// Delete a Sliding Object from stack
// ---------------------------------------------------
void sub_SlideO_from_Mem(int iSlideObj) // MGY
{
	int i;
	for (i = iSlideObj; i < SlideMem.count; i++) {
		Mem_to_SlideO(i + 1);
		SlideO_to_Mem(i);
	}
	SlideMem.count--;
	SlideO.s = (SlideMem.count > 0);
}

// ---------------------------------------------------
// If an object is sliding and is hit by a laser,
// delete it from stack. (Done before adding new slide direction to stack.)
// ---------------------------------------------------
void del_SlideO_from_Mem(int x, int y) // MGY
{
	int iSlideObj;
	for (iSlideObj = SlideMem.count; iSlideObj >= 1; iSlideObj--) {
		if ((SlideMem.Objects[iSlideObj].x == x) &&
			(SlideMem.Objects[iSlideObj].y == y)) {
			// remove this object
			sub_SlideO_from_Mem(iSlideObj);

			return;
		}
	}
	SlideO.s = (SlideMem.count > 0);
}

// ---------------------------------------------------
// Used to handle a bug :  the speed bug
// MGY - 22-nov-2002
// Return True if the tank is on Convoyor.
// ---------------------------------------------------
int TestIfConvCanMoveTank() {
	switch (Game.PF[Game.Tank.X][Game.Tank.Y]) {
	case 15:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1)) // Conveyor Up
			return (TRUE);
		break;
	case 16:
		if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y))
			return (TRUE);
		break;
	case 17:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1))
			return (TRUE);
		break;
	case 18:
		if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y))
			return (TRUE);
		break;
	}
	return (FALSE);
}

void SetButtons(int ButtonX) {
	EnableWindow(BT1, (ButtonX & 1) == 1);
	EnableWindow(BT2, (ButtonX & 2) == 2);
	EnableWindow(BT3, (ButtonX & 4) == 4);
	EnableWindow(BT4, (ButtonX & 8) == 8);
	EnableWindow(BT5, (ButtonX & 16) == 16);
	EnableWindow(BT6, (ButtonX & 32) == 32);
	EnableWindow(BT7, (ButtonX & 64) == 64);
	EnableWindow(BT8, (ButtonX & 128) == 128);
}

void FileError() {
	LPVOID lpMsgBuf;

	FormatMessage(
		FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
		NULL,
		GetLastError(),
		MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), // Default language
		(LPTSTR) & lpMsgBuf,
		0, NULL);
	// Display the string.
	MessageBox(MainH, lpMsgBuf, "System Error", MB_OK | MB_ICONINFORMATION);
	// Free the buffer.
	LocalFree(lpMsgBuf);
}

// 32	SPACEBAR
// 33	PAGE UP
// 34	PAGE DOWN
// 35	END
// 36	HOME
// 37	LEFT ARROW
// 38	UP ARROW
// 39	RIGHT ARROW
// 40	DOWN ARROW
void AddKBuff(char zz) {
	//Append key number to RecBuffer[] at RB_TOS (top of stack)
	//Increment RB_TOS

	int i;
	RecBuffer[RB_TOS] = zz;
	RB_TOS++;

	// Top of stack pointer is greater than rec buffer, realloc
	if (RB_TOS >= RecBufSize) {
		i = RecBufSize + RecBufStep;
		RecBuffer = GlobalReAlloc(RecBuffer, i, GMEM_MOVEABLE);
		if (RecBuffer == NULL) { // Recorder Buffer Overflow
			FileError();
			if (Recording) SendMessage(MainH, WM_SaveRec, 0, 0);
			RB_TOS = 0;
		} else RecBufSize = i;
	}
}

/* find the shortest path to the target via a fill search algorithm */
static void FindTarget(int px, int py, int pathlen) {
	if ((px < 0) || (px > 15) || (py < 0) || (py > 15)) return; // outer edges
	// if we hit something AND we are not at the tank then return
	if ((Game.PF[px][py] != 0) && (!((Game.Tank.X == px) && (Game.Tank.Y == py))))
		return; // we hit something - ouch

	if (findmap[px][py] <= pathlen) return;

	findmap[px][py] = pathlen++;

	if ((px == Game.Tank.X) && (py == Game.Tank.Y)) return; // speed's us up

	FindTarget(px - 1, py, pathlen);
	FindTarget(px + 1, py, pathlen);
	FindTarget(px, py - 1, pathlen);
	FindTarget(px, py + 1, pathlen);
}

int MouseOperation(int sp) {
	int dx, dy, XBigger, cx, cy, ltdir;

	dx = MBuffer[sp].X - Game.Tank.X;
	dy = MBuffer[sp].Y - Game.Tank.Y;
	XBigger = abs(dx) > abs(dy); // true if x is bigger than y

	if (MBuffer[sp].Z == 1) //Left mouse button clicked
	{
		// Mouse Move
		/* Fill the trace map */
		for (cx = 0; cx < 16; cx++)
			for (cy = 0; cy < 16; cy++)
				findmap[cx][cy] = BADMOVE;
		// We will test the destination manually
		dx = Game.PF[MBuffer[sp].X][MBuffer[sp].Y]; // temp store in dx
		if (!((dx < 3) || ((dx > 14) && (dx < 19)) ||
				(dx > 23) || ((Obj_Tunnel & dx) == Obj_Tunnel)))
			return (FALSE);
		findmap[MBuffer[sp].X][MBuffer[sp].Y] = 0; // destination
		/* flood fill search to find a shortest path to the push point. */
		FindTarget(MBuffer[sp].X - 1, MBuffer[sp].Y, 1);
		FindTarget(MBuffer[sp].X + 1, MBuffer[sp].Y, 1);
		FindTarget(MBuffer[sp].X, MBuffer[sp].Y - 1, 1);
		FindTarget(MBuffer[sp].X, MBuffer[sp].Y + 1, 1);

		/* if we didn't make it back to the players position, there is no valid path
		 * to that place.
		 */
		if (findmap[Game.Tank.X][Game.Tank.Y] == BADMOVE) {
			return (FALSE);
		} else {
			/* we made it back, so let's walk the path we just built up */
			cx = Game.Tank.X;
			cy = Game.Tank.Y;
			ltdir = Game.Tank.Dir; // we need to keep track of direction
			while (findmap[cx][cy]) {
				if ((cx > 0) && (findmap[cx - 1][cy] == (findmap[cx][cy] - 1))) {
					if (ltdir != 4) AddKBuff(VK_LEFT);
					AddKBuff(VK_LEFT);
					cx--;
					ltdir = 4;
				} else if ((cx < 15) && (findmap[cx + 1][cy] == (findmap[cx][cy] - 1))) {
					if (ltdir != 2) AddKBuff(VK_RIGHT);
					AddKBuff(VK_RIGHT);
					cx++;
					ltdir = 2;
				} else if ((cy > 0) && (findmap[cx][cy - 1] == (findmap[cx][cy] - 1))) {
					if (ltdir != 1) AddKBuff(VK_UP);
					AddKBuff(VK_UP);
					cy--;
					ltdir = 1;
				} else if ((cy < 15) && (findmap[cx][cy + 1] == (findmap[cx][cy] - 1))) {
					if (ltdir != 3) AddKBuff(VK_DOWN);
					AddKBuff(VK_DOWN);
					cy++;
					ltdir = 3;
				} else {
					/* if we get here, something is SERIOUSLY wrong, so we should abort */
					abort();
				}
			}
		}

	} else {
		// Mouse Shot / Right mouse button clicked
		if (XBigger) {
			if (dx > 0) {
				if (Game.Tank.Dir != 2) AddKBuff(VK_RIGHT); // Turn Right
			} else if (Game.Tank.Dir != 4) AddKBuff(VK_LEFT); // Turn Left
		} else {
			if (dy > 0) {
				if (Game.Tank.Dir != 3) AddKBuff(VK_DOWN); // Turn Down
			} else if (Game.Tank.Dir != 1) AddKBuff(VK_UP); // Turn Up
		}
		AddKBuff(VK_SPACE);
	}
	return (TRUE);
}

void InitBuffers() {
	int x;

	UndoP = 0;
	UndoBuffer = GlobalAlloc(GMEM_FIXED, UndoBufSize * sizeof(TGAMEREC)); // Undo Buffer
	RecBuffer = GlobalAlloc(GMEM_FIXED, RecBufSize); // Recording Buffer
	Backspace[BS_SP] = 0; // Clear Backspace stack
	MB_TOS = MB_SP = 0;
	SlideT.s = 0; // nothing sliding
	SlideO.s = 0;
	SlideMem.count = 0; // MGY

	UndoRollOver = UndoMax;
}

void ResetUndoBuffer()
// Reset Undo Buffer to 1 block only; all variable = 0
{
	UndoBuffer = GlobalReAlloc(UndoBuffer, UndoBufStep * sizeof(TGAMEREC), GMEM_MOVEABLE);
	if (UndoBuffer == NULL) { // Undo Buffer Allocation Error
		FileError();
	}
	UndoBufSize = UndoBufStep;
	UndoP = 0;
	UndoBuffer -> Tank.Dir = 0;
	// Lets also init the Mouse Buffer
	MB_TOS = MB_SP = 0;
}

void KillBuffers() {
	GlobalFree(UndoBuffer);
	GlobalFree(RecBuffer);
}

void UpdateUndo() // Come here whenever we move or shoot
{
	int i;
	PGAMEREC tmpUndoArray;

	UndoP++;
	if (UndoP >= UndoBufSize) {
		if (UndoP >= UndoMax) {
			UndoRollOver = (UndoP - 1); // Save Where we rolled Over
			UndoP = 0;
		} else {
			i = UndoBufSize + UndoBufStep;
			tmpUndoArray = GlobalReAlloc(UndoBuffer, i * sizeof(TGAMEREC), GMEM_MOVEABLE);
			if (tmpUndoArray == NULL) { // Undo Buffer Allocation Error
				MessageBox(MainH, txt019, txt007, MB_OK | MB_ICONERROR);
				UndoRollOver = (UndoP - 1); // Save Where we rolled Over
				UndoP = 0;
			} else {
				UndoBufSize = i;
				UndoBuffer = tmpUndoArray;
			}
		}
	}
	UndoBuffer[UndoP] = Game;
	EnableMenuItem(MMenu, 110, MF_BYCOMMAND | MF_ENABLED); // enable Undo Command
	EnableWindow(BT1, SW_SHOWNA);
}

void UndoStep() {
	if (UndoBuffer[UndoP].Tank.Dir == 0) return; // out of data
	Game = UndoBuffer[UndoP];
	RB_TOS = Game.RecP; // clear all keys not processed
	SlideT.s = 0; // stop any sliding
	SlideO.s = 0;
	SlideMem.count = 0; // MGY
	UndoBuffer[UndoP].Tank.Dir = 0;
	UndoP--;
	if (UndoP < 0) {
		UndoP = UndoRollOver;
	}
	MB_TOS = MB_SP = 0; // we need to cancle all mouse inputs
}

void PutSprite(char bmn, int x, int y)
// paint sprite ( bitmap ) at screen location x,y
// add grass behind if transparent
{
	if (BMSTA[bmn] == 1) {
		BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, BuffDC, BMA[1].X, BMA[1].Y, SRCCOPY);
		SetTextColor(gDC, RGB(0, 0, 0));
		SetBkColor(gDC, RGB(255, 255, 255));
		BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, MaskDC, BMA[bmn].X, BMA[bmn].Y, SRCAND);
		BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCPAINT);
	} else BitBlt(gDC, x, y, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCCOPY);
}

void UpDateSprite(int x, int y)
// re-paint sprite at Game Board Location x,y
{
	int bmn, bmn2, x1, y1;
	HBRUSH Bpen, penO;

	bmn = Game.BMF[x][y];
	x1 = XOffset + (x * SpBm_Width);
	y1 = YOffset + (y * SpBm_Height);

	// Draw top layer
	if (bmn == 55) // 55 is tunnel
	{
		Bpen = CreateSolidBrush(ColorList[GetTunnelID(x, y)]);
		penO = SelectObject(gDC, Bpen);
		Rectangle(gDC, x1, y1, x1 + SpBm_Width, y1 + SpBm_Height); // Fill cell with coloured rectangle of TunnelID colour
		SetTextColor(gDC, RGB(0, 0, 0));
		SetBkColor(gDC, RGB(255, 255, 255));
		BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, MaskDC, BMA[55].X, BMA[55].Y, SRCAND); // Draw tunnel with transparency
		BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[55].X, BMA[55].Y, SRCPAINT);
		SelectObject(gDC, penO);
		DeleteObject(Bpen);
	} else {
		if (BMSTA[bmn] == 1) // Sprite has a transparency mask
		{
			// Draw bottom layer
			bmn2 = Game.BMF2[x][y];

			if (bmn2 == 55) // 55 is tunnel - If bottom layer is a tunnel
			{
				Bpen = CreateSolidBrush(ColorList[((Game.PF2[x][y] & 0x0F) >> 1)]);
				penO = SelectObject(gDC, Bpen);
				Rectangle(gDC, x1, y1, x1 + SpBm_Width, y1 + SpBm_Height);
				SetTextColor(gDC, RGB(0, 0, 0));
				SetBkColor(gDC, RGB(255, 255, 255));
				BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, MaskDC, BMA[55].X, BMA[55].Y, SRCAND);
				BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[55].X, BMA[55].Y, SRCPAINT);
				SelectObject(gDC, penO);
				DeleteObject(Bpen);
			} else
				BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn2].X, BMA[bmn2].Y, SRCCOPY);

			SetTextColor(gDC, RGB(0, 0, 0));
			SetBkColor(gDC, RGB(255, 255, 255));
			BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, MaskDC, BMA[bmn].X, BMA[bmn].Y, SRCAND); // Draw mask
			BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCPAINT); // Draw sprite
		} else BitBlt(gDC, x1, y1, SpBm_Width, SpBm_Height, BuffDC, BMA[bmn].X, BMA[bmn].Y, SRCCOPY); // Draw sprite
	}
}

void UpDateTank()
// paint mask then tank sprite, we mask the cell so the back ground will show
{
	TankDirty = FALSE;
	SetTextColor(gDC, RGB(0, 0, 0));
	SetBkColor(gDC, RGB(255, 255, 255));
	BitBlt(gDC, XOffset + (Game.Tank.X * SpBm_Width), YOffset + (Game.Tank.Y * SpBm_Height),
		SpBm_Width, SpBm_Height, MaskDC, BMA[1 + Game.Tank.Dir].X, 0, SRCAND);
	BitBlt(gDC, XOffset + (Game.Tank.X * SpBm_Width), YOffset + (Game.Tank.Y * SpBm_Height),
		SpBm_Width, SpBm_Height, BuffDC, BMA[1 + Game.Tank.Dir].X, 0, SRCPAINT);
}

// Draw laser (not deflecting)
void UpDateLaser()
// paint laser
{
	HBRUSH ob;
	int x, y;

	ob = SelectObject(gDC, LaserColor);
	x = XOffset + (laser.X * SpBm_Width);
	y = YOffset + (laser.Y * SpBm_Height);
	if ((laser.Dir & 1) == 1) Rectangle(gDC, x + LaserOffset, y, x + SpBm_Width - LaserOffset, y + SpBm_Height);
	else Rectangle(gDC, x, y + LaserOffset, x + SpBm_Width, y + SpBm_Height - LaserOffset);
	SelectObject(gDC, ob);
}

// Did laser just hit a moving mirror? Let the laser move again.
int LaserBounceOnIce;

// Draw laser bouncing off a mirror from direction a to direction b. Also set LaserBounceOnIce if object moving
void UpDateLaserBounce(int a, int b)
{
	HBRUSH ob;
	int x, y, h;
	int iSlideObj; // MGY

	ob = SelectObject(gDC, LaserColor);
	x = XOffset + (laser.X * SpBm_Width);
	y = YOffset + (laser.Y * SpBm_Height);
	h = SpBm_Width / 2;

	// we need to stop advance the LaserShot if sliding on ice & hit
	for (iSlideObj = 1; iSlideObj <= SlideMem.count; iSlideObj++) // MGY
		// MGY
		if (SlideMem.Objects[iSlideObj].s &&
			(SlideMem.Objects[iSlideObj].x == laser.X) &&
			(SlideMem.Objects[iSlideObj].y == laser.Y)) LaserBounceOnIce = TRUE;
	//if (SlideO.s && (SlideO.x == laser.X) && (SlideO.y == laser.Y)) LaserBounceOnIce = TRUE;

	// Draw two parts of the reflecting laser
	switch (a) {
	case 1:
		Rectangle(gDC, x + LaserOffset, y + h, x + SpBm_Width - LaserOffset, y + SpBm_Height);
		break;
	case 2:
		Rectangle(gDC, x, y + LaserOffset, x + h, y + SpBm_Height - LaserOffset);
		break;
	case 3:
		Rectangle(gDC, x + LaserOffset, y, x + SpBm_Width - LaserOffset, y + h);
		break;
	case 4:
		Rectangle(gDC, x + h, y + LaserOffset, x + SpBm_Width, y + SpBm_Height - LaserOffset);
	}
	switch (b) {
	case 1:
		Rectangle(gDC, x + LaserOffset, y, x + SpBm_Width - LaserOffset, y + h);
		break;
	case 2:
		Rectangle(gDC, x + h, y + LaserOffset, x + SpBm_Width, y + SpBm_Height - LaserOffset);
		break;
	case 3:
		Rectangle(gDC, x + LaserOffset, y + h, x + SpBm_Width - LaserOffset, y + SpBm_Height);
		break;
	case 4:
		Rectangle(gDC, x, y + LaserOffset, x + h, y + SpBm_Height - LaserOffset);
	}
	SelectObject(gDC, ob);
}

void PutLevel()
// paint all game cells and the tank
{
	HBRUSH ob;
	int x, y;

	for (y = 0; y < 16; y++)
		for (x = 0; x < 16; x++) UpDateSprite(x, y);
	UpDateTank();
	TankDirty = FALSE;

	if (FindTank) // Newly loaded level so draw target lines to tank
	{
		// Draws red horizontal and vertical lines from tank when level fir
		ob = SelectObject(gDC, LaserColorR);
		SelectObject(gDC, GetStockObject(NULL_PEN));
		x = XOffset + (Game.Tank.X * SpBm_Width);
		y = YOffset + (Game.Tank.Y * SpBm_Height);
		Rectangle(gDC, x + LaserOffset, YOffset + 2, x + SpBm_Width - LaserOffset, YOffset + (16 * SpBm_Height));
		Rectangle(gDC, XOffset + 2, y + LaserOffset, XOffset + (16 * SpBm_Width), y + SpBm_Height - LaserOffset);
		SelectObject(gDC, ob);
	}
}

HBITMAP LoadBitmapFile(HDC dc, char * FileName)
// Load a WIndows style Bitmap file
{
	HANDLE F;
	LONG Size, n;
	LPBITMAPINFO P;
	BITMAPFILEHEADER Header;
	HBITMAP bm;
	LPVOID P2;

	bm = 0; // set error
	F = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
		FILE_FLAG_SEQUENTIAL_SCAN, NULL);
	if (F == INVALID_HANDLE_VALUE) return (0); // File not found
	ReadFile(F, & Header, sizeof(Header), & BytesMoved, NULL);
	if ((BytesMoved != sizeof(Header)) || (Header.bfType != 0x4d42))
		goto ErrExit1;
	Size = SetFilePointer(F, 0, NULL, FILE_END) - sizeof(Header); // Size = filesize(F) - Sizeof(header)
	SetFilePointer(F, sizeof(Header), NULL, FILE_BEGIN); // Reset File Position
	P = GlobalAlloc(GMEM_FIXED, Size); // Get Big lump of Memory
	if (P == 0) goto ErrExit1; // Memory Error

	// This only works with 32bit LCC if size > 65K
	if (!(ReadFile(F, P, Size, & BytesMoved, NULL))) FileError();

	if (P -> bmiHeader.biSize == sizeof(BITMAPINFOHEADER)) {
		n = Header.bfOffBits - sizeof(BITMAPFILEHEADER); //Compute image Location
		P2 = (char * ) P + n;
		bm = CreateDIBitmap(dc, (LPBITMAPINFOHEADER) P, CBM_INIT, P2, P, DIB_RGB_COLORS);
	}
	GlobalFree(P);
	ErrExit1:
		CloseHandle(F);
	return (bm);
}

HBITMAP LoadBitmapMem(HDC dc, LPBITMAPFILEHEADER Header)
// Load a WIndows style Bitmap from a memory block
{
	LPBITMAPINFO P;
	HBITMAP bm;
	LPVOID P2;

	if (Header -> bfType != 0x4d42) return (0);

	P = (char * ) Header + sizeof(BITMAPFILEHEADER);

	if (P -> bmiHeader.biSize == sizeof(BITMAPINFOHEADER)) {
		P2 = (char * ) Header + Header -> bfOffBits;
		bm = CreateDIBitmap(dc, (LPBITMAPINFOHEADER) P, CBM_INIT, P2, P, DIB_RGB_COLORS);
		return (bm);
	}
	return (0);
}

int LoadLTG(HDC dc, HBITMAP * GH, HBITMAP * MH, char * FN) {
	HANDLE F;
	TLTGREC tmpLTG;
	DWORD GSize, MSize, LTSize;
	void * P;
	char temps[250];

	if ((F = CreateFile(FN, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
			FILE_FLAG_SEQUENTIAL_SCAN, NULL)) == INVALID_HANDLE_VALUE) return (0);
	LTSize = SetFilePointer(F, 0, NULL, FILE_END);
	SetFilePointer(F, 0, NULL, FILE_BEGIN);

	if (!(ReadFile(F, & tmpLTG, sizeof(TLTGREC), & BytesMoved, NULL))) FileError();
	if (strcmp(tmpLTG.ID, LTG_ID) != 0) {
		MessageBox(MainH, txt031, txt007, MB_OK | MB_ICONERROR);
		return (FALSE);
	}
	GSize = tmpLTG.MaskOffset - sizeof(TLTGREC);
	MSize = LTSize - tmpLTG.MaskOffset;

	// transfer game bitmap from Filename -> GH
	P = GlobalAlloc(GMEM_FIXED, GSize); // Get Big lump of Memory
	if (P != 0) {
		if (!(ReadFile(F, P, GSize, & BytesMoved, NULL))) FileError();
		* GH = LoadBitmapMem(dc, P);
	}
	GlobalFree(P);

	// transfer Mask bitmap from Filename -> MH
	P = GlobalAlloc(GMEM_FIXED, MSize); // Get Big lump of Memory
	if (P != 0) {
		if (!(ReadFile(F, P, MSize, & BytesMoved, NULL))) FileError();
		* MH = LoadBitmapMem(dc, P);
	}
	GlobalFree(P);
	CloseHandle(F);
	return (TRUE);
}

// Load All the Bitmaps
void GFXInit() {
	HDC dc, tdc;
	HBITMAP Gh, Mh, xh2;
	int x, y, i;

	SetCurrentDirectory(GraphDN);
	dc = GetDC(MainH); // Get device context for drawing on

	BuffDC = CreateCompatibleDC(dc); // DC for All Sprites
	MaskDC = CreateCompatibleDC(dc); // DC for all Masks -- same size as Sprites

	tdc = CreateCompatibleDC(dc); // Temp DC
	// GraphM = Graphics Mode 0=int; 1=ext; 2=ltg
	if (GraphM == 1) // External
	{
		Gh = 0; // need this if error
		Mh = LoadBitmapFile(dc, MASK_BMP);
		if (Mh) Gh = LoadBitmapFile(dc, GAME_BMP);
		if (!(Mh || Gh)) GraphM = 0; // Error so Set Mode 0 - Internal
	} else if (GraphM == 2) // LTG
	{
		if (!(LoadLTG(dc, & Gh, & Mh, GraphFN))) GraphM = 0;
	}
	if (GraphM == 0) // Internal Graphics are used
	{
		Mh = LoadBitmap(hInst, "MASKBM");
		if (Mh) Gh = LoadBitmap(hInst, "GAMEBM");
	}
	if (!(Mh || Gh)) // last chance error check
	{
		GFXError = 1;
		if (GFXError != 0) MessageBox(0, "Graphics Loading Error", txt007, MB_OK | MB_ICONERROR);
		return;
	}
	// Create Mask Bitmap; Sized Properly for Screen
	SelectObject(MaskDC, Mh); // This sets up the B&W
	MaskBMH = CreateCompatibleBitmap(MaskDC, SpBm_Width * 10, SpBm_Height * 6);
	SelectObject(MaskDC, MaskBMH); // Put New Blank Bitmap in MaskDC
	xh2 = SelectObject(tdc, Mh); // Hold Old Value
	// Copy Bitmap to new size into MaskDC
	StretchBlt(MaskDC, 0, 0, SpBm_Width * 10, SpBm_Height * 6, tdc, 0, 0, 320, 192, SRCCOPY);
	SelectObject(tdc, xh2); // Restore Old Value
	DeleteObject(Mh); // Get Rid of original Bitmap

	// Create Game Bitmap; Sized Properly for Screen
	SelectObject(BuffDC, Gh); // This sets up the color
	BuffBMH = CreateCompatibleBitmap(BuffDC, SpBm_Width * 10, SpBm_Height * 6);
	SelectObject(BuffDC, BuffBMH); // Put New Blank Bitmap in GameDC
	xh2 = SelectObject(tdc, Gh); // Hold Old Value
	// Copy Bitmap to new size into GameDC
	StretchBlt(BuffDC, 0, 0, SpBm_Width * 10, SpBm_Height * 6, tdc, 0, 0, 320, 192, SRCCOPY);
	SelectObject(tdc, xh2); // Restore Old Value
	DeleteObject(Gh); // Get Rid of original Bitmap
	x = 0;
	y = 0;
	for (i = 1; i <= MaxBitMaps; i++) {
		BMA[i].X = x;
		BMA[i].Y = y;
		x += SpBm_Width;
		if (x >= (SpBm_Width * 10)) {
			x = 0;
			y += SpBm_Height;
		}
	}
	DeleteDC(tdc);
	ReleaseDC(MainH, dc);
	GFXOn = TRUE;
}

void GFXKill() {
	DeleteObject(MaskBMH);
	DeleteObject(BuffBMH);
	DeleteDC(MaskDC);
	DeleteDC(BuffDC);
	GFXOn = FALSE;
}

// Change Game Object
void ChangeGO(int x, int y, int CurSelBM) // Change Game Object
{
	int i;
	gDC = GetDC(MainH);
	if (CurSelBM == 1) // Tank
	{
		UpDateSprite(Game.Tank.X, Game.Tank.Y); // repaint under old tank
		Game.BMF[x][y] = 1;
		Game.PF[x][y] = 0;
		Game.Tank.X = x;
		Game.Tank.Y = y;
		UpDateSprite(Game.Tank.X, Game.Tank.Y); // paint under new tank
		UpDateTank();
	} else {
		if (CurSelBM == MaxObjects) {
			// Tunnel
			i = DialogBox(hInst, "LoadTID", MainH, (DLGPROC) LoadTID) << 1;
			Game.PF[x][y] = i + 0x40;
			Game.BMF[x][y] = 55; // 55 is tunnel
			UpDateSprite(x, y);
			ShowTunnelID();
		} else {
			Game.PF[x][y] = CurSelBM;
			Game.BMF[x][y] = GetOBM(CurSelBM);
			UpDateSprite(x, y);
		}

	}
	ReleaseDC(MainH, gDC);
}

// Convert Objects to bitmaps
void BuildBMField() {
	int x, y, i, j;
	unsigned char pt; // mgy 18-05-2003

	Game.Tank.X = 7;
	Game.Tank.Y = 15;
	Game.Tank.Dir = 1;
	Game.Tank.Firing = FALSE;
	for (x = 0; x < 16; x++)
		for (y = 0; y < 16; y++) {
			// --- mgy 18-05-2003 only legal pieces ---
			pt = Game.PF[x][y];
			if (pt > 0x19) {
				pt = GetTunnelID(x, y);
				Game.PF[x][y] = (pt << 1) + 0x40;
			}
			// --- end of 18-05-2003 ---

			if (Game.PF[x][y] == 1) {
				i = 1;
				Game.Tank.X = x;
				Game.Tank.Y = y;
				Game.PF[x][y] = 0;
			} else {
				if (Game.PF[x][y] < 64) i = GetOBM(Game.PF[x][y]);
				else if (ISTunnel(x, y)) i = 55; // 55 is tunnel
			}
			Game.BMF[x][y] = i;
			Game.BMF2[x][y] = 1;
			Game.PF2[x][y] = 0;
		}
	// this is a good place to reset the score counters }
	Game.ScoreMove = 0;
	Game.ScoreShot = 0;
}

//Start/stop game timer and set Game_On
void GameOn(int b) {
	if (b) SetTimer(MainH, 1, GameDelay, NULL);
	else KillTimer(MainH, 1);
	Game_On = b;
	#ifdef DEBUG
	if (b) DEBUG_Time = timeGetTime();
	DEBUG_Frames = 0;
	#endif
}

void JK3dFrame(HDC dc, int x, int y, int x2, int y2, int up) {
	HPEN Wpen, Bpen, penO;

	Wpen = CreatePen(PS_SOLID, 1, 0x00FFFFFF);
	Bpen = CreatePen(PS_SOLID, 1, 0x00808080);
	if (up) penO = SelectObject(dc, Wpen);
	else penO = SelectObject(dc, Bpen);
	MoveToEx(dc, x, y2, NULL);
	LineTo(dc, x, y);
	LineTo(dc, x2, y);
	if (up) SelectObject(dc, Bpen);
	else SelectObject(dc, Wpen);
	LineTo(dc, x2, y2);
	LineTo(dc, x, y2);
	SelectObject(dc, penO);
	DeleteObject(Bpen);
	DeleteObject(Wpen);
}

void JKSelFrame(HDC dc, int x, int y, int x2, int y2, int pnum) {
	HPEN Wpen, penO;
	long Color;

	if (pnum == 1) Color = 0x000000FF;
	else Color = 0x0000FF00;
	Wpen = CreatePen(PS_SOLID, 2, Color);
	penO = SelectObject(dc, Wpen);
	MoveToEx(dc, x + 1, y2, NULL);
	LineTo(dc, x + 1, y + 1);
	LineTo(dc, x2, y + 1);
	LineTo(dc, x2, y2);
	LineTo(dc, x + 1, y2);
	SelectObject(dc, penO);
	DeleteObject(Wpen);
}

// Translate Bitmap to Object
char GetOBM(char ob) {
	if ((ob > -1) && (ob <= MaxObjects)) return (GetOBMArray[ob]);
	else return (1);
}

void LoadLastLevel() {
	char temps[11];
	THSREC TempHSData;

	if (CurLevel < 2) return;
	GameOn(FALSE);
	F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, NULL);
	if (F1 == INVALID_HANDLE_VALUE) {
		MessageBox(MainH, txt001, txt007, MB_OK | MB_ICONERROR);
		PostMessage(MainH, WM_COMMAND, 108, 0);
		return;
	}
	F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, NULL);
	CurLevel--;
	do {
		CurLevel--;
		SetFilePointer(F1, CurLevel * sizeof(TLEVEL), NULL, FILE_BEGIN);
		ReadFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, NULL);
		if (BytesMoved < sizeof(TLEVEL)) {
			CloseHandle(F1);
			if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2);
			SendMessage(MainH, WM_GameOver, 0, 0);
			return;
		}
		if (SkipCL && (F2 != INVALID_HANDLE_VALUE)) {
			SetFilePointer(F2, CurLevel * sizeof(THSREC), NULL, FILE_BEGIN);
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
			if (BytesMoved < sizeof(THSREC)) TempHSData.moves = 0;
			if (TempHSData.moves > 0) CurRecData.SDiff = 128; // Error SDiff
		}
	} while ((CurLevel > 0) && (CurRecData.SDiff > 0) && ((Difficulty & CurRecData.SDiff) == 0));
	CloseHandle(F1);
	if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2);
	// Load For Real
	LoadNextLevel(TRUE, FALSE);
}

BOOL LoadNextLevel(int DirectLoad, int Scanning)
// Directload is true if we shouldn't use difficulties & Completed Level check
// Scanning is true if we are searching and dont want any errors displayed
{
	char temps[11];
	THSREC TempHSData;
	int SavedLevelNum;

	if (GameInProg) {
		SavedLevelNum = MessageBox(MainH, txt039, txt038, MB_YESNOCANCEL | MB_ICONQUESTION); //Game in progress, Do you want to save the game?
		if (SavedLevelNum == IDCANCEL) return (FALSE);
		if (SavedLevelNum == IDYES) SendMessage(MainH, WM_SaveRec, 0, 0);
	}
	GameOn(FALSE);
	SavedLevelNum = CurLevel;
	if (Difficulty == 0) SendMessage(MainH, WM_COMMAND, 225, 0); // Set Difficulty Window - Send change difficulty menu command
	if (Recording) SendMessage(MainH, WM_COMMAND, 123, 0); // Turn Off Recording if on
	// Open file "LaserTank.lvl" from: FileName<-LevelData<-"LaserTank.lvl"
	F1 = CreateFile(FileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, NULL);
	if (F1 == INVALID_HANDLE_VALUE) {
		MessageBox(MainH, txt001, txt007, MB_OK | MB_ICONERROR); //The Level file can not be found\nPlease select a new one
		PostMessage(MainH, WM_COMMAND, 108, 0);
		return FALSE;
	}

	// Open "LaserTank.hs" for local high scores
	F2 = CreateFile(HFileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_FLAG_RANDOM_ACCESS, NULL);
	do {
		SetFilePointer(F1, CurLevel * sizeof(TLEVEL), NULL, FILE_BEGIN);
		ReadFile(F1, & CurRecData, sizeof(TLEVEL), & BytesMoved, NULL);
		if (BytesMoved < sizeof(TLEVEL)) {
			CloseHandle(F1);
			if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2);
			CurLevel = SavedLevelNum; // If eof use last Level Number
			if (!Scanning) SendMessage(MainH, WM_GameOver, 0, 0);
			return FALSE;
		}
		if (SkipCL && (F2 != INVALID_HANDLE_VALUE) && (!DirectLoad)) {
			SetFilePointer(F2, CurLevel * sizeof(THSREC), NULL, FILE_BEGIN);
			ReadFile(F2, & TempHSData, sizeof(THSREC), & BytesMoved, NULL);
			if (BytesMoved < sizeof(THSREC)) TempHSData.moves = 0;
			if (TempHSData.moves > 0) CurRecData.SDiff = 128; // Error SDiff
		}
		CurLevel++;
		//? Trying to find a level that hasn't been completed?
	} while ((!DirectLoad) && (CurRecData.SDiff > 0) && ((Difficulty & CurRecData.SDiff) == 0));
	CloseHandle(F1);
	if (F2 != INVALID_HANDLE_VALUE) CloseHandle(F2);
	//Game.PF = CurRecData.PF;
	memcpy(Game.PF, CurRecData.PF, sizeof(TPLAYFIELD));
	BuildBMField();
	GameOn(TRUE);
	OKtoHS = TRUE;
	OKtoSave = TRUE;
	EnableMenuItem(MMenu, 110, MF_BYCOMMAND | MF_GRAYED); // disable Undo
	EnableMenuItem(MMenu, 112, MF_BYCOMMAND | MF_GRAYED); // disable Restore
	SetButtons(0xFA);
	FindTank = TRUE;
	SetTimer(MainH, 1, 700, NULL);
	InvalidateRect(MainH, NULL, TRUE);
	ResetUndoBuffer();
	if (RLL) {
		WritePrivateProfileString("DATA", psRLLN, FileName, INIFile);
		WritePrivateProfileString("DATA", psRLLL, itoa(CurLevel, temps, 10), INIFile);
	}
	Game.RecP = 0;
	RB_TOS = 0;
	SlideT.s = 0; // Just in case
	SlideO.s = 0;
	SlideMem.count = 0; // MGY
	if (ARecord && (!PBOpen)) SendMessage(MainH, WM_COMMAND, 123, 0);
	if (Backspace[BS_SP] != CurLevel) // if CurLevel != LastLevel
	{
		if (Backspace[BS_SP]) EnableMenuItem(MMenu, 118, MF_BYCOMMAND); // Enable Menu Item
		BS_SP++;
		if (BS_SP > 9) BS_SP = 0;
		Backspace[BS_SP] = CurLevel; // Add CurLevel to stack
	}
	return (TRUE);
}

void AssignHSFile() {
	char * P;

	strcpy(GHFileName, FileName);
	strcpy(strrchr(GHFileName, '.'), ".ghs");
	strcpy(HFileName, FileName);
	strcpy(strrchr(HFileName, '.'), ".hs");

	// Set up Record Default file name
	strcpy(PBFileName, FileName);
	P = strrchr(PBFileName, '.'); // Set Up to truncate file name
	if (P) P[0] = 0; // Set end of string
	strcat(PBFileName, "_0000.lpb"); // add to name
}

void CheckHighScore() {
	int x, i;

	if (!OKtoHS) return;
	F2 = CreateFile(HFileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, NULL,
		OPEN_ALWAYS, FILE_FLAG_RANDOM_ACCESS, NULL);

	if (F2 == INVALID_HANDLE_VALUE) FileError();
	// Check if All lower scores are filled in, if not then set levels
	if ((CurLevel * sizeof(THSREC)) > (i = SetFilePointer(F2, 0, NULL, FILE_END))) {
		HS.moves = 0; // Sets field to blank
		for (x = (i / sizeof(THSREC)); x < CurLevel - 1; x++)
			WriteFile(F2, & HS, sizeof(THSREC), & BytesMoved, NULL);
	}
	SetFilePointer(F2, (CurLevel - 1) * sizeof(THSREC), NULL, FILE_BEGIN);
	ReadFile(F2, & HS, sizeof(THSREC), & BytesMoved, NULL);
	if ((HS.moves == 0) || (Game.ScoreMove < HS.moves) || ((Game.ScoreMove == HS.moves) && (Game.ScoreShot < HS.shots))) {
		SendMessage(MainH, WM_NewHS, 0, 0);
		SetFilePointer(F2, (CurLevel - 1) * sizeof(THSREC), NULL, FILE_BEGIN);
		WriteFile(F2, & HS, sizeof(THSREC), & BytesMoved, NULL);
	}
	CloseHandle(F2);
}

void Animate() {
	int x, y;

	AniLevel++;
	AniCount = 0;
	if (AniLevel == 3) AniLevel = 0;
	for (x = 0; x < 16; x++)
		for (y = 0; y < 16; y++) {
			// Animate Conveyor Belts & Flag if under something
			switch (Game.PF2[x][y]) {
			case 2:
				Game.BMF2[x][y] = 6 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 15:
				Game.BMF2[x][y] = 24 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 16:
				Game.BMF2[x][y] = 27 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 17:
				Game.BMF2[x][y] = 30 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 18:
				Game.BMF2[x][y] = 33 + AniLevel;
				UpDateSprite(x, y);
				break;
			}
			// Now animate all top sprites
			switch (Game.PF[x][y]) {
			case 2:
				Game.BMF[x][y] = 6 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 3:
				Game.BMF[x][y] = 9 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 7:
				Game.BMF[x][y] = 16 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 8:
				Game.BMF[x][y] = 36 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 9:
				Game.BMF[x][y] = 39 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 10:
				Game.BMF[x][y] = 42 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 15:
				Game.BMF[x][y] = 24 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 16:
				Game.BMF[x][y] = 27 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 17:
				Game.BMF[x][y] = 30 + AniLevel;
				UpDateSprite(x, y);
				break;
			case 18:
				Game.BMF[x][y] = 33 + AniLevel;
				UpDateSprite(x, y);
				break;
			}
		}
	TankDirty = TRUE;
}

//Find the exit to a tunnel with matching ID (scans y:0-15, x:0-15) and set *x, *y to the destination
//sets WaitToTrans to TRUE of exit found in PF2 (under something) and does not change x,y
//sets BlackHole TRUE if no exit found
void TranslateTunnel(int * x, int * y) {
	int cx, cy, i;
	char bb;

	bb = Game.PF[ * x][ * y]; // bb is ID #
	WaitToTrans = FALSE;
	BlackHole = FALSE;
	for (cy = 0; cy < 16; cy++)
		for (cx = 0; cx < 16; cx++)
			if ((Game.PF[cx][cy] == bb) && (!(( * x == cx) && ( * y == cy)))) {
				* x = cx; // We found an exit YEA !!!
				* y = cy;
				return;
			}
	// check for blocked hole - something is over the exit
	// Scan the 2nd layer any matches are blocked holes
	for (cy = 0; cy < 16; cy++)
		for (cx = 0; cx < 16; cx++)
			if ((Game.PF2[cx][cy] == bb) && (!(( * x == cx) && ( * y == cy)))) {
				// We found one so we will set the flag
				WaitToTrans = TRUE;
				return; // Blocked so no warp
			}
	// There is no match, so it is a black hole
	BlackHole = TRUE;
}

void ConvMoveTank(int x, int y, int check) {
	UpDateSprite(Game.Tank.X, Game.Tank.Y);
	Game.Tank.Y += y;
	Game.Tank.X += x;
	if (ISTunnel(Game.Tank.X, Game.Tank.Y)) {
		TranslateTunnel( & Game.Tank.X, & Game.Tank.Y); // We moved into a tunnel
		if (BlackHole) PostMessage(MainH, WM_Dead, 0, 0); // The tunnel was a black hole
	}
	if (WaitToTrans) Game.Tank.Good = TRUE;
	TankDirty = TRUE;
	ConvMoving = TRUE;
	if (wasIce && check) {
		SlideT.x = Game.Tank.X;
		SlideT.y = Game.Tank.Y;
		SlideT.s = TRUE;
		SlideT.dx = x;
		SlideT.dy = y;
	}
	AntiTank();
}

void UpDateTankPos(int x, int y) {
	char temps[50];

	SoundPlay(S_Move);
	UpdateUndo();

	// Update move counter
	Game.ScoreMove++;
	SetTextAlign(gDC, TA_CENTER);
	SetTextColor(gDC, 0x0000FF00);
	SetBkColor(gDC, 0);
	TextOut(gDC, ContXPos + 48, 207, itoa(Game.ScoreMove, temps, 10), strlen(temps));

	UpDateSprite(Game.Tank.X, Game.Tank.Y);
	Game.Tank.Y += y;
	Game.Tank.X += x;
	Game.Tank.Good = FALSE; // we need it somewhere if we move off a tunnel
	if (ISTunnel(Game.Tank.X, Game.Tank.Y)) {
		TranslateTunnel( & Game.Tank.X, & Game.Tank.Y); // We moved into a tunnel
		if (BlackHole)
			PostMessage(MainH, WM_Dead, 0, 0); // The tunnel was a black hole
	}
	if (WaitToTrans)
		Game.Tank.Good = TRUE;
	TankDirty = TRUE;
}

// Set tank direction or move tank in direction if already facing. Then set up SlideT if on ice
void MoveTank(int d) {
	if (Game.Tank.Dir != d) // The Tank is Turning
	{
		Game.Tank.Dir = d;
		UpDateSprite(Game.Tank.X, Game.Tank.Y);
		TankDirty = TRUE;
		SoundPlay(S_Turn);
		return;
	}
	switch (d) {
	case 1:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y - 1))
			UpDateTankPos(0, -1);
		else
			SoundPlay(S_Head); // Ouch we are hitting something hard
		SlideT.dy = -1;
		SlideT.dx = 0;
		break;
	case 2:
		if (CheckLoc(Game.Tank.X + 1, Game.Tank.Y))
			UpDateTankPos(1, 0);
		else
			SoundPlay(S_Head);
		SlideT.dy = 0;
		SlideT.dx = 1;
		break;
	case 3:
		if (CheckLoc(Game.Tank.X, Game.Tank.Y + 1))
			UpDateTankPos(0, 1);
		else
			SoundPlay(S_Head);
		SlideT.dy = 1;
		SlideT.dx = 0;
		break;
	case 4:
		if (CheckLoc(Game.Tank.X - 1, Game.Tank.Y))
			UpDateTankPos(-1, 0);
		else
			SoundPlay(S_Head);
		SlideT.dy = 0;
		SlideT.dx = -1;
		break;
	}
	if (wasIce) {
		SlideT.x = Game.Tank.X;
		SlideT.y = Game.Tank.Y;
		SlideT.s = TRUE;
	}
}

int CheckLoc(int x, int y) {
	// Check if Tank can move
	if ((x < 0) || (x > 15) || (y < 0) || (y > 15))
		return (0);

	wasIce = ((Game.PF[x][y] == Obj_Ice) || (Game.PF[x][y] == Obj_ThinIce));

	if ((Game.PF[x][y] & Obj_Tunnel) == Obj_Tunnel)
		return (TRUE); //Can move into a tunnel square

	return (CheckArray[Game.PF[x][y]]); // Check flags to see if tank can move into this type of square
}

void MoveObj(int x, int y, int dx, int dy, int sf)
// Try to move object on square x,y that was pushed in dir dx,dy then play sound sf
// Update terrain under object's initial position (x,y)
//		Also unblock tunnel if Obj blocking tunnel and let other end activate (cx,cy)
//
// used by CheckLLoc and IceMoveO
{
	int obt, bm, i, bb, cx, cy, ok;

	obt = Game.PF[x][y]; // Get Object type
	bm = Game.BMF[x][y];
	if ((Game.PF2[x][y] & Obj_Tunnel) == Obj_Tunnel) // Check if Tunnel
	{
		// Unblock tunnel

		bb = Game.PF2[x][y] | 1; // bb is ID # w/ 1 set. 1 bit signifies that tunnel has an object on it waiting to be transported
		ok = FALSE;
		for (cy = 0; cy < 16; cy++)
			for (cx = 0; cx < 16; cx++)
				if ((Game.PF2[cx][cy] == bb) && (!((x == cx) && (y == cy)))) {
					// Search PF2[y,x] for another covered tunnel with same id (bb) & not same square
					// Search for other end of blocked tunnel
					ok = TRUE;
					goto MoveObj1;
					// Ok if something wants to move here; cx & cy set to orig
				}
		MoveObj1:
			if (ok) // We are Moving an Object
		{
			// Other end of blocked tunnel had an object so move it through now
			//Move object through a tunnel (from xy to cx,cy)
			Game.PF[x][y] = Game.PF[cx][cy]; // Transfer Blocked Object
			Game.BMF[x][y] = Game.BMF[cx][cy];

			Game.PF[cx][cy] = Game.PF2[cx][cy] & 0xFE; // Return Saved State
			Game.PF2[cx][cy] = 0;
			Game.BMF[cx][cy] = Game.BMF2[cx][cy];
			UpDateSprite(cx, cy);
		} else {
			// Did not find another end of this tunnel with an object on
			// Not Blocked Anymore
			Game.PF[x][y] = Game.PF2[x][y] & 0xFE; // Return Saved State strip
			Game.PF2[x][y] = 0;
			Game.BMF[x][y] = Game.BMF2[x][y];

			// We didn't find a match so maybe the tank is it
			if ((Game.PF[Game.Tank.X][Game.Tank.Y] == (bb & 0xFE)) && Game.Tank.Good) {
				Game.ScoreMove--; // MGY - 2003/05/18 - v408b15 -  Bartok Bug.lvl
				UpDateTankPos(0, 0);
				UndoP--;
			}
		}
	} else { // If not a tunnel
		//Move terrain from PF2 to PF
		Game.PF[x][y] = Game.PF2[x][y]; // Return Saved State
		Game.PF2[x][y] = 0;
		Game.BMF[x][y] = Game.BMF2[x][y];
	}

	UpDateSprite(x, y);
	// Source terrain updated

	// Now update destination
	x += dx;
	y += dy;

	// If destination is a tunnel then set x,y to tunnel's exit
	if (ISTunnel(x, y)) {
		// TranslateTunnel:
		//Find the exit to a tunnel with matching ID (scans y:0-15, x:0-15) and set *x, *y to the destination
		//sets WaitToTrans to TRUE of exit found in PF2 (under something) and does not change x,y
		//sets BlackHole TRUE if no exit found

		TranslateTunnel( & x, & y); // We moved into a tunnel
		if (BlackHole)
			return; // The tunnel was a black hole
	} else
		WaitToTrans = FALSE;

	// Move terrain to second layer for dest
	Game.PF2[x][y] = Game.PF[x][y]; // Save Return State

	if (WaitToTrans)
		Game.PF2[x][y] |= 1; // Set bit 1 if we are waiting to transport

	// Also move BMP to second layer
	Game.BMF2[x][y] = Game.BMF[x][y];

	if (Game.PF[x][y] != 3) //Not water terrain
	{
		// Move object to destination square
		Game.PF[x][y] = obt;
		Game.BMF[x][y] = bm;
	} else {
		// Dest square is water (ID=3)
		sf = S_Sink;
		if (obt == 5) //If is a block sinking
		{
			//Set id to GRASS and BMP to SUNK_BLOCK
			Game.PF[x][y] = 0;
			Game.PF2[x][y] = 0; // Pushing Block into Water }
			Game.BMF[x][y] = 19;
			Game.BMF2[x][y] = 19;
		}
	}
	UpDateSprite(x, y);
	if ((x == Game.Tank.X) && (y == Game.Tank.Y)) TankDirty = TRUE;
	SoundPlay(sf);
}

void IceMoveT() // Move the tank on the Ice
{
	int savei;

	if (Game.PF[SlideT.x][SlideT.y] == Obj_ThinIce) {
		Game.BMF[SlideT.x][SlideT.y] = 9;
		Game.PF[SlideT.x][SlideT.y] = Obj_Water; // Ice to Water
		UpDateSprite(SlideT.x, SlideT.y);
	}

	if (CheckLoc(SlideT.x + SlideT.dx, SlideT.y + SlideT.dy)) {
		savei = wasIce;
		ConvMoveTank(SlideT.dx, SlideT.dy, FALSE); // use this insted of UpDateTank
	} else {
		SlideT.s = FALSE;
		return;
	}

	SlideT.x += SlideT.dx; // Update Position
	SlideT.y += SlideT.dy; // Update Position
	if (!savei) SlideT.s = FALSE; // The ride is over
}

void IceMoveO() // Move an Object on the Ice
{
	int savei;
	int iSlideObj; // MGY

	for (iSlideObj = SlideMem.count; iSlideObj >= 1; iSlideObj--) // MGY
	{
		Mem_to_SlideO(iSlideObj); // Get from memory

		if (iSlideObj <= SlideMem.count) // just in case ... MGY
		{

			if (Game.PF2[SlideO.x][SlideO.y] == Obj_ThinIce) {
				Game.BMF2[SlideO.x][SlideO.y] = 9;
				Game.PF2[SlideO.x][SlideO.y] = Obj_Water; // Ice to Water
			}

			if (CheckLoc(SlideO.x + SlideO.dx, SlideO.y + SlideO.dy) &&
				(!((SlideO.x + SlideO.dx == Game.Tank.X) && (SlideO.y + SlideO.dy == Game.Tank.Y)))) {
				savei = wasIce;
				MoveObj(SlideO.x, SlideO.y, SlideO.dx, SlideO.dy, S_Push2);
				AntiTank();

				SlideO.x += SlideO.dx; // Update Position
				SlideO.y += SlideO.dy; // Update Position
				if (!savei) {
					SlideO.s = FALSE; // The ride is over
					SlideO_to_Mem(iSlideObj); // update memory
					sub_SlideO_from_Mem(iSlideObj);
				} else {
					SlideO_to_Mem(iSlideObj); // update memory
				}
			} else {

				if (Game.PF2[SlideO.x][SlideO.y] == Obj_Water)
					MoveObj(SlideO.x, SlideO.y, 0, 0, 0); // Drop Object in the water (was thin ice)
				SlideO.s = FALSE;
				SlideO_to_Mem(iSlideObj); // update memory
				sub_SlideO_from_Mem(iSlideObj);
				AntiTank(); // incase an anti-tank is behind a block
				//return; // MGY
			}
		}

	}

	Mem_to_SlideO(SlideMem.count); // Get from memory the last object of the list
	SlideO.s = (SlideMem.count > 0);
}

void KillAtank(int x, int y, char bm)
// used by CheckLLoc
// Kill the AntiTank on square x,y
// Replace bitmap with bm (dead tank bitmap for that dir tank)
// Replace object ID with 4 (solid)
// Play sound S_Anti1
{
	Game.PF[x][y] = 4; // Solid Object}
	Game.BMF[x][y] = bm; // Junk Bitmap}
	UpDateSprite(x, y);
	SoundPlay(S_Anti1);
}

int CheckLLoc(int x, int y, int dx, int dy)
// this is were the laser does its damage
// returns true if laser didn't hit anything and still in board
{
	if ((x < 0) || (x > 15) || (y < 0) || (y > 15)) //Laser out of board
	{
		return (FALSE);
	}

	if ((x == Game.Tank.X) && (y == Game.Tank.Y)) //Hit tank
	{
		SendMessage(MainH, WM_Dead, 0, 0);
		return (FALSE);
	}

	wasIce = FALSE;
	switch (Game.PF[x][y]) {

	case 0: //grass
	case 2: //flag
	case 3: //water
	case 15: //conveyor up
	case 16: //conveyor right
	case 17: //conveyor down
	case 18: //conveyor left
		return (TRUE);

	case 4: //solid
		SoundPlay(S_LaserHit);
		break;

	case 5: //block
		if (CheckLoc(x + dx, y + dy)) //Can block be moved in direction of laser? Is square free
			MoveObj(x, y, dx, dy, S_Push1); //Push block
		else
			SoundPlay(S_LaserHit);
		break;

	case 6: //wall
		Game.PF[x][y] = 0; //Set this wall object to grass (delete wall)
		Game.BMF[x][y] = 1; //Set this wall object to grass (bitmap)
		UpDateSprite(x, y);
		SoundPlay(S_Bricks);
		break;

	case 7: //antitank_up
		if (dy == 1) // Laser hit front of antitank
		{
			KillAtank(x, y, 54); //Replace antitank with ID=SOLID and frame=54 DEAD ANTITANK
			return (FALSE);
		} else if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3);
		else
			SoundPlay(S_LaserHit);
		break;

	case 8: //antitank_right
		if (dx == -1) {
			KillAtank(x, y, 52);
			return (FALSE);
		} else if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3);
		else
			SoundPlay(S_LaserHit);
		break;

	case 9: //antitank_down
		if (dy == -1) {
			KillAtank(x, y, 12);
			return (FALSE);
		} else if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3);
		else
			SoundPlay(S_LaserHit);
		break;

	case 10: //antitank_left
		if (dx == 1) {
			KillAtank(x, y, 53);
			return (FALSE);
		} else if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push3);
		else
			SoundPlay(S_LaserHit);
		break;

	case 11: //mirror_left_up
		if ((laser.Dir == 2) || (laser.Dir == 3))
			return (TRUE);
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2);
		else
			SoundPlay(S_LaserHit);
		break;

	case 12: //mirror_up_right
		if ((laser.Dir == 3) || (laser.Dir == 4))
			return (TRUE);
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2);
		else
			SoundPlay(S_LaserHit);
		break;

	case 13: //mirror_right_down
		if ((laser.Dir == 1) || (laser.Dir == 4))
			return (TRUE);
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2);
		else
			SoundPlay(S_LaserHit);
		break;

	case 14: //mirror_down_left
		if ((laser.Dir == 1) || (laser.Dir == 2))
			return (TRUE);
		if (CheckLoc(x + dx, y + dy))
			MoveObj(x, y, dx, dy, S_Push2);
		else
			SoundPlay(S_LaserHit);
		break;

	case 19: //glass
		if (laser.Good)
			// Put green reflecting glass sprite
			PutSprite(46, XOffset + (x * SpBm_Width), YOffset + (y * SpBm_Height));
		else
			// Put red reflecting glass sprite
			PutSprite(51, XOffset + (x * SpBm_Width), YOffset + (y * SpBm_Height));
		return (TRUE);

	case 20: //rotmirror_left_up
		if ((laser.Dir == 2) || (laser.Dir == 3))
			return (TRUE);
		Game.PF[x][y] = 21; // Replace ID with rotated mirror
		Game.BMF[x][y] = 48; // and replace bitmap
		UpDateSprite(x, y);
		SoundPlay(S_Rotate);
		break;

	case 21: //rotmirror_up_right
		if ((laser.Dir == 3) || (laser.Dir == 4))
			return (TRUE);
		Game.PF[x][y] = 22; // Replace ID with rotated mirror
		Game.BMF[x][y] = 49; // and replace bitmap
		UpDateSprite(x, y);
		SoundPlay(S_Rotate);
		break;

	case 22: //rotmirror_right_down
		if ((laser.Dir == 1) || (laser.Dir == 4))
			return (TRUE);
		Game.PF[x][y] = 23; // Replace ID with rotated mirror
		Game.BMF[x][y] = 50; // and replace bitmap
		UpDateSprite(x, y);
		SoundPlay(S_Rotate);
		break;

	case 23: //rotmirror_down_left
		if ((laser.Dir == 1) || (laser.Dir == 2))
			return (TRUE);
		Game.PF[x][y] = 20; // Replace ID with rotated mirror
		Game.BMF[x][y] = 47; // and replace bitmap
		UpDateSprite(x, y);
		SoundPlay(S_Rotate);
		break;

	case 24: // Ice
	case 25: // thin Ice
		return (TRUE);

	default:
		if (ISTunnel(x, y))
			return (TRUE);
	}

	// If object is moving into an ice square then add it to the Sliding stack
	if (wasIce) {
		// If is already sliding, del it !
		del_SlideO_from_Mem(x, y);
		// and add a new slide in a new direction
		SlideO.x = x + dx;
		SlideO.y = y + dy;
		SlideO.s = TRUE;
		SlideO.dx = dx;
		SlideO.dy = dy;
		add_SlideO_to_Mem();
	}
	// MGY
	else {
		// SlideO.s = FALSE;		// in case we side hit off of the ice
		del_SlideO_from_Mem(x, y);
	}
	return (FALSE);
}

void MoveLaser() {
	int x, y, oDir;

LaserMoveJump:

	LaserBounceOnIce = 0;
	x = 0;
	y = 0;
	switch (laser.Dir) {
	case 1:
		y = -1;
		break;
	case 2:
		x = +1;
		break;
	case 3:
		y = +1;
		break;
	case 4:
		x = -1;
	}
	if (CheckLLoc(laser.X + x, laser.Y + y, x, y)) // Check destination square and start objects there moving if needed
	{
		// Laser is still on the board

		if (laser.Firing)
			UpDateSprite(laser.X, laser.Y);
		
		laser.Y += y;
		laser.X += x;
		if (((Game.PF[laser.X][laser.Y] > 10) && (Game.PF[laser.X][laser.Y] < 15)) //Is mirror
			||
			((Game.PF[laser.X][laser.Y] > 19) && (Game.PF[laser.X][laser.Y] < 24))) //Is Rotating Mirror
		{

			// Reflect off mirror

			oDir = laser.Dir;

			// Update laser direction if hitting a mirror
			switch (Game.PF[laser.X][laser.Y]) {
			case 11: // mirror_left_up
			case 20: // rotmirror_left_up
				if (laser.Dir == 2) laser.Dir = 1;
				else laser.Dir = 4;
				break;

			case 12: // mirror_up_right
			case 21:
				if (laser.Dir == 3) laser.Dir = 2;
				else laser.Dir = 1;
				break;

			case 13: // mirror_right_down
			case 22:
				if (laser.Dir == 1) laser.Dir = 2;
				else laser.Dir = 3;
				break;

			case 14: // mirror_down_left
			case 23:
				if (laser.Dir == 1) laser.Dir = 4;
				else laser.Dir = 3;
			}

			// Draw laser in two halves, original direction and final direction
			UpDateLaserBounce(oDir, laser.Dir);
			SoundPlay(S_Deflb);
		} else // Not reflecting
			UpDateLaser(); // Draw laser as rectangle
		laser.Firing = TRUE;
	} else {
		// Laser is off the board / hit something solid

		Game.Tank.Firing = FALSE;
		if (laser.Firing)
			UpDateSprite(laser.X, laser.Y);

		// Antitank turn
		if (Game_On || VHSOn)
			AntiTank();

		// SpeedBug - MGY - 22-11-2002
		if (TestIfConvCanMoveTank())
			ConvMoving = TRUE;
	}

	// When drawing reflecting laser, LaserBounceOnIce is set to true if in a square with a sliding object
	if (LaserBounceOnIce)
		goto LaserMoveJump;
}

void FireLaser(int x, int y, int d, int sf) {
	char temps[30];

	Game.Tank.Firing = TRUE;

	laser.Dir = d;
	laser.X = x;
	laser.Y = y;
	laser.Firing = FALSE; // true if laser has been moved

	SoundPlay(sf);

	// Update the shot counter text
	SetTextAlign(gDC, TA_CENTER);
	SetTextColor(gDC, 0x0000FF00);
	SetBkColor(gDC, 0);
	itoa(Game.ScoreShot, temps, 10); // we incremented it in wm_timer
	TextOut(gDC, ContXPos + 134, 207, temps, strlen(temps));

	if (sf == 2)
		LaserColor = LaserColorG;
	else
		LaserColor = LaserColorR;
	laser.Good = (sf == 2);
	MoveLaser();
}

void AntiTank()
// Look for antitanks on same row/col as tank and let them fire (only if laser not already existing)
// Order: Right, left, down, above from Tank
{
	int x, y;
	// Program Anti tank seek }

	// Only one laser on board so returns if laser exists
	if (Game.Tank.Firing) return;

	x = Game.Tank.X; // Look to the right
	while (CheckLoc(x, Game.Tank.Y)) x++;
	if ((x < 16) && (Game.PF[x][Game.Tank.Y] == 10) && (Game.Tank.X != x)) {
		FireLaser(x, Game.Tank.Y, 4, S_Anti2);
		return;
	}
	x = Game.Tank.X; // Look to the left
	while (CheckLoc(x, Game.Tank.Y)) x--;
	if ((x >= 0) && (Game.PF[x][Game.Tank.Y] == 8) && (Game.Tank.X != x)) {
		FireLaser(x, Game.Tank.Y, 2, S_Anti2);
		return;
	}
	y = Game.Tank.Y; // Look Down
	while (CheckLoc(Game.Tank.X, y)) y++;
	if ((y < 16) && (Game.PF[Game.Tank.X][y] == 7) && (Game.Tank.Y != y)) {
		FireLaser(Game.Tank.X, y, 1, S_Anti2);
		return;
	}
	y = Game.Tank.Y; // Look Up
	while (CheckLoc(Game.Tank.X, y)) y--;
	if ((y >= 0) && (Game.PF[Game.Tank.X][y] == 9) && (Game.Tank.Y != y)) {
		FireLaser(Game.Tank.X, y, 3, S_Anti2);
		return;
	}
}

void PutSelectors() {
	int x, y, i, j;

	x = ContXPos + 5;
	y = 260;
	j = 1;
	for (i = 0; i <= MaxObjects; i++) {
		JK3dFrame(gDC, x - 1, y - 1, x + SpBm_Width, y + SpBm_Height, TRUE);
		if (i == CurSelBM_L) JKSelFrame(gDC, x - 1, y - 1, x + SpBm_Width, y + SpBm_Height, 1);
		if (i == CurSelBM_R) JKSelFrame(gDC, x - 1, y - 1, x + SpBm_Width, y + SpBm_Height, 2);
		PutSprite(GetOBM(i), x, y);
		x += SpBm_Width + 4;
		j++;
		if (j > EditBMWidth) {
			x = ContXPos + 5;
			y += SpBm_Height + 4;
			j = 1;
		}
	}
}

void ShowTunnelID() {
	int x, y;
	char temps[20];

	// scan and add Tunnel ID #s
	SetBkMode(gDC, OPAQUE);
	SetTextAlign(gDC, TA_LEFT);
	SetTextColor(gDC, 0);
	for (x = 0; x < 16; x++)
		for (y = 0; y < 16; y++)
			if (ISTunnel(x, y)) {
				sprintf(temps, "(%1d)", GetTunnelOldID(x, y));
				TextOut(gDC, 22 + (x * SpBm_Width), 20 + (y * SpBm_Height), temps, strlen(temps));
			}
}

void SetGameSize(int i) {
	char temps[11];
	CheckMenuItem(MMenu, 120, 0);
	CheckMenuItem(MMenu, 121, 0);
	CheckMenuItem(MMenu, 122, 0);
	CheckMenuItem(MMenu, 119 + i, MF_CHECKED);
	itoa(i, temps, 10);
	WritePrivateProfileString("SCREEN", psSize, temps, INIFile);
	if (GFXOn) GFXKill;
	switch (i) {
	case 1:
		SpBm_Width = 24;
		SpBm_Height = 24;
		ContXPos = 419;
		EditBMWidth = 6;
		SetWindowPos(MainH, 0, 0, 0, ContXPos + 190, 463, SWP_NOMOVE | SWP_NOZORDER);
		LaserOffset = 10;
		break;

	case 2:
		SpBm_Width = 32;
		SpBm_Height = 32;
		ContXPos = 550;
		EditBMWidth = 5;
		SetWindowPos(MainH, 0, 0, 0, ContXPos + 190, 591, SWP_NOMOVE | SWP_NOZORDER);
		LaserOffset = 13;
		break;

	case 3:
		SpBm_Width = 40;
		SpBm_Height = 40;
		ContXPos = 680;
		EditBMWidth = 4;
		SetWindowPos(MainH, 0, 0, 0, ContXPos + 190, 719, SWP_NOMOVE | SWP_NOZORDER);
		LaserOffset = 17;
		break;

	}
	SetWindowPos(Ed1, 0, ContXPos + 9, 99, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
	SetWindowPos(Ed2, 0, ContXPos + 9, 148, 0, 0, SWP_NOSIZE | SWP_NOZORDER);

	SetWindowPos(BT1, 0, ContXPos + 15, 255, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
	SetWindowPos(BT2, 0, ContXPos + 15, 280, 0, 0, SWP_NOSIZE | SWP_NOZORDER);

	SetWindowPos(BT3, 0, ContXPos + 15, 305, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
	SetWindowPos(BT4, 0, ContXPos + 15, 330, 0, 0, SWP_NOSIZE | SWP_NOZORDER);

	SetWindowPos(BT5, 0, ContXPos + 15, 380, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
	SetWindowPos(BT6, 0, ContXPos + 90, 380, 0, 0, SWP_NOSIZE | SWP_NOZORDER);

	SetWindowPos(BT7, 0, ContXPos + 90, 255, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
	SetWindowPos(BT8, 0, ContXPos + 90, 330, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
	SetWindowPos(BT9, 0, ContXPos + 15, 355, 0, 0, SWP_NOSIZE | SWP_NOZORDER);
	GraphM = GetPrivateProfileInt("SCREEN", psGM, 0, INIFile);
	if (GraphM == 2)
		GetPrivateProfileString("SCREEN", psGFN, "", GraphFN, MAX_PATH, INIFile);
	GetPrivateProfileString("SCREEN", psGDN, "", GraphDN, MAX_PATH, INIFile);
	if (strlen(GraphDN) == 0) {
		GetCurrentDirectory(MAX_PATH, GraphDN); //We only do this once
		WritePrivateProfileString("SCREEN", psGDN, GraphDN, INIFile);
	}
	GFXInit();
}

// Write data to .lpb file
// Write PBSRec:
//		 	char LName[31];				// Level Name
//			char Author[31];			// Author of the recording (player's initals get appended to front with "  -")
//			WORD Level;					// Level Number
//			WORD Size;					// Size of Data
// Write RecBuffer (see AddKBuff(), resizable)
void SavePBFile() {
	HANDLE Book;
	char temps[60];
	char SaveAuthor[31];

	// Get Hs.name (player's High Score name)
	GetPrivateProfileString("DATA", psUser, "", temps, 5, INIFile);
	if (stricmp(temps, HS.name) != 0) // String comparison (case insensitive)
	{
		strcpy(HS.name, temps); //strcpy(*dest, *src)
		WritePrivateProfileString("DATA", psUser, HS.name, INIFile);
	}

	if (temps[0] != '\0') {
		// Fill the name with spaces
		strcat(temps, "      ");
		temps[4] = '-'; // FIX: temps[3] = '-';  //temps = "HS - User Name"
		temps[5] = '\0';
	}
	// Add The Author's name
	strcat(temps, PBSRec.Author);
	// Limit the size
	temps[30] = '\0';

	// temps = "HS  -UserName....."
	// where HS is the palyer's high score initials,
	// and UserName is the name entered when saving, to a total of 30 bytes
	// Save	PBSRec
	strcpy(SaveAuthor, PBSRec.Author);
	strcpy(PBSRec.Author, temps);

	// Write file
	Book = CreateFile(PBFileName, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, 0, NULL); // Create New PlayBack File
	WriteFile(Book, & PBSRec, sizeof(PBSRec), & BytesMoved, NULL); // Save Header Info
	WriteFile(Book, RecBuffer, PBSRec.Size, & BytesMoved, NULL); // Data
	CloseHandle(Book);

	// restore 	PBSRec
	strcpy(PBSRec.Author, SaveAuthor);
}