import random
from requests import get
from datetime import datetime
from os import path, startfile, mkdir
from time import monotonic
import shutil

build = 14
version = "0.1.8"
build_date = 1650041242

current_directory = path.dirname(path.realpath(__file__))
print(f"running CLI from {current_directory}")


def download_update(current_build_version):
    try:
        r = get('https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true', stream=True)
        file_size = int(r.headers['content-length'])
        downloaded = 0
        start = last_print = monotonic()
        with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                downloaded += f.write(chunk)
                now = monotonic()
                if now - last_print > 0.1:
                    pct_done = round(downloaded / file_size * 100)
                    speed = round(downloaded / (now - start) / 1024)
                    print(f'Downloading. {pct_done}% done, avg speed {speed} kbps')
                    last_print = now
    except KeyError as e:
        print(f"Key error occured: {e}\n\nResorting to backup")
        r = get('https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true')
        with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
            f.write(r)

def check_for_update():
    print("Checking for update...")
    current_build_version = int((get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt")).content)
    if build < current_build_version:
        update_choice = input(f"Update available! You are on version {version} which is build {build}. The newest version is build {current_build_version}\n\nType 1 to download update, else not\n\n>>> ")
        if update_choice == "1":
            print("Downloading update...")
            download_update(current_build_version)
            print("Update downloaded. Launching new version...")
            startfile(f'{current_directory}\\DraggieTools-{current_build_version}.exe')
        else:
            print("Skipping update.")
            return
    else:
        print(f"Your tools are up to date. Running version {version} - build {build} - built at {datetime.fromtimestamp(1650035010).strftime('%Y-%m-%d %H:%M:%S')}. The server says the newest build is {current_build_version}.")


check_for_update()


def main():
    the_funny = ['Transfering sensitive files to The Criminal Network...', r'Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION', r'Problem opening the application running at executable "C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe". Would you like to scan this PC?']
    print(f"{random.choice(the_funny)}")
    print("\n\n\nWhat would you like to do, mon frère?")

    def choice1():
        x = input("\n\n1) Install this to desktop\n2) Install this to custom directory\n3) Create shortcut on desktop\n4) Refresh updates\n>>> ")
        if x == "1":
            print("Initialising.")
            directory = f"{current_directory}\\DraggieTools.exe"
            print(f"Current directory: {directory}")
        if x == "2":
            try:
                e = r"C:\Program Files"
                c = r"C:\Program Files\Draggie"
                y = input(f"Enter the new directory. For example, '{e}'. \nNote that wherever you install me to, a new folder will be added called 'Draggie' This means that inputting the directory above will be {c}.\n\nRight click to paste!\n>>> ")
                directory = f"{current_directory}\\DraggieTools.exe"
                print(f"Current directory: {directory}")
                try:
                    mkdir(f"{y}\\Draggie\\")
                except Exception as e:
                    pass
                shutil.copyfile(directory, f"{y}\\Draggie\\DraggieTools.exe")
                print(f"Successfully copied file to {y}\\Draggie\\DraggieTools.exe")
            except Exception as e:
                print(f"An error occured. {e}")
                print("Please make sure that the file has not been renamed.")
                choice1()
        if x == "3":
            print("lmao")
        if x == "4":
            check_for_update()
            choice1()
        else:
            choice1()
    
    choice1()


main()
