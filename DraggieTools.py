print("Loading modules...")

import sys
import time

start_time = time.time()


def print_loading_message(module_name):
    sys.stdout.write(f"Loading module {module_name}...                  ")
    sys.stdout.flush()
    sys.stdout.write("\r")
    sys.stdout.flush()


import os

# import pyi_splash

print_loading_message("subprocess.Popen")
from subprocess import Popen

print_loading_message("requests.get, requests.post")
from requests import get, post

print_loading_message("datetime.datetime")
from datetime import datetime

print_loading_message("os.path (+ 4 more)")
from os import environ, listdir, makedirs, mkdir, path, remove, startfile

print_loading_message("time.sleep, time.time, time.perf_counter")
from time import perf_counter, sleep, time

print_loading_message("uuid.uuid4")
import uuid
from uuid import uuid4

print_loading_message("tqdm.tqdm")
from tqdm import tqdm

print_loading_message("shutil.copyfile, shutil.SameFileError")
from shutil import SameFileError, copyfile

print_loading_message("pathlib")
import pathlib

print_loading_message("typing.Optional")
from typing import Optional

print_loading_message("random")
import random

print_loading_message("traceback")
import traceback

print_loading_message("logging")
import logging

print_loading_message("zipfile")
import zipfile

print_loading_message("threading.Event, threading.Thread")
from threading import Event, Thread
import threading

print_loading_message("base64")
from base64 import b64decode

print_loading_message("math.ceil")
from math import ceil

print_loading_message("cryptography.fernet.Fernet")
from cryptography.fernet import Fernet

print_loading_message("json")
import json

print_loading_message("hashlib")
import hashlib

print_loading_message("re")
import re

print_loading_message("lzma")
import lzma

print_loading_message("urllib.parse.urlsplit")
from urllib.parse import urlsplit

print_loading_message("getpass")
import getpass

print_loading_message("concurrent.futures")
import concurrent.futures as cf

print_loading_message("yt_dlp")
import yt_dlp as youtube_dl

print_loading_message("pypresence.Presence")
from pypresence import Presence

print_loading_message("asyncio")
import asyncio

print_loading_message("shutil")
import shutil

# import moviepy.editor
print_loading_message("nest_asyncio")
import nest_asyncio

nest_asyncio.apply()


from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

# if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
#    pyi_splash.update_text('UI Loaded ...')
#    pyi_splash.close()

end_time = time()

elapsed_time = end_time - start_time

sys.stdout.write("\r")
sys.stdout.flush()
print(f"All modules loaded! Took {round(elapsed_time, 7)}s      ")

dev_mode = False

global build, client

build = 67
version = "0.8.5"
build_date = 1685353104
username = getpass.getuser()
current_exe_path = sys.executable

environ_dir = environ['USERPROFILE']

start_time = time()

client = None

phrases = {
    'english': {
        'menu_options': '\n\n[0] Quit\n[1] Install to desktop\n[2] Install to custom directory\n[3] Refresh updates\n[4] Change language\n[5] View source code\n[6] Modify Fortnite Settings\n[7] AWTD\n[8] Torrent Downloader\n[9] AutoBrawlExtractor\n[10] Clean Up Files\n[11] Parse Discord StoreChannel\n[12] Reload Discord RPC\n[13] Install DraggieClient\n[14] YouTube Downloader\n[15] Bank Files Extractor\n[16] VideoMaker\n[17] VBS Script Launcher\n\n[dev] Open Developer Menu\n[log] Upload logs  \n\n>>> ',
        'key_error': 'Key error occurred: ',
        'backup': '\n\nResorting to backup',
        'downloading': 'Downloading.',
        'done_speed': 'done, average speed',
        'check_update': 'Checking for update...',
        'download_update': 'Downloading update...',
        'run_from': '\nRunning from',
        'menu_prompt': 'What would you like to do, my friend?',
        'server_says': 'The server says the newest build is',
        'running_version': '\nRunning version',
        'at': '@',
        'build': 'build',
        'update_available': '\nUpdate available!',
        'on_version': 'You are on version',
        'newest_version_build': 'The newest version is build',
        'press_enter_update': 'Press enter to download the update!',
        'downloading_opening': 'Downloading and opening up the source Python file in Explorer. To view it, open it in Notepad or you could upload it to an IDE online.',
        'which_build': 'which is build',
        'quitting': 'Quitting...',
        'newer_version': '\n\nHey, you\'re running on a version newer than the public build. That means you\'re very special UwU\n',
        'secret_menu': 'Welcome to the secret menu.',
        'skipping_file': 'Skipping file',
        'unsupported_extension': 'as it does not have a supported extension or it will not work.',
        'log_notice': 'Would you like to upload log files before deleting them? (Y/N)',
        'interacting_allowed': "Interacting allowed for",
        'file': 'file.',
        'input_threads': "Input the amount of threads to use to download files with:\n\n>>> ",
        'select_options': "Select options:\n\n1) See basic info and fingerprint hash\n2) Compare music to old version and extract additions\n3) Compare files to another version\n4) Download all background music files\n5) Download all files containing a string\n6) Open this archive's downloaded file folder\n0) Go back   \n\n>>> ",
        'read_info_from_file': "Read the following information from file",
        'amount_of_files': "Amount of files",
        'fingerprint_hash': "Fingerprint hash",
        'found_music_in_file': 'Found "music/background" in file: ',
        'search_term_input': "Enter the term to search all files for and it will be downloaded:\n\n>>> ",
        'search_all_archives': "[1] to search through ALL archives located in the DownloadedBuilds directory. Only select if you want to download multiple versions' assets.\n[Enter] Search for",
        "only_in_current_version": "only in current version: ",
        'searching_archive': "Searching archive: ",
        'found': '\nFound',
        "in_file": 'in file:',           # {phrases[language]['']}
        'not_downloading_exists': 'Not downloading the file due to it already being present. Please remove ',
        'not_downloading_exists_2': ' if you want it to be redownloaded.',
        'unsupported_extension_1': "Skipping file",
        'unsupported_extension_2': 'as it does not have a supported extension or it will not work.',
        'matching_files': 'matching files across',
        "total_files_in": 'total files in',
        "available_archives": 'available archives.',
        "S_as": 'Extracting Supercell game assets',
        "S_as_1": "files searched, ",
        "S_as_2": "downloaded.",
        "files_already_exist": 'files already exist.\n',
        'read_asset': "Read the following asset version from APK file: ",
        'apk_name_warning': "[IMPORTANT] As this is an APK file, the name has been set to default to Brawl Stars. ",
        'detected_architecture': "Detected Architecture: ",
        'unresolved_error': "\n[WARNING] An error has occured which cannot be resolved: ",
        'encrypted_csv_path_input': "Enter the path to the encoded file:\n\n>>> ",
        'processing': "Processing...",
        'unpacked_file_success': "\n\nSuccessfully unpacked the file. You can now view it at ",
        'supercell_archive_location': r"Enter the location of your Supercell archive file, e.g D:\Downloads\brawl.ipa. IPA files are preferred.",
        'select_option_supercell_archive': "\nUse an .ipa file or .apk file (for iOS and Android decices, respectively). Must not be unzipped.\n[0] Go back.\n[1] Search for all downloadable versions.\n[2] Decode a file with LZMA.",
        'select_downloaded_file': "\n[Enter] Select one of the",
        'select_downloaded_file_2': 'downloaded files.',
        'fetching_trusted_versions': "Fetching a list of all trusted versions from GitHub...",
        'download_all_builds_warning': "You have chosen to download ALL builds. If you would like to stop it, you will need to press Ctrl+C.",
        'downloading_build': "Downloading the build",
        'cumms_from': "comes from",
        'download_new_files': "Would you like to download new files?",
    },
    'french': {
        'key_error': 'Erreur de clé: ',
        'backup': '\n\nRecourir à la sauvegarde',
        'downloading': 'Téléchargement.',
        'done_speed': 'terminé, vitesse moyenne',
        'check_update': 'Vérification des mises à jour...',
        'download_update': 'Téléchargement de la mise à jour...',
        'run_from': '\nLancement à partir de',
        'menu_prompt': 'Que souhaitez-vous faire, mon ami?',
        'server_says': 'Le serveur indique que la dernière version est',
        'running_version': '\nVersion en cours d\'exécution',
        'at': '@',
        'build': 'build',
        'update_available': '\nMise à jour disponible !',
        'on_version': 'Vous êtes sur la version',
        'newest_version_build': 'La dernière version est la build',
        'press_enter_update': 'Appuyez sur Entrée pour télécharger la mise à jour !',
        'downloading_opening': 'Téléchargement et ouverture du fichier Python source dans Windows Explorer. Pour le voir, ouvrez-le dans le Bloc-notes ou vous pouvez le télécharger dans une IDE en ligne.',
        'which_build': 'qui est la build',
        'quitting': 'Quitter...',
        'newer_version': '\nHé, vous utilisez une version plus récente que la version publique. Cela signifie que vous êtes très spécial, selon moi.\n',
        'secret_menu': 'Bienvenue dans le menu secret.',
        'skipping_file': 'Ignorer le fichier',
        'unsupported_extension': 'car il n\'a pas d\'extension prise en charge ou ne fonctionnera pas.',
        'log_notice': 'Voulez-vous téléverser les fichiers avant de les supprimer ? (O/N)',
        'menu_options': '\n\n[0] Quitter\n[1] Installer sur le bureau\n[2] Installer dans un répertoire personnalisé\n[3] Actualiser les mises à jour\n[4] Changer de langue\n[5] Voir le code source\n[6] Modifier les paramètres de Fortnite\n[7] AWTD\n[8] Téléchargeur de torrents\n[9] Extracteur AutoBrawl\n\n>>> ',
        'download_new_files': "Voulez-vous télécharger de nouveaux fichiers ?",
    }
}


def l10n_text(key: str) -> str:
    try:
        if not language:
            value = key
        else:
            value = phrases[language][f'{key}']
        return value
    except Exception as e:
        log_print(f"[LocalisedText] Error occurred when getting localised string: {e}\n{traceback.format_exc()}", 4)
        return key


