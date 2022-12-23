from subprocess import Popen
from requests import get
from datetime import datetime
from os import path, startfile, mkdir, environ, listdir, remove
from time import monotonic, sleep, time
from uuid import uuid4
from tqdm import tqdm
import shutil
import pathlib
import sys
import random
import traceback
import logging
import zipfile
from threading import Event, Thread
from base64 import b64decode
from math import ceil
from cryptography.fernet import Fernet

dev_mode = True

build = 40
version = "0.5.0"
build_date = 1671805296

environ_dir = environ['USERPROFILE']

if not dev_mode:
    DraggieTools_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\DraggieTools")
    Draggie_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie")
    #   Fixes issues on first-time entry.
    if not path.exists(Draggie_AppData_Directory):
        mkdir(f"{environ_dir}\\AppData\\Roaming\\Draggie\\")
    if not path.exists(DraggieTools_AppData_Directory):
        mkdir(DraggieTools_AppData_Directory)

else:
    uuid_gen = uuid4()
    #uuid_gen = "test1234"
    DraggieTools_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie{uuid_gen}\\DraggieTools")
    Draggie_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie{uuid_gen}")

    if not path.exists(Draggie_AppData_Directory):
        mkdir(f"{environ_dir}\\AppData\\Roaming\\Draggie{uuid_gen}\\")
    if not path.exists(DraggieTools_AppData_Directory):
        mkdir(DraggieTools_AppData_Directory)


global stop_event, thread

def start_anim_loading(text):
    global stop_event, thread
    stop_event = Event()
    thread = Thread(target=loading_icon, args=(stop_event,text))
    thread.start()

def stop_anim_loading():
    global stop_event, thread
    stop_event.set()
    thread.join()

def loading_icon(stop_event, text):
    while not stop_event.is_set():
        for i in ["|", "/", "-", "\\"]:
            print(f"\r{text} {i}", end="")
            sleep(0.1)


if not path.exists(f"{DraggieTools_AppData_Directory}\\Logs"):
    mkdir(f"{DraggieTools_AppData_Directory}\\Logs")

if not path.exists(DraggieTools_AppData_Directory):
    mkdir(DraggieTools_AppData_Directory)

