from subprocess import Popen
from requests import get
from datetime import datetime
from os import path, startfile, mkdir, environ, listdir, remove, makedirs
from time import monotonic, sleep, time
from uuid import uuid4
from tqdm import tqdm
from shutil import copyfile, SameFileError
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
import json
import hashlib
import re
from urllib.parse import urlsplit
#import libtorrent as lt

dev_mode = False

global build

build = 50
version = "0.7.0"
build_date = 1673381640

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


def tqdm_download(download_url, save_dir):
    response = get(download_url, stream=True)

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte
    written = 0

    with open(save_dir, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=ceil(total_size // block_size), unit="KB", desc=download_url.split("/")[-1]):
            written = written + len(data)
            f.write(data)


def log_print(text):
    """
    Logs and prints the text inputted. The logging level is INFO.
    """
    logging.info(text)
    print(text)

global language, language_chosen

#   The following are new line separated every 10 index entries
#   Remember - the index starts at 0 lol
english = ["Key error occured: ", "\n\nResorting to backup", "Downloading.", "done, average speed", "Checking for update...", "Downloading update...", "\nRunning from", "What would you like to do, my friend?", "Transfering sensitive files to The Criminal Network...", "Your computer is hacked by IP: 5.172.193.104 like OS: LINUX/KALI LINUX and location: RUSSIAN FEDERATION",
           r"Problem opening the application running at executable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Would you like to scan this PC?", "\nRunning version", "@", "build", "The server says the newest build is", "\nUpdate available!", "You are on version", "The newest version is build", "Press enter to download the update!", "This is index 20 (defined under **language[19]**), if you see this then report as error.",
           "Downloading and opening up the source Python file in Explorer. To view it, open it in Notepad or you could upload it to an IDE online.", "which is build", "Quitting...", "\nHey, you're running on a version newer than the public build. That means you're very special UwU\n"]# Index number 23 -   ENGLISH

french = ["Desolée", "\n\nRecourir à la sauvegarde", "Téléchargement.", "fini, avec vitesse moyenne", "Vérification de la mise à jour...", "Téléchargement de la mise à jour...", "\nEn cours d'exécution à", "Qu'est-ce que tu voudrais faire, mon ami(e) ?", "Transfert de fichiers sensibles vers le réseau criminel...", "Votre ordinateur est piraté par IP : 5.172.193.104 comme OS : LINUX/KALI LINUX et emplacement : FÉDÉRATION DE RUSSIE",
          r"Problème d'ouverture de l'application exécutée sur l'exécutable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Voulez-vous scanner ce PC ?", "\nVersion en cours d'exécution est : ", "@", "mini-version", "Le serveur dit que la nouvelle version est", "\nMise à jour disponsible !", "Vous êtes sur le mini-version", "Le mini-version nouvelle est", "Ecrivez entre pour la télécharger.", "This is index 20 in french (defined under **language[19]**), if you see this then report as error.",
          "Ouverture du fichier Python source dans l'Explorateur. Pour le voir, ouvre ceci dans Bloc-notes Windows ou vous pouvez le télécharger sur un IDE en ligne.", "qui est le mini-version", "En train de quitter...", "\nBonjour! Vous etes sur un mini-version plus récente que la version pour le public. Vous etes vraiment spécial, UwU\n"]# Index number 23 - FRENCH

"""
Here are the prints for directory determining.
"""

if dev_mode:
    #logging.basicConfig(filename=f'{DraggieTools_AppData_Directory}\\Logs\\{version}-{build}-{time()}.log', encoding='utf-8', level=logging.debug)
    #logging.debug(f'Established uplink at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print(f"\n\n*-* Beta Tester Prints *-*\n\nAppData Directory: {DraggieTools_AppData_Directory}")
    sleep(0.05)
    print(f"Executable location: {sys.executable}")
    sleep(0.05)
    print(f"application_path: {path.dirname(path.abspath(__file__))}\n\nDevmode is ON, therefore enhanced logging is active.\nThe log file is located in the Roaming AppData directory")
    sleep(0.05)

logging.basicConfig(filename=f'{DraggieTools_AppData_Directory}\\Logs\\{version}-{build}-{time()}.log', encoding='utf-8', level=logging.DEBUG)
logging.debug(f'Established uplink at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

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
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w+", encoding="UTF-8") as x:
                x.close()
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' cleared")
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w", encoding="UTF-8") as x:
                x.write("French")
                x.close()
            logging.info(f"({datetime.now()}.strftime('%Y-%m-%d %H:%M:%S'): File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' written with 'French'")
            language_chosen = "French"
        else:
            print("Language updated to English.")
            language = english
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w+", encoding="UTF-8") as x:
                x.close()
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' cleared")

            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w") as x:
                x.write("English")
                x.close()
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' written with 'English'")
            language_chosen = "English"
    if dev_mode:
        logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Language successfully changed to {language_chosen}")


if path.exists(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt"):
    try:
        with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", encoding="UTF-8") as x:
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
else:
    #print("the file son't exist")
    change_language()


current_directory = path.dirname(path.realpath(__file__))
if dev_mode:
    logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: variable currrent_directory assigned with value {current_directory}")


def download_update(current_build_version):
    try:
        if not path.exists(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds'):
            mkdir(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds')

        tqdm_download("https://github.com/Draggie306/DraggieTools/raw/main/dist/DraggieTools.exe", f"{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe")
                
        with open(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt", "w") as file:
            file.write(f"{sys.executable}")
            file.close()
        
    except KeyError as e:
        print(f"Some error occured: {e}\n\nResorting to fallback method. Preferences will not be usedm saving to default directory.")
        print(f"{language[0]}{e}{language[1]}")
        r = get('https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true')
        with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
            f.write(r)


def secret_menu():
    print("Welcome to the secret menu.")
    x = input("[1] = The.Batman.2022.1080p.WEBRip.x264.AAC5.1-[YTS.MX]\n[2] = Batman.The.Dark.Knight.2008.1080p.BluRay.x264.YIFY\n\n>>> ")

    index = get("https://awtd.ibaguette.com/index.beans").content
    lines = index.splitlines()
    
    if x == "1":
        download_url = str(lines[1]).strip("b'").strip("'")
    if x == "2":
        download_url = str(lines[0]).strip("b'").strip("'")
        

    response = get(download_url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte
    written = 0

    x = uuid4()
    
    with open(f"{DraggieTools_AppData_Directory}\\{x}.mp4", "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=ceil(total_size // block_size), unit="KB", desc=download_url.split("/")[-1]):
            written = written + len(data)
            f.write(data)
    
    Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\{x}.mp4"')


def torrent_downloader():
    return log_print("The torrent downloader will be enabled in a later version of the program.")
    # Create a session object
    s = lt.session()

    # Set the session settings
    s.listen_on(6881, 6891)

    # Create a torrent_info object from the .torrent file
    x = input("Where do you want to download the torrent to? Right click to paste.\n\n>>> ")

    # Add the magnet link to the session
    params = {
        'save_path': x,
        'storage_mode': lt.storage_mode_t(2),
        'paused': False,
        'auto_managed': True,
        'duplicate_is_error': True
    }

    link = input("Enter the magnet link.\n\n>>> ")

    th = s.add_magnet_uri(link, params)

    # Set the download and upload rate limits
    #th.set_download_limit(8 * 1024)
    #th.set_upload_limit(2 * 1024)

    # Start downloading the magnet link
    while (not th.is_seed()):
        s.wait_for_alert(1000)

    # Print the torrent status
    print(th.status())



def cleanup_files():
    dir_paths =[f"{DraggieTools_AppData_Directory}\\Logs", f"{DraggieTools_AppData_Directory}\\UpdatedBuilds", f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache", f"{DraggieTools_AppData_Directory}\\SourceCode",
     f"{Draggie_AppData_Directory}\\AutoBrawlExtractor\\DownloadedBuilds", ]

    # Get the current time in seconds
    current_time = time()
    file_amount = 0

    for dir in dir_paths:
        # Loop through all the files in the directory
        if path.exists(dir):
            log_print(f"[FileCleanup] Inspecting directory {dir}.")
            for file in listdir(dir):
                # Get the path of the file
                file_path = path.join(dir, file)
                # Check the modification time of the file
                mod_time = path.getmtime(file_path)
                # Calculate the difference in seconds between the current time and the modification time
                time_diff = current_time - mod_time
                # Convert the difference in seconds to days
                time_diff_days = time_diff / (60 * 60 * 24)
                # If the file is older than 7 days
                if time_diff_days > 7:
                    # Delete the file
                    remove(file_path)
                    log_print(f"[FileCleanup] Cleaned up file at {file_path}")
                    file_amount += 1
        else:
            logging.info("Skipped directory as it doesn't exist.")
        sleep(0.2)
    
    log_print(f"[FileCleanup] Purged {file_amount} file(s).")
    

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
        Popen(f'explorer /select,"{fort_ini_directory}"')
    main()

def check_for_update():
    try:
        stop_event = Event()
        thread = Thread(target=loading_icon, args=(stop_event, language[4]))
        thread.start()
    except Exception as e:
        stop_event.set()
        thread.join()
        change_language()
        check_for_update()
    try:
        if path.isfile(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt"): # OverwriteOldVersion
            logging.debug(f"[OverwriteOldVersion] {Draggie_AppData_Directory}\\OldExecutableDir.txt exists!")
            with open(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt", "r") as file:
                old_sys_exe = file.read()
                file.close()
            if old_sys_exe == str(sys.executable):
                logging.error(f"[WARNING] The update cannot be applied to the current directory as you are running the file in the same place! Please download the update and wait for it to be closed.")
            else:
                logging.info(f"[OverwriteOldVersion] Removing OldExeDir.txt")
                remove(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt")
                logging.info(f"[OverwriteOldVersion] Removing old exe")
                remove(old_sys_exe)
                logging.info(f"[OverwriteOldVersion] Copying current exe to old sys exe")
                copyfile(str(sys.executable), old_sys_exe)
                logging.info(f"[OverwriteOldVersion] Copying current exe ({sys.executable}) to old sys exe ({old_sys_exe})")
        else:
            logging.debug(f"[OverwriteOldVersion] OldExeFile does not exist!")
    except Exception as e:
        log_print(f"Unable to overwrite older version. {e}")


    current_build_version = int((get('https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt')).text)
    stop_event.set()
    thread.join()
    if build < current_build_version:
        release_notes = str((get(f"https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Release%20Notes/release_notes_v{current_build_version}.txt")).text)
        log_print(f"\n{language[15]} {language[16]} {version} {language[21]} {build}.\n{language[17]} {current_build_version}. {language[18]}\n\n")
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
        log_print("Update downloaded. Launching new version...")
        if desktop_install_path == False:
            startfile(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe')
        else:
            desktop_dir = pathlib.Path.home() / 'Desktop'
            startfile(f'{desktop_dir}\\DraggieTools-{current_build_version}.exe')
        sys.exit()

    if current_build_version < build:
        print(language[23])
    else:
        print(f"{language[11]} {version} - {language[13]} {build} - {language[12]} {datetime.fromtimestamp(build_date).strftime('%Y-%m-%d %H:%M:%S')}. {language[14]} {current_build_version}.")


check_for_update()

def maniupulate_brawl_file(dir, brawl_versioning):
    brawl_versioning = str(brawl_versioning)
    print(f"Allowing manipulation of brawl file. [{brawl_versioning}]")
    archive = zipfile.ZipFile(dir, 'r')
    fingerprint_json = str(archive.read('Payload/Brawl Stars.app/res/fingerprint.json'), encoding="UTF-8")
    fingerprint_json = json.loads(fingerprint_json)
    x = input ("Select options:\n\n1) Grab fingerprint hash\n2) Compare music to old version and extract\n3) Compare all files\n4) Download all background music files\n5) Download all with custom string\n6) Open brawl downloaded file directory\n0) Go back   \n\n>>> ")
    if x == "1":
        print(f"Read the following information from file\nsha: {fingerprint_json['sha']}\nAmount of files: {len(fingerprint_json['files'])}")
    if x == "4":
        fingerprint_json = str(archive.read('Payload/Brawl Stars.app/res/fingerprint.json'), encoding="UTF-8")
        fingerprint_json = json.loads(fingerprint_json)
        for item in fingerprint_json['files']:
            if 'music/background' in item['file']:
                print(f"File: {item}")
                # The file field contains 'music/background'
                print(f'Found "music/background" in file: {item["file"]}')
                # Split the file field on the '\' character and take the first two elements
                dir_path = item['file'].split('/')[:2]

                # Join the elements back together with the '\' character
                dir_path = '\\'.join(dir_path)

                # Create the directory and its parent directories if they do not already exist
                makedirs(f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_versioning}\\{dir_path}', exist_ok=True)
                tqdm_download(f'https://game-assets.brawlstarsgame.com/{fingerprint_json["sha"]}/{item["file"]}', f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_versioning}\\{item["file"]}')
            else:
                #print(f"Not in file {item}")
                pass
        print("ok")
    if x == "5":
        search_term = input("Enter the term to search all files for and it will be downloaded:\n\n>>> ")
        x = input(f"Enter 1 to search through ALL archives located in the DownloadedBuilds directory\nHit enter and it will be searched for in current version: {fingerprint_json['version']}\n\n>>> ")
        file_cycle = True if x == "1" else False
        hits = 0
        files = 0
        archives = 0
        if file_cycle:
            available_archives = listdir(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
            for file in available_archives:
                if file.lower().endswith(".ipa") or file.lower().endswith(".zip"):
                    archive = zipfile.ZipFile(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds\\{file}", 'r')
                    archives += 1
                    new_fingerprint_json = str(archive.read('Payload/Brawl Stars.app/res/fingerprint.json'), encoding="UTF-8")
                    new_fingerprint_json = json.loads(new_fingerprint_json)
                    for item in fingerprint_json['files']:
                        files += 1
                        if search_term in item['file']:
                            print(f"File: {item}")
                            # The file field contains search_term
                            print(f'Found "{search_term}" in file: {item["file"]}')
                            hits += 1

                            # Split the file path on the '\' character and take all elements except the last one
                            dir_path = item["file"].split('/')[:-1]

                            # Join the elements back together with the '\' character
                            dir_path = '\\'.join(dir_path)

                            # Create the directory and its parent directories if they do not already exist
                            directory_to_save_to = f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_versioning}\\{dir_path}'
                            makedirs(directory_to_save_to, exist_ok=True)
                            tqdm_download(f'https://game-assets.brawlstarsgame.com/{new_fingerprint_json["sha"]}/{item["file"]}', f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_versioning}\\{item["file"]}')
                        else:
                            print(f"Unable to find the search term {search_term} in v{new_fingerprint_json['version']}: {item}")
                else:
                    print(f"Skipping file {file} as it does not have a supported extension or it will not work.")
        else:
            archives += 1
            new_fingerprint_json = str(archive.read('Payload/Brawl Stars.app/res/fingerprint.json'), encoding="UTF-8")
            new_fingerprint_json = json.loads(new_fingerprint_json)
            for item in fingerprint_json['files']:
                files += 1
                if search_term in item['file']:
                    print(f"File: {item}")
                    # The file field contains search_term
                    print(f'Found "{search_term}" in file: {item["file"]}')
                    hits += 1

                    # Split the file path on the '\' character and take all elements except the last one
                    dir_path = item["file"].split('/')[:-1]

                    # Join the elements back together with the '\' character
                    dir_path = '\\'.join(dir_path)

                    # Create the directory and its parent directories if they do not already exist
                    directory_to_save_to = f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_versioning}\\{dir_path}'
                    makedirs(directory_to_save_to, exist_ok=True)
                    tqdm_download(f'https://game-assets.brawlstarsgame.com/{new_fingerprint_json["sha"]}/{item["file"]}', f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_versioning}\\{item["file"]}')
                else:
                    print(f"Unable to find the search term {search_term} in v{new_fingerprint_json['version']}: {item}")
        print(f"Found {hits} hits across {files} total files in {archives} available archives.")
    if x == "6":
        Popen(f'explorer /select,"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_versioning}"')
    else:
        autobrawlextractor()

    maniupulate_brawl_file(dir, brawl_versioning)


def autobrawlextractor():
    Brawl_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor")
    Downloaded_Builds_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
    if not path.exists(f"{Brawl_AppData_Directory}\\Versions"):
        mkdir(f"{Brawl_AppData_Directory}\\Versions")
    def init_filetype(dir):
        """
        Initialises and checks the validity of the archive version provided. If the file provided is not valid, then the program will exit.
        """
        try:
            archive = zipfile.ZipFile(dir, 'r')
            try:
                string = str(archive.read('Payload/Brawl Stars.app/res/version.number'), encoding="UTF-8")
                store_type = "IPA"

                # Split the string into a list of lines
                lines = string.split('\n')

                # Iterate through the lines and extract the version and build values
                brawl_version = None
                brawl_build = None
                for line in lines:
                    if line.startswith('version='):
                        brawl_version = line.split('=')[1]
                    elif line.startswith('build='):
                        brawl_build = line.split('=')[1]
                print(f"Parsed build from file: {brawl_version}.{brawl_build}")
                if not path.exists(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{brawl_version}.{brawl_build}"):
                    mkdir(f"{Brawl_AppData_Directory}\\Versions\\{brawl_version}.{brawl_build}")
                maniupulate_brawl_file(dir, f"{brawl_version}.{brawl_build}")
                
            except KeyError:
                archive.read('classes.dex')
                store_type = "APK"
            if store_type:
                print(f"Detected Verson: {store_type}")
            else:
                print("Unknown version type please use the other OS' version")
                sleep(4)
        except Exception as e:
            print(f"Error occured: {e}")

    def number_one():
        print(r"Enter the location of your Brawl Stars archive file, e.g D:\Downloads\brawl.ipa. IPA files are preferred.")
        print("Use an .ipa file or .apk file (for iOS and Android decices, respectively). Must not be unzipped.")
        print("Alternatively, press 1 to search for all downloadable versions.\nType 0 to go back")

        amount_of_files = 0

        for i in listdir(Downloaded_Builds_AppData_Directory):
            amount_of_files = amount_of_files + 1

        if amount_of_files >= 1:
            print(f"\nYou have {amount_of_files} files already downloaded inside the DownloadedBuilds folder, [Enter] to go there.")

        location = input("\n>>> ")

        if location == "1":
            print("Fetching a list of all trusted versions from GitHub...")
            git_brawl_builds = get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/brawl_builds.txt")
            git_brawl_builds = git_brawl_builds.text
            urls = git_brawl_builds.splitlines()
            version_names = [re.search(r"laser-(\d+\.\d+)", url).group(1) for url in urls]
            for i, version_name in enumerate(version_names):
                print(f"[{i + 1}]   {version_name}")
            selected_version = (input("\nPlease select a version to download: (or '*' to download them all).\n\n>>> "))
            if selected_version == "*":
                print("You have chosen to download ALL builds. If you would like to stop it, you will need to press Ctrl+C.")
                amount = len(urls)
                downloaded_amount = 0
                for line in urls:
                    source = line.strip().split(' (')
                    source = source[0].strip(')')
                    real_file_name = path.basename(urlsplit(line).path)
                    if "Baguette Brigaders" in source:
                        source = (f"[VERIFIED] {source}")
                    print(f"Downloading the build {real_file_name}. This file comes from {source}")
                    tqdm_download(line, f"{Downloaded_Builds_AppData_Directory}\\{real_file_name}")
                    downloaded_amount += 1
                    print(f"\nSuccessfully downloaded build {real_file_name}. It is located at: {Downloaded_Builds_AppData_Directory}\\{real_file_name}\nOverall progress: {downloaded_amount}/{amount} ({round(downloaded_amount/amount)}%)")
                print(f"{downloaded_amount} builds have been saved!\n\n")
                number_one()

            selected_url = urls[int(selected_version) - 1]
            real_file_name = path.basename(urlsplit(selected_url).path)

            tqdm_download(selected_url, f"{Downloaded_Builds_AppData_Directory}\\{real_file_name}")
            print(f"\nDownloaded build {real_file_name}\nIt is located at: {Downloaded_Builds_AppData_Directory}\\{real_file_name}\n")
            number_one()

        if location == "":
            files = []
            f = 0
            for file in listdir(Downloaded_Builds_AppData_Directory):
                files.append(file)
            for i in files:
                print(f"[{f}] {i}")
                f += 1
            x = input("\nChoose file\n\n>>> ")
            try:
                init_filetype(f"{Downloaded_Builds_AppData_Directory}\\{files[int(x)]}")
            except ValueError:
                # Initialize variables to store the highest version number and corresponding filename
                highest_version = 0.0
                highest_version_file = ""
                # Iterate through each file in the list
                for f in files:
                    # Use regular expression to search for a string of digits with a dot in between (e.g., "x.x")
                    match = re.search(r"(\d+\.\d+)", f)
                    # If a match is found (i.e., if the file contains a version number of the format "x.x")
                    if match:
                        # Extract the version number as a float
                        archive_version = float(match.group(1))
                        # Compare the version number to the current highest version number (just iterating over the list to find the maximum value)
                        if archive_version > highest_version:
                            highest_version = archive_version
                            highest_version_file = f

                print(f"Error occured! Resorting to regex expression to find the most recent version, which appears to be in file {highest_version_file}")
                init_filetype(f"{Downloaded_Builds_AppData_Directory}\\{highest_version_file}")
            
        if location == "0":
            main()
        else:
            init_filetype(location)
    number_one()



def awtd():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-*-*-*-*-*-*-*-*-*-*-*-* Welcome to the Advanced Water Tech Demo Secret Area! *-*-*-*-*-*-*-*-*-*-*-*-\n")
    #print("Searching for installed versions...")
    if not path.exists(f"{DraggieTools_AppData_Directory}\\AWTD"):
        mkdir(f"{DraggieTools_AppData_Directory}\\AWTD")
    if path.exists(f"{DraggieTools_AppData_Directory}\\AWTD\\Config"):
        print("Found a config file.")
    else:
        # Create a stop event
        stop_event = Event()

        # Start the loading icon in a separate thread
        thread = Thread(target=loading_icon, args=(stop_event, "Checking for an installed version..."))
        thread.start()

        sleep(random.randint(1,3))

        # Set the stop event to stop the loading icon
        stop_event.set()

        # Wait for the thread to finish
        thread.join()

        print("\nUnable to detect an installed version.")
        print("Please enter your ACCESS KEY given to you.\nNote: this may only be used ONCE. It 'self-destructs' when entered.\nUpdates will still be applied automatically with a valid key!")
        inputted_key = input("Press right click to paste.\n\n>>> ")
        
        stop_event = Event()

        thread = Thread(target=loading_icon, args=(stop_event, f"Requesting the server to validate {inputted_key}"))
        thread.start()

        logging.info(f"Requesting the server to validate {inputted_key}")
        code_response = get(f"https://awtd.ibaguette.com/keys/{inputted_key}/type.awtd")

        stop_event.set()
        thread.join()

        if code_response.status_code == 404:
            log_print(f"\nThis is an invalid key. Please try again.")
            sleep(1.5)
            awtd()
        else:
            log_print("\n404 not received.")
            log_print("Reading and validating code")

            # Open the JSON file
            raw_version_info = get(f"https://awtd.ibaguette.com/staticKeys/a5e81fe8_4e21_4d58_a0db_ea0c25ee9086").content
            # Get the raw version info from the specified URL
            # The content is returned as bytes, so it needs to be converted to a string
            raw_version_info = str(raw_version_info).strip('b"b').strip("'")
            # Base64 decode the version info
            raw_version_info = b64decode(raw_version_info)
            
            # Load the JSON data into a Python object
            versions = json.loads(raw_version_info)
            # Get the current alpha, beta, and release versions
            current_alpha_version = versions['alpha']
            current_beta_version = versions['beta']
            current_release_version = versions['stable']

            # Get the text of the response and split it into lines
            code_response = code_response.text
            response_lines = code_response.splitlines()

            # Get the download URL from the second line of the response
            download_url = response_lines[1]
            # Get the first line of the response and convert it to a string
            response_line_0 = str(response_lines[0])

            # Check the first line of the response and set the branch and current version accordingly
            if response_line_0 == 'alpha':
                branch = "ALPHA"
                current_version = current_alpha_version
            elif response_line_0 == "beta":
                branch = "BETA"
                current_version = current_beta_version
            elif response_line_0 == "stable":
                branch = "STABLE"
                current_version = current_release_version
            else:
                branch = "Unknown"
                current_version = "Unknown"

            # Print a message indicating that the validation has completed and the branch has been determined
            log_print(f"[AWTD] Validation completed! The branch is {branch}.")
            log_print(f"Current Version to Download: {current_version}")

            # If the BuildCache directory does not exist, create it
            if not path.exists(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache"):
                mkdir(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache")

            # Print a message indicating that the download URL is being validated
            log_print(f"Validating Download URL.")
            # Base64 decode the download URL (pass 1)
            download_url = b64decode(download_url)
            # Print the result of the first base64 decoding
            log_print(f"[b64decode#1] [DECRYPT/thread1] binaryFCalc:{download_url}")
            # Base64 decode the download URL again (pass 2)
            download_url = b64decode(download_url)
            # Print the result of the second base64 decoding
            log_print(f"[b64decode#2] [STATIC KEY VALID] binaryValue:{download_url}")

            # Retrieve the key from the URL
            response = get(download_url)                    # make request to download_url and store the response in response
            log_print(f"[sha512pass2] {response.content}")
            key = (response.content).decode("utf-8")        # decode the content of response from bytes to a string and store it in key
            log_print(f"[sha512decryptor] [KeyThreadingInfo] {key}")

            # Use the key to create a Fernet object
            fernet_key = response_lines[3].strip("b'").strip("'")  # remove leading and trailing characters from fourth line of original response and store the result in fernet_key
            fernet = Fernet(fernet_key)                            # create a Fernet object using fernet_key as the key

            # Decrypt the message
            encrypted_message = f'{response_lines[2]}'      # store the third line of the original response in encrypted_message
            decrypted_message = fernet.decrypt(encrypted_message)   # decrypt encrypted_message using the Fernet object and store the result in decrypted_message
            #log_print(f"[sha512decryptor] {decrypted_message}")
            log_print("Successfully decrypted and resolved endpoint download url.")
            #print("Decrypted message:", decrypted_message)

            download_url=str(decrypted_message).strip("b'").strip("'")  # remove leading and trailing characters from decrypted_message and store the result in download_url


            log_print(f"\n\nThe files are ready to be downloaded. Note that this will be downloaded temporarily to {DraggieTools_AppData_Directory}\\AWTD\\BuildCache.\nInput 1 to start downloading.")
            
            x = input("\n\n>>> ")
            logging.info(f"Input: {x}")

            if x != "1":
                main()
            
            response = get(download_url, stream=True)

            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024  # 1 Kibibyte
            written = 0

            with open(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech.DraggiePAK", "wb") as f:
                for data in tqdm(response.iter_content(block_size), total=ceil(total_size // block_size), unit="KB", desc=download_url.split("/")[-1]):
                    written = written + len(data)
                    f.write(data)

            start_anim_loading("Successsfully downloaded the game's PAK file. Decrypting, unpacking and verifying contents...")

            try:
                with zipfile.ZipFile(f'{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech.DraggiePAK', 'r') as zip_ref:
                    zip_ref.extractall(f"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech", pwd=b"beans")
                    stop_anim_loading()
                    # Loop through the files in the folder

                    for filename in listdir(f'{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech'):
                        # Compute the full path of the file
                        filepath = path.join(f'{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech', filename)

                        # Open the file in binary mode
                        with open(filepath, 'rb') as f:
                            # Read the contents of the file
                            data = f.read()

                            # Compute the SHA1 hash of the file
                            sha1 = hashlib.sha1(data).hexdigest()

                            # Print the filename and hash
                            log_print(f'[HashVerification] Hash of "{filename}": {sha1}')


                    log_print("\nSuccessfully extracted all.")
                    Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\AWTD\\BuildCache\\Watertech"')
                    main()
            except Exception as e:
                log_print(e)
                awtd()

def dev_menu():
    global build
    x = input("\n\n1) Set build\n2) Set version\nSet unix time\n\n>>> ")
    if x == "1":
        build = int(input("Enter the build number: "))
        choice1()
    else:
        choice1()


def choice1():
    global language
    if language == french:
        x = input("\n\n1) Installer cela sur le bureau\n2) Installer cela dans un répertoire personnalisé\n3) Actualiser les mises à jour\n4) Changer de langue\n5) Afficher le code source\n6) Modifier les paramètres de Fortnite\n7) AWTD\n8) Téléchargeur de torrent\n9) AutoBrawlExtractor\n0) Quitter\n\n>>> ")
    else: 
        language = english
        x = input("\n\n1) Install this to desktop\n2) Install this to custom directory\n3) Refresh updates\n4) Change language\n5) View source code\n6) Modify Fortnite Settings\n7) AWTD\n8) Torrent Downloader\n9) AutoBrawlExtractor\n0) Quit\n\n>>> ")
    if x == "0":
        print("\n\n\n\n\n\nQuitting...")
        sys.exit()
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
            copyfile(directory, f"{desktop_dir}\\DraggieTools.exe")
            stop_anim_loading()
            print("\nCopied executable to the desktop. Note that if the file is deleted or an update is applied, this version will need to be updated again and this move be reapplied.")
            with open (f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
                e.write(f"{desktop_dir}")
            
        except FileNotFoundError:
            stop_anim_loading()
            print("\nRunning from PYTHON file. Not executable. This should print only in the development stage.")
            copyfile(f"{current_directory}\\DraggieTools.py", f"{desktop_dir}\\DraggieTools.py")
            print("I am very dumb. This will be improved later.")
        except SameFileError:
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
            copyfile(directory, f"{y}\\Draggie\\DraggieTools.exe")

            print(f"Successfully copied file to {y}\\Draggie\\DraggieTools.exe")
            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Copied file from '{directory}' to desired directory {y}\\Draggie\\DraggieTools.exe")
        except Exception as e:
            print(f"An error occured. {e}")
            print("Please make sure that the file has not been renamed.")
            logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {traceback.format_exc()}")
            choice1()
    if x == "3":
        check_for_update()
    if x == "4":
        change_language()
    if x == "5":
        view_source()
    if x == "6":
        fort_file_mod()
    if x == "7":
        awtd()
    if x == "8":
        torrent_downloader()
    if x == "9":
        autobrawlextractor()
    if x == "10":
        cleanup_files()
    if x == "69":
        print(";)")
        secret_menu()
    if x == "dev":
        dev_menu()

    else:
        choice1()

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