funny_messages = [
    r"Problem opening the application running at executable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Would you like to scan this PC?",
    "Please enter your credit card number for a free trial",
    "Transferring sensitive files to The Criminal Network...",
    "Your computer is hacked by IP: 5.172.193.104 like OS: LINUX/KALI LINUX and location: RUSSIAN FEDERATION",
    "Your internet connection will be disconnected in 10 seconds. Please panic!",
    "You have just won a lifetime supply of spam emails. Congratulations!",
    "The NSA is watching you. No, seriously. They're right behind you",
    "Insufficient funds. Please go rob a bank and try again",
    "Your computer has been upgraded to Windows 98. Enjoy the nostalgia!",
    "Warning: this program has been known to cause spontaneous dancing",
    "Your hard drive is full. Please delete all your files, including the ones you actually need",
    "Error: your keyboard has been replaced with a typewriter. Good luck!",
    "Your computer has been infected with a virus. The cure? A subscription to our premium antivirus software!",
    "Please wait while we install a new operating system... DOS!",
    "Error: user brain not found. Please insert coffee and try again",
    "Congratulations, you have been selected to participate in our new program: 'Extreme Keyboard Smashing'",
    "Your computer has been infected with a virus. The cure? A subscription to our premium antivirus software!",
    "Your computer has been selected to be the host of the next big cyber attack. Please prepare for the FBI to knock on your door",
    "Your keyboard has been upgraded to a potato. You're welcome!",
    "The matrix has you. But don't worry, we have a pill for that.",
    "Insufficient disk space. Please delete all your selfies and try again",
    "Your computer is now powered by hamsters on wheels. Please do not feed them",
    "Congratulations! You have just won a free trip to the blue screen of death",
    "Warning: this program has been known to cause side effects such as uncontrollable laughter",
    "Your computer is infected with a Trojan horse. Don't worry, we've got a Trojan condom for that!",
    "Your computer is running low on RAM. Please download more RAM at www.downloadmoreram.com"
]


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
    # uuid_gen = "test1234"
    DraggieTools_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie{uuid_gen}\\DraggieTools")
    Draggie_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie{uuid_gen}")

    if not path.exists(Draggie_AppData_Directory):
        mkdir(f"{environ_dir}\\AppData\\Roaming\\Draggie{uuid_gen}\\")
    if not path.exists(DraggieTools_AppData_Directory):
        mkdir(DraggieTools_AppData_Directory)

if not path.exists(f"{DraggieTools_AppData_Directory}\\Logs"):
    mkdir(f"{DraggieTools_AppData_Directory}\\Logs")
    print(f"[MainInit] Made DraggieTools_AppData_Directory Logs: {DraggieTools_AppData_Directory}\\Logs", 2)

if not path.exists(DraggieTools_AppData_Directory):
    mkdir(DraggieTools_AppData_Directory)
    print(f"[MainInit] Made DraggieTools_AppData_Directory: {DraggieTools_AppData_Directory}", 2)

