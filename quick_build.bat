@echo off
start powershell -NoProfile -ExecutionPolicy Bypass -Command "cd 'D:\Draggie Programs\Tools\DraggieTools\'; & 'pyinstaller.exe' --onefile --clean --icon=app.ico DraggieTools.py"
