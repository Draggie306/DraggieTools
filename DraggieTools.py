print("Loading modules...")

global build, client, stop_event, thread, use_slow_print_effect

import getpass
import sys
import time

build = 87
version = "0.9.1"
build_date = 1705783488
username = getpass.getuser()
current_exe_path = sys.executable
use_slow_print_effect = False

dev_mode = False

start_time = time.time()

import os
from os import environ, listdir, makedirs, mkdir, path, remove, startfile, system

system("chcp 65001")
system("title DraggieTools: Loading 35 modules...")


"""def print(text, end="\n", flush=True):
    sys.stdout.write(f"{text}{end}")"""


green_colour = "\033[92m"
red_colour = "\033[91m"
yellow_colour = "\033[93m"
blue_colour = "\033[94m"
orange_colour = "\033[33m"
cyan_colour = "\033[96m"
magenta_colour = "\033[95m"
reset_colour = "\033[0m"
lily_colour = "\033[95m"
clear_line = "\033[K"
up_one_line = "\033[F"
start_of_line = "\033[0G"
clear_from_line_start = "\033[1K"
clear_above_line_overwrite = "\033[F\033[K"
# modules = 1


def print_loading_message(module_name):
    # global modules
    # modules += 1
    sys.stdout.write("\033[K")
    sys.stdout.write(f"{green_colour}Loading module {module_name}...{reset_colour}")
    sys.stdout.flush()
    sys.stdout.write("\r")
    sys.stdout.flush()


print_loading_message("subprocess.Popen")
from subprocess import Popen

print_loading_message("datetime.datetime")
from datetime import datetime

print_loading_message("time.sleep, time.time, time.perf_counter")
from time import perf_counter, sleep, time

print_loading_message("uuid.uuid4")
import uuid
from uuid import uuid4

print_loading_message("tqdm.tqdm")
from tqdm import tqdm

print_loading_message("shutil.copyfile, shutil.SameFileError")
from shutil import SameFileError, copyfile, move

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
import threading
from threading import Event, Thread

print_loading_message("base64")
import base64

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

print_loading_message("subprocess")
import subprocess

print_loading_message("urllib.parse.urlsplit")
from urllib.parse import urlsplit

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

print_loading_message("psutil")
import psutil

print_loading_message("winshell")
import winshell

# import moviepy.editor
print_loading_message("nest_asyncio")
import nest_asyncio
nest_asyncio.apply()

print_loading_message("concurrent.futures")
from concurrent.futures import ThreadPoolExecutor, as_completed

print_loading_message("requests")
import requests

print_loading_message("io")
import io

# Codename Guide:
"""
DraggieTools: This file and binary exe
saturnian: Unity game
(Project)Lily: DraggieClient Downloader
dashNetworking: Fast, reliable, efficient, elegant, easy-to-use, custom netcode
Harry: Discord RPC

"""

end_time = time()

elapsed_time = end_time - start_time

quick_time = 1
alright_time = 2
slow_time = 3
very_slow_time = 5

if elapsed_time < quick_time:
    print(f"All modules loaded! Took {cyan_colour}{round(elapsed_time, 7)}s.{reset_colour}")
elif elapsed_time < alright_time:
    print(f"All modules loaded! Took {green_colour}{round(elapsed_time, 7)}s.{reset_colour}")
elif elapsed_time < slow_time:
    print(f"All modules loaded! Took {yellow_colour}{round(elapsed_time, 7)}s.{reset_colour}")
elif elapsed_time < very_slow_time:
    print(f"All modules loaded! Took {red_colour}{round(elapsed_time, 7)}s.{reset_colour}")


sys.stdout.write("\r")
sys.stdout.flush()
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

system(f"title DraggieTools v{version} (build {build}) initialised in {round(elapsed_time, 7)}s")

environ_dir = environ['USERPROFILE']

start_time = time()

client = None

