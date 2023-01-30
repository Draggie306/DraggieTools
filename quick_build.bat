@echo off
start powershell -NoProfile -ExecutionPolicy Bypass -Command "cd 'D:\Draggie Programs\Tools\DraggieTools\'; & 'pyinstaller.exe' --onefile --icon=app.ico --clean DraggieTools.py"