if not path.exists(f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache"):
    mkdir(f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache")

if not path.exists(f"{DraggieTools_AppData_Directory}\\SourceCode"):
    mkdir(f"{DraggieTools_AppData_Directory}\\SourceCode")

desktop_install_path = False

if path.exists(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt"):
    desktop_dir = pathlib.Path.home() / 'Desktop'
    with open (f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
        install_dir = e.read()
        if install_dir == str(desktop_dir): 
            logging.debug(f"Determined installLoc to be desktop @ {desktop_dir}")
            desktop_install_path = True
            
def get_first_line_of_term(search_phrase, file):
    with open(file, 'r', encoding="UTF-8") as f:
        line_num = 0
        for line in f.readlines():
            line_num += 1
            if line.find(search_phrase) >= 0:
                return(line_num)


def replace_line(file_name, line_num, text):
    line_num = line_num - 1
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def log_print(text):
    """
    Logs and prints the text inputted. The logging level is INFO.
    """
    logging.info(text)
    print(text)

global language, language_chosen

#   The following are new line separated every 10 index entries
#   Remember - the index starts at 0 lol
english = ["Key error occured: ", "\n\nResorting to backup", "Downloading.", "done, average speed", "Checking for update...", "Downloading update...", "Running from", "What would you like to do, my friend?", "Transfering sensitive files to The Criminal Network...", "Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION",
           r"Problem opening the application running at executable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Would you like to scan this PC?", "Running version", "@", "build", "The server says the newest build is", "\nUpdate available!", "You are on version", "The newest version is build", "Press enter to download the update!", "This is index 20 (defined under **language[19]**), if you see this then report as error.",
           "Downloading and opening up the source Python file in Explorer. To view it, open it in Notepad or you could upload it to an IDE online.", "which is build", "Quitting...", "\nHey, you're running on a version newer than the public build. That means you're very special UwU\n"]# Index number 23 -   ENGLISH

french = ["Desolée", "\n\nRecourir à la sauvegarde", "Téléchargement.", "finir, avec vitesse moyenne", "Vérification de la mise à jour...", "Téléchargement de la mise à jour...", "En cours d'exécution à", "Qu'est-ce que tu voudrais faire, mon ami(e) ?", "Transfert de fichiers sensibles vers le réseau criminel...", "Votre ordinateur est piraté par IP : 5.172.193.104 comme OS : LINUX UBUNTU et emplacement : FÉDÉRATION DE RUSSIE",
          r"Problème d'ouverture de l'application exécutée sur l'exécutable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Voulez-vous scanner ce PC ?", "Version en cours d'exécution", "@", "mini-version", "Le serveur dit que la nouvelle version est", "\nMise à jour disponsible !", "Vous êtes sur le mini-version", "Le mini-version nouvelle est", "Ecrivez entre pour la télécharger.", "This is index 20 in french (defined under **language[19]**), if you see this then report as error.",
          "Ouverture du fichier Python source dans l'Explorateur. Pour le voir, ouvre ceci dans Bloc-notes Windows ou vous pouvez le télécharger sur un IDE en ligne.", "qui est le mini-version", "En train de quitter...", "\nBonjour! Vous etes sur un mini-version plus récente que la version pour le public. Vous etes vraiment spécial, UwU\n"]# Index number 23 - FRENCH

"""
Here are the prints for directory determining.
"""

if dev_mode:
    logging.basicConfig(filename=f'{DraggieTools_AppData_Directory}\\Logs\\{version}-{build}-{time()}.log', encoding='utf-8', level=logging.DEBUG)
    logging.debug(f'Established uplink at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print(f"\n\n*-* Beta Tester Prints *-*\n\nAppData Directory: {DraggieTools_AppData_Directory}")
    sleep(0.05)
    print(f"Executable location: {sys.executable}")
    sleep(0.05)
    print(f"application_path: {path.dirname(path.abspath(__file__))}\n\nDevmode is ON, therefore enhanced logging is active.\nThe log file is located in the Roaming AppData directory")
    sleep(0.05)

directory = sys.executable
if dev_mode:
    logging.info(f"Assigned directory to {sys.executable}")


def change_language():
    global language, language_chosen
    language = None
    while language is None:
        x = input("Choose language\nChoisissez la langue\nEnglish = 1, French = 2\n\n>>> ")
        if x == "2":
            print("La langue est maintenant francais.")
            language = french
            with open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w+", encoding="UTF-8") as x:
                x.close()
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Langauge_Preference.txt' cleared")
            with open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w", encoding="UTF-8") as x:
                x.write("French")
                x.close()
            logging.info(f"({datetime.now()}.strftime('%Y-%m-%d %H:%M:%S'): File at path '{DraggieTools_AppData_Directory}\\Langauge_Preference.txt' written with 'French'")
            language_chosen = "French"
        else:
            print("Language updated to English.")
            language = english
            with open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w+", encoding="UTF-8") as x:
                x.close()
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Langauge_Preference.txt' cleared")

            with open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w") as x:
                x.write("English")
                x.close()
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Langauge_Preference.txt' written with 'English'")
            language_chosen = "English"
    if dev_mode:
        logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Language successfully changed to {language_chosen}")


if path.exists(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt"):
    try:
        with open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", encoding="UTF-8") as x:
            language_read = x.read()

        if language_read == "French":
            language = french
            print("Language set to French.")
            language_chosen = "French"
        else:
            language = english
            print("Language set to English.")
            language_chosen = "English"
    except Exception:
        change_language()


current_directory = path.dirname(path.realpath(__file__))
if dev_mode:
    logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: variable currrent_directory assigned with value {current_directory}")


def download_update(current_build_version):
    try:

        if not path.exists(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds'):
            mkdir(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds')

        download_url = "https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true"

        response = get(download_url, stream=True)

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024  # 1 Kibibyte
        written = 0

        with open(f"{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe", "wb") as f:
            for data in tqdm(response.iter_content(block_size), total=ceil(total_size // block_size), unit="KB", desc=download_url.split("/")[-1]):
                written = written + len(data)
                f.write(data)
                
        if desktop_install_path == True:
            try:
                shutil.copyfile(f"{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe", f"{desktop_dir}\\DraggieTools.exe")
                print(f"Installed update to preferred directory, the desktop.")
            except FileExistsError:
                remove(f"{desktop_dir}\\DraggieTools.exe")
                shutil.copyfile(f"{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe", f"{desktop_dir}\\DraggieTools.exe")
                print(f"Installed update to preferred directory, the desktop.")
        
    except KeyError as e:
        print(f"Some error occured: {e}\n\nResorting to fallback method. Preferences will not be usedm saving to default directory.")
        print(f"{language[0]}{e}{language[1]}")
        r = get('https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true')
        with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
            f.write(r)


def view_source():
    print(language[20])
    x = time()
    r = get('https://raw.githubusercontent.com/Draggie306/DraggieTools/main/DraggieTools.py')
    with open(f'{DraggieTools_AppData_Directory}\\SourceCode\\DraggieTools-v{version}-{build}-{x}.py', 'wb') as f:
        f.write(r.content)
    Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\SourceCode\\DraggieTools-v{version}-{build}-{x}.py"')


def fort_file_mod():
    fort_ini_directory = (f"{environ_dir}\\AppData\\Local\\FortniteGame\\Saved\\Config\\WindowsClient\\GameUserSettings.ini")
    if not path.isfile(fort_ini_directory):
        print("Unable to detect the INI settings file. Make sure your client is updated.")
        return

    print(f"Established uplink with {fort_ini_directory}")

    y = input("What would you like to change?\n1) Framerates\n2) Graphics Settings\nType 0 to open the directory\n\n>>> ")

    if y == "1":
        z = input("Okay, what type of framerate?\n\n1) FrameRateLimit (In-game and lobby) - note this will overwrite all other settings\n2) FrontendFrameRateLimit (Max Lobby FPS)\n\n>>> ")
        if z == "1":
            try:
                fps = int(input("Input desired FPS here:\n\n>>> "))
            except ValueError:
                print("Disallowed input. Try again")
                main()

            x = get_first_line_of_term("FrameRateLimit=", fort_ini_directory)

            replace_line(fort_ini_directory, x, f'FrameRateLimit={fps}.000000\n')

            print(f"Modified config FrameRateLimit in section [/Script/FortniteGame.FortGameUserSettings], line {x}")

        if z == "2":
            try:
                fps = int(input("Input desired FPS here:\n\n>>> "))
            except ValueError:
                print("Disallowed input. Try again")
                main()

            x = get_first_line_of_term("FrontendFrameRateLimit=", fort_ini_directory)
            print(f"first line of the codees = {x}")

            replace_line(fort_ini_directory, x, f'FrontendFrameRateLimit={fps}\n')
            logging.debug(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: main/fort_file_mod: {fort_ini_directory} has been modified! FrontendFrameRateLimit={fps}")
            logging.debug(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: main/fort_file_mod: {fort_ini_directory} has been modified! FrontendFrameRateLimit={fps}")
            print("Successfully modified config FrontendFrameRateLimit in section [/Script/FortniteGame.FortGameUserSettings]")

    if y == "2":
        graphics_settings = ["Low", "Medium", "High", "Epic"]
        eligible_settings = [
            ["3D Resolution", "View Distance", "Shadows", "Post Processing", "Textures", "Effects", "(hidden) Foliage", "(hidden) Shading", "Anti Aliasing", "(RTX only) Global Illumination", "(RTX only) Reflections"],
            ["sg.ResolutionQuality", "sg.ViewDistanceQuality", "sg.ShadowQuality", "sg.PostProcessQuality", "sg.TextureQuality", "sg.EffectsQuality", "sg.FoliageQuality", "sg.ShadingQuality", "sg.AntiAliasingQuality", "sg.GlobalIlluminationQuality", "sg.ReflectionQuality"]
        ]

        other_settings = [
            ["Culture", "Using DX12", "Using GPU Crash Debugging", "Ray Tracing", "Performance Mode Mesh Quality"],
            ["Culture", "bUseD3D12InGame", "bUseGPUCrashDebugging", "r.RayTracing.EnableInGame", "MeshQuality"]
        ]

        print("Reading graphics settings and quality presets...")

        for i in range(len(eligible_settings[1])):
            try:
                x = int(get_first_line_of_term(f"{eligible_settings[1][i]}=", fort_ini_directory))
                with open(fort_ini_directory, "r") as ini_file:
                    lines = ini_file.readlines()
                    target_line = (lines[x - 1])

                quality = target_line.split("=")
                quality = quality[1].split("\\")
                quality_level = int(quality[0])

                if eligible_settings[0][i] == "3D Resolution":
                    print(f"{eligible_settings[0][i]} = {quality_level}%")
                else:
                    print(f"{eligible_settings[0][i]} = {graphics_settings[quality_level]}")
                sleep(0.05)
            except Exception as e:
                print(f"Could not find the value associated with {eligible_settings[0][i]} - {e}")

        print("\nSearching for other settings...\n")

        for i in range(len(other_settings[1])):
            try:
                x = get_first_line_of_term(f"{other_settings[1][i]}=", fort_ini_directory)
                with open(fort_ini_directory, "r") as ini_file:
                    lines = ini_file.readlines()
                    target_line = (lines[x - 1])

                quality = target_line.split("=")
                quality = quality[1].split("\n")
                quality_level = (quality[0])

                print(f"{other_settings[0][i]} is set to '{quality_level}'")
            except Exception as e:
                print(f"Could not find the value associated with {other_settings[0][i]} - {e}")

        choice2 = input("\n\n1) Go back\n2) Modify a value\n\n>>> ")

        if choice2 != "2":
            return
        else:
            print("Default values are 0 for LOW/OFF\n1 for MEDIUM\n2 for HIGH\n3 for EPIC")
            print("\nOk, what would you like to change?")

    if y == "0":
        Popen(fort_ini_directory)
    main()


def check_for_update():
    try:
        stop_event = Event()
        thread = Thread(target=loading_icon, args=(stop_event,language[4]))
        thread.start()
    except Exception as e:
        change_language()
        check_for_update()
    current_build_version = int((get('https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt')).text)
    if build < current_build_version:
        release_notes = str((get(f"https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Release%20Notes/release_notes_v{current_build_version}.txt")).text)
        stop_event.set()
        thread.join()
        print(f"{language[15]} {language[16]} {version} {language[21]} {build}.\n{language[17]} {current_build_version}. {language[18]}\n\n")
        if language_chosen == "English":
            versions_to_get = current_build_version - build
            if versions_to_get == 1:
                print(f"You're {versions_to_get} build behind latest")
            else:
                print(f"You're {versions_to_get} builds behind latest")

            string = (f"Latest release notes (v{current_build_version}):\n\n{release_notes}\n")

            while current_build_version != (build + 1):
                current_build_version = current_build_version - 1
                version_patch = str((get(f"https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Release%20Notes/release_notes_v{(current_build_version)}.txt")).text)
                string = (string + f"\nv{current_build_version}:\n{version_patch}")
            print(f"\n{string}\n")

        update_choice = input(">>> ")
        if update_choice != "":
            print("Skipping update.")
            return

        logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {language[6]} - {DraggieTools_AppData_Directory}")
        download_update(current_build_version)
        print("Update downloaded. Launching new version - you can close this now.")
        if desktop_install_path == False:
            startfile(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe')
        else:
            desktop_dir = pathlib.Path.home() / 'Desktop'
            startfile(f'{desktop_dir}\\DraggieTools-{current_build_version}.exe')
        sys.exit()

    if current_build_version < build:
        stop_event.set()
        thread.join()
        print(language[23])
    else:
        print(f"{language[11]} {version} - {language[13]} {build} - {language[12]} {datetime.fromtimestamp(build_date).strftime('%Y-%m-%d %H:%M:%S')}. {language[14]} {current_build_version}.")
        stop_event.set()
        thread.join()

try:
    check_for_update()
except Exception as e:
    print(f"An error occured while getting the update.\n{e}\n\n")
    logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {traceback.format_exc()}")


def autobrawlextractor():
    Brawl_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor")
    Downloaded_Builds_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")

    def init_filetype(dir):
        """
        Initialises and checks the validity of the archive version provided. If the file provided is not valid, then the program will exit.
        """
        try:
            archive = zipfile.ZipFile(dir, 'r')
            try:
                archive.read('Payload/Brawl Stars.app/PkgInfo')
                version = "IPA"
            except KeyError:
                archive.read('classes.dex')
                version = "APK"
            if version:
                print(f"Detected Verson: {version}")
            else:
                print("Unknown version type please use the other OS' version")
                sleep(4)
                sys.exit()
        except Exception as e:
            print(f"Error occured: {e}")

    def number_one():
        print(r"Enter the location of your Brawl Stars archive file, e.g D:\Downloads\brawl.apk")
        print("Use an .ipa file or .apk file (for iOS and Android decices, respectively). Must not be unzipped.")
        print("Alternatively, press 1 to search for downloadable versions, if you do not have the file.")

        amount_of_files = 0

        for i in listdir(Downloaded_Builds_AppData_Directory):
            amount_of_files = amount_of_files + 1

        if amount_of_files >= 1:
            print(f"\nYou have {amount_of_files} files already downloaded inside the DownloadedBuilds folder")

        location = input("\n>>> ")

        if location == "1":
            print("Fetching available versions from GitHub...")
            latest_apk = str((get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Addons/AutoBrawlExtractor/latest.apk")).text)
            latest_ipa = str((get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Addons/AutoBrawlExtractor/latest.ipa")).text)
            apk_lines = latest_apk.splitlines()
            print(f"APK version {apk_lines[0]} is available to download. Source: {apk_lines[2]}")
            ipa_lines = latest_ipa.splitlines()
            print(f"IPA version {ipa_lines[0]} is available to download. Source: {ipa_lines[2]}")
            decision = input("Would you like to download the APK (type 1) or IPA (option 2). Alternatively, type enter to go back.\n\n>>> ")
            print(f"Files will be downloaded to {Brawl_AppData_Directory}/DownloadedBuilds")

            if decision == "1":
                download_dir = apk_lines[1]
                r = get(download_dir, stream=True)
                file_size = int(r.headers['content-length'])
                downloaded = 0
                start = last_print = monotonic()
                if not path.exists(f'{Brawl_AppData_Directory}\\DownloadedBuilds'):
                    mkdir(f'{Brawl_AppData_Directory}\\DownloadedBuilds')
                with open(f'{Brawl_AppData_Directory}\\DownloadedBuilds\\{apk_lines[0]}.apk', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        downloaded += f.write(chunk)
                        now = monotonic()
                        if now - last_print > 0.5:
                            pct_done = round(downloaded / file_size * 100)
                            speed = round(downloaded / (now - start) / 1024)
                            print(f'Downloading file. {pct_done}% - {speed} kbps')
                            last_print = now
                print("Downloaded the file!")

            if decision == "2":
                download_dir = ipa_lines[1]
                r = get(download_dir, stream=True)
                file_size = int(r.headers['content-length'])
                downloaded = 0
                start = last_print = monotonic()
                if not path.exists(f'{Brawl_AppData_Directory}\\DownloadedBuilds'):
                    mkdir(f'{Brawl_AppData_Directory}\\DownloadedBuilds')
                with open(f'{Brawl_AppData_Directory}\\DownloadedBuilds\\{ipa_lines[0]}.ipa', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        downloaded += f.write(chunk)
                        now = monotonic()
                        if now - last_print > 0.5:
                            pct_done = round(downloaded / file_size * 100)
                            speed = round(downloaded / (now - start) / 1024)
                            print(f'Downloading file. {pct_done}% - {speed} kbps')
                            last_print = now
                print("Downloaded the file!")
            number_one()
        else:
            init_filetype(location)
    number_one()

def awtd():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-*-*-*-*-*-*-*-*-*-*-*-* Welcome to the Advanced Water Tech Demo Secret Area! *-*-*-*-*-*-*-*-*-*-*-*-\n")
    print("Searching for installed versions...")
    if not path.exists(f"{DraggieTools_AppData_Directory}\\AWTD"):
        mkdir(f"{DraggieTools_AppData_Directory}\\AWTD")
    if path.exists(f"{DraggieTools_AppData_Directory}\\AWTD\\Config"):
        print("Found a config file.")
    else:
        # Create a stop event
        stop_event = Event()

        # Start the loading icon in a separate thread
        thread = Thread(target=loading_icon, args=(stop_event,))
        thread.start()

        #sleep(5)

        # Set the stop event to stop the loading icon
        stop_event.set()

        # Wait for the thread to finish
        thread.join()

        print("Unable to detect an installed version.")
        print("Please enter your ACCESS KEY given to you. Note: this may only be used ONCE. If this is used, then you will not be able to transfer the game to another system, nor give the key to anyone else. It 'self-destructs', but gives you access.")
        inputted_key = input("Press right click to paste.\n\n>>> ")
        
        stop_event = Event()

        thread = Thread(target=loading_icon, args=(stop_event,))
        thread.start()

        logging.info(f"Requesting the server to validate {inputted_key}")
        code_response = get(f"https://awtd.ibaguette.com/keys/{inputted_key}/type.awtd")

        stop_event.set()
        thread.join()

        if code_response.status_code == 404:
            log_print(f"\nThis is an invalid key. Please try again.")
            awtd()
        else:
            log_print("\n404 not received.")
            log_print("Validating code")
            code_response = code_response.text
            response_lines = code_response.splitlines()

            download_url = response_lines[1]
            #response_line0 = {response_lines[0]}

            if response_lines[0] == "alpha":
                version = "ALPHA"
            if response_lines[0] == "beta":
                version = "BETA"
            if response_lines[0] == "stable":
                version = "STABLE"
            else:
                version = "Unknown"

            log_print(f"Validation completed! The version is {version}")

            if not path.exists(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache"):
                mkdir(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache")
            #if not path.exists(f"C:\\Program Files\\Draggie\\AWTD"):
            #    mkdir(f"C:\\Program Files\\Draggie\\AWTD")

            log_print(f"Validating Download URL.")
            download_url = b64decode(download_url)          # pass 1 of base64
            log_print(f"[b64decode#1] {download_url}")
            download_url = b64decode(download_url)          # pass 2 of base64
            log_print(f"[b64decode#2] {download_url}")

            # Retrieve the key from the URL
            response = get(download_url)                    # get sha512 key from pass 2
            log_print(f"[sha512pass2] {response.content}")
            key = (response.content).decode("utf-8")
            print(f"key = {key}")

            # Use the key to create a Fernet object
            fernet_key = response_lines[3].strip("b'").strip("'")
            fernet = Fernet(fernet_key)

            # Decrypt the message
            encrypted_message = f'{response_lines[2]}'      # decrypt line 3 of original url hit using sha512 key
            decrypted_message = fernet.decrypt(encrypted_message)
            log_print(f"[sha512decryptor] {decrypted_message}")
            #print("Decrypted message:", decrypted_message)

            download_url=str(decrypted_message).strip("b'").strip("'")

            log_print(f"The files are ready to be downloaded. Note that this will be downloaded temporarily to {DraggieTools_AppData_Directory}\\AWTD\\BuildCache. Input 1 to start downloading.")
            
            response = get(download_url, stream=True)

            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024  # 1 Kibibyte
            written = 0

            with open(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech.DraggiePAK", "wb") as f:
                for data in tqdm(response.iter_content(block_size), total=ceil(total_size // block_size), unit="KB", desc=download_url.split("/")[-1]):
                    written = written + len(data)
                    f.write(data)

            print("Successsfully downloaded the game's PAK file. Decrypting, unpacking and verifying contents...")
            try:
                with zipfile.ZipFile(f'{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech.DraggiePAK', 'r') as zip_ref:
                    zip_ref.extractall(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech", pwd=b"beans")
                    print("Successfully extracted all.")
                    Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech"')
            except Exception as e:
                log_print(e)
                awtd()

def choice1():
    if language == french:
        x = input("\n\n1) Installez ceci sur le bureau\n2) Installez ceci dans un répertoire personnalisé\n3) Créez un raccourci sur le bureau\n4) Actualises les mises à jour\n5) Changez la langue\n6) Regarde le code source\n7) Changer les paramètres de Fortnite\n8) Quitter\n\n>>> ")
    else: 
        language = english
        x = input("\n\n1) Install this to desktop\n2) Install this to custom directory\n3) Create shortcut on desktop\n4) Refresh updates\n5) Change language\n6) View source code\n7) Modify Fortnite Settings\n8) Quit\n\n>>> ")
    if x == "1":
        desktop_dir = pathlib.Path.home() / 'Desktop'
        if path.exists(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt"):
            with open (f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", 'r') as e:
                install_dir = e.read()
                if install_dir == str(desktop_dir):
                    print("Existing desktop file preference exists.")
                    print("The file will now no longer be located on the desktop.\n")
                    with open (f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
                        e.close()
                        choice1()

        start_anim_loading("Initialising.")
        #print(f"Current directory: {directory}")
        try:
            shutil.copyfile(directory, f"{desktop_dir}\\DraggieTools.exe")
            stop_anim_loading()
            print("\nCopied executable to the desktop. Note that if the file is deleted or an update is applied, this version will need to be updated again and this move be reapplied.")
            with open (f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
                e.write(f"{desktop_dir}")
            
        except FileNotFoundError:
            stop_anim_loading()
            print("\nRunning from PYTHON file. Not executable. This should print only in the development stage.")
            shutil.copyfile(f"{current_directory}\\DraggieTools.py", f"{desktop_dir}\\DraggieTools.py")
            print("I am very dumb. This will be improved later.")
        except shutil.SameFileError:
            stop_anim_loading()
            print("\nThis cannot be performed. The files are the same. Maybe it's already on the desktop!")
    if x == "2":
        try:
            e = r"C:\Program Files"
            c = r"C:\Program Files\Draggie"
            y = input(f"Enter the new directory. For example, '{e}'. \nNote that wherever you install me to, a new folder will be added called 'Draggie' This means that inputting the directory above will be {c}.\n\nRight click to paste!\n>>> ")
            print(f"Current directory: {directory}")
            try:
                mkdir(f"{y}\\Draggie\\")
            except Exception:
                pass
            shutil.copyfile(directory, f"{y}\\Draggie\\DraggieTools.exe")

            print(f"Successfully copied file to {y}\\Draggie\\DraggieTools.exe")
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Copied file from '{directory}' to desired directory {y}\\Draggie\\DraggieTools.exe")
        except Exception as e:
            print(f"An error occured. {e}")
            print("Please make sure that the file has not been renamed.")
            logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {traceback.format_exc()}")
            choice1()
    if x == "3":
        print("Feature disabled due to a bug.")
    if x == "4":
        check_for_update()
        choice1()
    if x == "5":
        change_language()
        choice1()
    if x == "6":
        view_source()
        choice1()
    if x == "7":
        fort_file_mod()
        choice1()
    if x == "8":
        print("\n\n\n\n\n\nQuitting...")
        sys.exit()
    if x == "9":
        autobrawlextractor()
        choice1()
    if x == "000":
        awtd()
    else:
        choice1()


def main():
    try:
        print(f"{language[6]} {current_directory}")
    except:
        print("First time run detected.")
        change_language()
        print(f"{language[6]} {current_directory}")
    logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: main() subroutine executed")
    the_funny = [f'{language[8]}', f'{language[9]}', f'{language[10]}']
    print(f"{random.choice(the_funny)}")
    print(language[7])

    choice1()



try:
    main()
except Exception as e:
    print(f"An unhandled exception was encountered.\nShort: {e}\n\nLong:\n{traceback.format_exc()}\n\nIt would be appreciated if you generate a logfile and DM it Draggie#3060. Thanks!\n")
    logging.error(traceback.format_exc())
    main()