phrases = {
    'english': {
        'menu_pre_options': f"{red_colour}NOTE! In Tools v1.0.0, we will be updating to a more friendly GUI-based system! The one you're seeing now is temporary and will look much better in the future.{reset_colour}\n\nItems in {magenta_colour}magenta{reset_colour} have been recently optimised.\nItems in {green_colour}green{reset_colour} are new, and may be being worked on.\nItems in {yellow_colour}yellow{reset_colour} are in early development.\n",
        'menu_options': f'[0] Quit\n[1] Manage installation\n[2] Refresh updates\n[3] Change language\n{yellow_colour}[4] Optimise Fortnite Settings{reset_colour}\n{green_colour}[5] Manage your Draggie Games Library{reset_colour}\n{yellow_colour}[6] Torrent Downloader{reset_colour}\n[7] Supercell Game Tools\n[8] Clean Up Files\n{magenta_colour}[9] Discord Utilities{reset_colour}\n{magenta_colour}[10] Install DraggieClient{reset_colour}\n[11] YouTube Downloader\n{magenta_colour}[12] Bank Files Extractor{reset_colour}\n[13] VideoMaker\n[14] VBS Script Launcher\n\n[dev] Open Developer Menu\n[log] Upload logs  \n\n>>> ',
        'key_error': 'Key error occurred: ',
        'backup': '\n\nResorting to backup',
        'downloading': 'Downloading.',
        'done_speed': 'done, average speed',
        'check_update': 'Checking for update...',
        'download_update': 'Downloading update...',
        'run_from': '\nRunning from',
        'menu_prompt': f'\n{green_colour}What would you like to do, my friend?\n',
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
        'select_options': "Select options:\n\n1) See basic info and fingerprint hash\n2) Compare music to old version and extract changes\n3) Compare files to another version\n4) Download all background music files\n5) Download all files containing a string\n6) Open this archive's downloaded file folder\n0) Go back   \n\n>>> ",
        'read_info_from_file': "Read the following information from file",
        'amount_of_files': "Amount of assets",
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
        'menu_pre_options': f"Les éléments en {magenta_colour}magenta{reset_colour} ont été récemment optimisés. Les éléments en {green_colour}vert{reset_colour} sont nouveaux et peuvent être en cours de développement.\nLes éléments en {yellow_colour}jaune{reset_colour} sont en développement précoce.\n{red_colour}NOTE ! Dans les outils v1.0, nous allons passer à un système plus convivial basé sur l'interface graphique ! (Ceci est temporaire !){reset_colour}",
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
        'menu_options': '\n\n[0] Quitter\n[1] Installer sur le bureau\n[2] Installer dans un répertoire personnalisé\n[3] Actualiser les mises à jour\n[4] Changer de langue\n[5] Voir le code source\n[6] Modifier les paramètres de Fortnite\n[7] ProjectSaturnian\n[8] Téléchargeur de torrents\n[9] Extracteur AutoBrawl\n\n>>> ',
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
        log(f"[LocalisedText] Error occurred when getting localised string: {e}\n{traceback.format_exc()}", 4)
        return key


default_draggietools_settings = {
    "ydl_default_dir": None,
    "auto_update": True,
}


def slow_print(text, end="\n", flush=True):
    """
    Gives the illusion of text being typed out slowly.
    """
    for char in text:
        sleep(random.uniform(0.01, 0.05))
        print(char, end="", flush=True)
    print(end=end, flush=flush)


def set_draggietools_setting(setting: str, value: str) -> bool:
    """
    Sets a setting in the DraggieTools settings file. If the setting does not exist, it will be created.\n
    :param setting: The setting to set\n
    :param value: The value to set the setting to\n
    """
    settings_dir = f"{DraggieTools_AppData_Directory}\\tools_settings.json"
    if not path.exists(settings_dir):
        with open(settings_dir, "w") as f:
            log(f"[DraggieToolsSettings] Settings file not found. Creating one at {settings_dir}", 2, True)
            json.dump(default_draggietools_settings, f, indent=4)
    with open(settings_dir, "r") as f:
        data = json.load(f)
    data[setting] = value
    with open(settings_dir, "w") as f:
        json.dump(data, f, indent=4)
    return True


def get_draggietools_setting(setting: str) -> str | None:
    """
    Gets a setting from the DraggieTools settings file. If the setting does not exist, it will be created.\n
    :param setting: The setting to get\n
    """
    settings_dir = f"{DraggieTools_AppData_Directory}\\tools_settings.json"
    if not path.exists(settings_dir):
        with open(settings_dir, "w") as f:
            json.dump(default_draggietools_settings, f, indent=4)
    with open(settings_dir, "r") as f:
        data = json.load(f)

    if setting not in data:
        log(f"[DraggieToolsSettings] Setting {setting} not found in settings file. Returning None.", 3, True)
        return None
    return data[setting]


funny_messages = [
    r"Problem opening the application running at executable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Would you like to scan this PC?",
    "Please enter your credit card number for a free trial",
    "Transferring sensitive files to The Criminal Network...",
    "Your computer is hacked by IP: 5.172.193.104 like OS: LINUX/KALI LINUX and location: RUSSIAN FEDERATION",
    "Your internet connection will be disconnected in 10 seconds.",
    "You have just won a lifetime supply of spam emails. Congratulations!",
    "Waiting for the system to crash. Please be patient...",
    "Insufficient funds. Please go rob a bank and try again",
    r"Reading your emails... 0% complete..",
    r"Reading Chrome Browser history... 67% complete..",
    r"Reading Chrome Browser passwords... 100% complete..",
    r"Uploading your files to The Criminal Network... 100% complete..",
    r"Downloading your files from The Criminal Network... 100% complete..",
    "The Criminal Network has been hacked. Please wait while we transfer all your files to the FBI...",
    "Your computer has been upgraded to Windows 98. Enjoy the nostalgia!",
    "Warning: this program has been known to cause spontaneous dancing",
    "Your hard drive is full. Please delete all your files, including the ones you actually need",
    "Critical alert from Microsoft: your computer has been infected with a virus. Please call 1-800-SCAMMER to fix this issue",
    "Congratulations, you have been selected to participate in our new program: 'Extreme Keyboard Smashing'",
    "Your computer has been selected to be the host of the next big cyber attack",
    "Viruses detected. Please wait while we delete System32...",
    "Malware has been detected on your computer. Transferring sensitive files to The Criminal Network...",
    r"Encrypting all your files... 32% complete..",
    "UwU, what's this? A virus? OwO",
    "Glizzy Gladiator is now running in the background. Please do not close this window",
    "Your keyboard has been upgraded to a potato. You're welcome!",
    "Insufficient disk space. Please delete all your selfies and try again",
    r"Making a backup of your files... 0% complete..",
    "Make your computer easier to see. Enable the magnifier at Settings > Ease of Access > Magnifier",
    "Congratulations! You have just won a free trip to the blue screen of death",
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
    print(f"[MainInit] Made DraggieTools_AppData_Directory Logs: {DraggieTools_AppData_Directory}\\Logs")

if not path.exists(DraggieTools_AppData_Directory):
    mkdir(DraggieTools_AppData_Directory)
    print(f"[MainInit] Made DraggieTools_AppData_Directory: {DraggieTools_AppData_Directory}")

if not path.exists(f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache"):
    mkdir(f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache")
    print(f"[MainInit] Made UpdatedBuildsCache Directory: {DraggieTools_AppData_Directory}\\UpdatedBuildsCache")

if not path.exists(f"{DraggieTools_AppData_Directory}\\SourceCode"):
    mkdir(f"{DraggieTools_AppData_Directory}\\SourceCode")
    print(f"[MainInit] Made SourceCode Directory: {DraggieTools_AppData_Directory}\\SourceCode")


print(f"{clear_above_line_overwrite}Loading functions...")


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


def log(text, log_level: Optional[int] = 2, output: Optional[bool] = True, stacklevel: Optional[int] = None, component: Optional[str] = None, event: Optional[str] = None, raw: Optional[bool] = False):
    global use_slow_print_effect
    if raw:
        print(text, flush=True)
        log(f"[CalledRaw] {text}", 1, False, stacklevel=stacklevel)

    if not stacklevel:
        stacklevel = 1

    if component:
        if component.lower() == "dash":
            text = f"[dashNetworking] {text}"
        elif component.lower() == "main":
            text = f"[Main] {text}"
        elif component.lower() == "updater":
            text = f"[Updater] {text}"

    if output and not raw:
        if use_slow_print_effect:
            slow_print(text)
        else:
            print(text)
    else:
        if log_level == 1:
            if dev_mode:
                print(f"{cyan_colour}[dev debug]: {text}{reset_colour}")

    text = f"{datetime.now().strftime(r'[%d/%m/%Y %H:%M:%S.%f]').ljust(30)} | {text}"

    match log_level:
        case 1:
            log_prefix = "DEBUG"
            logging.debug(msg=f"{log_prefix}: {text}", stacklevel=stacklevel)
        case 2:
            log_prefix = "INFO"
            logging.info(msg=f"{log_prefix}: {text}", stacklevel=stacklevel)
        case 3:
            log_prefix = "WARNING"
            logging.warning(msg=f"{log_prefix}: {text}", stacklevel=stacklevel)
        case 4:
            log_prefix = "ERROR"
            logging.error(msg=f"{log_prefix}: {text}", stacklevel=stacklevel)
        case 5:
            log_prefix = "CRITICAL"
            logging.critical(msg=f"{log_prefix}: {text}", stacklevel=stacklevel)
        case _:
            log_prefix = "INFO"
            logging.info(msg=f"{log_prefix}: {text}", stacklevel=stacklevel)

    if event:
        if event == "Success":
            colour = green_colour
        elif event == "Warning":
            colour = yellow_colour
        elif event == "Error":
            colour = red_colour
        else:
            colour = blue_colour
        text = f"{colour}{text}{reset_colour}"


async def harry_loader():
    """
    Codename: Harry\n
    Loads the Discord rich presence
    """
    harry_client_id = 1076873298501173269
    try:
        global client
        client = Presence(harry_client_id)

        client.connect()
        status_update()
        log("[Harry/load] Presence loaded", 2, False)
    except Exception as e:
        log(f"[Harry/load] Unable to load the Discord rich presence: {e}", 4, False)


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
            return log("[Harry/update] Not updating status due to Discord not being present.", 3, False)
    except Exception as e:
        return log(f"[Harry/update] Unable to update the Discord rich presence: {e}", 4, False)





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


def get_first_line_of_term(search_phrase, file, return_line_string: Optional[bool] = False) -> int | str | None:
    with open(file, 'r', encoding="UTF-8") as f:
        line_num = 0
        for line in f.readlines():
            line_num += 1
            if line.find(search_phrase) >= 0:
                if return_line_string:
                    return line
                return (int(line_num))
    return None


def replace_line(file_name, line_num, text):
    line_num = line_num - 1
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


"""
try:
    x = dash_get("https://client.draggie.games")
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


class CustomTqdm(tqdm):
    def format_meter(self, *args, **kwargs):
        kwargs['n_fmt'] = f"{kwargs['n'] / 1024:,.3f}"
        kwargs['total_fmt'] = f"{kwargs['total'] / 1024:,.3f}"
        return super().format_meter(*args, **kwargs)


def tqdm_download(download_url, save_dir, desc: Optional[str] = None, overwrite: Optional[bool] = False, return_exceptions: Optional[bool] = False):
    # Networking component codename is dash
    def download_file(download_url, save_dir, desc: Optional[str] = None):
        response = dash_get(download_url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024  # 1 Kibibyte
        desc = download_url.split("/")[-1] if desc is None else desc
        # print(f"desc: {desc}")
        custom_bar_format = "{desc} - {percentage:3.2f}% |{bar}| ({n_fmt}MiB / {total_fmt}MiB @ {rate_fmt}) [{elapsed} elapsed, {remaining} remaining]{postfix}"
        with open(save_dir, "wb") as f:
            for data in CustomTqdm(response.iter_content(block_size), total=ceil(total_size // block_size), unit="KB", desc=desc, bar_format=custom_bar_format):
                f.write(data)
        print(reset_colour)
        log(f"[TQDM] Downloaded the file! {total_size} bytes. ({download_url})", 1, False, component="dash")

    if return_exceptions:
        download_file(download_url, save_dir, desc)
    else:
        try:
            if not path.exists(save_dir):
                os.makedirs(path.dirname(save_dir), exist_ok=True)
                log(f"Created directory {path.dirname(save_dir)}", 2, False, component="dash")
            download_file(download_url, save_dir, desc)
        except KeyboardInterrupt:
            log("Keyboard interrupt: going back to first choice.", 3, False, component="dash")
            return choice1()
        except Exception as e:
            log(f"\n[TQDMDownloadError] An error has occurred downloading the file. {download_url}\n{e}\n{traceback.format_exc()}", 4, component="dash")


def dash_get(*args, **kwargs):
    """
    Drop in replacement for requests.get that uses the logging system.
    """
    # Networking component codename is dash
    log(f"Getting data from: ({args[0]})", 1, False, component="dash")

    x = requests.get(*args, **kwargs)
    log(f"GET request returned with status code {x.status_code}. ({args[0]})", 1, False, component="dash")
    return x


def dash_post(*args, **kwargs):
    """
    Drop in replacement for requests.post that uses the logging system.
    """
    # Networking component codename is dash
    log(f"POSTing data to: ({args[0]})", 1, False, component="dash")
    x = requests.post(*args, **kwargs)
    log(f"POSTing data returned with status code {x.status_code}. ({args[0]})", 1, False, component="dash")
    return x


def download_chunk(url, start, end, save_dir, pbar):
    """
    Downloads a chunk of a file.
    """
    headers = {'Range': f'bytes={start}-{end}'}
    response = dash_get(url, headers=headers, stream=True)
    with open(f"{save_dir}.part{start}", "wb") as f:
        for data in response.iter_content(1024):
            f.write(data)
            pbar.update(len(data))


def tqdm_download2(download_url, save_dir, desc=None, num_threads: Optional[int] = 4):
    response = dash_get(download_url, stream=True)
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

    with open(save_dir, "wb") as f:  # merge the chunks
        for i in range(num_threads):
            with open(f"{save_dir}.part{i * chunk_size}", "rb") as part_file:
                f.write(part_file.read())
            os.remove(f"{save_dir}.part{i * chunk_size}")


def change_language() -> str:
    global language, language_chosen
    language = None
    while language is None:
        status_update(details="Choosing language", state="English or French?")
        x = input("\n\n\n\nChoose a language! Input the number and hit enter.\nChoisissez une langue ! Entrez le numéro et appuyez sur Entrée.\n\n[1] English\n[2] Français\n\n>>> ")
        lang_pref_dir = f"{DraggieTools_AppData_Directory}\\Language_Preference.txt"
        if x == "2":
            log("La langue est maintenant le français !")
            language = 'french'
            with open(lang_pref_dir, "w+", encoding="UTF-8") as x:
                x.close()
            log(f"File at path '{lang_pref_dir}' cleared")
            with open(lang_pref_dir, "w", encoding="UTF-8") as x:
                x.write("french")
                x.close()
            log(f"File at path '{lang_pref_dir}' written with 'French'")
            language_chosen = "french"
        else:
            log("The language has been set to English!")
            language = 'english'
            with open(lang_pref_dir, "w+", encoding="UTF-8") as x:
                x.close()
            log(f"File at path '{lang_pref_dir}' cleared")

            with open(lang_pref_dir, "w") as x:
                x.write("english")
                x.close()
            log(f"File at path '{lang_pref_dir}' written with 'English'")
            language_chosen = "english"
    status_update(details="Choosing language", state=f"Set language to {language_chosen}!")
    sleep(0.1)
    if dev_mode:
        log(f"Language successfully changed to {language_chosen}")
    return language_chosen


def get_language() -> str:
    """Returns the user's language. Currently `english` or `french`.\nIf the language file doesn't exist, it will be created."""
    if path.exists(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt"):
        try:
            with open(f"{DraggieTools_AppData_Directory}\\Language_Preference.txt", encoding="UTF-8") as x:
                language_read = x.read()

            if language_read == "french":
                language = 'french'
                log("Langue mise a jour: francais.")
            else:
                language = 'english'
                log(f"{clear_above_line_overwrite}Language set to English.")
        except Exception:
            language = change_language()
    else:
        log("[get_language] Language file doesn't exist when checking, using blocking change_language function", 3, False)
        language = change_language()
    return language

# clear_above_line_overwrit - run 50 times


temp = 0
while temp < 50:
    print(f"\r{clear_above_line_overwrite}", end="")
    temp += 1

language = get_language()
log(f"[MainInit] Language set to {language}", 2, False)


def cmini_extraction():
    log("Entering cmini_extraction function for Bank File Extraction", 2, False)
    bankfilepath = input(f"Enter the {lily_colour}INPUT PATH{reset_colour}. This is the folder containing the .bank files you wish to extract.\nIf you do not have this, you can search for them using AutoBrawlExtractor (option 9).\n\n>>> ")
    outputpath = input(f"Now, enter the {lily_colour}OUTPUT PATH{reset_colour}. This is where the extracted files will be placed.\n\n>>> ")
    os.makedirs(outputpath, exist_ok=True)

    utils_path = os.path.join(outputpath, ".utils")
    if not os.path.exists(utils_path):
        log("Dependencies don't seem to be present. Downloading to .utils folder...", 1, False)
        using_ibaguette = False

        utils_path = outputpath + r"\.utils"  # create a folder called .utils in the output directory
        makedirs(utils_path, exist_ok=True)
        archive_link = "https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/Addons/bankFileExt/.utils.zip" if not using_ibaguette else \
            "https://cdn.ibaguette.com/cdn/Tools/bankFileExt/.utils.zip"
        log(f"Downloading utility prerequisite files to {utils_path} directory...", 1, True)
        tqdm_download(archive_link, utils_path + r"\.utils.zip")
        with open(utils_path + r"\.utils.zip", 'rb') as zip_ref:
            with zipfile.ZipFile(zip_ref, 'r') as zip:
                zip.extractall(utils_path)
        log(f"All files downloaded! Utils path = {utils_path}", 1, False)

    quickbms_exe = utils_path + r"\quickbms.exe"
    fsb_aud_extr_exe = utils_path + r"\fsb_aud_extr.exe"
    bmsfile = utils_path + r"\Script.bms"

    # batchfile limitation: below must be in the same directory as the fsb files
    move(utils_path + r"\fsb_dec.bat", outputpath + r"\fsb_dec.bat")  # source THEN destination

    batchfile = outputpath + r"\fsb_dec.bat"
    log(f"batchfile_path: {batchfile}", output=False)

    # Check if all the files exist

    if not os.path.isfile(quickbms_exe) or not os.path.isfile(bmsfile) or not os.path.isfile(batchfile) or not os.path.isfile(fsb_aud_extr_exe):
        log("Missing files, redownloading...", 2, False)
        for file in os.listdir(utils_path):
            log(f"Deleting {file}...", 2, True)
            os.remove(os.path.join(utils_path, file))
        os.rmdir(utils_path)
        cmini_extraction()
        return

    # Replace content in batchfile to match the path to the fsb_aud_extr.exe file

    target_string = 'D:\\Supercell Extraction Tools\\Bank Files (to wav)\\bank files\\fsb_aud_extr.exe'
    replacement_string = fsb_aud_extr_exe

    with open(batchfile, 'r') as file:
        file_contents = file.read()
        modified_contents = file_contents.replace(target_string, replacement_string)

    with open(batchfile, 'w+') as file:
        log(f"Writing to batchfile: {modified_contents}", 2, False)
        file.write(modified_contents)

    # Execute the quickbms extractor file with parameters

    command = f'& "{os.path.normpath(quickbms_exe)}" -d "{os.path.normpath(bmsfile)}" "{os.path.normpath(bankfilepath)}" "{os.path.normpath(outputpath)}"'
    log(f"Executing command: {command}")

    # Start the subprocess and hide the window

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    proc = subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command", command], stdout=subprocess.PIPE, startupinfo=startupinfo)

    # Wait for the subprocess to complete and get the output

    output = proc.communicate()[0]
    output_str = output.decode()

    # log the output

    log(output_str, 1)
    log(f"Completed extraction of .fsb files from .bank files. Output path: {outputpath}", 2, True)

    # Run the batchfile

    log("Running batchfile to extract all the files from the fsb files...", 2, False)
    with open(batchfile, "r") as file:
        file_contents = file.read()
        log(f"Batchfile contents: {file_contents}", 2, False)

    log(f"{magenta_colour}Executing command with subprocess.Popen: {batchfile}. working directory is {outputpath}", 2, True)
    start_anim_loading(f"{magenta_colour}Extracting waveform files from FSB... this make take some time...")
    log(f"Full command: \n{batchfile}\nstdout: {proc.stdout}\ncwd: {outputpath}", 2, False)

    proc = subprocess.Popen([batchfile], stdout=subprocess.PIPE, cwd=outputpath)
    output = proc.communicate()[0]
    output_str = output.decode()
    stop_anim_loading()
    log(f"{green_colour}Extracting all was successfully completed.\n\nLog of files extracted:\n------\n{output_str}\n------\n", 2, True)

    log("Performing additional cleanup...", 2, True)

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
                    wav_filename = os.path.basename(os.path.normpath(dst_dir))
                    grandparent_foldername = os.path.basename(os.path.normpath(os.path.dirname(dst_dir)))
                    grandparentdir = os.path.dirname(os.path.dirname(dst_dir))

                    log(f"Wav filename: {wav_filename}, grandparent foldername: {grandparent_foldername}, grandparent directory: {grandparentdir}", 2, False)
                    log(f"Attempting to move {os.path.join(root, file)} to {grandparentdir + file}", 1, False)
                    shutil.move(os.path.join(root, file), os.path.join(grandparentdir, file))

                    log(f"{green_colour}Moved {os.path.join(root, file)} to {grandparentdir + file}", 2, True)
                    wavfiles = wavfiles + 1

                    if len(os.listdir(root)) <= 1:
                        log("the root is only one file, removing the directory...")
                        shutil.rmtree(root, ignore_errors=True)
                        oldpaths = oldpaths + 1
                    """if len(os.listdir(os.path.dirname(root))) <= 1:
                        log(f"the parent directory {os.path.dirname(root)} is only one file, removing the directory...")
                        shutil.rmtree(os.path.dirname(root), ignore_errors=True)
                        oldpaths = oldpaths + 1"""
            except Exception as e:
                log(f"Error while moving file: {e}", 3, True)

    # check for bank folders and remove them

    for file in os.listdir(outputpath):
        if file.endswith(".bank"):
            log(f"Removing bank folder {os.path.join(outputpath, file)}", 2, True)
            shutil.rmtree(os.path.join(outputpath, file), ignore_errors=True)
            oldpaths = oldpaths + 1

    # check for empty directories and remove them from root directory
    # this is to avoid empty folders in output/folder/empty_folder

    for root, dirs, files in os.walk(outputpath):
        for dir in dirs:
            if len(os.listdir(os.path.join(root, dir))) == 0:
                log(f"Removing empty directory {os.path.join(root, dir)}", 2, True)
                shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
                oldpaths = oldpaths + 1

    log("Additional cleanup completed!", 2, True)
    log(f"\n.wav files created: {wavfiles}\nPaths prettified: {oldpaths}", 2, True)

    open_in_explorer = input("Open the output folder in explorer? (y/n): ") # nice to have, but not necessary
    if open_in_explorer == "y":
        os.startfile(outputpath)
    log("Done!", 1, True)


# end of cmini function. phew! that was a lot of code. finished at 11:30pm


def download_update(current_build_version):
    try:
        if not path.exists(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds'):
            mkdir(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds')

        try:
            tqdm_download("https://github.com/Draggie306/DraggieTools/raw/main/dist/DraggieTools.exe", f"{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe")
        except Exception as e:
            log(f"Unable to download the update from raw GitHub. Trying from the custom Draggie Games content delivery network. {e}", 3, False)
            tqdm_download("https://tools.draggie.games", f"{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe")

        with open(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt", "w") as file:
            file.write(f"{sys.executable}")
            file.close()
            log(f"Old executable directory saved to {Draggie_AppData_Directory}\\OldExecutableDir.txt", 2, False)

    except Exception as e:
        log(f"Some error occured: {e}\n\nResorting to fallback method. Preferences will not be used, saving to default directory.")
        log(f"{traceback.format_exc()}", 4, False)
        log(f"{language[0]}{e}{language[1]}")
        r = dash_get('https://tools.draggie.games')
        with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
            f.write(r)

        try:
            with open(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt", "w") as file:
                file.write(f"{sys.executable}")
                file.close()
            log(f"Old executable directory saved to {Draggie_AppData_Directory}\\OldExecutableDir.txt", 2, False)
        except Exception as e:
            log(f"Unable to save old executable directory to {Draggie_AppData_Directory}\\OldExecutableDir.txt. {e}, {traceback.format_exc()}", 4, False)


def secret_menu():
    log("Welcome to the secret menu.")
    x = input("[1] = The.Batman.2022.1080p.WEBRip.x264.AAC5.1-[YTS.MX]\n[2] = Batman.The.Dark.Knight.2008.1080p.BluRay.x264.YIFY\n\n>>> ")

    index = dash_get("https://awtd.ibaguette.com/index.beans").content
    lines = index.splitlines()

    if x == "1":
        download_url = str(lines[1]).strip("b'").strip("'")
    else:
        download_url = str(lines[0]).strip("b'").strip("'")

    response = dash_get(download_url, stream=True)
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
    try:
        import libtorrent as lt
    except ImportError as e:
        log(f"Unable to import libtorrent. {e}\nPlease compile it yourself and put it in the same directory as DraggieTools.exe", 4, True)

    def download_torrent(magnet_link):
        # Create a session
        session = lt.session({'listen_interfaces': '0.0.0.0:6881'})

        # Get torrent info from the magnet link
        torrent_info = lt.torrent_info(magnet_link)

        # Add torrent to the session
        torrent_handle = session.add_torrent({'ti': torrent_info, 'save_path': '.'})

        # Get the status of the torrent
        torrent_status = torrent_handle.status()

        print('Starting download:', torrent_status.name)

        # While the torrent is not seeding (i.e., it's still downloading)
        while not torrent_status.is_seeding:
            torrent_status = torrent_handle.status()

            print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                torrent_status.progress * 100, torrent_status.download_rate / 1000, torrent_status.upload_rate / 1000,
                torrent_status.num_peers, torrent_status.state), end=' ')

            # Check for alerts
            alerts = session.pop_alerts()
            for alert in alerts:
                if alert.category() & lt.alert.category_t.error_notification:
                    print(alert)

            sys.stdout.flush()

            time.sleep(1)

        print(torrent_handle.status().name, 'download complete')


def cleanup_files():
    # Get the current time in seconds
    current_time = time()
    file_amount = 0

    things_to_delete = input("Over time, your use of DraggieTools might create additional files.\nWhat do you want to delete?\n\n[1] = Logs\n[2] = UpdatedBuilds\n[3] = UpdatedBuildsCache\n[4] = SourceCode\n[5] = Downloaded Builds from ABS\n[6] Project Saturnian Data\n[7] = All\n\n>>> ")
    dir_paths = None
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
        dir_paths = [f"{Draggie_AppData_Directory}\\Saturnian"]
    elif things_to_delete == "7":
        dir_paths = [f"{DraggieTools_AppData_Directory}\\Logs",
                     f"{DraggieTools_AppData_Directory}\\UpdatedBuilds",
                     f"{DraggieTools_AppData_Directory}\\UpdatedBuildsCache",
                     f"{DraggieTools_AppData_Directory}\\SourceCode",
                     f"{Draggie_AppData_Directory}\\AutoBrawlExtractor\\DownloadedBuilds"
                     ]
    upload_log = None
    if not dir_paths:
        return log("[FileCleanup] No directories to delete from.", log_level=3)
    # Loop through all the directories

    for dir in dir_paths:
        if path.exists(dir):
            log(f"[FileCleanup] Inspecting directory {dir}.")
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
                    log(f"[FileCleanup] Cleaned up file at {file_path}")
                    file_amount += 1
        else:
            log("Skipped directory as it doesn't exist.")
        sleep(0.2)

    log(f"[FileCleanup] Purged {file_amount} file(s).")


def view_source():
    log(phrases[language]['downloading_opening'])
    x = time()
    r = dash_get('https://raw.githubusercontent.com/Draggie306/DraggieTools/main/DraggieTools.py')
    with open(f'{DraggieTools_AppData_Directory}\\SourceCode\\DraggieTools-v{version}-{build}-{x}.py', 'wb') as f:
        f.write(r.content)
    Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\SourceCode\\DraggieTools-v{version}-{build}-{x}.py"')


def fort_file_mod():
    fort_ini_directory = (f"{environ_dir}\\AppData\\Local\\FortniteGame\\Saved\\Config\\WindowsClient\\GameUserSettings.ini")
    if not path.isfile(fort_ini_directory):
        return log("Unable to detect the INI settings file. Please run Fortnite at least once to generate this file.", log_level=3)

    log(f"Established uplink with {fort_ini_directory}")

    log("What would you like to do?\n[0] Go back\n[1] Open the file in explorer\n[2] Modify framerate settings\n[3] Modify graphics settings\n[4] Select optimisations\n>>> ")

    y = input("\n\n>>> ")

    match y:
        case "0":
            return
        case "4":
            cosmetic_streaming = get_first_line_of_term("CosmeticStreamingEnabled=", fort_ini_directory, return_line_string=True)
            if "CodeSet_Disabled" not in cosmetic_streaming:
                # always ask for user confirmation before modifying the file
                log("Cosmetic streaming is enabled. This downloads cosmetics in the background, which can cause lag spikes.\nWould you like to disable it? (y/n)")
                cosm_choice = input("\n\n>>> ")
                match cosm_choice:
                    case "y":
                        replace_line(fort_ini_directory, cosmetic_streaming, "CosmeticStreamingEnabled=CodeSet_Disabled\n")
                        log("Disabled cosmetic streaming!")
                    case _:
                        log("Okay, not disabling cosmetic streaming.")
            else:
                log("Cosmetic streaming is disabled. This downloads cosmetics in the background, which can cause lag spikes")

            preferred_rendermode = get_first_line_of_term("PreferredRHI", fort_ini_directory, return_line_string=True)
            if "dx12" not in preferred_rendermode.lower():
                log("DX12 is not enabled. This can be beneficial for performance on some (newer) hardware, and unlock more advanced graphics settings.\nWould you like to enable it? (y/n)")
                dx12_choice = input("\n\n>>> ")
                match dx12_choice:
                    case "y":
                        replace_line(fort_ini_directory, preferred_rendermode, "PreferredRHI=dx12\n")
                        log("Enabled DX12!")
                    case _:
                        log("Okay, not enabling DX12.")

            vsync = get_first_line_of_term("bUseVSync=", fort_ini_directory, return_line_string=True)
            if "false" not in vsync.lower():
                log("VSync is enabled. This can cause input lag.\nWould you like to disable it? (y/n)")
                vsync_choice = input("\n\n>>> ")
                match vsync_choice:
                    case "y":
                        replace_line(fort_ini_directory, vsync, "bUseVSync=False\n")
                        log("Disabled VSync!")
                    case _:
                        log("Okay, not disabling VSync.")

        case "1":
            Popen(f'explorer /select,"{fort_ini_directory}"')
        case "2":
            z = input("Okay, what type of framerate?\n\n1) FrameRateLimit (In-game and lobby) - note this will be priority over all other settings\n2) FrontendFrameRateLimit (Max Lobby FPS)\n\n>>> ")
            if z == "1":
                try:
                    fps = int(input("Input desired FPS here:\n\n>>> "))
                except ValueError:
                    log("Disallowed input. Try again")
                    return main()

                x = get_first_line_of_term("FrameRateLimit=", fort_ini_directory)

                replace_line(fort_ini_directory, x, f'FrameRateLimit={fps}.000000\n')

                log(f"Modified config FrameRateLimit in section [/Script/FortniteGame.FortGameUserSettings], line {x}")

            if z == "2":
                try:
                    fps = int(input("Input desired FPS here:\n\n>>> "))
                except ValueError:
                    log("Disallowed input. Try again")
                    return main()

                x = get_first_line_of_term("FrontendFrameRateLimit=", fort_ini_directory)
                log(f"first line of the codees = {x}")

                replace_line(fort_ini_directory, x, f'FrontendFrameRateLimit={fps}\n')
                logging.debug(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: main/fort_file_mod: {fort_ini_directory} has been modified! FrontendFrameRateLimit={fps}")
                logging.debug(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: main/fort_file_mod: {fort_ini_directory} has been modified! FrontendFrameRateLimit={fps}")
                log("Successfully modified config FrontendFrameRateLimit in section [/Script/FortniteGame.FortGameUserSettings]")

        case "3":
            graphics_settings = ["Low", "Medium", "High", "Epic"]
            eligible_settings = [
                ["3D Resolution", "View Distance", "Shadows", "Post Processing", "Textures", "Effects", "(hidden) Foliage", "(hidden) Shading", "Anti Aliasing", "(RTX only) Global Illumination", "(RTX only) Reflections"],
                ["sg.ResolutionQuality", "sg.ViewDistanceQuality", "sg.ShadowQuality", "sg.PostProcessQuality", "sg.TextureQuality", "sg.EffectsQuality", "sg.FoliageQuality", "sg.ShadingQuality", "sg.AntiAliasingQuality", "sg.GlobalIlluminationQuality", "sg.ReflectionQuality"]
            ]

            other_settings = [
                ["Culture", "Using DX12", "Using GPU Crash Debugging", "Ray Tracing", "Performance Mode Mesh Quality"],
                ["Culture", "bUseD3D12InGame", "bUseGPUCrashDebugging", "r.RayTracing.EnableInGame", "MeshQuality"]
            ]

            log("Reading graphics settings and quality presets...")

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
                        log(f"{eligible_settings[0][i]} = {quality_level}%")
                    else:
                        log(f"{eligible_settings[0][i]} = {graphics_settings[quality_level]}")
                    sleep(0.05)
                except Exception as e:
                    log(f"Could not find the value associated with {eligible_settings[0][i]} - {e}")

            log("\nSearching for other settings...\n")

            for i in range(len(other_settings[1])):
                try:
                    x = get_first_line_of_term(f"{other_settings[1][i]}=", fort_ini_directory)
                    with open(fort_ini_directory, "r") as ini_file:
                        lines = ini_file.readlines()
                        target_line = (lines[x - 1])

                    quality = target_line.split("=")
                    quality = quality[1].split("\n")
                    quality_level = (quality[0])

                    log(f"{other_settings[0][i]} is set to '{quality_level}'")
                except Exception as e:
                    log(f"Could not find the value associated with {other_settings[0][i]} - {e}")

            choice2 = input("\n\n1) Go back\n2) Modify a value\n\n>>> ")

            if choice2 != "2":
                return
            else:
                log("Default values are 0 for LOW/OFF\n1 for MEDIUM\n2 for HIGH\n3 for EPIC")
                log("\nOk, what would you like to change?")
    main()


def check_for_update():
    try:
        log(phrases[language]['check_update'], 2, True)
    except Exception:
        change_language()
        check_for_update()
    try:
        if path.isfile(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt"): # OverwriteOldVersion
            log(f"[OverwriteOldVersion] {Draggie_AppData_Directory}\\OldExecutableDir.txt exists!", 1, False)
            with open(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt", "r") as file:
                old_sys_exe = file.read()
                file.close()
            if old_sys_exe == str(sys.executable):
                log("[WARNING] The update cannot be applied to the current directory as you are running the file in the same place! Please download the update and wait for it to be closed.", 4)
            else:
                log("[OverwriteOldVersion] Removing OldExeDir.txt")
                remove(f"{Draggie_AppData_Directory}\\OldExecutableDir.txt")
                log("[OverwriteOldVersion] Removing old exe")
                remove(old_sys_exe)
                log("[OverwriteOldVersion] Copying current exe to old sys exe")
                copyfile(str(sys.executable), old_sys_exe)
                log(f"[OverwriteOldVersion] Copying current exe ({sys.executable}) to old sys exe ({old_sys_exe})")
        else:
            log("[OverwriteOldVersion] OldExeFile does not exist!", 3, False)
    except Exception as e:
        log(f"Unable to overwrite older version. {e}", 4)

    try:
        current_build_version = int((dash_get('https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/build.txt')).text)
    except Exception as e:
        log(f"\nUnable to check for update. {e}\n\nIt looks like the GitHub update servers might be blocked by your network! I'll still work, but some features might be limited.", 4)
        current_build_version = build
    if build < current_build_version: # if build is less than current version - so there's an update available.
        release_notes = str((dash_get(f"https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/Release%20Notes/release_notes_v{current_build_version}.txt")).text)
        log(f"\n{phrases[language]['update_available']} {phrases[language]['on_version']} {version} {phrases[language]['which_build']} {build}.\n{phrases[language]['newest_version_build']} {current_build_version}\n\n", event="success")
        if language == "english":
            versions_to_get = current_build_version - build
            if versions_to_get == 1:
                log(f"You're {versions_to_get} build behind latest")
            else:
                log(f"You're {versions_to_get} builds behind latest")

            string = (f"Latest release notes (v{current_build_version}):\n\n{release_notes}\n")

            while current_build_version != (build + 1):
                current_build_version = current_build_version - 1
                version_patch = str((dash_get(f"https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/Release%20Notes/release_notes_v{(current_build_version)}.txt")).text)
                string = (string + f"\nv{current_build_version}:\n{version_patch}\n\n")
            log(f"\n{string}\n")

        update_choice = input(f"{phrases[language]['press_enter_update']}\n\n>>> ")
        if update_choice != "":
            log("Skipping update.")
            return

        log(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {language[6]} - {DraggieTools_AppData_Directory}")
        download_update(current_build_version)
        log("Update downloaded. Launching new version...")
        if not desktop_install_path:
            startfile(f'{DraggieTools_AppData_Directory}\\UpdatedBuilds\\DraggieTools-{current_build_version}.exe')
        else:
            desktop_dir = pathlib.Path.home() / 'Desktop'
            startfile(f'{desktop_dir}\\DraggieTools-{current_build_version}.exe')
        sys.exit()

    if current_build_version < build:
        log(phrases[language]['newer_version'])
    else:
        log(f"{phrases[language]['running_version']} {version} - {phrases[language]['build']} {build} - {phrases[language]['at']} {datetime.fromtimestamp(build_date).strftime('%Y-%m-%d %H:%M:%S')}. {phrases[language]['server_says']} {current_build_version}.")


def maniupulate_brawl_file(dir, app_version: Optional[str] = None, arch_type: Optional[str] = None, app_name: Optional[str] = None, fingerprint_json: Optional[dict] = None, server_hostname: Optional[str] = None):
    # dir is the directory of the archive. Typically ends in .ipa or .apk, or .json (for fingerprint.json)
    # app_version is the version of the app, e.g. 36.270
    # Arch_type is either IPA or APK. This doesn't really matter, but formats can be different.
    # app_name is the name of the app, e.g. Brawl Stars
    # fingerprint_json is the fingerprint.json file as a dict. This will override all other parameters if it is not None.

    log(f"Parameters: dir={dir}, app_version={app_version}, arch_type={arch_type}, app_name={app_name}, fingerprint_json={bool(fingerprint_json)}, server_hostname={server_hostname}") if dev_mode else None

    app_version = str(app_version) if app_version else "Unknown version"
    server_hostname = None if not server_hostname else server_hostname

    download_urls = {
        "Brawl Stars": "game-assets.brawlstarsgame.com",
        "Boom Beach": "game-assets.boombeach.com",
        "Clash of Clans": "game-assets.clashofclans.com",
        "Clash Royale": "game-assets.clashroyaleapp.com",
        "Clash Mini": "game-assets.clashminigame.com",
    }

    for app in download_urls:
        if app_name is not None and app_name in app:
            server_hostname = download_urls[app]
            log(f"Found server hostname for {app_name}: {server_hostname}")
            break

    if not server_hostname:
        if "{'file': 'image/brawl_icon.png', 'sha': '1d4c42c9968153c3e220c1420ea87ecc62808afd'}" in fingerprint_json['files']:
            server_hostname = download_urls["Brawl Stars"]
        elif "font/BoomBeach.ttf" in fingerprint_json['files']:
            server_hostname = download_urls["Boom Beach"]
        elif "font/ClashofClans" in fingerprint_json['files']:
            server_hostname = download_urls["Clash of Clans"]

        log(f"\nCouldn't reliably find server hostname for {app_name}, please input the correct one if this is wrong.\nYou can press [enter] to continue with: '{server_hostname}')")
        log("Alternatively, here are the options:")

        iterations = 0
        for app in download_urls:
            iterations += 1
            log(f"{iterations}: {app}" if iterations != len(download_urls) else f"{iterations}: {app}", 1, True)

        server_hostname = input("\n\n>>> ")

        match server_hostname.lower():
            case "":
                log(f"Continuing with {server_hostname}")
            case "1":
                server_hostname = download_urls["Brawl Stars"]
            case "2":
                server_hostname = download_urls["Boom Beach"]
            case "3":
                server_hostname = download_urls["Clash of Clans"]
            case "4":
                server_hostname = download_urls["Clash Royale"]
            case "5":
                server_hostname = download_urls["Clash Mini"]
            case _:
                server_hostname = server_hostname
        log(f"Set base download URL to {server_hostname}")

    status_update(details="Extracting Supercell game assets", state=f"Loaded {app_name} v{app_version} ({arch_type})")
    game_download_url = server_hostname

    # "Select options:\n\n1) See basic info and fingerprint hash\n2) Compare music to old version and extract additions\n3) Compare files to another version\n4) Download all background music files\n5) Download all files containing a string\n6) Open this archive's downloaded file folder\n0) Go back   \n\n>>> ",
    x = input(phrases[language]['select_options'])
    match x:
        case "1":
            log(f"{l10n_text('read_info_from_file')}:\n{l10n_text('fingerprint_hash')}: {fingerprint_json['sha']}\n{l10n_text('amount_of_files')}: {len(fingerprint_json['files'])}\n\n")
        case "2":
            # Build index of current files in the directory
            json_files = []
            return log("Not implemented yet")
            for file in listdir(dir):
                if file.endswith(".json"):
                    json_files.append(file)
        case "3":  # this is the get list of new/modified/deleted files
            downloadedbuilds_appdata_dir = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
            amount_of_files = 0

            # Get secondary IPA files

            for i in listdir(downloadedbuilds_appdata_dir):
                amount_of_files = amount_of_files + 1

            log(f"\n[Enter] Select one of the {amount_of_files} downloaded files.")
            files = []
            f = 0

            for file in listdir(downloadedbuilds_appdata_dir):
                files.append(file)
            for i in files:
                log(f"[{f}] {i}")
                f += 1
            x = input("\nChoose file\n\n>>> ")
            ipa_2_dir = f"{downloadedbuilds_appdata_dir}\\{files[int(x)]}"

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
                        log(f"Found a modified file: {file_object['file']}")
                        modified_files_count += 1
                else:
                    new_files.append(file_object['file'])
                    log(f"Found a new file: {file_object['file']}")
                    new_files_count += 1

            for file2 in files2:
                file1 = next((file for file in files1 if file['file'] == file2['file']), None)
                if not file1:
                    deleted_files.append(file2['file'])
                    log(f"Found a deleted file: {file2['file']}")
                    deleted_files_count += 1

            # log('New files:', new_files)
            # log('Modified files:', modified_files)
            # log('Deleted files:', deleted_files)
            log(f"Found {new_files_count} new files, {modified_files_count} modified files and {deleted_files_count} deleted files.")
            log(f"COMPARED v{data1['version']} (StartPoint) to v{data2['version']} (OldVersion)")

            # now download the new and modified files

            choice_1 = input(f"\n{phrases[language]['download_new_files']}\n\n>>> ")

            if choice_1 == "1":
                log("ok")

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

                log(f"Downloaded {downloads} new files.")
                Popen(f"explorer {base_directory}")

            sleep(1)
        case "4":
            log("Not implemented yet")
        case "5":
            threads = int(input(phrases[language]['input_threads']))
            log(f"[AutoBrawlExtractor] Threads chosen to download: {threads}")
            search_term = input(phrases[language]['search_term_input'])
            x = input(f"{phrases[language]['search_all_archives']} '{search_term}' {phrases[language]['only_in_current_version']} {fingerprint_json['version']}\n\n>>> ")
            file_cycle = True if x == "1" else False
            hits = 0
            files = 0
            archives = 0
            skips = 0
            if not file_cycle:
                archives += 1
                with cf.ThreadPoolExecutor(max_workers=threads) as executor:
                    log("An executor has been loaded", 1, False)
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
                log(f"{phrases[language]['found']} {hits} {phrases[language]['matching_files']} {files} {phrases[language]['total_files_in']} {archives} {phrases[language]['available_archives']} {skips} {phrases[language]['files_already_exist']}")
                status_update(details=f"{phrases[language]['S_as']}", state=f"{files} {phrases[language]['S_as_1']} {hits} {phrases[language]['S_as_2']}")
                return maniupulate_brawl_file(dir=dir, app_version=app_version, arch_type=arch_type, app_name=app_name, fingerprint_json=fingerprint_json, server_hostname=server_hostname)

            available_archives = listdir(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
            for file in available_archives:
                log(f"Checked file '{file}' in {available_archives}")
                if not file.lower().endswith(".ipa") or file.lower().endswith(".zip") or file.lower().endswith(".json"):
                    log(f"{phrases[language]['unsupported_extension_1']} {file} {phrases[language]['unsupported_extension_2']}")
                    return choice1()
                with cf.ThreadPoolExecutor(max_workers=threads) as executor:
                    futures = []

                    log("An executor has been loaded", 1, False)

                    if not file.lower().endswith(".json"):
                        archive = zipfile.ZipFile(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds\\{file}", 'r')
                        archives += 1
                        log(f"{phrases[language]['searching_archive']} {file}")
                        new_fingerprint_json = str(archive.read(f'{app_name}res/fingerprint.json'), encoding="UTF-8")
                        new_fingerprint_json = json.loads(new_fingerprint_json)
                    else:
                        new_fingerprint_json = json.loads(file)
                    try:
                        fingerprint_sha = new_fingerprint_json["sha"]
                    except Exception as e:
                        log(f"Unable to find a valid fingerprint.json file in {file}.\n{e}")

                    for item in new_fingerprint_json['files']:
                        # log(f"Searching file: {item}", end='\r')
                        # log("\n")
                        files += 1
                        if search_term in item['file']:
                            log(f"Found '{search_term}' in file: {item}")
                            # The file field contains search_term
                            log(f"{phrases[language]['found']} {search_term} {phrases[language]['in_file']} {item['file']}")
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
                                log(f"{phrases[language]['not_downloading_exists']}{item['file']} {phrases[language]['not_downloading_exists_2']}")
                                skips += 1
                        else:
                            pass
                            # log(f"Unable to find the search term {search_term} in v{new_fingerprint_json['version']}: {item}")
            return maniupulate_brawl_file(dir=dir, app_version=app_version, arch_type=arch_type, app_name=app_name, fingerprint_json=fingerprint_json, server_hostname=server_hostname)
        case "6":
            Popen(f'explorer /select,"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{app_version}"')
        case _:
            autobrawlextractor()

    maniupulate_brawl_file(dir, app_version, app_name, arch_type, fingerprint_json=fingerprint_json, server_hostname=server_hostname)


def init_filetype(dir):
    """
    Initialises and checks the validity of the archive version provided. If the file provided is not valid, then the program will exit.\nMay return the game.
    """
    # remove ", ', from dir
    dir = dir.replace("'", "")
    dir = dir.replace('"', "")

    dir = os.path.abspath(dir)
    app_name = None
    try:
        if "fingerprint.json" in dir:
            with open(dir, "r") as json_file:
                fingerprint_json = json.loads(json_file.read())
            version_name = fingerprint_json['version']
            log(f"[init_filetype] Found fingerprint.json file! Version: {version_name}, files loaded: {len(fingerprint_json['files'])}]")
            maniupulate_brawl_file(dir, f"{version_name}", app_name=None, arch_type="fingerprint", fingerprint_json=fingerprint_json)
    except Exception as e:
        log(f"Unable to load fingerprint.json file. {e}", 4, True)
    archive = zipfile.ZipFile(dir, 'r')
    brawl_appdata_dir = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor")
    try:
        arch_type = None
        new_fingerprint_json = None
        game = None

        for file in archive.filelist:
            # log(f"Checking file: {file.filename}")
            if file.filename.endswith("fingerprint.json"):
                new_fingerprint_json = str(archive.read(file), encoding="UTF-8")
                new_fingerprint_json = json.loads(new_fingerprint_json)
                version_name = new_fingerprint_json['version']
                log(f"Found fingerprint.json file! Version: {version_name}, files loaded: {len(new_fingerprint_json['files'])}")

                if "laser" in file.filename:
                    app_name = "Brawl Stars"
                elif "magic" in file.filename:
                    app_name = "Clash of Clans"
                elif "scroll" in file.filename:
                    app_name = "Clash Royale"
                elif "board" in file.filename:
                    app_name = "Clash Mini"

        if not new_fingerprint_json:
            log("Unable to find fingerprint.json file which is required to extract the assets!", 4)

        if not path.exists(f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\Versions\\{version_name}"):
            mkdir(f"{brawl_appdata_dir}\\Versions\\{version_name}")
            log(f"Made directory: {brawl_appdata_dir}\\Versions\\{version_name}")

        log(f"{phrases[language]['detected_architecture']}{arch_type}")

        log(f"Game detected: {app_name}")
        maniupulate_brawl_file(dir=dir, app_version=f"{version_name}", app_name=app_name, fingerprint_json=new_fingerprint_json)
    except Exception as e:
        log(f"\n[WARNING] An error has occured which cannot be resolved: {e}")
        logging.error(e)


def csv_decoder():
    import os

    # Credit: https://github.com/proydakov/supercell_resource_decoder/blob/master/lib_csv.py

    path = input("Enter the path to the encrypted CSV file:\n\n>>> ")

    # if the path is a folder

    def parse_csv(path):
        basename, _ = os.path.splitext(path)
        decodedname = basename + "_DECODED.csv"

        log(f"{green_colour}{phrases[language]['processing'], path, '->', decodedname}")

        try:
            with open(path, 'rb') as f:
                data = f.read()
        except Exception as e:
            log(f"Error: File not found. {e}")
            log(traceback.format_exc())

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
                log(f"\n\nSuccessfully unpacked the file. You can now view it at {decodedname}\n")
        except Exception:
            log(f"Invalid input: {traceback.format_exc()}", 4, True)

    if os.path.isdir(path):
        log(f"Path is a directory. Parsing all CSV files in {path}", 2, True)
        for file in os.listdir(path):
            if file.endswith(".csv"):
                parse_csv(os.path.join(path, file))
    else:
        parse_csv(path)

    open_in_explorer = input("Do you want to open the folder containing the decoded CSV files? (y/n)\n\n>>> ")
    if open_in_explorer.lower() == "y":
        Popen("explorer.exe /select, " + path)

    autobrawlextractor()


def autobrawlextractor():
    brawl_appdata_dir = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor")
    downloadedbuilds_appdata_dir = (f"{environ_dir}\\AppData\\Roaming\\Draggie\\AutoBrawlExtractor\\DownloadedBuilds")
    if not path.exists(f"{brawl_appdata_dir}\\Versions"):
        makedirs(f"{brawl_appdata_dir}\\Versions")
    if not path.exists(downloadedbuilds_appdata_dir):
        makedirs(downloadedbuilds_appdata_dir)

    def number_one():
        log(r"Enter the location of your Supercell archive file, e.g D:\Downloads\brawl.ipa. IPA files are preferred.")
        log("\nUse an .ipa file or .apk file (for iOS and Android decices, respectively). Must not be unzipped.")
        log("[0] Go back.\n[1] Search for all downloadable versions.\n[2] Decode CSV Files with LZMA.\n(Alternatively, enter path or drag and drop the file here.)\n")

        amount_of_files = 0

        for i in listdir(downloadedbuilds_appdata_dir):
            amount_of_files = amount_of_files + 1

        if amount_of_files >= 1:
            log(f"\n[Enter] Select one of the {amount_of_files} downloaded files.")

        location = input("\n>>> ")

        match location:
            case "1":
                log("Fetching a list of all trusted versions from GitHub...")
                git_brawl_builds = dash_get("https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/Addons/AutoBrawlExtractor/brawl_builds.txt")
                git_brawl_builds = git_brawl_builds.text
                urls = git_brawl_builds.splitlines()
                version_names = [re.search(r"laser-(\d+\.\d+)", url).group(1) for url in urls]
                for i, version_name in enumerate(version_names):
                    log(f"[{i + 1}]   {version_name}")
                selected_version = (input("\nPlease select a version to download: ('*' to download them all, '0' to see other apps.).\n\n>>> "))
                if selected_version == "*":
                    log("You have chosen to download ALL builds. If you would like to stop it, you will need to press Ctrl+C.")
                    amount = len(urls)
                    downloaded_amount = 0
                    for line in urls:
                        source = line.strip().split(' (')
                        source_url = source[0]
                        source_loc = source[1].strip(')')
                        real_file_name = path.basename(urlsplit(source_url).path)
                        if "Baguette Brigaders" in source_loc:
                            source_loc = (f"a verified source: {source_loc}")
                        log(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
                        tqdm_download(source_url, f"{downloadedbuilds_appdata_dir}\\{real_file_name}")
                        downloaded_amount += 1
                        log(f"\nSuccessfully downloaded build {real_file_name}. It is located at: {downloadedbuilds_appdata_dir}\\{real_file_name}\nOverall progress: {downloaded_amount}/{amount} (~{round((downloaded_amount/amount)*100)}%\n")
                    log(f"{downloaded_amount} builds have been saved!\n\n")
                    number_one()
                if selected_version == "0":
                    clash_mini = "https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/Addons/AutoBrawlExtractor/ipas/board.txt"
                    clash_of_clans = "https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/Addons/AutoBrawlExtractor/ipas/magic.txt"
                    brawl_stars = "https://cdn.jsdelivr.net/gh/Draggie306/DraggieTools@latest/Addons/AutoBrawlExtractor/ipas/laser.txt"

                    game_choice = input("Which game would you like to download builds for?\n\n[1] Clash Mini\n[2] Clash of Clans\n[3] Brawl Stars\n\n>>> ")

                    if game_choice == "1":
                        game = clash_mini
                    if game_choice == "2":
                        game = clash_of_clans
                    if game_choice == "3":
                        game = brawl_stars

                    log("Fetching a list of all trusted versions from GitHub...")
                    git_clash_mini_builds = dash_get(game)
                    urls = (git_clash_mini_builds.text).splitlines()

                    if game_choice == "1":
                        version_names = [re.search(r"board-(\d+\.\d+)", url).group(1) for url in urls]
                    if game_choice == "2":
                        version_names = [re.search(r"magic-(\d+\.\d+)", url).group(1) for url in urls]
                    if game_choice == "3":
                        version_names = [re.search(r"laser-(\d+\.\d+)", url).group(1) for url in urls]

                    for i, version_name in enumerate(version_names):
                        log(f"[{i + 1}]   {version_name}")

                    selected_version = input("\nChoose a version to download: ('*' to download them all).\n\n>>> ")

                    if selected_version == "*":
                        source = line.strip().split(' (')
                        source_url = source[0]
                        source_loc = source[1].strip(')')
                        real_file_name = path.basename(urlsplit(source_url).path)
                        if "Baguette Brigaders" in source_loc:
                            source_loc = (f"a verified source: {source_loc}")
                        log(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
                        tqdm_download(source_url, f"{downloadedbuilds_appdata_dir}\\{real_file_name}")
                    else:
                        selected_url = urls[int(selected_version) - 1]
                        source = selected_url.strip().split(' (')
                        source_url = source[0]
                        source_loc = source[1].strip(')')
                        real_file_name = path.basename(urlsplit(source_url).path)
                        if "Baguette Brigaders" in source_loc:
                            source_loc = (f"a verified source: {source_loc}")
                            log(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
                        tqdm_download(source_url, f"{downloadedbuilds_appdata_dir}\\{real_file_name}")
                        log(f"\nDownloaded build {real_file_name}\nIt is located at: {downloadedbuilds_appdata_dir}\\{real_file_name}\n")

                selected_url = urls[int(selected_version) - 1]
                source = selected_url.strip().split(' (')
                source_url = source[0]
                source_loc = source[1].strip(')')
                real_file_name = path.basename(urlsplit(source_url).path)
                if "Baguette Brigaders" in source_loc:
                    source_loc = (f"a verified source: {source_loc}")
                    log(f"Downloading the build {real_file_name}. This file comes from {source_loc}")
                tqdm_download(source_url, f"{downloadedbuilds_appdata_dir}\\{real_file_name}")
                log(f"\nDownloaded build {real_file_name}\nIt is located at: {downloadedbuilds_appdata_dir}\\{real_file_name}\n")
                number_one()

            case "":
                files = []
                f = 0
                for file in listdir(downloadedbuilds_appdata_dir):
                    files.append(file)
                for i in files:
                    log(f"[{f}] {i}")
                    f += 1
                x = input("\nChoose file\n\n>>> ")
                try:
                    init_filetype(f"{downloadedbuilds_appdata_dir}\\{files[int(x)]}")
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

                    log(f"No valid build specified, resorting to regex expression to find the most recent version, which appears to be in file {highest_version_file}")
                    init_filetype(f"{downloadedbuilds_appdata_dir}\\{highest_version_file}")
            case "2":
                csv_decoder()
            case "0":
                main()
            case _:
                init_filetype(location)
    number_one()


def project_saturnian(state: Optional[str] = None, details: Optional[str] = None, known_token: Optional = None):
    """
    This function is used to manage the Saturnian project, now Draggie Games Account library.
    It is used to authenticate with the Draggie Games Accounts server and download the latest version of the games redeemed on the user account.
    :param state: Whether the user has safely logged in already, we do not need to post data to the server again.
    :param known_token: The pre-existing response from the server, if it exists.
    """
    saturnian_appdir = f"{Draggie_AppData_Directory}\\Saturnian"
    entitlements_json = f"{saturnian_appdir}\\entitlements_data.json"

    cached_token = None
    username = getpass.getuser()
    username = f"{username.lower()}.3d060a9b-f248-4e2b-babd-e6d5d2c2ab8b"
    # generate a key from the username
    hash_key = hashlib.sha256(username.encode()).digest()
    # create a Fernet key from the hash
    fernet_key = Fernet(base64.urlsafe_b64encode(hash_key))
    log(f"fernet_key: {fernet_key}", output=False)

    def encrypt_token(token):
        log("[encrypt_token] encrypting token")
        encrypted_binary_token = fernet_key.encrypt(token.encode())
        # log(f"[encrypt_token] encrypted_binary_token: {encrypted_binary_token}")
        # convert the binary token to a string
        encrypted_token = encrypted_binary_token.decode()
        # log(f"[encrypt_token] encrypted_token: {encrypted_token}")
        return encrypted_token

    def decrypt_token(encrypted_token):
        # log("[decrypt_token] decrypting token")
        token = encrypted_token
        return fernet_key.decrypt(token)

    def read_tokenfile_contents():
        """
        Gets the encrypted token, if it exists.
        """
        # log("[read_tokenfile_contents] Reading token file contents...", output=False, log_level=1)
        if os.path.isfile(f"{saturnian_appdir}\\token.bin"):
            with open(f"{saturnian_appdir}\\token.bin", "r") as f:
                cached_token = f.read()
                log(f"[read_tokenfile_contents] Found cached token: {cached_token}", output=False)
                return cached_token
        log("[read_tokenfile_contents] No cached token found.", output=False)
        return None

    def write_token(encrypted_token):
        """
        Writes the unencrypted token to a file. YOU MUST ENCRYPT THE TOKEN BEFORE PASSING IT TO THIS FUNCTION.
        """
        # log("[write_token] writing encrypted token")
        if not os.path.isdir(saturnian_appdir):
            os.makedirs(saturnian_appdir, exist_ok=True)
            log(f"[write_token] Created directory: {saturnian_appdir}")
        with open(f"{saturnian_appdir}\\token.bin", "wb") as f:
            f.write(encrypted_token.encode())
            # log(f"[write_token] Wrote encrypted token to file: {encrypted_token}")

    def read_datafile_attribute(attribute, entitlement: Optional[str] = "default"):
        """
        Reads the datafile and returns the value of the attribute under the given entitlement
        """
        try:
            with open(entitlements_json, "r") as f:
                entitlements_data = json.load(f)
                log(f"[gamesManager/ReadDatafile] Read datafile: {entitlements_data}", log_level=1, output=False)
            # Fix for errors which occur when entitlement is not found
            if entitlement not in entitlements_data:
                entitlements_data[entitlement] = {}

            return entitlements_data[entitlement].get(attribute)
        except Exception as e:
            if attribute == "install_dir":
                log(f"[saturnian/datafile] Error reading datafile for attribute {attribute}, returning default value: {saturnian_appdir}", log_level=3)
                return saturnian_appdir
            return log(f"[saturnian/datafile] Error reading Saturnian data file: {e}", log_level=4)

    def write_datafile_attribute(attribute, value, entitlement):
        """
        Writes the value of the attribute to the datafile.
        """
        try:
            with open(entitlements_json, "r") as f:
                entitlements_data = json.load(f)
                log(f"[gamesManager/WriteDatafile] Read datafile: {entitlements_data}", log_level=1, output=False)
            entitlements_data.setdefault(entitlement, {})[attribute] = value
            entitlements_data[entitlement][attribute] = value
            with open(entitlements_json, "w") as f:
                json.dump(entitlements_data, f, indent=4)
                log(f"[saturnian/datafile] Wrote attribute {attribute} under entitlement {entitlement} to datafile: {value}", log_level=1)
        except Exception as e:
            log(f"[saturnian/datafile] Error writing attribute {attribute} to datafile: {e}", log_level=4)


    if not known_token:
        log("Authenticating with the Draggie Games Accounts server...") 

        if not os.path.isfile(entitlements_json):
            log("[saturnian] No data file found. Creating one now...", log_level=3)
            os.makedirs(saturnian_appdir, exist_ok=True)
            with open(entitlements_json, "w") as f:
                first_info = {
                    "default": {
                        "current_version": None, "tier": None, "install_dir": saturnian_appdir
                    },
                    "saturnian_beta_tester": {
                        "current_version": None, "tier": None, "install_dir": saturnian_appdir
                    }
                }
                json.dump(first_info, f)
                log(f"{green_colour}[saturnian] Gamedata file created successfully.")

        cached_token = read_tokenfile_contents()

        if not cached_token:
            log(f"\n\n[DraggieGamesAccounts] {red_colour}You must log in to download builds from the gameserver, and to validate your license.{reset_colour}", log_level=3)
            log(f"[DraggieGamesAccounts] {magenta_colour}If you do not have an account, you can create one at:{cyan_colour} https://alpha.draggiegames.com/register{reset_colour}", log_level=3)
            log(f"\n\n{yellow_colour}Please enter your Draggie Games login credentials below.{reset_colour}", log_level=3)
            email = input(f"\n{yellow_colour}Email: {reset_colour}")
            password = getpass.getpass(f"{yellow_colour}Password (hidden): {reset_colour}")
            log(f"{blue_colour}Logging in...")
            login = dash_post("https://client.draggie.games/login", json={"email": email, "password": password, "from": "SaturnianUpdater/DraggieTools"})

            if not login.status_code == 200:
                log("\n\nLogin failed! Please try again.", log_level=4)
                return project_saturnian()

            log(f"\n\n{green_colour}Login successful.\n")
            server_token = login.json()["auth_token"]
            # log(f"Server returned token: {server_token}", log_level=1)
            newly_encrypted_token = encrypt_token(server_token)
            log(f"newly_encrypted_token: {newly_encrypted_token}", log_level=1, output=False)
            write_token(newly_encrypted_token)
            log("Token written to file.", log_level=1, output=False)

            preferred_install_location = input(f"{reset_colour}\n\nIf you would like to change the default install location, please enter it below. Otherwise, press enter.\n\n>>> ")
            if preferred_install_location != "":
                custom_install_location = preferred_install_location
                if not os.path.isdir(custom_install_location):
                    os.makedirs(custom_install_location, exist_ok=True)
                    log(f"Created directory: {custom_install_location}")
                write_datafile_attribute("install_dir", custom_install_location, "default")
            else:
                write_datafile_attribute("install_dir", saturnian_appdir, "default")

        try:
            cached_token = read_tokenfile_contents()
            if not cached_token:
                log("No cached token found. Please try again.", log_level=4)
                project_saturnian()
            encrypted_token = cached_token
            log(f"encrypted_token: {encrypted_token}", output=False)
            decrypted_token = decrypt_token(encrypted_token)
            # log(f"token: {decrypted_token}", output=False)
            token = decrypted_token.decode()
            # log(f"Final read token: {decrypted_token}", output=False)
        except Exception:
            clear_token = input("There was an error reading the token file. Would you like to clear the cached token and try again? (y/n)\n\n>>> ")
            match clear_token:
                case "y":
                    token_dir = f"{saturnian_appdir}\\token.bin"
                    if not os.path.isdir(saturnian_appdir):
                        os.makedirs(saturnian_appdir, exist_ok=True)
                        log(f"[write_token] Created directory: {saturnian_appdir}")
                    if os.path.isfile(token_dir):
                        os.remove(token_dir)
                        log(f"[write_token] Deleted file: {token_dir}")
                    else:
                        log(f"[write_token] File not found: {token_dir}", log_level=3)
                    project_saturnian()
                case _:
                    log("Exiting...")
                    return choice1()
            return choice1()

        # After validating the token, we can use it to log in.
        log(f"[DGamesAuth] Token decryption successful from file at '{saturnian_appdir}\\token.bin'.", output=False)
        log("Logging in to your account...\n", raw=True)

        def token_login(token):
            headers = {
                "Authorisation": f"{token}",
                "User-Agent": "SaturnianUpdater/DraggieTools",
                "From": "SaturnianUpdater/DraggieTools",
                "DraggieTools-Version": f"{build}",
            }

            endpoint = "https://client.draggie.games/token_login"
            login = dash_post(endpoint, json={"token": token, "from": "SaturnianUpdater/DraggieTools"}, headers=headers)
            if not login.status_code == 200:
                log(f"{red_colour}Token login failed. Error {login.status_code}: {login.content}\n\n{login.text['message'] if hasattr(login.text, 'message') else login.text}", output=True)
                os.remove(f"{saturnian_appdir}\\token.bin")
                input("Enter any key to continue...")
                return choice1()

            response = json.loads(login.content)
            log(f"{green_colour}Token login successful. Received response: {response}", output=False)
            log(f"{green_colour}{response['message']}", output=True)
            status_update(details=f"Logged in as: {response['account']}", state="Project Saturnian")
            return token
            # log(f"Received token login content: {login.content}")

        known_token = token_login(token)
        # log(f"new_token: {known_token}")
        log(f"{green_colour}Logged in successfully!\n{reset_colour}", output=True)

    def get_entitlement_info(known_token):
        log("Checking the server for what games you have access to...", output=True, raw=True)

        headers = {
            "Authorisation": known_token,
            "User-Agent": "SaturnianUpdater/DraggieTools",
            "From": "SaturnianUpdater/DraggieTools",
            "DraggieTools-Version": f"{build}",
        }

        endpoint = "https://client.draggie.games/api/v1/saturnian/game/gameData/licenses/validation"
        x = dash_get(endpoint, headers=headers)
        if not x.status_code == 200:
            log(f"[saturnian/errors.account] ERROR: Received Saturnian version status code: {x.status_code}", log_level=4)
            error_message = json.loads(x.content)
            log(f"[saturnian/errors.account] \n\nvvvvvvvvvvvvvvvvvvvvvvvvvvvv\nERROR: {error_message['message']}\n^^^^^^^^^^^^^^^^^^^^^^^^^^", log_level=4)
            if os.path.isfile(f"{saturnian_appdir}\\token.bin"):
                os.remove(f"{saturnian_appdir}\\token.bin")
                log("\n[saturnian/errors.account] Your token may have expired. Please log in again.", log_level=4)
                return project_saturnian()

        try:
            response = json.loads(x.content)

            # New server logic (v0.8.6) - the server now returns a list of entitlements, which are used to determine the account type.
            # This means that the user can redeem multiple entitlements. Display the entitlements to the user, and let them choose which one to use.
            entitlements = response["entitlements"]
            # print(entitlements)

            """
            Entitlements example:
            {
                'saturnian_alpha_tester': {'currentVersion': '14', 'downloadUrl': 'https://saturnian-co.../build.zip', 'type': 'alpha', 'friendlyName': 'Saturnian Alpha Tester', 'folderName': 'SaturnianGame'},
                'saturnian_beta_tester': {'currentVersion': '0', 'downloadUrl': 'n/a', 'type': 'beta', 'friendlyName': 'Saturnian Beta Tester', 'folderName': 'SaturnianGame'},
            }
            """

            if len(entitlements) > 1:
                log(f"\n[DGames/Account] You have {green_colour}{len(entitlements)}{reset_colour} entitlements. Choose one to manage!\n")

                match_int = {}
                for i, entitlement in enumerate(entitlements):
                    log(f"[{i + 1}] {green_colour}{entitlements[entitlement]['friendlyName']}{reset_colour}")
                    match_int[i + 1] = entitlement
                choice = input("\n\n>>> ")
                log(f"[UserInput] Choice inputted: {choice}. Due to 0-indexing, the actual choice is {int(choice)}.", output=False)
                try:
                    entitlement = entitlements[match_int[int(choice)]]  # get the entitlement from the list
                except Exception as e:
                    log(f"[saturnian/errors.account] Error choosing entitlement: {e}", log_level=4)
                    return choice1()

                log(f"\n{green_colour}Manage your installation of {entitlement['friendlyName']}{reset_colour}! What would you like to do?")
                log(f"This game's current version is build: {entitlement['currentVersion']} ({entitlement['type']})")
                return entitlement

            else:
                # get first
                entitlement = entitlements[list(entitlements.keys())[0]]
                log(f"\n{green_colour}Manage your installation of {entitlement['friendlyName']}{reset_colour}! What would you like to do?")
                log(f"This game's current version is build: {entitlement['currentVersion']} ({entitlement['type']})")
                return entitlement

        except Exception as e:
            log(f"[saturnian/errors.account] Exception: {e}", log_level=4)
            log(f"[saturnian/errors] Received version status code: {x.status_code}", log_level=4)
            choice1()

    server_entitlement_response = get_entitlement_info(known_token)

    if not server_entitlement_response:
        log("[saturnian/errors] No entitlements found! Make sure you have a valid account.", log_level=4)
        return choice1()

    saturnian_current_version = server_entitlement_response["currentVersion"]

    # Read the json file
    try:
        with open(entitlements_json, "r") as f:
            entitlement_alldata = json.load(f)
            log(f"{green_colour}[saturnian] Successfully read datafile.", output=False)
            log(f"entitlement_alldata contents: {entitlement_alldata}", output=False, log_level=1)
    except Exception as e:
        return log(f"[saturnian/errors] Error reading Saturnian data file: {e}", log_level=4)

    def promote_project_lily():
        """
        Prompts the user to install the AutoUpdate project codename Lily.
        """
        if get_draggietools_setting("promote_lily") == "False":
            log(f"{green_colour}[saturnian/promote_lily] Not promoting AutoUpdate.", log_level=1, output=False)
            project_saturnian(known_token=known_token)
        log("\nMake sure to check out the Draggie Games Discord server and assign roles for updates: https://discord.gg/GfetCXH")
        client = input(f"Note: {orange_colour}the Game Library{reset_colour} is still in development, so there may be bugs.\n\n{orange_colour}NOTICE: To auto update the project, make sure you have {magenta_colour}AutoUpdate{orange_colour} installed.{reset_colour}\nWould you like to open the {magenta_colour}AutoUpdate{reset_colour} menu now? Y/N\n\n>>> ")
        match client.lower():
            case "y":
                draggieclient()
            case _:
                set_draggietools_setting("promote_lily", "False")
                log("Returning to main menu...")
                project_saturnian(known_token=known_token)

    # Now, if the server version is different from the local version, we need to update Saturnian.

    def download_saturnian_build(path_to_download=Optional[str]):
        download_url = server_entitlement_response["downloadUrl"]
        log(f"{green_colour}[saturnian/buildDL] Downloading Project Saturnian! This may take a while...")
        # log(f"[saturnian/buildDL] Grabbing authenticated build from {download_url}", output=False)

        preferred_install_location = read_datafile_attribute("install_dir", server_entitlement_response["id"])
        tqdm_download(download_url, f"{preferred_install_location}\\Saturnian.bin", overwrite=True, desc=f"Project Saturnian v{saturnian_current_version}")

        log(f"{green_colour}[saturnian/buildDL] Download complete. Decompressing...")
        start_anim_loading("Decompressing...")
        try:
            with zipfile.ZipFile(f"{preferred_install_location}\\Saturnian.bin", "r") as zip_ref:
                zip_ref.extractall(f"{preferred_install_location}\\{server_entitlement_response['folderName']}")
        except Exception as e:
            stop_anim_loading()
            log(f"\n{red_colour}[saturnian/errors] Error extracting Saturnian build: {e}", log_level=4, event="error")
            return False
        stop_anim_loading()
        sys.stdout.flush()
        sys.stdout.write("\r")  # TODO: make it clear the line above
        sys.stdout.flush()
        log(f"\n{green_colour}[saturnian/buildDL] Extraction complete.")
        write_datafile_attribute("current_version", saturnian_current_version, server_entitlement_response["id"])
        return 1

    current_version = read_datafile_attribute("current_version", server_entitlement_response["id"])
    if saturnian_current_version != current_version:
        string_to_prompt = ""
        if not current_version:
            # Cool slow print effect
            slow_print(f"\n{yellow_colour}Hold up, looks like you haven't installed the game yet!\n")
            string_to_prompt = f"\n{yellow_colour}Would you like to install the latest version of {server_entitlement_response['friendlyName']}? Press [Enter] to confirm, or input any path to specify a custom download location.{reset_colour}"
        else:
            slow_print(f"\n{yellow_colour}Hold up, looks like an update is available for this one!\n")
            string_to_prompt = f"\nWould you like to update {server_entitlement_response['friendlyName']} from build {current_version} to {saturnian_current_version}? Press [Enter] to confirm, or input any path to specify a custom download location.{reset_colour}"
        log(string_to_prompt)
        choice = input("\n\n>>> ")
        match choice:
            case "":
                log("[saturnian/Updater] Downloading build...")
            case "0":
                return choice1()
            case _:
                log(f"[saturnian/Updater] Downloading build to {choice}...")
                write_datafile_attribute("install_dir", choice, server_entitlement_response["id"])

        log(f"[saturnian/Updater] Downloading build version {saturnian_current_version}...")
        result = download_saturnian_build()
        if not result:
            return log(f"{red_colour}[saturnian/Updater] Update download failed.", log_level=4, event="error")
        log(f"{green_colour}[saturnian/Updater] Update download was successful.")

        write_datafile_attribute(attribute="current_version", value=saturnian_current_version, entitlement=server_entitlement_response["id"])
        write_datafile_attribute("tier", server_entitlement_response["type"], server_entitlement_response["id"])
        promote_project_lily()

    preferred_install_location = read_datafile_attribute("install_dir", server_entitlement_response["id"])

    # folder_structure_to_find_exe_in = (f"{preferred_install_location}\\{server_entitlement_response['folderName']}")
    folder_structure_to_find_exe_in = os.path.join(preferred_install_location, server_entitlement_response['folderName'])

    exe_found = False
    if os.path.isdir(folder_structure_to_find_exe_in):
        for filename in os.listdir(folder_structure_to_find_exe_in):
            if filename.endswith(".exe"):
                log(f"[saturnian/findexec] Found executable file {filename} in {folder_structure_to_find_exe_in}.", 2, False)
                exe_found = True
                break

    if not exe_found:
        log(f"Unable to find executable in {preferred_install_location}\\{server_entitlement_response['folderName']}", log_level=4, output=True)
        log(f"\n[saturnian/Updater] Couldn't find a downloaded program! This might be because you deleted it, or the download failed.\n{blue_colour}Input 1 to download, or 0 to return to the main menu.{reset_colour}")
        choice = input("\n\n>>> ")
        match choice:
            case "0":
                return choice1()
            case _:
                try:
                    os.makedirs(folder_structure_to_find_exe_in, exist_ok=True)
                    result = download_saturnian_build()
                    if not result:
                        log(f"{red_colour}[saturnian/Updater] Update download failed.", log_level=4, event="error")
                        log(f"{red_colour}[saturnian/Updater] Please make sure there is enough space on your drive, you have a stable internet connection, and you have the correct permissions to write to the directory \"{preferred_install_location}\".", log_level=4, event="error")
                        return choice1()
                    log(f"\n{green_colour}[saturnian/Updater] Update completed!")
                except Exception as e:
                    return log(f"[saturnian/errors] Error in buildType downloading Saturnian build: {e}", log_level=4, event="error")

    to_open = input(f"\n\n{cyan_colour}Manage your installation of the game!{reset_colour}\n\n[0] Back to main menu\n[1] Back to Draggie Games menu\n[2] Open the game\n[3] Uninstall the project\n[4] Open the game folder\n[5] Quick uninstall/reinstall\n[6] Change installation directory\n[7] Sign out\n\n>>> ")
    match to_open.lower():
        case "0":
            return choice1()
        case "1":
            return project_saturnian(known_token=known_token)
        case "2":
            preferred_install_location = read_datafile_attribute("install_dir", server_entitlement_response["id"])
            log(f"[saturnian/Updater] Opening {preferred_install_location}\\{server_entitlement_response['folderName']}\\{server_entitlement_response['executableName']}", output=False)
            Popen(f"{preferred_install_location}\\{server_entitlement_response['folderName']}\\{server_entitlement_response["executableName"]}")
            sleep(4)
        case "3":
            log("[saturnian/Updater] Uninstalling project...")
            log(f"\nNOTE: By continuing, you will delete ALL files in the directory \"{preferred_install_location}\\{server_entitlement_response['folderName']}\". Any files you may have added to this directory will be deleted.")
            log(f"\n{yellow_colour}Are you sure you want to continue? (y/n){reset_colour}")
            delete_choice = input("\n\n>>> ")
            if delete_choice.lower() == "n":
                log("Okay, returning to main menu...")
                return project_saturnian()
            try:
                # Remove directory tree
                # shutil.rmtree(f"{preferred_install_location}\\SaturnianGame")
                dir_path = f"{preferred_install_location}\\{server_entitlement_response['folderName']}"

                # walk through all files and directories
                for root, dirs, files in os.walk(dir_path, topdown=False):
                    for name in files:
                        #  full file path construct anddelete
                        file_path = os.path.join(root, name)
                        os.remove(file_path)
                        log(f"{green_colour}[saturnian/Updater] Removed {file_path}", log_level=2, output=True)
                    for name in dirs:
                        # full dir path construct and delete
                        dir_to_remove = os.path.join(root, name)
                        os.rmdir(dir_to_remove)
                        log(f"{green_colour}[saturnian/Updater] Removed directory {dir_to_remove}", log_level=2, output=True)

                # remove root directory
                os.rmdir(dir_path)
                log(f"{green_colour}[saturnian/Updater] Removed root @ {dir_path}", log_level=2, output=True)

                os.remove(f"{preferred_install_location}\\Saturnian.bin")
                log(f"{green_colour}[saturnian/Updater] Removed SaturnianGame binary download", log_level=2, output=True)

                # Right now don't forget to remove it from the config file so autoupdate doesn't try to update it
                write_datafile_attribute("current_version", None, server_entitlement_response["id"])

                log(f"\n{green_colour}[saturnian/Updater] Saturnian uninstalled successfully.")
            except Exception as e:
                log(f"\n[saturnian/errors] An issue occurred when fully uninstalling Saturnian:\n> {e}", log_level=4, event="error")
                return sleep(1)
        case "4":
            preferred_install_location = read_datafile_attribute("install_dir")
            Popen(f'explorer /select,"{preferred_install_location}\\{server_entitlement_response["folderName"]}"')
        case "5":
            def uninstall_reinstall():
                log("[saturnian/Updater] Uninstalling Saturnian...")
                try:
                    # Remove directory tree
                    # shutil.rmtree(f"{preferred_install_location}\\SaturnianGame")
                    dir_path = f"{preferred_install_location}\\SaturnianGame"

                    # walk through all files and directories
                    for root, dirs, files in os.walk(dir_path, topdown=False):
                        for name in files:
                            #  full file path construct anddelete
                            file_path = os.path.join(root, name)
                            os.remove(file_path)
                            log(f"{green_colour}[saturnian/Updater] Removed {file_path}", log_level=2, output=True)
                        for name in dirs:
                            # full dir path construct and delete
                            dir_to_remove = os.path.join(root, name)
                            os.rmdir(dir_to_remove)
                            log(f"{green_colour}[saturnian/Updater] Removed directory {dir_to_remove}", log_level=2, output=True)

                    # remove root directory
                    os.rmdir(dir_path)
                    log(f"{green_colour}[saturnian/Updater] Removed root @ {dir_path}", log_level=2, output=True)

                    os.remove(f"{preferred_install_location}\\Saturnian.bin")
                    log(f"{green_colour}[saturnian/Updater] Removed SaturnianGame binary download", log_level=2, output=True)

                    log(f"\n{green_colour}[saturnian/Updater] Saturnian uninstalled successfully.")
                except Exception as e:
                    log(f"\n[saturnian/errors] Error fully uninstalling Saturnian: {e}", log_level=4, event="error")
                    sleep(1)
                    log("\n[saturnian/errors] Attempting to reinstall Saturnian...")

                log(f"[saturnian/Updater] Downloading build version {saturnian_current_version}...")
                result = download_saturnian_build()

                if not result:
                    log(f"{red_colour}[saturnian/Updater] Update download failed.", log_level=4, event="error")
                    log(f"{red_colour}[saturnian/Updater] Please make sure there is enough space on your drive, you have a stable internet connection, and you have the correct permissions to write to the directory \"{preferred_install_location}\".", log_level=4, event="error")
                    return project_saturnian()
                log(f"{green_colour}[saturnian/Updater] Update download was successful.")

                write_datafile_attribute("current_version", saturnian_current_version, server_entitlement_response["id"])
                write_datafile_attribute("tier", server_entitlement_response["type"], server_entitlement_response["id"])

            amount_to_change = get_draggietools_setting("saturnian_uninstall_reinstall_amount")
            if amount_to_change is None:
                amount_to_change = 1
            else:
                amount_to_change = int(amount_to_change)

            while amount_to_change > 0:
                uninstall_reinstall()
                amount_to_change -= 1
                log(f"Still have {amount_to_change} more to go..." if amount_to_change > 0 else "Done!")

        case "6":
            log("[saturnian/Updater] Changing installation directory...")
            start_time = time()
            try:
                new_saturnian_install_dir = input("Enter the new installation directory:\n\n>>> ")
                if not os.path.isdir(new_saturnian_install_dir):
                    os.makedirs(new_saturnian_install_dir, exist_ok=True)
                # Cut/move the files over
                try:
                    for file in os.listdir(f"{preferred_install_location}\\SaturnianGame"):
                        shutil.move(f"{preferred_install_location}\\SaturnianGame\\{file}", f"{new_saturnian_install_dir}\\SaturnianGame\\{file}")
                        log(f"{green_colour}[saturnian/Updater] Moved {file} to {new_saturnian_install_dir}\\SaturnianGame\\{file}", log_level=2, output=True)
                except Exception as e:
                    log(f"[saturnian/errors] Error moving files, there may be no files to move: {e}", log_level=3)
                # Write the new data file with the new directory
                write_datafile_attribute("install_dir", new_saturnian_install_dir, server_entitlement_response["id"])
                end_time = time()
                log(f"{green_colour}[saturnian/Updater] Installation directory changed successfully. Took {end_time - start_time} seconds.")
                sleep(2)
            except Exception as e:
                return log(f"[saturnian/errors] Error changing installation directory: {e}\n{traceback.format_exc()}", log_level=4, event="error")
        case "7":
            log("[saturnian/Updater] Signing out...")
            os.remove(f"{saturnian_appdir}\\token.bin")
            log("[saturnian/Updater] Token removed.")
            project_saturnian()
        case _:
            log(f"{red_colour}[saturnian/Updater] Invalid option. Please try again.")
            sleep(1)
            project_saturnian()

    project_saturnian()


def upload_log_file(file_path, delete_after_upload: Optional[bool] = False):
    url = "https://logs.draggie.games/tools"

    filename = path.basename(file_path)
    username = getpass.getuser()
    new_filename = f"[{username}]-{filename}"

    with open(file_path, 'rb') as f:
        contents = f.read()

    files = {
        'file': (new_filename, contents),
    }

    response = dash_post(url, files=files)
    if response.status_code == 429:
        log(f"{red_colour}Hit ratelimit while uploading the logfile {file_path}. Status code: {response.status_code}", 2)
        log(f"{red_colour}Waiting 20 seconds before trying again...", 2)
        sleep(20)
        upload_log_file(file_path)
    elif response.status_code != 200:
        log(f"{red_colour}Failed to upload the logfile {file_path}. Status code: {response.status_code}", 2)
    else:
        log(f"{green_colour}Uploaded the logfile {file_path}. Status code: {response.status_code}", 2)
        if delete_after_upload:
            os.remove(file_path)
            log(f"{green_colour}Deleted the logfile {file_path}", 2)


def upload_logs(most_recent: Optional[int] = None, no_confirm: Optional[bool] = True):
    logging_dir = f"{DraggieTools_AppData_Directory}\\Logs"
    files = listdir(logging_dir)
    files = [path.join(logging_dir, file) for file in files]

    # sort the files based on their creation time
    files.sort(key=path.getctime)

    # select the most recent x files
    if most_recent:
        files = files[-most_recent:]

    log(f"Files to upload: {files}", 1, False)

    if len(files) > 20:
        log(f"{yellow_colour}[WARNING] That's a lot of files to upload, you will probably hit the rate limit. Please confirm that you want to upload {len(files)} files.", 2)
        if no_confirm:
            confirm = input(f"{yellow_colour}Do you want to continue? (y/n)\n\n>>> ")
            if confirm.lower() == "y":
                pass
            else:
                return log(f"{yellow_colour}Cancelled upload.", 2)
        else:
            log(f"{yellow_colour}Continuing upload.", 2)
    # upload each file
    for file in files:
        upload_log_file(file)


def dev_menu():
    global build, use_slow_print_effect
    log("\n\n[1] Set build\n[2] Set version\n[3] Set unix time\n[4] Reload entire code (Dangerous)\n[5] Launch CMD executor\n[6] Open log directory\n[7] Upload logs\n[8] Open Discord token dumper\n[9] View Client Logs\n[10] CDN Diagnostic\n[11] Workers.dev test\n[12] Saturnian redownload adjustment\n[13] View source code\n[14] Toggle slow print effect")
    x = input("\n\n>>> ")
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
        case "5":
            cmd_launcher()
        case "6":
            Popen(f'explorer "{DraggieTools_AppData_Directory}\\Logs"')
        case "7":
            upload_logs()
        case "8":
            print("no")
        case "9":
            target_path = os.path.expanduser("~\\AppData\\Local\\Draggie\\Client\\client.exe")
            lily_ensure_appdata_dir = (f"{environ_dir}\\AppData\\Local\\Draggie\\Client")
            if not os.path.isdir(lily_ensure_appdata_dir):
                os.makedirs(lily_ensure_appdata_dir, exist_ok=True)
                log(f"[dev_lily] Created directory: {lily_ensure_appdata_dir}")
            lily_logs = os.path.join(lily_ensure_appdata_dir, "logs")
            if not os.path.isdir(lily_logs):
                os.makedirs(lily_logs, exist_ok=True)
                log(f"[dev_lily] Created directory: {lily_logs}")
            Popen(f'explorer "{lily_logs}"')

            lily_log_amount = 0
            items_folder = 0
            for file in listdir(lily_logs):
                items_folder += 1
                if file.endswith(".log"):
                    lily_log_amount += 1
                    try:
                        Popen(f'"{lily_logs}\\{file}"')
                    except Exception as e:
                        log(f"[dev_lily] Error opening file {file}: {e}")
            print(f"Opened {lily_log_amount} log files in {items_folder} items")

        case "10":
            validator_file = "tools_test.txt"
            cdn_tester = {
                "ibaguette_cdn": {
                    "main": "https://cdn.ibaguette.com",
                    "aliases": {"https://test.ibaguette.com", "https://nea.geog.uk"},
                    "service": "Cloudflare R2",
                    },
                "ibaguette_other_storage": {
                    "main": "htpps://storage.ibaguette.com",
                    "aliases": {},
                    "service": "Cloudflare R2",
                    },
                "draggiegames_cdns": {
                    "main": "https://assets.draggie.games",
                    "aliases": {"https://test.draggie.games"},
                    "service": "Cloudflare R2",
                    },
                "dgames_saturnian_builds": {
                    "main": "https://saturnian-content-download-euwest001-prod.draggie.games",
                    "aliases": {"https://l.geog.uk", "https://saturnian-content.draggie.games"},
                    "service": "Cloudflare R2",
                    },
                "yt-content": {
                    "main": "https://yt-assets.ibaguette.com",
                    "aliases": {"https://yt.draggie.games"},
                    "service": "Cloudflare R2",
                    },
                "papers": {
                    "main": "https://papers.ibaguette.com",
                    "aliases": {"https://research.geog.uk"},
                    "service": "Cloudflare R2",
                    },
                "cheatsheet-assets": {
                    "main": "https://cheatsheet-assets.ibaguette.com",
                    "aliases": {},
                    "service": "Cloudflare R2",
                    },
                "_unsorted": {
                    "main": "https://aic.draggie.games",
                    "aliases": {"https://autoupdateclient.draggie.games", "https://lily.draggie.games"},
                    "service": "Cloudflare R2",
                    },
            }
            good_cdns = 0
            bad_cdns = 0
            total_main_cdns = 0
            total_aliases = 0
            total_cdns = 0

            for cdn, cdn_data in cdn_tester.items():
                log(f"Testing CDN: {cdn}")
                try:
                    r = requests.get(f'{cdn_data["main"]}/{validator_file}')
                    log(f"[ERROR] Main CDN '{cdn_data['main']}' returned status code {r.status_code}" if r.status_code != 200 else f"[GOOD] Main CDN '{cdn_data['main']}' returned status code {r.status_code}")
                    good_cdns += 1 if r.status_code == 200 else 0
                    bad_cdns += 1 if r.status_code != 200 else 0
                except Exception as e:
                    log(f"[ERROR] Main CDN '{cdn_data['main']}' returned an error: ({e})")
                    bad_cdns += 1
                total_cdns += 1
                total_main_cdns += 1

                log("\nTesting aliases" if len(cdn_data["aliases"]) > 0 else f"Finished testing {cdn}")
                for alias in cdn_data["aliases"]:
                    try:
                        r = requests.get(f"{alias}/{validator_file}")
                        log(f"[GOOD] Alias '{alias}' returned status code {r.status_code}" if r.status_code == 200 else f"[ERROR] Alias '{alias}' returned status code {r.status_code}")
                        good_cdns += 1 if r.status_code == 200 else 0
                        bad_cdns += 1 if r.status_code != 200 else 0
                    except Exception as e:
                        log(f"[ERROR] Alias '{alias}' returned an error: ({e})")
                        bad_cdns += 1
                    total_aliases += 1
                    total_cdns += 1
                log("\n")

            log(f"Finished testing {total_cdns} CDNs, {total_main_cdns} main CDNs and {total_aliases} aliases. {good_cdns} good CDNs and {bad_cdns} bad CDNs.")
        case "11":
            urls_to_check = [
                "https://github.com/Draggie306/DraggieTools/raw/main/dist/DraggieTools.exe",
                "https://raw.githubusercontent.com/Draggie306/DraggieTools/main/dist/DraggieTools.exe",
                "https://draggiegames.com/",
                "https://ibaguette.com/",
            ]
            for url in urls_to_check:
                try:
                    log(f"Checking {url}")
                    r = requests.get(url)
                    log(f"[GOOD] {url} returned status code {r.status_code}")
                except Exception as e:
                    log(f"[ERROR] {url} returned an error: ({e})")
            # download to z:\temp
            url = "https://draggietools.draggie.workers.dev/"
            log(f"Downloading from {url}")
            r = requests.get(url)
            log(f"[GOOD] {url} returned status code {r.status_code}")
            with open("Z:\\temp\\DraggieTools.exe", "wb") as f:
                f.write(r.content)
        case "12":
            # Quick uninstall/reinstall for Saturnian change amount
            saturnian_uninstall_reinstall_amount = int(input("Enter the amount of times you want to uninstall/reinstall Saturnian:\n\n>>> "))
            set_draggietools_setting("saturnian_uninstall_reinstall_amount", saturnian_uninstall_reinstall_amount)
            log(f"Set to {saturnian_uninstall_reinstall_amount}. Go to the Saturnian menu to use it.")
        case "13":
            status_update(details="Viewing DraggieTools source code.")
            view_source()
        case "14":
            use_slow_print_effect = not use_slow_print_effect
            log(f"Set use_slow_print_effect to {use_slow_print_effect}")
        case _:
            choice1()

    dev_menu()


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
                log("Invalid file detected")
                return Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\DiscordParse\\{file}"')
        log("Loaded file")
    except Exception as e:
        log("I'm opening up the Discord parser directory. Please paste in your file which is to be processed")
        if not path.isfile(f"{DraggieTools_AppData_Directory}\\DiscordParse"):
            makedirs(f"{DraggieTools_AppData_Directory}\\DiscordParse", exist_ok=True)
        Popen(f'explorer /select,"{DraggieTools_AppData_Directory}\\DiscordParse"')
        return log(f"No valid file or improperly formatted json file exists! You have to put the file in the folder {DraggieTools_AppData_Directory}\\DiscordParse\n\n{e}", log_level=3)

    x = input("[1] Parse current file and output everything.\n[2] Organise current file and output JSON files for each server\n\n")

    if x == "1":
        log("loading...\n")

        start_time = perf_counter()  # start timer

        for line in file.splitlines():  # splitlines() is faster than split('\n')
            # check if line starts with '['
            if line.strip().startswith("["):
                discord_file = json.loads(line)
                log("============== NEW GUILD ==============")
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
                        log(f"Channel type: {channel_type}")
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

                    log(f"\n----------------{extra_text}----------------\n\nServer: {guild_id}\nName: {name}\nID: {id}\nLast Message ID: {lastMessageId} ({calculate_time_discord(lastMessageId)})\nLast Pin Timestamp: {lastPinTimestamp}\nNSFW: {nsfw}\nPosition: {position}\nRate Limit Per User: {rate_limit_per_user}\nTopic: {topic}\n")
                    # sleep(0.1)

        log(f"Operation completed ({round((perf_counter() - start_time), 7)}s)")

    if x == "2":
        server_num = 0
        channel_num = 0
        server_data = {}
        for line in file.splitlines():
            if line.strip().startswith("["):
                discord_file = json.loads(line)
                for channel in discord_file:
                    log(f"Got channel ({channel_num})")
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
                log(f"Writing data... ({server_num})")
                server_num = server_num + 1


def videomaker():
    import moviepy
    return log("This feature is currently disabled due to a bug in moviepy. Please use the old version of DraggieTools for this feature.", log_level=3)
    audio_dir = input("Enter path to ogg files: ")
    output_dir = input("Enter output dir path (there will be a temp folder located in here): ")

    log(moviepy.editor.TextClip.list('font'))

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
    log("loading files...")
    num = 0
    audio_extensions = ('.ogg', '.mp3', '.m4a', '.wav')
    audio_files = []
    for root, dirs, files in os.walk(audio_dir):
        for file in files:
            if file.endswith(audio_extensions):
                log(f"Found matching file: {file}")
                audio_files.append(os.path.join(root, file))
                num = num + 1
    log(f"Loaded {num} audio files.")

    def two():
        log("Gathering information about all files...")
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

        # log a message to indicate successful execution
        end_time = time.time()
        log(f"Files concatenated successfully in {end_time - start_time:.2f} seconds!")
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

            log(f"processing audio file {filename}")

            # Generate temp mp4 files
            output_file = os.path.join(output_dir, 'temp', f"{os.path.splitext(os.path.basename(audio_file))[0]}.mp4")
            final_video.write_videofile(output_file, fps=30, codec='libx264', preset="slow", audio=True, audio_codec=None, threads=12)
            time.sleep(0.5)

        if __name__ == '__main__':
            start_time = time.time()
            with cf.ThreadPoolExecutor(max_workers=threads) as executor:
                futures = []

                for iteration, audio_file in enumerate(audio_files):
                    # log(f"[iteration {iteration}] processing audio file {audio_file}")
                    try:
                        futures.append(executor.submit(process_audio_file, audio_file))
                    except Exception as e:
                        log(e)

                # wait for all threads to finish
                cf.wait(futures)

                # concatenate video clips and write output file
                end_time = time.time()
                log(f"Rendered video clips for all files in {end_time - start_time:.2f} seconds!")
                two()

    inn = input(f"[1] Render selected files from the OGG directory {audio_dir}\n[2] Render preprocessed mp4 files in the temp folder\n\n>>> ")

    if inn == "1":
        one()
    else:
        two()

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


def yt_download():
    log("Initialising downloader...", 1, True)
    ydl = youtube_dl.YoutubeDL()
    save_dir = get_draggietools_setting("ydl_default_dir")
    if not save_dir:
        log("No default directory set to download to, you can set one in the settings menu.", 3, True)
    else:
        log(f"Files will be downloaded to: {green_colour}{save_dir}{reset_colour}", 1, True)

    # Get the best audio stream link
    youtube_video = input("Enter the URL of the video/playlist, or the query to search for:\n\n>>> ")
    start_time = time()

    if "http" not in youtube_video:
        try:
            log(f"A valid URL protocol (HTTP(s)) was not provided, searching for term {green_colour}\"{youtube_video}\"{reset_colour}...", 1, True)
            audio_info = ydl.extract_info(f"ytsearch:{youtube_video}", download=False)['entries'][0]
            youtube_video = audio_info['webpage_url']
        except youtube_dl.utils.YoutubeDLError as e:
            log("There was an error getting information from the provided URL. Please try again later.", log_level=3)
            log(e, 4, False)
            choice1()
    else:
        try:
            audio_info = ydl.extract_info(youtube_video, download=False)
        except youtube_dl.utils.YoutubeDLError as e:
            log(f"{red_colour}There was an error getting information from the provided URL. Please try again later.", log_level=3)
            log(f"{e}{reset_colour}", 4, True)
            choice1()

    log(f"\n\n[draggietools] Found a matching video with title: {green_colour}{audio_info['title']}{reset_colour}. URL: {green_colour}{youtube_video}{reset_colour}", 1, True)
    # print attributes of audio_info object
    log(f"{blue_colour}[DEBUG] Available formats:")
    for format in audio_info['formats']:
        log(f"{blue_colour}{format['format']}{reset_colour} is available at {green_colour}{format['url'] if 'manifest_url' not in format else 'n/a'}")
    print(f"-----------------------\n{reset_colour}", end="")

    if 'duration' in audio_info if audio_info else False:
        log("Not a playlist")

        def get_format(extract_type):
            highest_sample_rate = 0
            highest_audio_bitrate = 0
            highest_total_bitrate = 0
            for format in audio_info['formats']:
                if extract_type == "audio":
                    if format['vcodec'] == 'none': # check if the format is audio-only
                        if 'asr' in format and format['asr'] > highest_sample_rate:
                            highest_sample_rate = format['asr']  # update highest_sample_rate
                            log(f"Updated highest sample rate to {highest_sample_rate}Hz")
                        if 'abr' in format and format['asr'] == highest_sample_rate:
                            if format['abr'] > highest_audio_bitrate:
                                highest_audio_url = format['url']
                                highest_audio_bitrate = format['abr']
                                # highest_audio_format_id = format['format_id']
                                log(f"New best audio bitrate: {highest_audio_bitrate}")
                                highest_format = format

                elif extract_type == "video":
                    if format['acodec'] == 'none': # check if the format is video-only
                        if 'vbr' in format and format['vbr'] > highest_total_bitrate:
                            highest_total_bitrate = format['vbr'] # update highest_total_bitrate
                            highest_video_url = format['url']
                            # highest_video_format_id = format['format_id']
                            log(f"New best video bitrate: {highest_total_bitrate}")
                            highest_format = format

            log(f"Highest audio bitrate: {highest_audio_bitrate}\nHighest video bitrate: {highest_total_bitrate}")

            return highest_format
            # log(f"Highest audio quality: {highest_audio_url}\nHighest video URL: {highest_video_url}")

        save_dir = get_draggietools_setting("ydl_default_dir")
        if not save_dir:
            save_dir = input("Enter the directory you want to save the file to:\n\n>>> ")
            ask_for_default = input("Do you want to set this as your default directory? (y/n)\n\n>>> ")
            if ask_for_default == "y":
                set_draggietools_setting("ydl_default_dir", save_dir)
                log(f"Set {save_dir} as your default directory for YouTube downloads.", 1, False)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir, exist_ok=True)

        what_to_do = input(f"\n\nWhat do you want to do?\n{red_colour}[0] Restart Downloader Tool{reset_colour}\n[1] Download audio\n[2] Download video\n[3] Download both\n[4] Download both and merge into one file\n\n>>> ")

        start_time_download = time()
        match what_to_do:
            case "1":
                ydl_opts_2 = get_ydl_info(f"audio-{audio_info['title']}", "audio", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts_2) as ydl:
                    ydl.download([youtube_video])
            case "2":
                ydl_opts_2 = get_ydl_info(f"video-{audio_info['title']}", "video", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts_2) as ydl:
                    ydl.download([youtube_video])
            case "3":
                ydl_opts_2 = get_ydl_info(f"audio-{audio_info['title']}", "audio", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts_2) as ydl:
                    ydl.download([youtube_video])

                ydl_opts_2 = get_ydl_info(f"video-{audio_info['title']}", "video", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts_2) as ydl:
                    ydl.download([youtube_video])
            case "4": # case "4":
                ydl_opts_2 = get_ydl_info(f"both-ytdl-default-{audio_info['title']}", "both", directory=save_dir)
                with youtube_dl.YoutubeDL(ydl_opts_2) as ydl:
                    ydl.download([youtube_video])
            case _: # case "0":
                log("Cancelled download.", 3, False)
                return yt_download()

    else:
        try:
            if audio_info['entries']:
                log("Playlist detected", 1, False)
        except KeyError:
            return log("Not a playlist, not a video, don't know to do with this URL. Report this to DraggieTools on GitHub.", log_level=3, output=True)

        log("Going through a playlist...", 1, False)
        what_to_do = input("What do you want to do?\n[0] Go back\n[1] Download audio\n[2] Download video\n[3] Download both and merge into one file\n\n>>> ")

        if not save_dir:
            save_dir = input("Enter the directory you want to save the file to:\n\n>>> ")
            ask_for_default = input("Do you want to set this as your default directory? (y/n)\n\n>>> ")
            if ask_for_default == "y":
                set_draggietools_setting("ydl_default_dir", save_dir)
                log(f"Set {save_dir} as your default directory for YouTube downloads.", 1, False)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

        start_time_download = time()
        # Download every video in the playlist
        match what_to_do:
            case "1": # download best audio
                for video in audio_info['entries']:
                    ydl_opts = get_ydl_info(title=video['title'], type="audio", directory=save_dir)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video['webpage_url']])
            case "2": # download best video
                for video in audio_info['entries']:
                    ydl_opts = get_ydl_info(title=video['title'], type="video", directory=save_dir)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video['webpage_url']])
            case "3": # download both
                for video in audio_info['entries']:
                    ydl_opts = get_ydl_info(title=video['title'], type="both", directory=save_dir)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video['webpage_url']])
            case _: # case "0":
                log("Cancelled download.", 3, False)
                return yt_download()

    log(f"{green_colour}[download]  Finished in {round(time() - start_time_download, 2)} seconds.")
    log(f"{green_colour}[ytdl]      Finished in {round(time() - start_time, 2)} seconds.")


def draggieclient():
    # Project Lily: aka DraggieClient
    status_update(details="Installing software", state="Project Lily")
    lily_initial_choice = input("\nWhat do you want to do?\n[0] Go back\n[1] Install\n[2] Uninstall\n[3] View Logs\n[4] Manage Settings\n\n>>> ")

    try:
        target_path = os.path.expanduser("~\\AppData\\Local\\Draggie\\Client\\client.exe")
        lily_ensure_appdata_dir = (f"{environ_dir}\\AppData\\Local\\Draggie\\Client")
        lily_ensure_appdata_dir_via_expanded = (f"{os.path.expanduser('~')}\\AppData\\Local\\Draggie\\Client")
    except Exception as e:
        return log(f"[ProjectLily] There was a critical error with trying to determine access to an essential directory: {e}: {traceback.format_exc()}.\n\n", log_level=4)

    if not os.path.exists(lily_ensure_appdata_dir):
        try:
            log("[ProjectLily] Prerequisite directory does not exist. Creating it now...")
            os.makedirs(lily_ensure_appdata_dir, exist_ok=True)
            log(f"{green_colour}[ProjectLily] Prerequisite directory made: {lily_ensure_appdata_dir}")
        except Exception as e:
            log(f"[ProjectLily] There was a critical error with trying to create a directory: {e}: {traceback.format_exc()}. Trying again with a different method...\n\n", log_level=3)
            os.makedirs(lily_ensure_appdata_dir_via_expanded, exist_ok=True)
            log(f"{green_colour}[ProjectLily] Prerequisite directory made: {lily_ensure_appdata_dir_via_expanded}")

    match lily_initial_choice:
        case "1":
            if not os.path.exists(f"{lily_ensure_appdata_dir}\\Logs"):
                os.makedirs(f"{lily_ensure_appdata_dir}\\Logs", exist_ok=True)
                log(f"{green_colour}[ProjectLily] Prerequisite directory made: {lily_ensure_appdata_dir}\\Logs")

            log("Downloading AutoUpdateClient build v45...")
            try:
                tqdm_download("https://autoupdateclient.draggie.games/AutoUpdate45.exe", target_path, return_exceptions=True)
                os.startfile(target_path)
                save_json()
                log(f"{green_colour}Your system now has DraggieClient installed! Running in the background, it will automatically keep all of your files by me up to date! Enjoy.")
            except PermissionError as e:
                log(f"[ProjectLily] {e}\nThe client is likely running! We don't need to install it again.", log_level=3)
            except Exception as e:
                log(f"[ProjectLily] An error occured: {e}: {traceback.format_exc()}", log_level=4)
        case "2":
            startup_path = os.path.join(winshell.startup(), "Client.lnk")
            if os.path.exists(startup_path):
                os.remove(startup_path)
            try:
                os.remove(os.path.expanduser("~\\AppData\\Local\\Draggie\\Client\\client.exe"))
            except Exception as e:
                log(f"[ProjectLily] Unable to remove client.exe - it is likely that it is running: {e}", log_level=3)

            for proc in psutil.process_iter():
                try:
                    target_path = os.path.expanduser("~\\AppData\\Local\\Draggie\\Client\\client.exe")
                    process = psutil.Process(proc.pid)
                    procname = "client.exe"
                    if proc.name() == procname:
                        process_exe = process.exe()
                        log(f"Found client.exe running at {process_exe}\nAttempting to kill process...")
                        if process_exe.lower() == target_path:
                            proc.kill()
                            log(f"{green_colour}Client has been killed.")
                        os.remove(os.path.expanduser("~\\AppData\\Local\\Draggie\\Client\\client.exe"))
                        log(f"{green_colour}[ProjectLily] Client has been uninstalled and removed from startup successfully.")
                except Exception as e:
                    log(f"[ProjectLily] Unable to kill and completely remove client.exe: {e}", log_level=3)
        case "3":
            log_subdir = os.path.expanduser("~\\AppData\\Local\\Draggie\\Client\\Logs")
            if not os.path.exists(log_subdir):
                os.makedirs(log_subdir, exist_ok=True)
            os.startfile(log_subdir)
        case "4":
            # return log("This is not yet implemented.")
            json_settings_dir = os.path.join(lily_ensure_appdata_dir, "Client_Settings.json")
            if not os.path.exists(json_settings_dir):
                with open(json_settings_dir, 'w') as f:
                    json.dump({
                        "startup": True,
                        "autoupdate": True,
                        "autoupdate_interval": "default",
                        "autoupdate_interval_unit": "default",
                    }, f)
            with open(json_settings_dir, 'r') as f:
                json_settings = json.load(f)
                for key, value in json_settings.items():
                    log(f"{key}: {value}", output=False)
                choice_client_settings = input("What do you want to do?\n[1] Change startup\n[2] Change autoupdate\n>>> ")
                match choice_client_settings:
                    case "1":
                        choice_client_settings_startup = input("Do you want to enable or disable startup?\n[1] Enable\n[2] Disable\n>>> ")
                        match choice_client_settings_startup:
                            case "1":
                                json_settings["startup"] = True
                                with open(json_settings_dir, 'w') as f:
                                    json.dump(json_settings, f)
                                log(f"{green_colour}[ProjectLily] Startup enabled.")
                            case "2":
                                json_settings["startup"] = False
                                with open(json_settings_dir, 'w') as f:
                                    json.dump(json_settings, f)
                                log(f"{red_colour}[ProjectLily] Startup disabled.")
                                draggieclient()
                    case "2":
                        choice_client_settings_autoupdate = input("Do you want to enable or disable autoupdate?\n[1] Enable\n[2] Disable\n>>> ")
                        match choice_client_settings_autoupdate:
                            case "1":
                                json_settings["autoupdate"] = True
                                with open(json_settings_dir, 'w') as f:
                                    json.dump(json_settings, f)
                                log(f"{green_colour}[ProjectLily] Autoupdate enabled.")
                            case "2":
                                json_settings["autoupdate"] = False
                                with open(json_settings_dir, 'w') as f:
                                    json.dump(json_settings, f)
                                log(f"{red_colour}[ProjectLily] Autoupdate disabled.")
                                draggieclient()
        case _:
            log(f"{red_colour}[ProjectLily] Invalid choice. Please try again.", log_level=3)
    sleep(1)
    return choice1()


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
        log(f"Unable to write current information: {e}")


def vbs_script_launcher():
    vbs_funny_long = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/Important-Disk-Data.vbs"
    vbs_funny = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/diskdata-trimmed.vbs"
    keyboard_rgb = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/keyboard-rgb.vbs"
    amazing_site = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/Have-you-heard-of-this-amazing-website.bat"
    cd_eject = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/cd.vbs"
    delete = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/delete.bat"
    fool = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/fool.vbs"
    hackingmatrix = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/Hackingmatrix.bat"
    infinite_bat = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/infinite.bat"
    l_vbs = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/L.vbs"
    no = r"https://cdn.ibaguette.com/cdn/Tools/script-pranks/no.bat"

    choice_vbs = input("What script do you want to download?\n1. Important Disk Data\n2. Keyboard RGB\n3. Have you heard of this amazing website?\n4. CD Eject\n5. Delete\n6. Fool\n7. Hacking Matrix\n8. Infinite\n9. L\n10. No\n11. Short Prank\n\nChoice: ")
    log("Downloading script...")
    match choice_vbs:
        case "1":
            filename = "Important-Disk-Data.vbs"
            url = vbs_funny_long
        case "2":
            filename = "keyboard-rgb.vbs"
            url = keyboard_rgb
        case "3":
            filename = "Have-you-heard-of-this-amazing-website.bat"
            url = amazing_site
        case "4":
            filename = "cd.vbs"
            url = cd_eject
        case "5":
            filename = "delete.bat"
            url = delete
        case "6":
            filename = "fool.vbs"
            url = fool
        case "7":
            filename = "Hackingmatrix.bat"
            url = hackingmatrix
        case "8":
            filename = "infinite.bat"
            url = infinite_bat
        case "9":
            filename = "L.vbs"
            url = l_vbs
        case "10":
            filename = "no.bat"
            url = no
        case "11":
            filename = "diskdata-trimmed.vbs"
            url = vbs_funny
        case _:
            log("Invalid choice. Quitting...")
            return choice1()
    try:
        tqdm_download(url, f"{DraggieTools_AppData_Directory}\\{filename}")
        os.startfile(f"{DraggieTools_AppData_Directory}\\{filename}")
    except Exception as e:
        log(f"Error: {e}")


def cmd_launcher():
    # Project Jake: Execute commands in cmd from within the executable
    log("This mode will loop until you press CTRL+C.")
    username = getpass.getuser()
    while True:
        x = input(f"\nC:\\Users\\{username}> ")
        log(f"Executing command: {x}", log_level=2, output=False)
        try:
            os.system(x)
        except Exception as e:
            log(f"Error: {e}", log_level=3, output=True)


def custom_discord_rpc():
    return log("Feature is work in progress.", log_level=3)
    log("Initialising...", log_level=1, output=True)
    try:
        with open(f"{DraggieTools_AppData_Directory}\\DiscordRPC\\CustomRPC.json", 'r') as f:
            rpc_data = json.load(f)
    except FileNotFoundError:
        log("No RPC data found. Creating new file...", log_level=1, output=True)
        with open(f"{DraggieTools_AppData_Directory}\\DiscordRPC\\CustomRPC.json", 'w') as f:
            json.dump({
                "details": "DraggieTools",
            })


def discord_tools():
    log("Discord Tools submenu.")
    print("[1] Parse Discord StoreChannel\n[2] Reload Discord RPC\n[3] Set Custom Status\n\n")
    choice_discord_tools = input(">>> ")

    match choice_discord_tools:
        case "1":
            discord_parse()
        case "2":
            log("Reloading Discord RPC...")
            asyncio.run(harry_loader())
        case "3":
            custom_discord_rpc()
        case _:
            log("Invalid choice. Quitting...")
            return choice1()


def install_command():
    location = input("Where do you want to install me to?\n[1] Desktop\n[custom directory] Custom\n\n>>> ")

    match location:
        case "1":
            desktop_dir = pathlib.Path.home() / 'Desktop'
            if path.exists(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt"):
                with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", 'r') as e:
                    install_dir = e.read()
                    if install_dir == str(desktop_dir):
                        log("Existing desktop file preference exists.")
                        log("The file will now no longer be located on the desktop.\n")
                        with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
                            e.close()
                        with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w") as f:
                            f.write(f"{sys.executable}\n{build}")
                        choice1()

            start_anim_loading("Initialising.")
            # log(f"Current directory: {directory}")
            try:
                copyfile(directory, f"{desktop_dir}\\DraggieTools.exe")
                stop_anim_loading()
                log("\nCopied executable to the desktop. Note that if the file is deleted or an update is applied, this version will need to be updated again and this move be reapplied.")
                with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
                    e.write(f"{desktop_dir}\n{build}")
            except FileNotFoundError:
                stop_anim_loading()
                log("\nRunning from PYTHON file. Not executable. This should log only in the development stage.")
                copyfile(f"{current_directory}\\DraggieTools.py", f"{desktop_dir}\\DraggieTools.py")
                log("I am very dumb. This will be improved later.")
            except SameFileError:
                stop_anim_loading()
                log("\nThis cannot be performed. The files are the same. Maybe it's already on the desktop!")
        case _:
            log("Custom directory selected.")
            y = location
            try:
                e = r"C:\Program Files"
                # y = input(f"Enter the new directory. For example, '{e}'. \nNote that wherever you install me to, a new folder will be added called 'Draggie' This means that inputting the directory above will be {c}.\n\nRight click to paste!\n>>> ")
                log(f"Current directory: {directory}")
                try:
                    mkdir(f"{y}\\Draggie\\")
                except Exception:
                    pass
                copyfile(directory, f"{y}\\Draggie\\DraggieTools.exe")

                log(f"Successfully copied file to {y}\\Draggie\\DraggieTools.exe")
                log(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Copied file from '{directory}' to desired directory {y}\\Draggie\\DraggieTools.exe")
            except Exception as e:
                log(f"An error occured. {e}")
                log("Please make sure that the file has not been renamed.")
                logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {traceback.format_exc()}")
                choice1()


def choice1():
    try:
        log(phrases[language]['menu_pre_options'], 1, True)
        x = input(phrases[language]['menu_options'])
        status_update(details="Selecting what to do...")
        """y = x/0 # in case we need to do some quick error checking!
        log(y)"""
        print(reset_colour)
        if x == "0":
            log(f"Goodbye! {time()}\nHope you found me useful.", 2, False)
            log("\n\n\n\n\n\nQuitting...")
            if client:
                client.close()
            sys.exit()

        match x:
            case "1":
                install_command()
            case "2":
                check_for_update()
            case "3":
                change_language()
            case "4":
                status_update(details="Modifying GameUserSettings.ini...")
                fort_file_mod()
            case "5":
                status_update(details="Managing Draggie Games Library", state="Draggie Games")
                project_saturnian()
            case "6":
                status_update(details="Downloading a torrent")
                torrent_downloader()
            case "7":
                status_update(details="Extracting Supercell game assets")
                autobrawlextractor()
            case "8":
                status_update(details="Cleaning up files")
                cleanup_files()
            case "9":
                status_update(details="In the Discord Tools menu")
                discord_tools()
            case "10":
                status_update(details="Installing AutoUpdater")
                draggieclient()
            case "11":
                status_update(details="In the YouTube downloader")
                yt_download()
            case "12":
                status_update(details="In the CMini Extraction Tool")
                cmini_extraction()
            case "13":
                status_update(details="Video Maker")
                videomaker()
            case "14":
                status_update(details="In the VBS Script Launcher")
                vbs_script_launcher()
            case "dev":
                status_update(details="In the developer menu")
                dev_menu()
            case "log":
                status_update(details="Uploading some logs")
                upload_logs()

            case "69":
                log(";)")
                status_update(details="In the secret menu", state="")
                secret_menu()

            case _:
                choice1()
        choice1()
    except KeyboardInterrupt:
        log("\nCancelled current operation.", raw=True)
        try:
            sleep(1)
        except KeyboardInterrupt:
            log("Press Ctrl+C 3 more times to exit.", raw=True)
            try:
                sleep(2)
            except KeyboardInterrupt:
                log("Press Ctrl+C 2 more times to exit..", raw=True)
                try:
                    sleep(3)
                except KeyboardInterrupt:
                    log("Press Ctrl+C 1 more time to exit...", raw=True)
                    try:
                        sleep(4)
                    except KeyboardInterrupt:
                        log("Goodbye!", raw=True)
                        return sys.exit(0)

            log("Okay, I'll stay.", raw=True)
            sleep(1)
        return choice1()
    except Exception as e:
        log(f"\n[WARNING] An unknown exception has occured: {e}\n\nTraceback: {traceback.format_exc(limit=5, chain=True)}\n\n", log_level=4)
        upload_logs_on_error_choice = input("To help fix this issue, you can upload your logs by pressing Enter. (Type 1 to not upload your logs.)\n\n>>> ")
        if not upload_logs_on_error_choice == "1":
            upload_logs(5)
        return choice1()


def main():
    try:
        log(f"{phrases[language]['run_from']} {current_directory}")
    except Exception:
        log("First time run detected.")
        change_language()
        log(f"{phrases[language]['run_from']}", 2)
    log(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: main() subroutine executed", 1, False)
    log(f"{green_colour}{random.choice(funny_messages)}")
    log(phrases[language]['menu_prompt'])
    save_json()

    choice1()


sys.stdout.write("\r")
sys.stdout.flush()
log(f"{clear_above_line_overwrite}Done! Loading base data...")

desktop_install_path = False

if path.exists(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt"):
    log("[MainInit] InstallDir_Pref exists.", 2, False)
    desktop_dir = pathlib.Path.home() / 'Desktop'
    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", "w+") as e:
        install_dir = e.read()
        if install_dir == str(desktop_dir):
            log(f"Determined install_dir to be desktop @ {desktop_dir}")
            desktop_install_path = True
        log(f"[MainInit] Determined install_dir to be '{install_dir}'. Read from file at {DraggieTools_AppData_Directory}\\InstallDir_Pref.txt")
else:
    log("[MainInit] Setting new file preference exists.", 2, False)
    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", 'w+') as f:
        f.close()
    with open(f"{DraggieTools_AppData_Directory}\\InstallDir_Pref.txt", 'w') as f:
        f.write(f"{DraggieTools_AppData_Directory}\n{build}")

log("[MainInit] Checking for update", 2, False)
check_for_update()

log("\nLoading Discord RPC...")


def start_discord_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(harry_loader())


loop = asyncio.new_event_loop()
thread = threading.Thread(target=start_discord_event_loop, args=(loop,))
thread.start()


current_directory = path.dirname(path.realpath(__file__))
if dev_mode:
    log(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: variable currrent_directory assigned with value {current_directory}")


try:
    log("Done! Entering program...")
    # pyi_splash.close()
    main()
except Exception as e:
    log(f"An unhandled exception was encountered.\nShort: {e}\n\nLong:\n{traceback.format_exc()}\n\nIt would be appreciated if you generate a logfile and DM it Draggie#3060. Thanks!\n")
    logging.error(traceback.format_exc())
    beans = input("Type 1 to upload your logs!\n\n>>> ")
    if beans == "1" or beans == "":
        upload_logs()
    main()