if not path.exists(f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache"):
    mkdir(f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache")
    print(f"[MainInit] Made UpdatedBuildsCache Directory: {DraggieTools_AppData_Directory}\\UpdatedBuildsCache", 2)

if not path.exists(f"{DraggieTools_AppData_Directory}\\SourceCode"):
    mkdir(f"{DraggieTools_AppData_Directory}\\SourceCode")
    print(f"[MainInit] Made SourceCode Directory: {DraggieTools_AppData_Directory}\\SourceCode", 2)


print("Loading functions...")


async def load_presence():
    discord_client_id = 1076873298501173269
    try:
        # Create a new instance of the client
        global client
        # Create a new instance of the client
        client = Presence(discord_client_id)

        # Connect to the Discord API
        client.connect()

        # Set your presence
        status_update()
        log_print("Loaded the presence.", 2, False)
    except Exception as e:
        log_print(f"Unable to load the Discord rich presence: {e}", 4, True)


def status_update(details: Optional[str] = f"Selecting what to do... (v{build})",
                  state: Optional[str] = "In the main menu",
                  large_image: Optional[str] = "https://cdn.ibaguette.com/cdn/RotatingCats_128.gif",
                  large_text: Optional[str] = f"Build: {build} // Version {version}",
                  small_image: Optional[str] = "https://cdn.ibaguette.com/cdn/BrigadersRotating_512.gif",
                  small_text: Optional[str] = "Be active in Baguette Brigaders for a prize",
                  buttons: Optional[list] = [{"label": "Join Server", "url": "https://discord.com/invite/7zaRexVaH5"},
                                             {"label": "Download DraggieTools", "url": "https://github.com/Draggie306/DraggieTools/raw/main/dist/DraggieTools.exe"}],
                  start=start_time,
                  ):
    """
    `details`: The first thing that should be chosen. It is the top of the presence.\n
    `state`: Appears below the details.
    `start`: Do not change unless it's important. Should be `time()`.
    """

    try:
        if client:
            client.update(state=state, details=details, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text, buttons=buttons, start=start)
        else:
            return log_print("Not updating status due to Discord not being present.", 3, False)
    except Exception as e:
        return log_print(f"Unable to update the Discord rich presence: {e}", 4, True)


"""
Here are the prints for directory determining.
"""

if dev_mode:
    print(f"\n\n*-* Beta Tester Prints *-*\n\nAppData Directory: {DraggieTools_AppData_Directory}")
    sleep(0.05)
    print(f"Executable location (Where the EXE file is saved locally): {sys.executable}")
    sleep(0.05)
    print(f"Absolute Application Path (Wher PyInstaller runs EXE from): {path.dirname(path.abspath(__file__))}\n\nDevmode is ON, therefore enhanced logging is active.\nThe log file is located in the Roaming AppData directory")
    sleep(0.05)

logging.basicConfig(filename=f'{DraggieTools_AppData_Directory}\\Logs\\[{username}]_{version}-{build}-{time()}.log', encoding='utf-8', level=logging.DEBUG)
logging.debug(f'Established uplink at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

directory = sys.executable
if dev_mode:
    logging.info(f"Assigned directory to {sys.executable}")


logging.debug(f"[MainInit] Took {elapsed_time} to load modules")


def log_print(text, log_level: Optional[int] = 2, output: Optional[bool] = True) -> None:
    """
    Logs and prints the text inputted. The logging level is\n1: DEBUG\n2: INFO (default)\n3: WARNING\n4: ERROR\n5: CRITICAL
    """
    match log_level:
        case 1:
            logging.debug(text)
        case 2:
            logging.info(text)
        case 3:
            logging.warning(text)
        case 4:
            logging.error(text)
        case 5:
            logging.critical(text)
        case _:
            logging.info(text)
    if output:
        print(text)
    # if output else logging.info("The above log was not shown to the console")


global stop_event, thread


def start_anim_loading(text):
    global stop_event, thread
    stop_event = Event()
    thread = Thread(target=loading_icon, args=(stop_event, text))
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


def get_first_line_of_term(search_phrase, file):
    with open(file, 'r', encoding="UTF-8") as f:
        line_num = 0
        for line in f.readlines():
            line_num += 1
            if line.find(search_phrase) >= 0:
                return (int(line_num))


def replace_line(file_name, line_num, text):
    line_num = line_num - 1
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


"""
try:
    x = get("https://client.draggie.games")
except:
    pass
"""


def refresh():
    with open(__file__) as fo:
        source_code = fo.read()
        byte_code = compile(source_code, __file__, "exec")
        exec(byte_code)


def refresh2():
    exec(open(__file__).read())


def tqdm_download(download_url, save_dir, desc: Optional[str] = None):
    try:
        response = get(download_url, stream=True)

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024  # 1 Kibibyte
        written = 0
        # status_update(details="Downloading a file", state=f"{total_size} bytes")
        if desc is None:
            desc = download_url.split("/")[-1]
        log_print(f"Attempting to download a file. Content length: {total_size} bytes. ({download_url})", 1, False)
        with open(save_dir, "wb") as f:
            for data in tqdm(response.iter_content(block_size), total=ceil(total_size // block_size), unit="KB", desc=desc):
                written = written + len(data)
                f.write(data)
        log_print(f"Downloaded the file! {total_size} bytes. ({download_url})", 1, False)
    except KeyboardInterrupt:
        log_print("Keyboard interrupt: going back to first choice.", 3)
        return choice1()
    except Exception as e:
        log_print(f"\n[DownloadError] An error has occured downloading the file. {download_url}\n{e}\n{traceback.format_exc()}", 4)


def download_chunk(url, start, end, save_dir, pbar):
    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers, stream=True)
    with open(f"{save_dir}.part{start}", "wb") as f:
        for data in response.iter_content(1024):
            f.write(data)
            pbar.update(len(data))


def tqdm_download2(download_url, save_dir, desc=None, num_threads: Optional[int] = 4):
    response = requests.get(download_url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    chunk_size = ceil(total_size / num_threads)

    if desc is None:
        desc = download_url.split("/")[-1]

    with tqdm(total=total_size, unit="B", desc=desc) as pbar:
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for i in range(num_threads):
                start = i * chunk_size
                end = min((i + 1) * chunk_size - 1, total_size - 1)
                futures.append(executor.submit(download_chunk, download_url, start, end, save_dir, pbar))

            for future in as_completed(futures):
                future.result()

    with open(save_dir, "wb") as f: # merge the chunks
        for i in range(num_threads):
            with open(f"{save_dir}.part{i * chunk_size}", "rb") as part_file:
                f.write(part_file.read())
            os.remove(f"{save_dir}.part{i * chunk_size}")


def change_language():
    global language, language_chosen
    language = None
    while language is None:
        status_update(details="Choosing language", state="English or French?")
        x = input("Choose language\nChoisissez la langue\nEnglish = 1, French = 2\n\n>>> ")
        if x == "2":
            print("La langue est maintenant francais.")
            language = 'french'
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w+", encoding="UTF-8") as x:
                x.close()
            log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' cleared")
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w", encoding="UTF-8") as x:
                x.write("french")
                x.close()
            log_print(f"({datetime.now()}.strftime('%Y-%m-%d %H:%M:%S'): File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' written with 'French'")
            language_chosen = "french"
        else:
            print("Language updated to English.")
            language = 'english'
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w+", encoding="UTF-8") as x:
                x.close()
            log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' cleared")

            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", "w") as x:
                x.write("english")
                x.close()
            log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: File at path '{DraggieTools_AppData_Directory}\\Language_Preference.txt' written with 'English'")
            language_chosen = "english"
    status_update(details="Choosing language", state=f"Set language to {language_chosen}!")
    sleep(0.1)
    if dev_mode:
        log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Language successfully changed to {language_chosen}")
    return language_chosen


def get_language():
    """Returns the user's language. Currently `english` or `french`.\nIf the language file doesn't exist, it will be created."""
    if path.exists(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt"):
        try:
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", encoding="UTF-8") as x:
                language_read = x.read()

            if language_read == "french":
                language = 'french'
                print("Langue mise a jour: francais.")
            else:
                language = 'english'
                print("Language set to English.")
        except Exception:
            language = change_language()
    else:
        log_print("[get_language] Language file doesn't exist when checking, using blocking change_language function", 3, False)
        language = change_language()
    return language


language = get_language()
log_print(f"[MainInit] Language set to {language}", 2, False)


def cmini_extraction():
    print("CMINI_EXTRACTION")
    import subprocess
    bankfilepath = input("Enter the INPUT PATH. This must contain the bank files.\n\n>>> ")
    outputpath = input("Enter the output path to nicely put everything in afterwards.\n\n>>> ")
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)

    utils_path = input("Enter the path to the folder with all the required dependencies. Leave blank and they will be downloaded to the output directory.\n\n>>> ")

    # quickbms_exe = input("Enter the path to the quickBMS.exe file:\n\n\n>>>")
    # bmsfile = input("Enter the path to the script.bms file:\n\n\n>>>")

    if utils_path == "":
        utils_path = outputpath + r"\.utils" # create a folder called .utils in the output directory
        makedirs(utils_path, exist_ok=True)
        log_print(f"Downloading utility prerequisite files to {utils_path} directory...", 1, True)
        tqdm_download("https://cdn.discordapp.com/attachments/1100802918527008778/1100803066313322548/fmodex.dll", utils_path + r"\fmodex.dll")
        tqdm_download("https://cdn.discordapp.com/attachments/1100802918527008778/1100803066674028594/fmodL.dll", utils_path + r"\fmodL.dll")
        tqdm_download("https://cdn.discordapp.com/attachments/1100802918527008778/1100803067022159913/fsb_dec.bat", outputpath + r"\fsb_dec.bat") # batchfile must be in parent directory
        tqdm_download("https://cdn.discordapp.com/attachments/1100802918527008778/1100803067772948561/fsb_aud_extr.exe", utils_path + r"\fsb_aud_extr.exe")
        tqdm_download("https://cdn.discordapp.com/attachments/1100802918527008778/1100803068121067530/fmod_extr.exe", utils_path + r"\fmod_extr.exe")
        tqdm_download("https://cdn.discordapp.com/attachments/1100802918527008778/1100803068439830659/Script.bms", utils_path + r"\Script.bms")
        tqdm_download("https://cdn.discordapp.com/attachments/1100802918527008778/1100803068813135955/quickbms.exe", utils_path + r"\quickbms.exe")
        log_print(f"All files downloaded! Utils path = {utils_path}", 1, False)

    quickbms_exe = utils_path + r"\quickbms.exe"
    fsb_aud_extr_exe = utils_path + r"\fsb_aud_extr.exe"
    bmsfile = utils_path + r"\Script.bms"
    batchfile = outputpath + r"\fsb_dec.bat" # batchfile limitation: must be in the same directory as the fsb files

    log_print(f"batchfile_path: {batchfile}")

    # Check if all the files exist

    if not os.path.isfile(quickbms_exe) or not os.path.isfile(bmsfile) or not os.path.isfile(batchfile) or not os.path.isfile(fsb_aud_extr_exe):
        print("Missing files! Please redownload the dependencies.")
        return

    # Replace content in batchfile to match the path to the fsb_aud_extr.exe file

    target_string = 'D:\\Supercell Extraction Tools\\Bank Files (to wav)\\bank files\\fsb_aud_extr.exe'
    replacement_string = fsb_aud_extr_exe

    with open(batchfile, 'r') as file:
        file_contents = file.read()
        modified_contents = file_contents.replace(target_string, replacement_string)

    with open(batchfile, 'w') as file:
        file.write(modified_contents)

    # Execute the quickbms extractor file with parameters

    command = f'& "{os.path.normpath(quickbms_exe)}" -d "{os.path.normpath(bmsfile)}" "{os.path.normpath(bankfilepath)}" "{os.path.normpath(outputpath)}"'
    log_print(f"Executing command: {command}")

    # Start the subprocess and hide the window

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    proc = subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command", command], stdout=subprocess.PIPE, startupinfo=startupinfo)

    # Wait for the subprocess to complete and get the output

    output = proc.communicate()[0]
    output_str = output.decode()

    # Print the output

    log_print(output_str, 1)
    log_print("Successfully extracted some files!")

    # Run the batchfile

    log_print("Running batchfile to extract all the files from the fsb files...", 2, False)
    log_print(f"Executing command with subprocess.Popen: {batchfile}. working directory is {outputpath}", 2, True)
    start_anim_loading("Extracting waveform files from FSB... this make take some time...")
    proc = subprocess.Popen([batchfile], stdout=subprocess.PIPE, cwd=outputpath)
    output = proc.communicate()[0]
    output_str = output.decode()
    stop_anim_loading()
    log_print(f"Extracting all was successfully completed.\n\nLog of files extracted:\n------\n{output_str}\n------\n", 2, True)

    log_print("Performing additional cleanup...", 2, True)

    wavfiles = 0
    oldpaths = 0

    # move all created files up to grandparent directory, and remove parent folders
    # this is to avoid folders with the same name - e.g. example/music_background.bank/music_background/wavefile.wav
    # we just want example/music_background/wavefile.wav

    for root, dirs, files in os.walk(outputpath):
        for file in files:
            try:
                if file.endswith('.wav'):
                    dst_dir = os.path.join(root.replace('.bank', ''), file) # remove bank extension from the directory name

                    os.makedirs(os.path.dirname(dst_dir), exist_ok=True)

                    # get name of current, wanted target folder
                    parentname = os.path.basename(os.path.normpath(dst_dir))
                    grandparentname = os.path.basename(os.path.normpath(os.path.dirname(dst_dir)))
                    grandparentdir = os.path.dirname(os.path.dirname(dst_dir))

                    print(parentname, grandparentname, grandparentdir)
                    shutil.move(os.path.join(root, file), os.path.join(grandparentdir, file))

                    log_print(f"Moved {os.path.join(root, file)} to {grandparentdir + file}", 2, True)
                    wavfiles = wavfiles + 1

                    if len(os.listdir(root)) <= 1:
                        log_print("the root is only one file, removing the directory...")
                        shutil.rmtree(root, ignore_errors=True)
                        oldpaths = oldpaths + 1
                    """if len(os.listdir(os.path.dirname(root))) <= 1:
                        log_print(f"the parent directory {os.path.dirname(root)} is only one file, removing the directory...")
                        shutil.rmtree(os.path.dirname(root), ignore_errors=True)
                        oldpaths = oldpaths + 1"""
            except Exception as e:
                log_print(f"Error while moving file: {e}", 3, True)

    # check for bank folders and remove them

    for file in os.listdir(outputpath):
        if file.endswith(".bank"):
            log_print(f"Removing bank folder {os.path.join(outputpath, file)}", 2, True)
            shutil.rmtree(os.path.join(outputpath, file), ignore_errors=True)
            oldpaths = oldpaths + 1

    # check for empty directories and remove them from root directory
    # this is to avoid empty folders in output/folder/empty_folder

    for root, dirs, files in os.walk(outputpath):
        for dir in dirs:
            if len(os.listdir(os.path.join(root, dir))) == 0:
                log_print(f"Removing empty directory {os.path.join(root, dir)}", 2, True)
                shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
                oldpaths = oldpaths + 1

    log_print("Additional cleanup completed!", 2, True)
    log_print(f"\n.wav files created: {wavfiles}\nPaths prettified: {oldpaths}", 2, True)

    open_in_explorer = input("Open the output folder in explorer? (y/n): ") # nice to have, but not necessary
    if open_in_explorer == "y":
        os.startfile(outputpath)
    log_print("Done!", 1, True)


# end of cmini function. phew! that was a lot of code. finished at 11:30pm


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
    else:
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


"""def torrent_downloader():
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
    # th.set_download_limit(8 * 1024)
    # th.set_upload_limit(2 * 1024)

    # Start downloading the magnet link
    while (not th.is_seed()):
        s.wait_for_alert(1000)

    # Print the torrent status
    print(th.status())"""


def cleanup_files():
    # Get the current time in seconds
    current_time = time()
    file_amount = 0

    things_to_delete = input("What do you want to delete?\n\n[1] = Logs\n[2] = UpdatedBuilds\n[3] = UpdatedBuildsCache\n[4] = SourceCode\n[5] = AutoBrawlExtractor\\DownloadedBuilds\n[6] = All\n\n>>> ")

    if things_to_delete == "1":
        dir_paths = [f"{DraggieTools_AppData_Directory}\\Logs"]
    elif things_to_delete == "2":
        dir_paths = [f"{DraggieTools_AppData_Directory}\\UpdatedBuilds"]
    elif things_to_delete == "3":
        dir_paths = [f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache"]
    elif things_to_delete == "4":
        dir_paths = [f"{DraggieTools_AppData_Directory}\\SourceCode"]
    elif things_to_delete == "5":
        dir_paths = [f"{Draggie_AppData_Directory}\\AutoBrawlExtractor\\DownloadedBuilds"]
    elif things_to_delete == "6":
        dir_paths = [f"{DraggieTools_AppData_Directory}\\Logs",
                     f"{DraggieTools_AppData_Directory}\\UpdatedBuilds",
                     f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache",
                     f"{DraggieTools_AppData_Directory}\\SourceCode",
                     f"{Draggie_AppData_Directory}\\AutoBrawlExtractor\\DownloadedBuilds"
                     ]
    upload_log = None
    # Loop through all the directories

    for dir in dir_paths:
        if path.exists(dir):
            log_print(f"[FileCleanup] Inspecting directory {dir}.")
            for file in listdir(dir):
                file_path = path.join(dir, file)
                mod_time = path.getmtime(file_path)
                # Calculate the difference in seconds between the current time and the modification time
                time_diff = current_time - mod_time
                time_diff_days = time_diff / (60 * 60 * 24)
                if time_diff_days > 7:
                    if file.endswith(".log"):
                        if not upload_log:
                            x = (input(phrases[language]['log_notice'])).lower()
                            if x == "y":
                                upload_log = True
                            else:
                                upload_log = False
                        if upload_log is True:
                            upload_log_file(f"{dir}\\{file}")
                    # Delete the file
                    remove(file_path)
                    log_print(f"[FileCleanup] Cleaned up file at {file_path}")
                    file_amount += 1
        else:
            log_print("Skipped directory as it doesn't exist.")
        sleep(0.2)

    log_print(f"[FileCleanup] Purged {file_amount} file(s).")


def view_source():
    print(phrases[language]['downloading_opening'])
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
                return main()

            x = get_first_line_of_term("FrameRateLimit=", fort_ini_directory)

            replace_line(fort_ini_directory, x, f'FrameRateLimit={fps}.000000\n')

            print(f"Modified config FrameRateLimit in section [/Script/FortniteGame.FortGameUserSettings], line {x}")

        if z == "2":
            try:
                fps = int(input("Input desired FPS here:\n\n>>> "))
            except ValueError:
                print("Disallowed input. Try again")
                return main()

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
        thread = Thread(target=loading_icon, args=(stop_event, phrases[language]['check_update']))
        thread.start()
    except Exception:
        stop_event.set()
        thread.join()
        change_language()
        check_for_update()
    try:
        if path.isfile(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt"): # OverwriteOldVersion
            log_print(f"[OverwriteOldVersion] {Draggie_AppData_Directory}\\OldExecutableDir.txt exists!", 1, False)
            with open(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt", "r") as file:
                old_sys_exe = file.read()
                file.close()
            if old_sys_exe == str(sys.executable):
                log_print("[WARNING] The update cannot be applied to the current directory as you are running the file in the same place! Please download the update and wait for it to be closed.", 4)
            else:
                log_print("[OverwriteOldVersion] Removing OldExeDir.txt")
                remove(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt")
                log_print("[OverwriteOldVersion] Removing old exe")
                remove(old_sys_exe)
                log_print("[OverwriteOldVersion] Copying current exe to old sys exe")
                copyfile(str(sys.executable), old_sys_exe)
                log_print(f"[OverwriteOldVersion] Copying current exe ({sys.executable}) to old sys exe ({old_sys_exe})")
        else:
            log_print("[OverwriteOldVersion] OldExeFile does not exist!", 3, False)
    except Exception as e:
        log_print(f"Unable to overwrite older version. {e}", 4)

    try:
        current_build_version = int((get('https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt')).text)
        stop_event.set()
        thread.join()
    except Exception as e:
        stop_event.set()
        thread.join()
        log_print(f"\nUnable to check for update. {e}\n\nIt looks like the GitHub update servers might be blocked by your network! I'll still work, but some features might be limited.", 4)
        current_build_version = build
    if build < current_build_version: # if build is less than current version - so there's an update available.
        release_notes = str((get(f"https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Release%20Notes/release_notes_v{current_build_version}.txt")).text)
        log_print(f"\n{phrases[language]['update_available']} {phrases[language]['on_version']} {version} {phrases[language]['which_build']} {build}.\n{phrases[language]['newest_version_build']} {current_build_version}\n\n")
        if language == "english":
            versions_to_get = current_build_version - build
            if versions_to_get == 1:
                print(f"You're {versions_to_get} build behind latest")
            else:
                print(f"You're {versions_to_get} builds behind latest")

            string = (f"Latest release notes (v{current_build_version}):\n\n{release_notes}\n")

            while current_build_version != (build + 1):
                current_build_version = current_build_version - 1
                version_patch = str((get(f"https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Release%20Notes/release_notes_v{(current_build_version)}.txt")).text)
                string = (string + f"\nv{current_build_version}:\n{version_patch}\n\n")
            print(f"\n{string}\n")

        update_choice = input(f"{phrases[language]['press_enter_update']}\n\n>>> ")
        if update_choice != "":
            print("Skipping update.")
            return

        log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {language[6]} - {DraggieTools_AppData_Directory}")
        download_update(current_build_version)
        log_print("Update downloaded. Launching new version...")
        if not desktop_install_path:
            startfile(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe')
        else:
            desktop_dir = pathlib.Path.home() / 'Desktop'
            startfile(f'{desktop_dir}\\DraggieTools-{current_build_version}.exe')
        sys.exit()

    if current_build_version < build:
        print(phrases[language]['newer_version'])
    else:
        print(f"{phrases[language]['running_version']} {version} - {phrases[language]['build']} {build} - {phrases[language]['at']} {datetime.fromtimestamp(build_date).strftime('%Y-%m-%d %H:%M:%S')}. {phrases[language]['server_says']} {current_build_version}.")


def maniupulate_brawl_file(dir, app_version, app_name, arch_type, fingerprint_json: Optional[dict] = None):
    app_version = str(app_version)
    print(f"{phrases[language]['interacting_allowed']} '{app_name}' {phrases[language]['file']}. [v{app_version}]")
    if app_name is None:
        app_name = ""
    if not fingerprint_json:
        archive = zipfile.ZipFile(dir, 'r')

        # Get fingerprint.json from archive

        if arch_type == "IPA":
            fingerprint_json = str(archive.read(f'{app_name}res/fingerprint.json'), encoding="UTF-8")
        else:
            fingerprint_json = str(archive.read('assets/fingerprint.json'), encoding="UTF-8")

        fingerprint_json = json.loads(fingerprint_json)

        # find out what game it is

        if "Brawl Stars" in app_name:
            game_download_url = "game-assets.brawlstarsgame.com"
            app_name = "Brawl Stars"
        elif "Boom Beach" in app_name:
            game_download_url = "game-assets.boombeach.com"
            app_name = "Boom Beach"
        elif "Clash of Clans" in app_name:
            game_download_url = "game-assets.clashofclans.com"
            app_name = "Clash of Clans"
        elif "Clash Royale" in app_name:
            game_download_url = "game-assets.clashroyaleapp.com"
            app_name = "Clash Royale"
        elif "Clash Mini" in app_name:
            game_download_url = "game-assets.clashminigame.com"
            app_name = "Clash Mini"
        else:
            app_name = "[unknown]"
    else: # or just fingerprint json as that's all we really need
        fingerprint_json = fingerprint_json
        if "Brawl Stars" in app_name:
            game_download_url = "game-assets.brawlstarsgame.com"
            app_name = "Brawl Stars"
        elif "Boom Beach" in app_name:
            game_download_url = "game-assets.boombeach.com"
            app_name = "Boom Beach"
        elif "Clash of Clans" in app_name:
            game_download_url = "game-assets.clashofclans.com"
            app_name = "Clash of Clans"
        elif "Clash Royale" in app_name:
            game_download_url = "game-assets.clashroyaleapp.com"
            app_name = "Clash Royale"
        elif "Clash Mini" in app_name:
            game_download_url = "game-assets.clashminigame.com"
            app_name = "Clash Mini"
        if not app_name:
            game_choice = input("The file entered is a fingerprint file. Please specify the game you want to extract assets from.\n1. Brawl Stars\n2. Boom Beach\n3. Clash of Clans\n4. Clash Royale\n5. Clash Mini\n\n>>> ")
            match game_choice:
                case "1":
                    game_download_url = "game-assets.brawlstarsgame.com"
                    app_name = "[Fingerprint] Brawl Stars"
                case "2":
                    game_download_url = "game-assets.boombeach.com"
                    app_name = "[Fingerprint] Boom Beach"
                case "3":
                    game_download_url = "game-assets.clashofclans.com"
                    app_name = "[Fingerprint] Clash of Clans"
                case "4":
                    game_download_url = "game-assets.clashroyaleapp.com"
                    app_name = "[Fingerprint] Clash Royale"
                case "5":
                    game_download_url = "game-assets.clashminigame.com"
                    app_name = "[Fingerprint] Clash Mini"
                case _:
                    return print("Invalid choice. Exiting.")

    status_update(details="Extracting Supercell game assets", state=f"Loaded: {app_name} (v{app_version}) - {arch_type}")

    x = input(phrases[language]['select_options'])
    match x:
        case "1":
            print(f"{l10n_text('read_info_from_file')}:\n{l10n_text('fingerprint_hash')}: {fingerprint_json['sha']}\n{l10n_text('amount_of_files')}: {len(fingerprint_json['files'])}\n\n")
        case "2":
            if not fingerprint_json:
                fingerprint_json = str(archive.read(f'{app_name}res/fingerprint.json'), encoding="UTF-8")
                fingerprint_json = json.loads(fingerprint_json)
            for item in fingerprint_json['files']:
                if 'music/background' in item['file']:
                    log_print(f"Found 'music/background' in file: {item}", 1, False)
                    # The file field contains 'music/background'
                    print(f"{phrases[language]['found_music_in_file']}{item['file']}")
                    # Split the file field on the '\' character and take the first two elements
                    dir_path = item['file'].split('/')[:2]

                    # Join the elements back together with the '\' character
                    dir_path = '\\'.join(dir_path)

                    # Create the directory and its parent directories if they do not already exist
                    makedirs(f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{app_version}\\{dir_path}', exist_ok=True)
                    tqdm_download(f'https://{game_download_url}/{fingerprint_json["sha"]}/{item["file"]}', f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{app_version}\\{item["file"]}')
                else:
                    # print(f"Not in file {item}")
                    pass
            print("ok")
        case "3": # this is the get list of new/modified/deleted files
            Downloaded_Builds_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
            amount_of_files = 0

            # Get secondary IPA files

            for i in listdir(Downloaded_Builds_AppData_Directory):
                amount_of_files = amount_of_files + 1

            print(f"\n[Enter] Select one of the {amount_of_files} downloaded files.")
            files = []
            f = 0

            for file in listdir(Downloaded_Builds_AppData_Directory):
                files.append(file)
            for i in files:
                print(f"[{f}] {i}")
                f += 1
            x = input("\nChoose file\n\n>>> ")
            ipa_2_dir = f"{Downloaded_Builds_AppData_Directory}\\{files[int(x)]}"

            archive = zipfile.ZipFile(ipa_2_dir, 'r')
            if arch_type == "IPA":
                fingerprint_json_ipa2 = str(archive.read(f'{app_name}res/fingerprint.json'), encoding="UTF-8")

            # Load both fingerprint.json files and convert from dict to json

            # files = fingerprint_json['files']

            data1 = fingerprint_json
            data2 = json.loads(fingerprint_json_ipa2)

            # now get the files from each fingerprint.json file

            files1 = data1['files']
            files2 = data2['files']

            new_files = []
            modified_files = []
            deleted_files = []
            new_files_count = 0
            modified_files_count = 0
            deleted_files_count = 0

            # find the new, modified and deleted files

            for file_object in files1:
                file2 = next((file for file in files2 if file['file'] == file_object['file']), None)
                if file2:
                    if file_object['sha'] != file2['sha']:
                        modified_files.append(file_object['file'])
                        print(f"Found a modified file: {file_object['file']}")
                        modified_files_count += 1
                else:
                    new_files.append(file_object['file'])
                    print(f"Found a new file: {file_object['file']}")
                    new_files_count += 1

            for file2 in files2:
                file1 = next((file for file in files1 if file['file'] == file2['file']), None)
                if not file1:
                    deleted_files.append(file2['file'])
                    print(f"Found a deleted file: {file2['file']}")
                    deleted_files_count += 1

            # print('New files:', new_files)
            # print('Modified files:', modified_files)
            # print('Deleted files:', deleted_files)
            print(f"Found {new_files_count} new files, {modified_files_count} modified files and {deleted_files_count} deleted files.")
            print(f"COMPARED v{data1['version']} (StartPoint) to v{data2['version']} (OldVersion)")

            # now download the new and modified files

            choice_1 = input(f"\n{phrases[language]['download_new_files']}\n\n>>> ")

            if choice_1 == "1":
                print("ok")

                question = input("Do you want to filter by a string? (y/n)\n\n>>> ")
                if question == "y":
                    string = input("Enter string\n\n>>> ")
                    new_files = [x for x in new_files if string in x]
                downloads = 0
                for new_file_object in new_files:
                    base_directory = f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{app_version}_vs_{data2['version']}\\"
                    new_path = os.path.join(base_directory + new_file_object)
                    if not os.path.exists(os.path.dirname(new_path)):
                        os.makedirs(os.path.dirname(new_path), exist_ok=True)
                    tqdm_download(f'https://{game_download_url}/{data1["sha"]}/{new_file_object}', new_path)
                    downloads += 1

                print(f"Downloaded {downloads} new files.")
                Popen(f"explorer {base_directory}")

            sleep(1)
        case "4":
            print("Not implemented yet")
        case "5":
            threads = int(input(phrases[language]['input_threads']))
            log_print(f"[AutoBrawlExtractor] Threads chosen to download: {threads}")
            search_term = input(phrases[language]['search_term_input'])
            x = input(f"{phrases[language]['search_all_archives']} '{search_term}' {phrases[language]['only_in_current_version']} {fingerprint_json['version']}\n\n>>> ")
            file_cycle = True if x == "1" else False
            hits = 0
            files = 0
            archives = 0
            skips = 0
            if file_cycle:
                available_archives = listdir(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
                for file in available_archives:
                    log_print(f"Checked file '{file}' in {available_archives}")
                    if file.lower().endswith(".ipa") or file.lower().endswith(".zip") or file.lower().endswith(".json"):
                        with cf.ThreadPoolExecutor(max_workers=threads) as executor:
                            futures = []

                            log_print("An executor has been loaded", 1, False)

                            if not file.lower().endswith(".json"):
                                archive = zipfile.ZipFile(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds\\{file}", 'r')
                                archives += 1
                                print(f"{phrases[language]['searching_archive']} {file}")
                                new_fingerprint_json = str(archive.read(f'{app_name}res/fingerprint.json'), encoding="UTF-8")
                                new_fingerprint_json = json.loads(new_fingerprint_json)
                            else:
                                new_fingerprint_json = json.loads(file)
                            try:
                                fingerprint_sha = new_fingerprint_json["sha"]
                            except Exception as e:
                                print(f"Unable to find a valid fingerprint.json file in {file}.\n{e}")

                            for item in new_fingerprint_json['files']:
                                # print(f"Searching file: {item}", end='\r')
                                # print("\n")
                                files += 1
                                if search_term in item['file']:
                                    log_print(f"Found '{search_term}' in file: {item}")
                                    # The file field contains search_term
                                    print(f"{phrases[language]['found']} {search_term} {phrases[language]['in_file']} {item['file']}")
                                    hits += 1

                                    # Split the file path on the '\' character and take all elements except the last one
                                    dir_path = item["file"].split('/')[:-1]

                                    # Join the elements back together with the '\' character
                                    dir_path = '\\'.join(dir_path)

                                    # Create the directory and its parent directories if they do not already exist
                                    directory_to_save_to = f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\ALL\\{dir_path}'
                                    makedirs(directory_to_save_to, exist_ok=True)

                                    if not os.path.isfile(f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\ALL\\{item["file"]}'):
                                        futures.append(executor.submit(tqdm_download, f'https://{game_download_url}/{fingerprint_sha}/{item["file"]}', f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\ALL\\{item["file"]}'))
                                    else:
                                        print(f"{phrases[language]['not_downloading_exists']}{item['file']} {phrases[language]['not_downloading_exists_2']}")
                                        skips += 1
                                else:
                                    pass
                                    # print(f"Unable to find the search term {search_term} in v{new_fingerprint_json['version']}: {item}")
                    else:
                        print(f"{phrases[language]['unsupported_extension_1']} {file} {phrases[language]['unsupported_extension_2']}")
            else:
                archives += 1
                with cf.ThreadPoolExecutor(max_workers=threads) as executor:
                    log_print("An executor has been loaded", 1, False)
                    futures = []
                    for item in fingerprint_json['files']:
                        files = files + 1
                        if search_term in item['file']:
                            hits = hits + 1
                            dir_path = item["file"].split('/')[:-1]
                            dir_path = '\\'.join(dir_path)
                            directory_to_save_to = f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{app_version}\\{dir_path}'
                            makedirs(directory_to_save_to, exist_ok=True)
                            url = f'https://{game_download_url}/{fingerprint_json["sha"]}/{item["file"]}'
                            path = f'{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{app_version}\\{item["file"]}'
                            futures.append(executor.submit(tqdm_download, url, path))
            print(f"{phrases[language]['found']} {hits} {phrases[language]['matching_files']} {files} {phrases[language]['total_files_in']} {archives} {phrases[language]['available_archives']} {skips} {phrases[language]['files_already_exist']}")
            status_update(details=f"{phrases[language]['S_as']}", state=f"{files} {phrases[language]['S_as_1']} {hits} {phrases[language]['S_as_2']}")
        case "6":
            Popen(f'explorer /select,"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{app_version}"')
        case _:
            autobrawlextractor()

    maniupulate_brawl_file(dir, app_version, app_name, arch_type, fingerprint_json=fingerprint_json)


def init_filetype(dir):
    """
    Initialises and checks the validity of the archive version provided. If the file provided is not valid, then the program will exit.\nMay return the game.
    """
    app_name = None
    if dir.endswith(".json"):
        with open(dir, "r") as json_file:
            fingerprint_json = json.loads(json_file.read())
        version_name = fingerprint_json['version']
        maniupulate_brawl_file(dir, f"{version_name}", app_name=None, arch_type="fingerprint", fingerprint_json=fingerprint_json)
    archive = zipfile.ZipFile(dir, 'r')
    Brawl_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor")
    try:
        arch_type = None

        for file in archive.filelist:
            if file.is_dir() and file.filename.endswith("Payload/"):
                arch_type = "IPA"
            if file.filename.endswith("fingerprint.json"):
                new_fingerprint_json = str(archive.read(file), encoding="UTF-8")
                new_fingerprint_json = json.loads(new_fingerprint_json)
                version_name = new_fingerprint_json['version']
            if file.filename.endswith('.app/'):
                app_name = path.splitext(file.filename)[0]
        if not arch_type:
            arch_type = "APK"
            new_fingerprint_json = str(archive.read('assets/fingerprint.json'), encoding="UTF-8")
            new_fingerprint_json = json.loads(new_fingerprint_json)
            version_name = new_fingerprint_json['version']
            print(f"{phrases[language]['read_asset']}v{version_name}")
            app_name = "Brawl Stars"
            print({phrases[language]['apk_name_warning']})

        if not path.exists(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{version_name}"):
            mkdir(f"{Brawl_AppData_Directory}\\Versions\\{version_name}")
            log_print(f"Made directory: {Brawl_AppData_Directory}\\Versions\\{version_name}")

        print(f"{phrases[language]['detected_architecture']}{arch_type}")
        maniupulate_brawl_file(dir, f"{version_name}", app_name, arch_type, fingerprint_json=None)
    except Exception as e:
        print(f"\n[WARNING] An error has occured which cannot be resolved: {e}")
        logging.error(e)


def csv_decoder():
    import os

    # Credit: https://github.com/proydakov/supercell_resource_decoder/blob/master/lib_csv.py

    path = input("Enter the path to the encrypted CSV file:\n\n>>> ")

    # if the path is a folder

    def parse_csv(path):
        basename, _ = os.path.splitext(path)
        decodedname = basename + "_DECODED.csv"

        print(phrases[language]['processing'], path, "->", decodedname)

        try:
            with open(path, 'rb') as f:
                data = f.read()
        except Exception as e:
            log_print(f"Error: File not found. {e}")
            print(traceback.format_exc())

        tempdata = bytearray()

        for i in range(0, 8):
            tempdata.append(data[i])

        for i in range(0, 4):
            tempdata.append(0)

        for i in range(8, len(data)):
            tempdata.append(data[i])

        try:
            with open(decodedname, 'wb') as f:
                decompressor = lzma.LZMADecompressor()
                unpack_data = decompressor.decompress(tempdata)
                f.write(unpack_data)
                print(f"\n\nSuccessfully unpacked the file. You can now view it at {decodedname}\n")
        except Exception:
            log_print(f"invalid input: {traceback.format_exc()}")

    if os.path.isdir(path):
        log_print(f"Path is a directory. Parsing all CSV files in {path}", 2, True)
        for file in os.listdir(path):
            if file.endswith(".csv"):
                parse_csv(os.path.join(path, file))
    else:
        parse_csv(path)

    open_in_explorer = input("Do you want to open the folder containing the decoded CSV files? (y/n)\n\n>>> ")
    if open_in_explorer.lower() == "y":
        os.startfile(os.path.dirname(os.path.realpath(__file__)))

    autobrawlextractor()


def autobrawlextractor():
    Brawl_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor")
    Downloaded_Builds_AppData_Directory = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
    if not path.exists(f"{Brawl_AppData_Directory}\\Versions"):
        makedirs(f"{Brawl_AppData_Directory}\\Versions")
    if not path.exists(Downloaded_Builds_AppData_Directory):
        makedirs(Downloaded_Builds_AppData_Directory)

    def number_one():
        print(r"Enter the location of your Supercell archive file, e.g D:\Downloads\brawl.ipa. IPA files are preferred.")
        print("\nUse an .ipa file or .apk file (for iOS and Android decices, respectively). Must not be unzipped.")
        print("[0] Go back.\n[1] Search for all downloadable versions.\n[2] Decode CSV Files with LZMA.")

        amount_of_files = 0

        for i in listdir(Downloaded_Builds_AppData_Directory):
            amount_of_files = amount_of_files + 1

        if amount_of_files >= 1:
            print(f"\n[Enter] Select one of the {amount_of_files} downloaded files.")

        location = input("\n>>> ")

        if location == "1":
            print("Fetching a list of all trusted versions from GitHub...")
            git_brawl_builds = get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Addons/AutoBrawlExtractor/brawl_builds.txt")
            git_brawl_builds = git_brawl_builds.text
            urls = git_brawl_builds.splitlines()
            version_names = [re.search(r"laser-(\d+\.\d+)", url).group(1) for url in urls]
            for i, version_name in enumerate(version_names):
                print(f"[{i + 1}]   {version_name}")
            selected_version = (input("\nPlease select a version to download: ('*' to download them all, '0' to see other apps.).\n\n>>> "))
            if selected_version == "*":
                print("You have chosen to download ALL builds. If you would like to stop it, you will need to press Ctrl+C.")
                amount = len(urls)
                downloaded_amount = 0
                for line in urls:
                    source = line.strip().split(' (')
                    source_url = source[0]
                    source_loc = source[1].strip(')')
                    real_file_name = path.basename(urlsplit(source_url).path)
                    if "Baguette Brigaders" in source_loc:
                        source_loc = (f"a verified source: {source_loc}")
                    print(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
                    tqdm_download(source_url, f"{Downloaded_Builds_AppData_Directory}\\{real_file_name}")
                    downloaded_amount += 1
                    print(f"\nSuccessfully downloaded build {real_file_name}. It is located at: {Downloaded_Builds_AppData_Directory}\\{real_file_name}\nOverall progress: {downloaded_amount}/{amount} (~{round((downloaded_amount/amount)*100)}%\n")
                print(f"{downloaded_amount} builds have been saved!\n\n")
                number_one()
            if selected_version == "0":
                clash_mini = "https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Addons/AutoBrawlExtractor/ipas/board.txt"
                clash_of_clans = "https://raw.githubusercontent.com/Draggie306/DraggieTools/main/Addons/AutoBrawlExtractor/ipas/magic.txt"

                game_choice = input("Which game would you like to download builds for?\n\n[1] Clash Mini\n[2] Clash of Clans\n\n>>> ")

                if game_choice == "1":
                    game = clash_mini
                if game_choice == "2":
                    game = clash_of_clans

                print("Fetching a list of all trusted versions from GitHub...")
                git_clash_mini_builds = get(game)
                urls = (git_clash_mini_builds.text).splitlines()

                if game_choice == "1":
                    version_names = [re.search(r"board-(\d+\.\d+)", url).group(1) for url in urls]
                if game_choice == "2":
                    version_names = [re.search(r"magic-(\d+\.\d+)", url).group(1) for url in urls]
                for i, version_name in enumerate(version_names):
                    print(f"[{i + 1}]   {version_name}")

                selected_version = input("\nChoose a version to download: ('*' to download them all).\n\n>>> ")

                if selected_version == "*":
                    source = line.strip().split(' (')
                    source_url = source[0]
                    source_loc = source[1].strip(')')
                    real_file_name = path.basename(urlsplit(source_url).path)
                    if "Baguette Brigaders" in source_loc:
                        source_loc = (f"a verified source: {source_loc}")
                    print(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
                    tqdm_download(source_url, f"{Downloaded_Builds_AppData_Directory}\\{real_file_name}")
                else:
                    selected_url = urls[int(selected_version) - 1]
                    source = selected_url.strip().split(' (')
                    source_url = source[0]
                    source_loc = source[1].strip(')')
                    real_file_name = path.basename(urlsplit(source_url).path)
                    if "Baguette Brigaders" in source_loc:
                        source_loc = (f"a verified source: {source_loc}")
                        print(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
                    tqdm_download(source_url, f"{Downloaded_Builds_AppData_Directory}\\{real_file_name}")
                    print(f"\nDownloaded build {real_file_name}\nIt is located at: {Downloaded_Builds_AppData_Directory}\\{real_file_name}\n")

            selected_url = urls[int(selected_version) - 1]
            source = selected_url.strip().split(' (')
            source_url = source[0]
            source_loc = source[1].strip(')')
            real_file_name = path.basename(urlsplit(source_url).path)
            if "Baguette Brigaders" in source_loc:
                source_loc = (f"a verified source: {source_loc}")
                print(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
            tqdm_download(source_url, f"{Downloaded_Builds_AppData_Directory}\\{real_file_name}")
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

                print(f"No valid build specified, resorting to regex expression to find the most recent version, which appears to be in file {highest_version_file}")
                init_filetype(f"{Downloaded_Builds_AppData_Directory}\\{highest_version_file}")
        if location == "2":
            csv_decoder()
        if location == "0":
            main()
        else:
            init_filetype(location)
    number_one()


def awtd():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-*-*-*-*-*-*-*-*-*-*-*-* Welcome to the Advanced Water Tech Demo Secret Area! *-*-*-*-*-*-*-*-*-*-*-*-\n")
    # print("Searching for installed versions...")
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

        sleep(random.randint(1, 3))

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

        log_print(f"Requesting the server to validate {inputted_key}")
        code_response = get(f"https://awtd.ibaguette.com/keys/{inputted_key}/type.awtd")

        stop_event.set()
        thread.join()

        if code_response.status_code == 404:
            log_print("\nThis is an invalid key. Please try again.")
            sleep(1.5)
            awtd()
        else:
            log_print("\n404 not received.")
            log_print("Reading and validating code")

            # Open the JSON file
            raw_version_info = get("https://awtd.ibaguette.com/staticKeys/a5e81fe8_4e21_4d58_a0db_ea0c25ee9086").content
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
            log_print("Validating Download URL.")
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
            # log_print(f"[sha512decryptor] {decrypted_message}")
            log_print("Successfully decrypted and resolved endpoint download url.")
            # print("Decrypted message:", decrypted_message)

            download_url = str(decrypted_message).strip("b'").strip("'")  # remove leading and trailing characters from decrypted_message and store the result in download_url

            log_print(f"\n\nThe files are ready to be downloaded. Note that this will be downloaded temporarily to {DraggieTools_AppData_Directory}\\AWTD\\BuildCache.\nInput 1 to start downloading.")

            x = input("\n\n>>> ")
            log_print(f"Input: {x}")

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


def upload_log_file(file_path):
    url = "https://logs.draggie.games/tools"

    filename = path.basename(file_path)
    username = getpass.getuser()
    new_filename = f"[{username}]-{filename}"

    files = {
        'file': (new_filename, open(file_path, 'rb'))
    }

    print(new_filename)
    response = post(url, files=files)
    log_print(f"Uploading the logfile {file_path}. Status code: {response.status_code}", 2)


def upload_logs(most_recent: Optional[int] = None):
    logging_dir = f"{DraggieTools_AppData_Directory}\\Logs"
    files = listdir(logging_dir)
    files = [path.join(logging_dir, file) for file in files]

    # sort the files based on their creation time
    files.sort(key=path.getctime)

    # select the most recent x files
    if most_recent:
        files = files[-most_recent:]

    log_print(f"Files to upload: {files}", 1, False)

    # upload each file
    for file in files:
        upload_log_file(file)


def dev_menu():
    global build
    x = input("\n\n[1] Set build\n[2] Set version\n[3] Set unix time\n[4] Reload entire code (Dangerous)\n>>> ")
    match x:
        case "1":
            build = int(input("Enter the build number: "))
            choice1()
        case "2":
            version = str(input("Enter version number: "))
            choice1()
        case "3":
            build_date = int(input("Enter unix seconds (int): "))
            choice1()
        case "4":
            refresh()
        case _:
            choice1()


def calculate_time_discord(snowflake):
    if snowflake == "N/A" or snowflake is None:
        return "Unknown"
    else:
        snowflake = int(snowflake)
        unix_timestamp = 1420070400000 + int((f"{snowflake:b}")[:-22], 2)
        stringe = datetime.utcfromtimestamp(unix_timestamp / 1000).strftime('%d/%m/%Y, %H:%M:%S')
        return stringe


def discord_parse():
    try:
        for file in listdir(f"{DraggieTools_AppData_Directory}\\DiscordParse"):
            if not file.endswith("bak"):
                with open(f"{DraggieTools_AppData_Directory}\\DiscordParse\\{file}", 'r', encoding="utf-8") as f:
                    file = f.read()
            else:
                print("Invalid file detected")
                return Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\DiscordParse\\{file}"')
        print("Loaded file")
    except Exception as e:
        print("I'm opening up the Discord parser directory. Please paste in your file which is to be processed")
        if not path.isfile(f"{DraggieTools_AppData_Directory}\\DiscordParse"):
            makedirs(f"{DraggieTools_AppData_Directory}\\DiscordParse", exist_ok=True)
        Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\DiscordParse"')
        return print(f"No valid file or improperly formatted json file exists! You have to put the file in the folder {DraggieTools_AppData_Directory}\\DiscordParse\n\n{e}")

    x = input("[1] Parse current file and output everything.\n[2] Organise current file and output JSON files for each server\n\n")

    if x == "1":
        print("loading...\n")

        start_time = perf_counter() # start timer

        for line in file.splitlines(): # splitlines() is faster than split('\n')
            # check if line starts with '['
            if line.strip().startswith("["):
                discord_file = json.loads(line)
                print("============== NEW GUILD ==============")
                for channel in sorted(discord_file, key=lambda discord_file: discord_file["position_"]):
                    channel_type = channel.get("type")
                    extra_text = "----------------"
                    if channel_type == 4:
                        extra_text = "CATEGORY CHANNEL"
                    elif channel_type == 2 or channel_type == 0:
                        extra_text = "--TEXT CHANNEL--"
                    elif channel_type == 5:
                        extra_text = "--RULES CHANNEL--"
                    elif channel_type == 15:
                        extra_text = "--FORUM CHANNEL--"
                    else:
                        print(f"Channel type: {channel_type}")
                    id = channel.get("id")
                    name = channel.get("name")
                    position = channel.get("position_")
                    topic = channel.get("topic_")
                    lastMessageId = channel.get("lastMessageId")
                    lastPinTimestamp = channel.get("lastPinTimestamp", "N/A")
                    nsfw = channel.get("nsfw_")
                    rate_limit_per_user = channel.get("rateLimitPerUser_")
                    topic = channel.get("topic_")
                    guild_id = channel.get("guild_id")

                    print(f"\n----------------{extra_text}----------------\n\nServer: {guild_id}\nName: {name}\nID: {id}\nLast Message ID: {lastMessageId} ({calculate_time_discord(lastMessageId)})\nLast Pin Timestamp: {lastPinTimestamp}\nNSFW: {nsfw}\nPosition: {position}\nRate Limit Per User: {rate_limit_per_user}\nTopic: {topic}\n")
                    # sleep(0.1)

        print(f"Operation completed ({round((perf_counter() - start_time), 7)}s)")

    if x == "2":
        server_num = 0
        channel_num = 0
        server_data = {}
        for line in file.splitlines():
            if line.strip().startswith("["):
                discord_file = json.loads(line)
                for channel in discord_file:
                    print(f"Got channel ({channel_num})")
                    channel_num = channel_num + 1
                    guild_id = channel.get("guild_id")
                    if guild_id not in server_data:
                        server_data[guild_id] = []
                    server_data[guild_id].append({
                        'name': channel.get("name"),
                        'id': channel.get("id"),
                        'position': channel.get("position_"),
                        'topic': channel.get("topic_"),
                        'lastMessageId': channel.get("lastMessageId"),
                        'lastPinTimestamp': channel.get("lastPinTimestamp", "N/A"),
                        'nsfw': channel.get("nsfw_"),
                        'rate_limit_per_user': channel.get("rateLimitPerUser_"),
                        'guild_id': guild_id,
                    })
        for server_id, channels in server_data.items():
            with open(f'{DraggieTools_AppData_Directory}\\DiscordParse\\{server_id}.json', 'w') as outfile:
                json.dump(sorted(channels, key=lambda x: x['position']), outfile, indent=4)
                print(f"Writing data... ({server_num})")
                server_num = server_num + 1


def videomaker():
    import moviepy
    return print("This feature is currently disabled due to a bug in moviepy. Please use the old version of DraggieTools for this feature.")
    audio_dir = input("Enter path to ogg files: ")
    output_dir = input("Enter output dir path (there will be a temp folder located in here): ")

    print(moviepy.editor.TextClip.list('font'))

    # set file paths
    # audio_dir = r'D:\App Files\Brawl Music\test'

    # create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # create temp directory if it doesn't exist
    temp_dir = os.path.join(output_dir, 'temp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    else:
        x = input(f"want to delete all files in {output_dir}/temp? y/n: ")
        if x == "y":
            # create output directory if it doesn't exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            for i in os.listdir(os.path.join(output_dir, 'temp')):
                os.remove(os.path.join(output_dir, 'temp', i))
        else:
            pass

    # load audio files
    print("loading files...")
    num = 0
    audio_extensions = ('.ogg', '.mp3', '.m4a', '.wav')
    audio_files = []
    for root, dirs, files in os.walk(audio_dir):
        for file in files:
            if file.endswith(audio_extensions):
                print(f"Found matching file: {file}")
                audio_files.append(os.path.join(root, file))
                num = num + 1
    print(f"Loaded {num} audio files.")

    def two():
        print("Gathering information about all files...")
        # set the input and output directories

        input_dir = (os.path.join(output_dir, 'temp'))

        if not os.path.exists(input_dir):
            os.makedirs(input_dir)

        # create an empty list to store file names
        file_list = []

        # iterate over all the converted files in the temp directory with .mp4 extension
        for file in os.listdir(input_dir):
            if file.endswith(".mp4"):
                file_list.append(os.path.join(input_dir, file))

        # create a new file named 'list.txt' in the output directory and write the file names in it
        with open(os.path.join(output_dir, "list.txt"), "w") as file:
            for file_name in file_list:
                file.write(f"file '{file_name}'\n")

        # execute ffmpeg command to concatenate the files listed in 'list.txt' and create 'final_output.mp4' in the output directory
        # final_export in the output directory (not temp)

        final_name = f"{num}_combined_files_export_{uuid.uuid4()}.mp4"

        x = input("do you want to use 1, 2 or 3? (1 is recommended)\n\n>>> ")

        start_time = time.time()

        if x == "1":
            os.system(f"ffmpeg -safe 0 -f concat -segment_time_metadata 1 -i {os.path.join(output_dir, 'list.txt')} -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 {os.path.join(output_dir, final_name)}")
        if x == "2":
            os.system(f"ffmpeg -safe 0 -f concat -segment_time_metadata 1 -i {os.path.join(output_dir, 'list.txt')} -vf select=concatdec_select -af aselect=concatdec_select {os.path.join(output_dir, final_name)}")
        if x == 3:
            os.system(f"ffmpeg -f concat -safe 0 -i {os.path.join(output_dir, 'list.txt')} -c copy {os.path.join(output_dir, final_name)}")

        # print a message to indicate successful execution
        end_time = time.time()
        print(f"Files concatenated successfully in {end_time - start_time:.2f} seconds!")
        time.sleep(1)

    def one():
        import concurrent.futures as cf
        threads = int(input("Enter the amount of threads you want to run (~600mb RAM each for 1 minute file): "))

        def process_audio_file(audio_file):
            audio = moviepy.editor.AudioFileClip(audio_file)

            # create video clip with black background
            video_clip = moviepy.editor.ColorClip((1920, 1080), color=(0, 0, 0)).set_duration(audio.duration)

            # create text clip with filename overlay
            filename = os.path.splitext(os.path.basename(audio_file))[0]

            text_clip = moviepy.editor.TextClip(f"{filename}.ogg", fontsize=50, font="Lilita One", color='white')
            text_clip = text_clip.set_position('center').set_duration(audio.duration)

            video_with_new_audio = video_clip.set_audio(audio)

            final_video = moviepy.editor.CompositeVideoClip([video_with_new_audio, text_clip])

            print(f"processing audio file {filename}")

            # Generate temp mp4 files
            output_file = os.path.join(output_dir, 'temp', f"{os.path.splitext(os.path.basename(audio_file))[0]}.mp4")
            final_video.write_videofile(output_file, fps=30, codec='libx264', preset="slow", audio=True, audio_codec=None, threads=12)
            time.sleep(0.5)

        if __name__ == '__main__':
            start_time = time.time()
            with cf.ThreadPoolExecutor(max_workers=threads) as executor:
                futures = []

                for iteration, audio_file in enumerate(audio_files):
                    # print(f"[iteration {iteration}] processing audio file {audio_file}")
                    try:
                        futures.append(executor.submit(process_audio_file, audio_file))
                    except Exception as e:
                        print(e)

                # wait for all threads to finish
                cf.wait(futures)

                # concatenate video clips and write output file
                end_time = time.time()
                print(f"Rendered video clips for all files in {end_time - start_time:.2f} seconds!")
                two()

    inn = input(f"[1] Render selected files from the OGG directory {audio_dir}\n[2] Render preprocessed mp4 files in the temp folder\n\n>>> ")

    if inn == "1":
        one()
    else:
        two()


def yt_download():
    print("Hi!")
    # Create a YoutubeDL object
    ydl = youtube_dl.YoutubeDL()

    def get_ydl_info(title, type, directory):
        directory = os.path.join(directory, title + '.%(ext)s')
        ydl_opts_bestboth = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': directory
        }

        ydl_opts_bestvideo = {
            'format': 'bestvideo/best',
            'outtmpl': directory
        }

        ydl_opts_bestaudio = {
            'format': 'bestaudio/best',
            'outtmpl': directory
        }

        match type:
            case "both":
                return ydl_opts_bestboth
            case "video":
                return ydl_opts_bestvideo
            case "audio":
                return ydl_opts_bestaudio

    # Get the best audio stream link
    youtube_video = input("Enter the URL of the video or playlist:\n\n>>> ")
    start_time = time()
    try:
        audio_info = ydl.extract_info(youtube_video, download=False)
    except youtube_dl.utils.YoutubeDLError as e:
        log_print(e, 3, False)
        try:
            audio_info = ydl.extract_info(f"ytsearch:{youtube_video}", download=False)['entries'][0]
            youtube_video = audio_info['webpage_url']
        except youtube_dl.utils.YoutubeDLError as e:
            log_print("There was an error getting information from the provided URL. Please try again later.")
            log_print(e, 4, False)
            choice1()

    print(f"\n\n[draggietools] Found matching video: {audio_info['title']}\n\n")
    highest_audio_bitrate = 0
    highest_total_bitrate = 0
    highest_audio_url = ''
    highest_sample_rate = 0
    highest_video_url = ''
    highest_video_format = ''
    highest_audio_format = ''

    if audio_info['formats']:
        print("Not a playlist")

        def old_download():
            for format in audio_info['formats']:
                if format['vcodec'] == 'none': # check if the format is audio-only
                    if 'asr' in format and format['asr'] > highest_sample_rate:
                        highest_sample_rate = format['asr']  # update highest_sample_rate
                        print(f"Updated highest sample rate to {highest_sample_rate}Hz")
                    if 'abr' in format and format['asr'] == highest_sample_rate:
                        if format['abr'] > highest_audio_bitrate:
                            highest_audio_url = format['url']
                            highest_audio_bitrate = format['abr']
                            # highest_audio_format_id = format['format_id']
                            print(f"New best audio bitrate: {highest_audio_bitrate}")
                            highest_audio_format = format

                if format['acodec'] == 'none': # check if the format is video-only
                    if 'vbr' in format and format['vbr'] > highest_total_bitrate:
                        highest_total_bitrate = format['vbr'] # update highest_total_bitrate
                        highest_video_url = format['url']
                        # highest_video_format_id = format['format_id']
                        print(f"New best video bitrate: {highest_total_bitrate}")
                        highest_video_format = format

            print(f"Highest audio quality: {highest_audio_url}\nHighest video URL: {highest_video_url}")

        # old_download()

        what_to_do = input("What do you want to do?\n[1] Download audio\n[2] Download video\n[3] Download both\n[4] Download both and merge into one file\n\n>>> ")
        save_dir = input("Enter the directory you want to save the file to:\n\n>>> ")

        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

        start_time_download = time()
        if what_to_do == "1":
            ydl_opts = get_ydl_info(audio_info['title'], "audio", directory=save_dir)
            x = tqdm_download2(highest_audio_url, os.path.join(save_dir, f"{audio_info['title']}[audio].{highest_audio_format['ext']}"), desc="Downloading highest quality audio...")
        elif  what_to_do == "2":
            ydl_opts = get_ydl_info(audio_info['title'], "video", directory=save_dir)
            y = tqdm_download2(highest_video_url, os.path.join(save_dir, f"{audio_info['title']}[video].{highest_video_format['ext']}"), desc="Downloading highest quality video...")
        elif what_to_do == "3":
            ydl_opts = get_ydl_info(audio_info['title'], "both", directory=save_dir)
            tqdm_download2(highest_audio_url, os.path.join(save_dir, f"{audio_info['title']}[audio].{highest_audio_format['ext']}"), desc="Downloading highest quality audio...")
            tqdm_download2(highest_video_url, os.path.join(save_dir, f"{audio_info['title']}[video].{highest_video_format['ext']}"), desc="Downloading highest quality video...")
            print("Downloaded both files!")
        else:
            ydl_opts = get_ydl_info(audio_info['title'], "both", directory=save_dir)
            pass

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_video])

    else:
        try:
            if audio_info['entries']:
                log_print("Playlist detected", 1, False)
        except KeyError:
            return log_print("Not a playlist, not a video, no clue what to do with this URL", 4, True)

        log_print("Going through a playlist...", 1, False)
        what_to_do = input("What do you want to do?\n[1] Download audio\n[2] Download video\n[3] Download both and merge into one file\n\n>>> ")
        save_dir = input("Enter the directory you want to save the file to:\n\n>>> ")

        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

        start_time_download = time()
        # Download every video in the playlist
        if what_to_do == "1": # download best audio
            for video in audio_info['entries']:
                ydl_opts = get_ydl_info(title=video['title'], type="audio", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video['webpage_url']])
        if what_to_do == "2": # download best video
            for video in audio_info['entries']:
                ydl_opts = get_ydl_info(title=video['title'], type="video", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video['webpage_url']])
        if what_to_do == "3": # download both
            for video in audio_info['entries']:
                ydl_opts = get_ydl_info(title=video['title'], type="both", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video['webpage_url']])

    log_print(f"[download]  Finished in {round(time() - start_time_download, 2)} seconds.")
    log_print(f"[ytdl]      Finished in {round(time() - start_time, 2)} seconds.")


def draggieclient():
    try:
        target_path = os.path.expanduser("~\\AppData\\Local\\Draggie\\Client\\client.exe")
        Ensure_Client_AppData_Directory = (f"{environ_dir}\\AppData\\Local\\Draggie\\Client")
    except Exception as e:
        log_print(f"There was a critical error with trying to determine access to an essential directory: {e}: {traceback.format_exc()}.\n\n\nRetrying with other directory")

    # -*-*-*-*-* DIRECTORY CREATION *-*-*-*-*-

    if not os.path.exists(Ensure_Client_AppData_Directory):
        os.makedirs(Ensure_Client_AppData_Directory, exist_ok=True)
        log_print(f"makedirs: {Ensure_Client_AppData_Directory}")

    if not os.path.exists(f"{Ensure_Client_AppData_Directory}\\Logs"):
        os.mkdirs(f"{Ensure_Client_AppData_Directory}\\Logs", exist_ok=True)
        log_print(f"mkdir: {Ensure_Client_AppData_Directory}\\Logs")

    log_print("Prerequisites installed.\nDownloading client...")
    try:
        tqdm_download("https://autoupdateclient.draggie.games/AutoUpdate20.exe", target_path)
    except PermissionError as e:
        return print(f"{e}\nMaybe you already have DraggieClient installed?")
    except Exception as e:
        return print(f"An error occured: {e}: {traceback.format_exc()}")
    os.startfile(target_path)
    save_json()
    log_print("Your system now has DraggieClient installed! Running in the background, it will keep all of your files by me up to date! Enjoy.")


def save_json():
    try:
        with open(os.path.join(DraggieTools_AppData_Directory, 'Client_AutoUpdateInfo.txt'), 'w') as f:
            json.dump({
                "build": build,
                "version": version,
                "buildTime": build_date,
                "tools_installation_directory": directory,
            }, f)
    except Exception as e:
        log_print(f"Unable to write current information: {e}")


def vbs_script_launcher():
    vbs_funny_long = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/Important-Disk-Data.vbs"
    keyboard_rgb = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/keyboard-rgb.vbs"
    amazing_site = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/Have-you-heard-of-this-amazing-website.bat"
    cd_eject = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/cd.vbs"
    delete = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/delete.bat"
    fool = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/fool.vbs"
    hackingmatrix = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/Hackingmatrix.bat"
    infinite_bat = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/infinite.bat"
    l = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/L.vbs"
    no = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/no.bat"

    choice_vbs = input("What script do you want to download?\n1. Important Disk Data\n2. Keyboard RGB\n3. Have you heard of this amazing website?\n4. CD Eject\n5. Delete\n6. Fool\n7. Hacking Matrix\n8. Infinite\n9. L\n10. No\n\nChoice: ")
    log_print("Downloading script...")
    match choice_vbs:
        case "1":
            filename = "Important-Disk-Data.vbs"; url = vbs_funny_long
        case "2":
            filename = "keyboard-rgb.vbs"; url = keyboard_rgb
        case "3":
            filename = "Have-you-heard-of-this-amazing-website.bat"; url = amazing_site
        case "4":
            filename = "cd.vbs"; url = cd_eject
        case "5":
            filename = "delete.bat"; url = delete
        case "6":
            filename = "fool.vbs"; url = fool
        case "7":
            filename = "Hackingmatrix.bat"; url = hackingmatrix
        case "8":
            filename = "infinite.bat"; url = infinite_bat
        case "9":
            filename = "L.vbs"; url = l
        case "10":
            filename = "no.bat"; url = no
        case _:
            print("Invalid choice. Quitting...")
            choice1()
    try:
        tqdm_download(url, f"{DraggieTools_AppData_Directory}\\{filename}")
        os.startfile(f"{DraggieTools_AppData_Directory}\\{filename}")
    except Exception as e:
        log_print(f"Error: {e}")


def choice1():
    try:
        x = input(phrases[language]['menu_options'])
        status_update(details="Selecting what to do...")
        """y = x/0 # in case we need to do some quick error checking!
        print(y)"""
        if x == "0":
            log_print(f"Goodbye! {time()}\nHope you found me useful.", 2, False)
            print("\n\n\n\n\n\nQuitting...")
            if client:
                client.close()
            sys.exit()

        match x:
            case "1":
                desktop_dir = pathlib.Path.home() / 'Desktop'
                if path.exists(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt"):
                    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", 'r') as e:
                        install_dir = e.read()
                        if install_dir == str(desktop_dir):
                            print("Existing desktop file preference exists.")
                            print("The file will now no longer be located on the desktop.\n")
                            with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
                                e.close()
                            with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w") as f:
                                f.write(f"{sys.executable}\n{build}")
                            choice1()

                start_anim_loading("Initialising.")
                # print(f"Current directory: {directory}")
                try:
                    copyfile(directory, f"{desktop_dir}\\DraggieTools.exe")
                    stop_anim_loading()
                    print("\nCopied executable to the desktop. Note that if the file is deleted or an update is applied, this version will need to be updated again and this move be reapplied.")
                    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
                        e.write(f"{desktop_dir}\n{build}")
                except FileNotFoundError:
                    stop_anim_loading()
                    print("\nRunning from PYTHON file. Not executable. This should print only in the development stage.")
                    copyfile(f"{current_directory}\\DraggieTools.py", f"{desktop_dir}\\DraggieTools.py")
                    print("I am very dumb. This will be improved later.")
                except SameFileError:
                    stop_anim_loading()
                    print("\nThis cannot be performed. The files are the same. Maybe it's already on the desktop!")
            case "2":
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
                    log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Copied file from '{directory}' to desired directory {y}\\Draggie\\DraggieTools.exe")
                except Exception as e:
                    print(f"An error occured. {e}")
                    print("Please make sure that the file has not been renamed.")
                    logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {traceback.format_exc()}")
                    choice1()
            case "3":
                check_for_update()
            case "4":
                change_language()
            case "5":
                status_update(details="Viewing DraggieTools source code.")
                view_source()
            case "6":
                status_update(details="Modifying GameUserSettings.ini...")
                fort_file_mod()
            case "7":
                status_update(details="Installing software")
                awtd()
            case "8":
                status_update(details="Downloading a torrent")
                # torrent_downloader()
            case "9":
                status_update(details="Extracting Supercell game assets")
                autobrawlextractor()
            case "10":
                status_update(details="Cleaning up files")
                cleanup_files()
            case "11":
                status_update(details="Parsing Discord files")
                discord_parse()
            case "12":
                print("Reloading Discord RPC...")
                asyncio.run(load_presence())
            case "13":
                status_update(details="Installing DraggieClient")
                draggieclient()
            case "14":
                status_update(details="In the YouTube downloader")
                yt_download()
            case "15":
                status_update(details="Clash Mini'ing")
                cmini_extraction()
            case "16":
                status_update(details="Video Maker")
                videomaker()
            case "17":
                status_update(details="In the VBS Script Launcher")
                vbs_script_launcher()
            case "dev":
                status_update(details="In the developer menu")
                dev_menu()
            case "log":
                status_update(details="Uploading some logs")
                upload_logs()

            case "69":
                print(";)")
                status_update(details="In the secret menu", state="")
                secret_menu()

            case _:
                choice1()

        choice1()
    except KeyboardInterrupt:
        logging.warning(f"Handled general keyboard interrupt: \n{traceback.format_exc()}")
        return choice1()
    except Exception as e:
        log_print(f"\n[WARNING] An unknown exception has occured: {e}\n\n{traceback.format_exc()}", 4)
        beans = input("Type 1 to upload your logs!\n\n>>> ")
        if beans == "1" or beans == "":
            upload_logs(5)
        return choice1()


def main():
    try:
        log_print(f"{phrases[language]['run_from']} {current_directory}")
    except Exception:
        log_print("First time run detected.")
        change_language()
        log_print(f"{phrases[language]['run_from']}", 2)
    log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: main() subroutine executed", 1, False)
    print(random.choice(funny_messages))
    print(phrases[language]['menu_prompt'])
    save_json()

    choice1()


print("Done! Loading base data...")

desktop_install_path = False

if path.exists(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt"):
    log_print("[MainInit] InstallDir_Pref exists.", 2, False)
    desktop_dir = pathlib.Path.home() / 'Desktop'
    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
        install_dir = e.read()
        if install_dir == str(desktop_dir):
            log_print(f"Determined install_dir to be desktop @ {desktop_dir}")
            desktop_install_path = True
        log_print(f"[MainInit] Determined install_dir {install_dir}. Read from file InstallDir_Pref", 2, False)
else:
    log_print("[MainInit] Setting new file preference exists.", 2, False)
    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", 'w+') as f:
        f.close()
    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", 'w') as f:
        f.write(f"{DraggieTools_AppData_Directory}\n{build}")

log_print("[MainInit] Checking for update", 2, False)
check_for_update()

print("\nLoading Discord RPC...")


def start_discord_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(load_presence())


loop = asyncio.new_event_loop()
thread = threading.Thread(target=start_discord_event_loop, args=(loop,))
thread.start()


current_directory = path.dirname(path.realpath(__file__))
if dev_mode:
    log_print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: variable currrent_directory assigned with value {current_directory}")


try:
    print("Done! Entering program...")
    # pyi_splash.close()
    main()
except Exception as e:
    print(f"An unhandled exception was encountered.\nShort: {e}\n\nLong:\n{traceback.format_exc()}\n\nIt would be appreciated if you generate a logfile and DM it Draggie#3060. Thanks!\n")
    logging.error(traceback.format_exc())
    beans = input("Type 1 to upload your logs!\n\n>>> ")
    if beans == "1" or beans == "":
        upload_logs()
    main()
