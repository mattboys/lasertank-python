
def GetPrivateProfileString(app, key, default, filename):
    """
    Get data from ini file
    Port of
    DWORD GetPrivateProfileString(
      LPCTSTR lpAppName,  (app)
      LPCTSTR lpKeyName,  (key)
      LPCTSTR lpDefault,  (default)
      LPTSTR  lpReturnedString,
      DWORD   nSize,
      LPCTSTR lpFileName  (filename)
    )
    https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getprivateprofilestring
    """
    import configparser
    config = configparser.ConfigParser()
    config.read(filename)
    return config.get(section=app, option=key, fallback=default)




class System:
  def __init__(self):
    self.LastLevel = 0
    self.CurLevel = 0
    self.RLL = False
    self.GameInProg = False
    self.Game_On = False
    self.INIFile = INIFileName
    self.Difficulty = 0  # Selected difficulty filter
    self.Recording = False
    self.UI = UI()

  def command_new_game(self):  # Menu 101
    self.LastLevel = self.CurLevel
    self.CurLevel = 0   
    if self.RLL:  # Remember Last Level
      self.CurLevel = int(GetPrivateProfileString("DATA", psRLLL, "1", self.INIFile))
      self.CurLevel -= 1
    if not LoadNextLevel(True, False):
      self.CurLevel = self.LastLevel

  def DialogBox(self, dialog_name):
    # TODO
    pass

  def SendMessage_225_ChangeDifficulty(self):
    x = self.Game_On
    self.GameOn(False)
    self.DialogBox("DiffBox")
    GameOn(x)
    return 0

  def SendMessage_123_TurnOffRecording(self):
    if self.UI.GetMenuState(MMenu, 123).is_checked() :
      self.UI.SetMenuState(MMenu, 123, checked=False)
      self.Recording = False
      EnableMenuItem(MMenu, 117, MF_GRAYED)
      SetWindowText(MainH, App_Title)
    else:
      CheckMenuItem(MMenu, 123, MF_CHECKED)
      self.Recording = True
      EnableMenuItem(MMenu, 117, 0) # enable Save Recording
      SetWindowText(MainH, REC_Title)
    return 0

  def command_WM_SaveRec(self):
    # TODO
    pass

  def SetTimer(self, delay):
    # Sends WM_TIMER message when timer up (delay in ms)
    # TODO
    pass

  def KillTimer(self):
    # TODO
    pass

  def GameOn(self, b):
    # Start/stop game timer and set Game_On
    if b:
      SetTimer(GameDelay)
    else:
      KillTimer();
    self.Game_On = b;
  

  def LoadNextLevel(self, DirectLoad, Scanning):
    # Directload is true if we shouldn't use difficulties & Completed Level check
    # Scanning is true if we are searching and dont want any errors displayed
    if self.GameInProg:
      if tkinter.messagebox.askyesnocancel(message=txt039, title=txt038):  # Game in progress, Do you want to save the game?
        self.command_WM_SaveRec() 
      else:
        return False
      
    self.GameOn(False)
    ######################################################
    # TODO next
    #####################################################
    SavedLevelNum = self.CurLevel
    if self.Difficulty == 0:
      self.SendMessage_225_ChangeDifficulty()  # Set Difficulty Window - Send change difficulty menu command
    if self.Recording:
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
