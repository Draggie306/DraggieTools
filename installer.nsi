; The name of the installer
Name "DraggieTools"

; To change from default installer icon:
Icon "app.ico"

; The setup filename
OutFile "DraggieTools_Setup.exe"

; The default installation directory
InstallDir $PROGRAMFILES\Draggie\DraggieTools

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\DraggieTools" "Install_Dir"

RequestExecutionLevel admin

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "DraggieTools (required)"
  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there (you can add more File lines too)
  ; File "D:\Draggie Programs\Tools\DraggieTools\dist\DraggieTools.exe"
  
  inetc::get "https://raw.githubusercontent.com/Draggie306/DraggieTools/main/dist/DraggieTools.exe" "$INSTDIR\DraggieTools.exe" \ /END
  Pop $0
 
  ; Wildcards are allowed:
  ; File *.dll
  ; To add a folder named MYFOLDER and all files in it recursively, use this EXACT syntax:
  ; File /r MYFOLDER\*.*
  ; See: https://nsis.sourceforge.io/Reference/File
  ; MAKE SURE YOU PUT ALL THE FILES HERE IN THE UNINSTALLER TOO
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\DraggieTools "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieTools" "DisplayName" "DraggieTools"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieTools" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieTools" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieTools" "NoRepair" 1
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  ExecShell "open" "$INSTDIR\DraggieTools.exe"
  
SectionEnd

Section /o "Client"
  SetOutPath $INSTDIR
  
  inetc::get "https://autoupdateclient.draggie.games/AutoUpdate40.exe" "DraggieClient.exe" /END
  Pop $0
  
  WriteRegStr HKLM SOFTWARE\DraggieClient "Install_Dir" "$INSTDIR"
  
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieClient" "DisplayName" "DraggieClient"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieClient" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieClient" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieClient" "NoRepair" 1
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  ExecShell "open" "$INSTDIR\DraggieClient.exe"
  
SectionEnd


; Optional section (can be disabled by the user)
Section /o "Start Menu Shortcuts (optional)"
  CreateDirectory "$SMPROGRAMS\DraggieTools"
  CreateShortcut "$SMPROGRAMS\DraggieTools\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortcut "$SMPROGRAMS\DraggieTools\DraggieTools.lnk" "$INSTDIR\DraggieTools.exe" "" "$INSTDIR\DraggieTools.exe" 0
  
SectionEnd


;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieTools"
  DeleteRegKey HKLM SOFTWARE\DraggieTools

  ; Remove files and uninstaller
  ; MAKE SURE NOT TO USE A WILDCARD. IF A
  ; USER CHOOSES A STUPID INSTALL DIRECTORY,
  ; YOU'LL WIPE OUT OTHER FILES TOO
  Delete $INSTDIR\DraggieTools.exe
  Delete $INSTDIR\uninstall.exe

  ; Remove shortcuts, if any
  Delete "$SMPROGRAMS\DraggieTools\*.*"

  ; Remove directories used (only deletes empty dirs)
  RMDir "$SMPROGRAMS\DraggieTools"
  RMDir "$INSTDIR"
 
SectionEnd
  
Section "Uninstall" /o

  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DraggieClient"
  DeleteRegKey HKLM SOFTWARE\DraggieClient

  ; Remove files and uninstaller
  ; MAKE SURE NOT TO USE A WILDCARD. IF A
  ; USER CHOOSES A STUPID INSTALL DIRECTORY,
  ; YOU'LL WIPE OUT OTHER FILES TOO
  Delete $INSTDIR\DraggieClient.exe
  Delete $INSTDIR\uninstall.exe

  ; Remove shortcuts, if any
  Delete "$SMPROGRAMS\DraggieClient\*.*"

  ; Remove directories used (only deletes empty dirs)
  RMDir "$SMPROGRAMS\DraggieClient"
  RMDir "$INSTDIR"


SectionEnd
