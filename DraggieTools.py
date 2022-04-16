import random
from requests import get, head
from datetime import datetime
from os import path, startfile, mkdir, environ
from time import monotonic
import shutil
from sys import exit

build = 19
version = "0.2.4"
build_date = 1650051197

global language

english = ["Key error occured: ", "\n\nResorting to backup", "Downloading.", "done, average speed", "Checking for update...\n", "Downloading update...", "Running from", "What would you like to do, my friend?", "Transfering sensitive files to The Criminal Network...", "Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION", r"Problem opening the application running at executable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Would you like to scan this PC?", "Your tools are up to date. Running version", "built at", "build", "The server says the newest build is", "Update available!", "You are on version", "The newest version is build", "Type 1 to download update, or enter to skip", "This is index 20 (defined under **language[20]**), if you see this then report as error.", "Opening up the source Python file in Explorer. To view it, open it in Notepad or you could upload it to an IDE online."]# Index number 20 -   ENGLISH
french = ["Desolée", "\n\nRecourir à la sauvegarde", "Téléchargement.", "fini, vitesse moyenne", "Vérification de la mise à jour...\n", "Téléchargement de la mise à jour...", "En cours d'exécution à", "Qu'est-ce que tu voudrais faire, mon ami(e) ?", "Transfert de fichiers sensibles vers le réseau criminel...", "Votre ordinateur est piraté par IP : 5.172.193.104 comme OS : LINUX UBUNTU et emplacement : FÉDÉRATION DE RUSSIE", r"Problème d'ouverture de l'application exécutée sur l'exécutable 'C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe'. Voulez-vous scanner ce PC ?", "Vos outils sont à jour. Version en cours d'exécution", "fait à", "mini-version", "Le serveur dit que la nouvelle version est", "Mise à jour disponsible !", "Vous êtes sur le mini-version", "Le mini-version nouvelle est", "Ecrivez 1 pour télécharge la mise à jour, ou entre pour ignorer", "This is index 20 in french (defined under **language[20]**), if you see this then report as error.", "Ouverture du fichier Python source dans l'Explorateur. Pour le voir, ouvre ceci dans Bloc-notes Windows ou vous pouvez le télécharger sur un IDE en ligne."]#     FRENCH
DraggieTools_AppData_Directory = (f"{environ['USERPROFILE']}\\AppData\\Roaming\\Draggie\\DraggieTools")

def change_language():
    global language
    language = None
    while language is None:
        x = input("Choose language\nChoisissez la langue\nEnglish = 1, French = 2\n\n>>> ")
        if x == "2":
            print("La langue est maintenant francais.")
            language = french
            x = open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w+")
            x.close()
            x = open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w")
            x.write("French")
            x.close()
        else:
            print("Language updated to English.")
            language = english
            x = open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w+")
            x.close()
            x = open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt", "w")
            x.write("English")
            x.close()

if not path.exists(DraggieTools_AppData_Directory):
    mkdir(DraggieTools_AppData_Directory)
if path.exists:
    try:
        x = open(f"{DraggieTools_AppData_Directory}\\Langauge_Preference.txt")
        language_read = x.read()
        x.close
        if language_read == "French":
            language = french
            print("Language set to French.")
        else:
            language = english
            print("Language set to English.")
    except Exception as e:
        change_language()


current_directory = path.dirname(path.realpath(__file__))
print(f"{language[6]} {current_directory}")


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
                    print(f'{language[2]} {pct_done}% {language[3]} {speed} kbps')
                    last_print = now
    except KeyError as e:
        print(f"{language[0]}{e}{language[1]}")
        r = get('https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true')
        with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
            f.write(r)


def view_source():
    print(language[20])

def check_for_update():
    print(language[4])
    x = (get('https://draggietools.ibaguette.com/checks/version_link.txt')).text
    current_build_version = int((get(x)).content)
    if build < current_build_version:
        release_notes = str((get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/release_notes.txt")).content)
        print(f"{language[15]} {language[16]} {version} {language[17]} {build}. {language[18]} {current_build_version}\n\n{language[19]}\n")
        if language == "English":
            print(f"Release notes: \n{release_notes}\n")
        update_choice = input("")
        if update_choice == "1":
            print(language[6])
            download_update(current_build_version)
            print("Update downloaded. Launching new version...")
            startfile(f'{current_directory}\\DraggieTools-{current_build_version}.exe')
            exit()
        else:
            print("Skipping update.")
            return
    else:
        print(f"{language[11]} {version} - {language[13]} {build} - {language[12]} {datetime.fromtimestamp(1650035010).strftime('%Y-%m-%d %H:%M:%S')}. {language[14]} {current_build_version}.")


check_for_update()


def main():
    the_funny = [f'{language[8]}', f'{language[9]}', f'{language[10]}']
    print(f"{random.choice(the_funny)}")
    print(language[7])

    def choice1():
        if language == french:
            x = input("\n\n1) Installez ceci sur le bureau\n2) Installez ceci dans un répertoire personnalisé\n3) Créez un raccourci sur le bureau\n4) Actualises les mises à jour\n5) Changez la langue\n6) Regarde le code source\n\n>>> ")
        if language == english:
            x = input("\n\n1) Install this to desktop\n2) Install this to custom directory\n3) Create shortcut on desktop\n4) Refresh updates\n5) Change language\n6) View source code\n\n>>> ")
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
                except Exception:
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
        if x == "5":
            change_language()
            choice1()
        if x == "6":
            view_source()
            choice1()
        else:
            choice1()

    choice1()


main()
