import random
from requests import get
from datetime import datetime
from os import path

build = 2
version = "0.0.2"
build_date = 1650035323

current_directory = path.dirname(path.realpath(__file__))
print(f"running CLI from {current_directory}")


def check_for_update():
    print("Checking for update...")
    current_build_version = get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt")
    current_build_version = int(current_build_version.content)
    if build < current_build_version:
        update_choice = input(f"Update available! You are on version {version} which is build {build}. The new version is build {current_build_version}\n\nType 1 to download update, else not")
        if update_choice == 1:
            r = get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/dist/DraggieTools.exe")
            with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
                f.write(r.content)
        else:
            return
    else:
        print(f"Your tools are up to date. Running version {version} - build {build} - built at {datetime.fromtimestamp(1650035010).strftime('%Y-%m-%d %H:%M:%S')}")


check_for_update()


def main():
    the_funny = ['Transfering sensitive files to The Criminal Network...', 'Your Computer Has Been FUCKED by the Trojan!', r'Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION', r'Problem opening the application running at executable "C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe". Would you like to scan this PC?']
    print(random.choice(the_funny))
    print("\n\n\nWhat would you like to do, mon frère?")


main()
