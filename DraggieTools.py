import random
from requests import get
from datetime import datetime
from os import path, startfile
from time import monotonic
import shutil

build = 8
version = "0.1.3"
build_date = 1650039706

current_directory = path.dirname(path.realpath(__file__))
print(f"running CLI from {current_directory}")

current_build_version = int((get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt")).content)


class BColours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def download_update():
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


def check_for_update():
    print("Checking for update...")
    if build < current_build_version:
        update_choice = input(f"{BColours.WARNING}Update available! You are on version {version} which is build {build}. The newest version is build {current_build_version}\n\n{BColours.ENDC}Type 1 to download update, else not\n\n>>> ")
        if update_choice == "1":
            print(f"{BColours.OKBLUE}Downloading update...")
            download_update()
            print("Update downloaded. Launching new version...")
            startfile(f'{current_directory}\\DraggieTools-{current_build_version}.exe')
        else:
            print("Skipping update.")
            return
    else:
        print(f"{BColours.OKGREEN}Your tools are up to date. Running version {version} - build {build} - built at {datetime.fromtimestamp(1650035010).strftime('%Y-%m-%d %H:%M:%S')}. The server says the newest build is {current_build_version}.{BColours.ENDC}")


check_for_update()


def main():
    the_funny = ['Transfering sensitive files to The Criminal Network...', 'Your Computer Has Been FUCKED by the Trojan!', r'Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION', r'Problem opening the application running at executable "C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe". Would you like to scan this PC?']
    print(f"{BColours.WARNING}{random.choice(the_funny)}{BColours.ENDC}")
    print("\n\n\nWhat would you like to do, mon frère?")

    def choice1():
        x = input("\n\n1) Install this to desktop\n2) Install this to custom directory\n3) Create shortcut on desktop\n\n>>> ")
        if x == "1":
            print("Initialising.")
            directory = f"{current_directory}\\{path.basename(__file__)}"
            print(f"Current directory: {directory}")
        if x == "2":
            e = r"C:\Program Files"
            c = r"C:\Program Files\Draggie"
            y = input(f"Enter the new directory. For example, '{e}'. \nNote that wherever you install me to, a new folder will be added called 'Draggie' This means that inputting the directory above will be {c}.\n\nRight click to paste!\n>>> ")
            directory = f"{current_directory}\\{path.basename(__file__)}"
            print(f"Current directory: {directory}")
            shutil.copyfile(directory, f"{y}\\Draggie\\{path.basename(__file__)}")
            print(f"Successfully copied file to {y}\\Draggie\\{path.basename(__file__)}")
        if x == "3":
            print("lmao")
        else:
            choice1()
    
    choice1()


main()