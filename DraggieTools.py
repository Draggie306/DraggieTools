import random
from requests import get
from datetime import datetime

build = 1
version = "0.0.2"
build_date = 1650035323


def check_for_update():
    print("Checking for update...")
    current_build_version = get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt")
    current_build_version = int(current_build_version.content)
    if build < current_build_version:
        update_choice = input(f"Update available! You are on version {version} which is build {build}. The new version is build {current_build_version}\n\nType 1 to download update, else not")
        if update_choice == 1:
            r = get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/DraggieTools.py")
            with open('DraggieTools.py', 'wb') as f:
                f.write(r.content)
        else:
            return
    else:
        print(f"Your tools are up to date. Running version {version} - build {build} - built at {datetime.fromtimestamp(1650035010).strftime('%Y-%m-%d %H:%M:%S')}")


check_for_update()

def main():
    the_funny = ['Transfering sensitive files to The Criminal Network...', 'Your Computer Has Been FUCKED by the Trojan!', 'Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION', 'Problem opening the application running at executable "C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe". Would you like to scan this PC?']
    print(random.choice(the_funny))

main()
