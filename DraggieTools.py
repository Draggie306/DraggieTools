import random
from requests import get
from datetime import datetime
from os import path, startfile
from subprocess import Popen
from time import monotonic

build = 3
version = "0.0.2"
build_date = 1650035323

current_directory = path.dirname(path.realpath(__file__))
print(f"running CLI from {current_directory}")

current_build_version = int((get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt")).content)

def download_update():
    r = get('https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true', stream=True)
    file_size = int(r.headers['content-length'])
    downloaded = 0
    start = last_print = monotonic()
    with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            downloaded += f.write(chunk)
            now = monotonic()
            if now - last_print > 1:
                pct_done = round(downloaded / file_size * 100)
                speed = round(downloaded / (now - start) / 1024)
                print(f'Downloading. {pct_done}% done, avg speed {speed} kbps')
                last_print = now

def check_for_update():
    print("Checking for update...")
    if build < current_build_version:
        update_choice = input(f"Update available! You are on version {version} which is build {build}. The new version is build {current_build_version}\n\nType 1 to download update, else not\n\n>>> ")
        if update_choice == "1":
            print("Downloading update...")
            download_update()
            print("Update downloaded. Launching new version...")
            startfile(f'{current_directory}\\DraggieTools-{current_build_version}.exe')
        else:
            print("Skipping update.")
            return
    else:
        print(f"Your tools are up to date. Running version {version} - build {build} - built at {datetime.fromtimestamp(1650035010).strftime('%Y-%m-%d %H:%M:%S')}. The server says the newest build is {current_build_version}")


check_for_update()


def main():
    the_funny = ['Transfering sensitive files to The Criminal Network...', 'Your Computer Has Been FUCKED by the Trojan!', r'Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION', r'Problem opening the application running at executable "C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe". Would you like to scan this PC?']
    print(random.choice(the_funny))
    print("\n\n\nWhat would you like to do, mon frère?")
    x = input("")
    print(x)

main()
