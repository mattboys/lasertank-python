
         **************************************************************
         ***  Welcome to the LaserTank Update: Levels, High Scores  ***
         ***  and Playback Files Utility, Version 5.2.2 (Freeware)  ***
         **************************************************************


  +++++++++++++++++
  Distributed Files
  +++++++++++++++++

     The LTUpdate.ZIP archive contains the following files:
        LTUpdate.exe - LaserTank Update: Levels, High Scores and Playback Files
                         program.
        ReadMeUp.TXT - This file.
        VerHstUp.TXT - LaserTank Update: Levels, High Scores and Playback Files
                         Utility version history.
        WBDCC34I.DLL - Dynamic Linked Library (DLL), for WinBatch 2001N, that
                         is required by LTUpdate.exe (from Wilson WindowWare,
                         Inc., Ref. http://www.windowware.com or
                         http://www.winbatch.com).
        WWZIP34I.DLL - DLL required, for the Zipping and un-Zipping of files,
                         by LTUpdate.exe (from Wilson WindowWare, Inc., Ref.
                         http://www.windowware.com or http://www.winbatch.com).

     See below for installation and usage instructions, and Warning codes.

  ==============================================================================


  ++++++++++++++++++++++++++
  Description of the Program
  ++++++++++++++++++++++++++

     The LaserTank Update: Levels, High Scores and Playback Files program
  (LTUpdate.exe) automates (most of) the work required to update your LaserTank
  data files for the Official levels collections.  There are four types of
  LaserTank data files: Levels (.LVL), Global High Scores (.GHS), (Local) High
  Scores (.HS) and Playback (.LPB).  The basic LaserTank data files (.LVL, .GHS
  and .HS) are described on the "LaserTank Help Page" of the LaserTank web site;
  e.g., http://perso.cgocable.ca/lasertank/ > English > Help Page.  A Playback
  (.LPB) file is created by the LaserTank program when you record, and/or save,
  the level that you are playing or have completed.  Playback files are
  described in the "Recording & Playback" section of the LaserTank Help file.

     The Official levels collections are in the direct links on the "Download
  New Levels & View High Scores Lists" page of the LaserTank web site; i.e. (as
  of the modified date of this file): Beginner-I, Beginner-II, Challenge-I,
  Challenge-II, Challenge-III, Challenge-IV, Challenge-V, Gary-I, Gary-II,
  LaserTank, Sokoban-I, Sokoban-II and Special-I.  This web page can be reached
  as follows;
       http://perso.cgocable.ca/lasertank/ > English > New Levels & High Scores.

     This program requires the "All Levels, GHS & Reports in one zip file"
  updates archive, Updates.zip, that is on (and was downloaded from) the
  "Download New Levels & View High Scores Lists" page of the LaserTank web site
  (listed above).  This archive contains: the updated .LVL and .GHS files for
  each Official levels collection, and a "Report" .HTML file that specifies the
  changes in each Official levels collection.  For example, the LaserTank.lvl,
  LaserTank.ghs and LaserTank_Report.html files in Updates.ZIP are for the
  "LaserTank" levels collection.  These files are used to update: your .HS and
  .LPB files, and your copies of the .LVL and .GHS files, for the Official
  levels collections.  (Note, this archive also contains other files that are
  not processed by this program.)

     The downloaded Updates.zip archive, and this program, must be located in
  "Your LaserTank Folder", <YourLTFolder>; e.g., C:\Games\LaserTank\.  By
  definition, <YourLTFolder> is the folder (including its full path) that
  contains: your copies of the "Official" .LVL, .GHS and "Report" .HTML files;
  and your .HS files for the Official levels collections (and probably your copy
  of the LaserTank program, LaserTank.exe).

     IMPORTANT! The changes specified and implemented in the files in the
  Updates.zip archive are incremental (i.e., they are relative to the previously
  posted update).  Hence, you should verify (manually) the results of the first
  execution of the LTUpdate.exe program on your computer (see the "How to Use
  the Program" section below).  Subsequently, the LTUpdate.exe program MUST be
  used every time a new Updates.zip archive is posted (usually at the beginning
  of every month) in order to keep your LaserTank data files (.LVL, .GHS, .HS
  and .LPB) for the Official levels collections current and correct.  In other
  words, running this program with the current Updates.zip archive, after
  skipping one (or more) Updates.zip archive(s), could result in erroneous or
  deleted .HS and/or .LPB files for one, or more, of the Official levels
  collections.  See Note 4 below for information about user modified Levels
  files.

     This program issues a warning (see "A" in the Warning Codes section below)
  if any file that was extracted from the Updates.zip archive is more than 45
  days newer than its matching file in <YourLTFolder>.  At a minimum, the
  Updates.zip archive that is used must be new (e.g., not previously processed
  by this program).  Hence, none of its .LVL, .GHS or "Report" .HTML files can
  be older than their matching files in <YourLTFolder>, and at least one of its
  files must be newer than its matching file in <YourLTFolder>.

     This program performs the following operations:

        1) Compiles and displays a New/Updated Files List (NUFL) that consists
          of the .LVL, .GHS and "Report" .HTML files in the downloaded
          Updates.zip archive that are either not in, or newer than those in,
          <YourLTFolder>.

        2) Optionally backs up all of the existing:
              * Files in <YourLTFolder> that are on the NUFL.
              * .HS files in <YourLTFolder> that could be changed; i.e., that
               correspond to the .LVL files on the NUFL.
              * "Standard Named and Located Playback" (SNAL-LPB) files (see
               Note 1 below) that will be deleted, replaced, or renamed and
               (possibly) moved.  Usually these SNAL-LPB files are for the
               Modified, Deleted, "Moved from" and "Moved to" levels in the
               .LVL files on the NUFL.
          A Backup File List (BFL) containing all of these files is generated.
          This list, without its SNAL-LPB files (if any), is displayed first.
          You can select either, neither or both of the following backup
          methods for the BFL files:
              a) Append "_Old" (without the quotes) to the right side of the
                root name of each file on the BFL.  For example, LaserTank.lvl
                is backed up as LaserTank_Old.lvl.  Any existing "_Old" backup
                files will be replaced (overwritten) without an option to back
                them up.
              b) Copy each file on the BFL to a LaserTank Data Backup Archive,
                LTDataBackup.ZIP, in <YourLTFolder>.  This archive will be
                created if it doesn't exist.  If it already exists (in
                <YourLTFolder>), the previous version of this archive will be
                updated (see Note 2 below) without an option to back it up.

        3) Extracts the Updates.zip archive files on the NUFL to <YourLTFolder>.
          The existing files will be replaced.  Note, the .txt (case sensitive)
          files in this archive (e.g., Levels_Name.txt and README.txt) are not
          extracted.

        4) Deletes the (local) high scores (.HS file entries) of the Modified
          and Deleted levels in the .LVL files on the BFL (as specified in their
          corresponding "Report" .HTML files).  See Notes 3 and 4 below.

        5) Moves the (local) high scores (.HS file entries) of the Moved levels
          in the .LVL files on the BFL (as specified in their corresponding
          "Report" .HTML  files).  The high scores of these levels are deleted
          from the "Moved from" files (see Note 3 below).  The required "Moved
          to" .HS files will be created (in <YourLTFolder>) if they don't
          already exist.

        6) Optionally deletes the SNAL-LPB files (see Note 1 below) for the
          Modified levels in the .LVL files on the BFL.  See Note 4 below also.

        7) Deletes the SNAL-LPB files (see Note 1 below) for the Deleted levels
          in the .LVL files on the BFL.

        8) Renames, changes the level numbers in the headers of, and (possibly)
          moves, the SNAL-LPB files (see Note 1 below) for the Moved levels in
          the .LVL files on the BFL.  See Note 5 below also.

        9) Sets (or resets) the size of every updated or created .HS file to
          either (user selected):
              a) (Default) Ten (bytes/level) times the highest completed level
                number in it (i.e., to 10*Nhc bytes where Nhc is its highest
                level number with Moves greater than zero).  If no levels are
                completed in a .HS file (i.e., Nhc = 0), it's deleted (or not
                created).  Or,
              b) Ten (bytes/level) times the number of levels in its
                corresponding .LVL file.  (This will make it easier for you to
                identify and access the levels that you have not completed -  
                see Note 6 below).
          This choice is reversible.

        10) Optionally documents all of the actions taken, and the changes made
           (or considered) by this program.  This "Updates Log" information can
           be viewed and/or copied to a text file, LTUpLog.TXT, in
           <YourLTFolder>.  If <YourLTFolder>\LTUpLog.TXT doesn't exist, it will
           be created.  If <YourLTFolder>\LTUpLog.TXT exists, you can open it in
           the associated (registered) application for .TXT files (see Caution 5
           below) before writing the new Updates Log information to it.
           Then/Else, you can append the new Updates Log information to the end
           (after the old information), or insert it at the beginning (before
           the old information), of an existing <YourLTFolder>\LTUpLog.TXT file.
           Or, you can replace the contents of an existing
           <YourLTFolder>\LTUpLog.TXT file with the new Updates Log information
           from the current execution of this program.

        11) Optionally copies the new Updates Log information (see Operation 10
           above) to the Windows Clipboard (replacing its contents - if any).

        12) Optionally opens (for viewing or editing) any created or modified
           Updates Log file (see Operation 10 above).  This file is opened (if
           requested) in the associated (registered) application for .TXT files
           (see Caution 5 below).

     If you start a second instance of this program (e.g., by double-clicking on
  its desktop icon when it's already running), you will be prompted to
  (optionally) open either this ReadMe file (<YourLTFolder>\ReadMeUp.TXT), or
  the current, Updates Log file (<YourLTFolder>\LTUpLog.TXT - see Operation 10
  above), if they exist.  The selected file is opened in the associated
  (registered) application for .TXT files (see Caution 5 below).

     Note 1: This program only recognizes and processes "Standard Named and
  Located Playback" (SNAL-LPB) files.  A SNAL-LPB file for a given level:
        * Has a "Standard/Default" name (the default name suggested by the
         LaserTank program); i.e., <LVLFileRootName>_<dddd>.lpb, where
         <LVLFileRootName> is the root name of the Levels (.LVL) file that
         contains the level (i.e., the name of the levels collection), <dddd> is
         the 4-digit level number (with leading zeros if required), and the both
         the root name and the extension are case insensitive; and,
        * Is located either in <YourLTFolder> or a <LVLFileRootName>-named
         subfolder of it.  (The default location is the folder that contains the
         LaserTank program.)
  For example, if <YourLTFolder> is C:\Games\LaserTank\, then both:
        C:\Games\LaserTank\Sokoban-I_0123.lpb, and
        C:\Games\LaserTank\Sokoban-I\Sokoban-I_0123.LPB,
  would be SNAL-LPB files for level number 123 in the Sokoban-I.lvl file.
  WARNING: If both of these .LPB files exist, this program will only process the
  one in the <LVLFileRootName>-named subfolder of <YourLTFolder>
  (C:\Games\LaserTank\Sokoban-I\Sokoban-I_0123.LPB in the above example).

     Note 2: If backup method "b" is specified in Operation 2 above and the
  LaserTank Data Backup Archive, <YourLTFolder>\LTDataBackup.ZIP, exists: its
  existing BFL files will be replaced, new BFL files will be added to it,
  and its other files (if any) will not be altered or deleted.

     Note 3: A deleted high score in Operations 4 or 5 above may be replaced if
  the level is replaced.

     Note 4: This program will delete the high scores and (optionally) the
  SNAL-LPB files (if any) for levels (in the Levels files in Updates.ZIP) that
  were manually modified since the last time it was (successfully) run.  For
  this process, "manually modified" means that the level's Playfield was changed
  by the user (e.g., using the editor that is build into the LaserTank program).
  To avoid losing the high scores for these modified levels, you should make
  SNAL-LPB files when you solve them, and backup these files when asked by the
  LTUpdate.exe program.  You can then restore, and use, these backup Playback
  files to restore the high scores for these modified levels.

     Note 5: If the SNAL-LPB file for a Moved level exists, it will be (renamed,
  changed and) placed (or left) in the relevant <LVLFileRootName>-named
  subfolder of <YourLTFolder> (see Note 1 above) if this subfolder exists.
  Otherwise, it will be (renamed, changed and) placed (or left) in
  <YourLTFolder>.

     Note 6: Assume that you are running the LaserTank program with the "Gary-x"
  levels collection, and that Nlvl is the number of levels in Gary-x.lvl and Nhc
  (< Nlvl) is the highest completed level number in Gary-x.hs.  By default, the
  size of Gary-x.hs (in bytes) is 10 (bytes/level) times Nhc.  When you select
  "View High Scores" on LaserTank's "File" menu, only levels 1 to Nhc are
  listed.  However, if you selected option "b" in Operation 9 above and the size
  of Gary-x.hs is 10*Nlvl bytes, all Nlvl of the Gary-x.lvl levels will be
  listed; and, hence, the uncompleted levels between Nhc and Nlvl can be easily
  identified and accessed.

     Note 7: This program creates a ~TEMP subfolder in <YourLTFolder> to
  temporarily hold the files extracted from the Updates.zip archive and the
  older .HS and SNAL-LPB files that could be changed or deleted.  This
  subfolder, and its contents, are deleted just before the execution of this
  program is completed.  If this program is prematurely terminated (e.g., by a
  fatal error condition), you may have to manually delete (or rename or move)
  this subfolder and its contents.  See the "Premature Termination Warning"
  section below.

     CAUTION 1: In addition to the optional backups described in Operation 2
  above, you should manually backup all of the "Official" .LVL, .GHS and .HS
  files in <YourLTFolder> (using alternate methods) before executing this
  program.  Also, to be completely safe, you should manually backup all of your
  SNAL-LPB files for the levels in the Official levels collections (using
  alternate methods) before executing this program.  You may need these backup
  files if this program is prematurely terminated (e.g., by a fatal error
  condition), or if an unforeseen processing error occurs.  See the "Premature
  Termination Warning" section below.

     CAUTION 2: This program assumes that the Updates.zip file (case insensitive
  name) in <YourLTFolder> is a valid (e.g., unmodified) "All Levels, GHS &
  Reports in one zip file" updates archive that was downloaded from the
  "Download New Levels & View High Scores Lists" page of the LaserTank web site.

     CAUTION 3: This program assumes that all of the existing: .HS files in
  <YourLTFolder>, and SNAL-LPB files, that could be changed (see Operations
  4 - 9 above) are valid LaserTank High Scores and Playback files, respectively.

     CAUTION 4: This program assumes that the .LVL and .HS files in
  <YourLTFolder>, with the same root names, are "corresponding" Levels and High
  Scores files (i.e., they contain data for the same collection of levels).

     CAUTION 5: If they exist, this program assumes that ReadMeUp.TXT and
  LTUpLog.TXT in <YourLTFolder> are standard text files.  Also, this program
  assumes that .TXT files are associated with (registered to) an existing
  application on your computer (the default is the Windows Notepad).  You may
  get an Error message if Notepad is your associated application, and you try to
  open a LTUpLog.TXT file that is larger than about 50 KB.  Proceed with caution
  if you get such an Error message.  (I don't think this restriction applies in
  Windows XP, and later.)

     CAUTION 6: Editing or changing the date/time of any file that could be
  referenced, modified or replaced by this program could produce ERRONEOUS
  RESULTS and/or IRREVERSIBLE LOSS of information (unless this program, or you,
  have backed up your LaserTank data files as described in Operation 2 and
  CAUTION 1 above).

     CAUTION 7: The execution of this program is paused several times to display
  information, and allow user input.  Also, it may be paused to allow the user
  to correct an error condition.  Unless specifically authorized in the
  displayed dialog box, you must not: delete, modify, move, rename, change the
  accessibility of (i.e., open in another program in Read-deny mode), or change
  the attributes of (e.g., make Read-only):
        * Any file that has been or could be referenced, replaced, deleted or
         modified by this program; or,
        * The ~TEMP subfolder of <YourLTFolder> (see Note 7 above) or any of
         its files.
  Also, you must not add any sub-subfolders to this ~TEMP subfolder.  Any of
  these actions could produce FATAL PROGRAM ERRORS, ERRONEOUS RESULTS, and/or
  IRREVERSIBLE LOSS of information (unless this program, or you, have backed up
  your LaserTank data files as described in Operation 2 and CAUTION 1 above).

     CAUTION 8: This program reads the "Report" .HTML or files (that were
  extracted from the Updates.ZIP archive) as text files.  It assumes that the
  text you see when any of these files are opened in an HTML viewer/editor is an
  accurate representation of the text in the file; e.g., that a space is a space
  (" ") and not the HTML character entity "&nbsp;".

     CAUTION 9: This program assumes that a level is "Deleted" (and hence not
  replaced) if, and only if: it becomes Not Rated, and the first 13 characters
  of its name become "Deleted Level" (case sensitive).

     CAUTION 10: This program assumes that each Official levels collection
  contains no more than 4096 levels.  Note, this limit is currently 2030 in the
  LaserTank levels collection and 2000 in the others.

  ==============================================================================


  ++++++++++++++++++++++++++++++++++++++++
  Installation and Removal of This Utility
  ++++++++++++++++++++++++++++++++++++++++

     Although the LaserTank Update: Levels, High Scores and Playback Files
  program has only been tested on Windows 95, 98, NT 4.0, XP, Vista and 7
  systems, it should run on any 32-bit, or higher, Windows platform.  A vertical
  screen resolution of at least 768 pixels is required to fully display some of
  the dialog boxes generated by this program.

     To install this utility, just extract the LTUpdate.exe, WBDCC34I.DLL and
  WWZIP34I.DLL files from the LTUpdate.ZIP archive to <YourLTFolder> (see the
  "Description of the Program" section above).  (Note: this WBDCC34I.DLL file is
  identical to the one required by the LaserTank Utilities, and Developer's
  Utilities, Suites.)  This ReadMeUp.TXT and the VerHstUp.TXT files are for
  information only - so you don't have to un-Zip them from the LTUpdate.ZIP
  archive to run the LTUpdate.exe program.

     You can create shortcuts (e.g., in your Start menu, or on your Desktop) to
  the LTUpdate.exe program in the usual manner (see your Windows documentation - 
  Ha, Ha, Ha).  The "Start in" folder of these shortcuts must be <YourLTFolder>.
  Note, the LTUpdate.exe program can also be run directly in the usual manner
  (e.g., by double-clicking its listing or icon in the Windows Explorer).

     You may move the WBDCC34I.DLL and/or WWZIP34I.DLL files to any folder that
  is in your search PATH (environment variable).

     To uninstall this utility, just delete the files that you extracted to
  install it (e.g., LTUpdate.exe, WBDCC34I.DLL and WWZIP34I.DLL), and remove the
  shortcuts that you created (if any).  CAUTION: As noted above, WBDCC34I.DLL
  may be used by other programs.

  ==============================================================================


  ++++++++++++++++++++++
  How to Use the Program
  ++++++++++++++++++++++

     To use the LaserTank Update Levels, High Scores and Playback Files program:

        Step 1: Download the "All Levels, GHS & Reports in one zip file" Updates
          archive, Updates.zip, to <YourLTFolder> (see the "Description of the
          Program" section above).  The Updates.zip archive is posted on the
          "Download New Levels & View High Scores Lists" page of the LaserTank
          web site.  To get to this page: go to
          http://perso.cgocable.ca/lasertank/, then click on "English" (or
          "Français"), and then click on "New Levels & High Scores" (or
          "Tableaux & Records").

        Step 2: Make sure that the "Offical" (see the "Description of the
          Program" section above): Levels (.LVL), High Scores (.GHS and .HS),
          and "Report" .HTML files in <YourLTFolder> are not: Read-only, or open
          by other applications in Read-deny mode.  Also, make sure that your
          existing SNAL-LPB files (see Note 1 in the "Description of the
          Program" section above) for the levels in the Official levels
          collections are not: Read-only, or open by other applications in
          Read-deny mode.

        Step 3: If backup method "a" is to be specified (see Operation 2 in the
          "Description of the Program" section above), make sure that all of the
          existing append "_Old" backup files in <YourLTFolder> (e.g., the files
          with root names ending "_Old") are not: Read-only, or open by other
          applications in Read-deny mode.  If required, the existing "_Old"
          backup files in <YourLTFolder> will be replaced (overwritten) without
          an option to back them up.  So, move or rename them now (before
          running this program) if you want to save them.

        Step 4: If backup method "b" is to be specified (see Operation 2 in the
          "Description of the Program" section above) and the LTDataBackup.ZIP
          file exists in <YourLTFolder>, make sure that it's not: Read-only, or
          open by another application in Read-deny mode.  The contents of the
          existing <YourLTFolder>\LTDataBackup.ZIP file will be changed without
          an option to back it up.  So, move or rename it now (before running
          this program) if you want to preserve its contents.

        Step 5: If the updating of an existing Updates Log file
          (<YourLTFolder>\LTUpLog.TXT) is to be specified (see Operation 10 in
          the "Description of the Program" section above), make sure that it's
          not: Read-only, or open by another application in Read-deny mode.  You
	  will be given the option to back up an existing
          <YourLTFolder>\LTUpLog.TXT file before it's modified or replaced.

        Step 6: Run the LaserTank Update: Levels, High Scores and Playback Files
          program, LTUpdate.exe, and follow its prompts.  If this is the FIRST
          EXECUTION OF THIS PROGRAM on your computer (since LaserTank was
          installed), click on the "No" button if the Warning "A" prompt appears
          (or click on its "Yes" button each time it appears), and see Step 7
          below.  Whenever you run this program, it's HIGHLY RECOMENDED that you
          select at least one backup method (see Operation 2 in the "Description
          of the Program" section above), and at least one "create/update" the
          Updates Log file (and/or its information) option (see Operations 10
          and 11 in the "Description of the Program" section above).

        Step 7: If this is not an "incremental" update (e.g., this is the first
          time that this program is being run on your computer - see Warning
          Code A-2 below), you should manually verify the updates for all of the
          (deleted and) replaced, and moved, levels that were specified in the
          "Report" .HTML files (in <YourLTFolder>).  Specifically, you should
          check the high scores of, and the SNAL-LPB files for, these levels.
          You will have to manually correct any errors.

     The execution of this program is paused several times to display
  information and allow user inputs.  Also, it may be paused to allow the user
  to correct error conditions.  Unless specifically authorized in the displayed
  dialog box, you must not: delete, modify, move, rename, change the
  accessibility of (i.e., open in another program in Read-deny mode), or change
  the attributes of (e.g., make Read-only), any file that has been or could be
  referenced, modified, replaced or deleted by this program.

     IMPORTANT NOTE 1: The changes specified and implemented in the files in the
  Updates.zip archive are incremental (i.e., they are relative to the previously
  posted update).  Hence, after the results of its first execution are verified
  (manually), the LTUpdate.exe program MUST be used every time a new Updates.zip
  archive is posted (normally at the beginning of every month) in order to keep
  your LaserTank .LVL, .GHS, .HS and SNAL-LPB files for the Official levels
  collections current and correct.  In other words, running this program with
  the current Updates.zip archive, after skipping one (or more) Updates.zip
  archive(s), could result in ERRONEOUS and/or DELETED .HS and/or SNAL-LPB
  files.

     IMPORTANT NOTE 2: If you have manually modified the Playfield of any level
  in the Levels files in Updates.ZIP since the last time this program was
  (successfully) run, see Note 4 in the "Description of the Program" section
  above.

     This program is spyware and adware free, and it does not connect to any
  internet servers.

  ==============================================================================


  ++++++++++++++++++++++++++++++++++++
  Premature Termination of the Program
  ++++++++++++++++++++++++++++++++++++

     The execution of the LTUpdate.exe program can be (prematurely) terminated
  by pressing the <Ctrl>+<Pause/Break> keys (simultaneously), and then clicking
  on the "OK" button (or pressing the <Enter> key) to clear the WinBatch "Error:
  194" dialog box if it pops up.  If the program is minimized (e.g., to a button
  on the Taskbar), you may have to open it (e.g., click on its Taskbar button or
  select it with the <Alt>+<Tab> keys combination) before pressing the
  <Ctrl>+<Pause/Break> keys combination.  WARNING! Pressing the
  <Ctrl>+<Pause/Break> keys combination may terminate all non-minimized programs
  that use the WBDCC34I.DLL file (see the "Installation and Removal of This
  Utility" section above).

     PREMATURE TERMINATION WARNING: The LTUpdate.exe program is "prematurely"
  terminated if it stops (or is stopped by the user, see the above paragraph)
  before it is finished and without the user clicking on the "Exit", "Cancel"
  or "X" button in a dialog box, or pressing a hot-key (e.g., <Esc> or
  <Alt>+<F4>) to close a dialog box.  Before rerunning this program (if
  possible), you should (must):

        * Manually delete the ~TEMP subfolder of <YourLTFolder> (if it still
         exists) and its contents (see Note 7 in the "Description of the
         Program" section above).  Since this subfolder may contain useful
         files, you may want to move its contents to another temporary location
         until the problem that caused the premature termination of the program
         is resolved.

        * Use the backup files (see Operation 2 and CAUTION 1 in the
         "Description of the Program" section above) to restore all of the
         original, Official: .LVL, .GHS, .HS and "Report" .HTML files in
         <YourLTFolder>; and the original SNAL-LPB files.  If you didn't specify
         any backup files, you're on your own.  Rerunning this program with the
         same Updates.zip archive (if possible), without restoring the original
         LaserTank .LVL, .GHS, .HS and SNAL-LPB files, could produce ERRONEOUS
         RESULTS in, and/or IRREVERSIBLE LOSS of, .HS and/or SNAL-LPB files.

  ==============================================================================


  +++++++++++++
  Warning Codes
  +++++++++++++

     The following Warning codes may be generated by the LaserTank Update:
  Levels, High Scores and Playback Files program (<YourLTFolder> is defined in
  the "Description of the Program" section above):

        A) One, or more, of the original files in <YourLTFolder> were more than
          45 days older than their matching files in the "All Levels, GHS &
          Reports in one zip file" updates archive (Updates.zip); i.e., the
          executed update spanned more than 45 days.  That is, either:
              1) It was more than 45 days since the last Updates.zip file was
                posted on the LaserTank web site and used with this program.
                Proceeding after receiving this warning was probably harmless.
                Or,
              2) This update was not incremental; i.e., either:
                    a) This was the first time that this program was executed on
                      your computer (since LaserTank was installed); or,
                    b) One, or more, posted Updates.zip files were skipped
                      between the one that was used for this execution and the
                      one that was used for the previous execution of this
                      program.
                Proceeding after receiving this warning could have produced
                ERRONEOUS RESULTS in, and/or IRREVERSIBLE LOSS of, High Scores
                (.HS) and/or SNAL-LPB files (see Note Z below).  You should
                manually verify the updates as described in Step 7 in the "How
                to Use the Program" section above.

        B) One, or more, of the relevant .LVL, .GHS or "Report" .HTML files that
          were originally in <YourLTFolder> were Read-only and/or they were open
          by other applications in Read-deny mode.  At least one of these files
          was deleted, moved or renamed by the user before the updating was
          started.  This could have produced a "hard to reverse" LOSS of
          information.

        C) One, or more, of the relevant High Scores (.HS) files that were
          originally in <YourLTFolder> were Read-only and/or they were open by
          other applications in Read-deny mode.  At least one of these files was
          deleted, moved or renamed by the user before the updating was started.
          This could have produced ERRONEOUS RESULTS in the new .HS file, and/or
          an IRREVERSIBLE LOSS of high scores data (see  Note Z  below).

        D) One, or more, of the relevant .LVL, .GHS or "Report" .HTML backup
          files that were originally in <YourLTFolder> (e.g., the ones with
          "_Old" appended to the right side of their root names) were Read-only
          and/or they were open by other applications in Read-deny mode.  At
          least one of these files was deleted, moved or renamed by the user
          before the updating was started.  This could have produced an
          IRREVERSIBLE or "hard to reverse" LOSS of information (see Note Z
          below).

        E) One, or more, of the relevant, High Scores (.HS) backup files that
          were originally in <YourLTFolder> (e.g., the ones with "_Old" appended
          to the right side of their root names) were Read-only and/or they were
          open by other applications in Read-deny mode.  At least one of these
          files was deleted, moved or renamed by the user before the updating
          was started.  This could have produced an IRREVERSIBLE LOSS of high
          scores information (see Note Z below).

        F) The original LaserTank Data Backup Archive (LTDataBackup.ZIP) in
          <YourLTFolder> was Read-only and/or it was open by another application
          in Read-deny mode.  Hence, this program could not update it.  The
          updating of this archive was skipped (deselected by the user).  This
          could have produced an IRREVERSIBLE LOSS of information (see Note Z
          below).  Also, since they were not updated, the files in this
          LTDataBackup.ZIP archive probably became invalid.  Note, this (orig-
          inal) archive may have been deleted, moved or renamed by the user.

        G) Since updating it was not specified, one or more of the files in the
          original LaserTank Data Backup Archive (LTDataBackup.ZIP) in
          <YourLTFolder> probably became invalid.

        H) No backup method was (or remained) selected for the relevant
          LaserTank .LVL, .GHS, "Report" .HTML , .HS, and .LPB files.  Hence,
          they WERE NOT BACKED UP before they were replaced.  This could have
          produced an IRREVERSIBLE LOSS of information (see Note Z below).
          Also, since they were not updated, any existing backup files for these
          files, and/or the files in an existing Data Backup Archive
          (LTDataBackup.ZIP), probably became invalid.

        I) One, or more, of the updated Levels (.LVL) files do not have
          corresponding "Report" files.  Hence, the high scores of Modified or
          Deleted levels in, or levels Moved from, these .LVL files (if any)
          could not be deleted by this program.  However, this program will copy
          the high scores of any levels that are moved to these files.

        J) For unknown reasons, at least one of the relevant LaserTank .LVL,
          .GHS or .HS files that were originally in <YourLTFolder> could not be
          backed up by appending "_Old" to the right side of their root names.
          This could have produced an IRREVERSIBLE LOSS of information (see
          Note Z below).  Also, since they were not updated, any existing backup
          files for these files probably became invalid.

        K) For unknown reasons, a LaserTank Data Backup Archive
          (LTDataBackup.ZIP) could not be created in <YourLTFolder>, or the
          existing LTDataBackup.ZIP file in <YourLTFolder> could not be updated
          using the relevant LaserTank .LVL, .GHS or .HS files that were
          originally in <YourLTFolder>.  This could have produced an
          IRREVERSIBLE LOSS of information (see Note Z below).  Also, since they
          were not updated, the .LVL, .GHS and .HS  files in an existing Data
          Backup Archive probably became invalid.

        L) For unknown reasons, one or more of the relevant High Scores (.HS)
          files that were originally in <YourLTFolder> could not be copied to
          its ~TEMP subfolder.  This could have produced ERRONEOUS RESULTS for,
          and/or IRREVERSIBLE LOSS of, high scores information for Moved levels
          (if any) (see Note Z below).

        M) By user request, at least one SNAL-LPB file (see Note 1 in the
          "Description of the Program" section above) for a Modified level was
          not deleted.  These files may not be valid for their Modified levels.

        N) At least one SNAL-LPB file (see Note 1 in the "Description of the
          Program" section above) for a Modified or Deleted level was Read-only
          and/or it was open by another application in Read-deny mode.  Hence,
          it/they could not be deleted by this program as requested by the user
          (for a Modified level) or required (for a Deleted level).  Some of
          these files may have been manually deleted, moved or renamed by the
          user.  However, one or more of these files were not deleted, moved or
          renamed; and hence, they probably became invalid.

        O) One, or more, SNAL-LPB files (see Note 1 in the "Description of the
          Program" section above) for "Moved to" levels were Read-only and/or
          they were open by other applications in Read-deny mode.  Hence, this
          program could not delete them (as required because their corresponding
          "Moved from" level SNAL-LPB files don't exist).  Some of these files
          may have been manually deleted, moved or renamed by the user.
          However, one or more of these files were not deleted, moved or
          renamed; and hence, they probably became invalid.

        P) At least one SNAL-LPB file (see Note 1 in the "Description of the
          Program" section above) for a "Moved from" level was Read-only and/or
          it was open by another application in Read-deny mode.  Hence, it/they
          could not be renamed/moved by this program.  These SNAL-LPB files and
          the SNAL-LPB files for their designated "Moved to" levels (if they
          exist) probably became invalid.

        Q) One, or more, of the files in Warning O (above) were manually
          deleted, moved or renamed by the user.  This could have produced
          ERRONEOUS RESULTS for, and/or IRREVERSIBLE LOSS of, playback
          information for Moved levels (if any) (see Note Z below).

        R) One, or more, SNAL-LPB files (see Note 1 in the "Description of the
          Program" section above) for "Moved to" levels were Read-only and/or
          they were open by other applications in Read-deny mode.  Hence, they
          could not be replaced by their designated (renamed and modified)
          "Moved from" levels SNAL-LPB files.  These "Moved from" and "Moved to"
          SNAL-LPB files probably became invalid.  Note, some of these files may
          have been manually deleted, moved or renamed by the user.

        S) For unknown reasons, one or more of your relevant SNAL-LPB files
          (see Note 1 in the "Description of the Program" section above) could
          not be backed up by appending "_Old" to the right side of their root
          names.  This could have produced an IRREVERSIBLE LOSS of these files
          (see Note Z below).  Also, since they were not updated, any existing
          SNAL-LPB backup files probably became invalid.

        T) For unknown reasons, one or more of your relevant SNAL-LPB files (see
          Note 1 in the "Description of the Program" section above) could not be
          added to the LaserTank Data Backup Archive (LTDataBackup.ZIP) in
          <YourLTFolder>.  This could have produced an IRREVERSIBLE LOSS of
          these files (see Note Z below).  Also, since they were not updated,
          the SNAL-LPB files in an existing Data Backup Archive probably became
          invalid.

        U) Although at least one backup method was selected, no relevant
          LaserTank .LVL, .GHS, .HS, "Report" .HTML, or SNAL-LPB files were
          found (in <YourLTFolder>) to back up.  Hence, no backup operations
          were performed.  Since they were not updated, any existing backup
          files for these files, and/or the files in an existing LaserTank Data
          Backup Archive (<YourLTFolder>\LTDataBackup.ZIP), probably became
          invalid.

        V) For unknown reasons, one or more of your relevant SNAL-LPB files (see
          Note 1 in the "Description of the Program" section above) could not be
          moved to the ~TEMP subfolder of <YourLTFolder>.  This could have
          produced ERRONEOUS RESULTS for, and/or IRREVERSIBLE LOSS of, playback
          information for Moved levels (if any) (see Note Z below).

        W) For unknown reasons, one or more of your relevant SNAL-LPB files (see
          Note 1 in the "Description of the Program" section above) could not be
          deleted or renamed/moved.  This could have produced ERRONEOUS RESULTS
          for, and/or IRREVERSIBLE LOSS of, playback information (see Note Z
          below).

     Note Z: The term "IRREVERSIBLE LOSS" in these warnings only applies if you,
  or the LTUpdates.exe program, didn't backup your LaserTank data files as
  described in Operation 2 and/or CAUTION 1 in the "Description of the Program"
  section above.  Hence, it's HIGHLY RECOMENDED that you select at least one of
  the backup methods offered in this Operation 2.

  ==============================================================================


  +++++++++++++++
  Version History
  +++++++++++++++

     See the VerHstUp.TXT file.

  ==============================================================================


  +++++++++++++++++++++++++
  Liability and Legal Stuff
  +++++++++++++++++++++++++

     This software is provided "AS IS", and without any expressed and/or implied
  warranties of any kind.  The author of this software will not take any
  responsibilities for any damages that may occur with its use.  The user
  assumes the entire risk of using this software.

     This software may not be distributed as part of any commercial product
  (including "shareware") without a prior licence agreement with the author.
  All rights remain with the author.  See the next section for the address of
  the author.

  ==============================================================================


  +++++++++++++++++++++
  Contacting the Author
  +++++++++++++++++++++

     If you have questions, comments, enhancement requests, improvement
  suggestions or bug reports about this program or its documentation, you can
  email me (in English please) at DrWiseKing@comcast.net or
  DrWiseKing@verizon.net.  Or you can post a message to the Yahoo! LaserTank
  group,
       http://groups.yahoo.com/group/LaserTank/.
  You can also get to this group from the LaserTank web site; i.e., go to
  http://perso.cgocable.ca/lasertank/, then click on "English" (or "Français"),
  and then click on "Yahoo Group" (or "Groupe Yahoo").

  ==============================================================================


        Enjoy,
        Harvey Solomon (DrWiseKing)
        Woodstock, Maryland, USA 21163
