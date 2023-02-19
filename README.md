# DraggieTools

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

This is a set of useful tools packaged into a quick and easy CLI which helps me do things, and also may be useful for anyone else! You can either download the Python source file and run yourself with the required imports, or go to /dist/DraggieTools.exe and download the executable, no imports required.

This has been optimised for Windows (using Windows paths and PyInstaller) so other systems may not work correctly. (Merge requests are always welcome though if you want to change this!)

For AutoBrawlExtractor, scroll down to see how it works.

> The file automatically updates to wherever it has been installed, so I recommend installing it to the desktop. As a result, it will require itself to be connected to github servers or it will throw errors, so cannot be used offline. It just checks the current build in this repo's `build.txt` and compares it to the one defined in the python code. If `githubusercontent.com` is blocked on the network, it will most likely fail.

# FortniteUserSettings

This is activated when you input [6] in the main menu. In this mode, you can:
- change and update your ingame FPS
- change and update your lobby FPS, removing the 120fps cap
- change and update graphics settings
- display all your current graphics settings
- take you quickly to the location of this saved file.

The most useful part of this in my opinion is unlocking the lobby FPS. To do this, select the `Framerate` option, then `FrontendFrameRateLimit` and then input something like 169 or 240. Enjoy!

# AutoBrawlExtractor
This is activated when you input [9] in the main menu. In ABS mode, you can:
- download assets directly from Supercell servers
- compare and extract the files of different versions of games
- download new (and old) build archives

To download assets, firstly you need to download a build from a list that I have made. It ranges from IPA v26 to the current build v47 for Brawl Stars. (Other apps will be available soon like Clash of Clans and Clash Mini.)

After an archive has been downloaded, the program will then inspect it and you can do many things. For example, downloading all music files, downloading files with a specific string or more. 

If you have multiple archives downloaded, you will be able to download files from between all versions. Let's say you want to download all music in updates throughout 2022. Simply download every build from 42.330 to 47.190, input `/music` and you're good to go.

It will even download files in the `/background` directory which is not included in APK or IPA builds' files.

## How does downloading the assets work?
Downloading Supercell assets require the `fingerprint.json` in the directory `Payload/<game>.app/res/fingerprint.json`. Then, in this json file, scroll to the bottom and there will be the `sha` and `version` keys, below all the files in the `files` key. (Prettifying the json will make this easier)

The important thing here is the value to the `sha` key. For example, for version 45.198.1, the sha is 117431f533a659d4a02a29d2e56b7ef74006d781.

> In Python, this can be accessed by:
```
import zipfile, json
archive = zipfile.ZipFile('path/to/file', 'r')
fingerprint_json = str(archive.read('Payload/Brawl Stars.app/res/fingerprint.json'), encoding="UTF-8")
fingerprint_json = json.loads(fingerprint_json)
sha = fingerprint_json['sha']
print (sha)
```

Next, you will need to get the download URL of the files. Note that this is the same syntax for all the Supercell games.

The base URL for Brawl Stars' assets is `game-assets.brawlstarsgame.com`. You can see this by looking at DNS requests while opening up the game for the first time.
You will then need to use the `sha` value from `fingerprint.json` as the initial path. This would look like `https://<base dir>/<sha>/`

Finally, you will need to put the location of the target file on the end of this path. This can be seen in the `files` key and subkeys in `fingerprint.json`, or by knowing a little about where a target file may be located in the archive. For example, `robot_factory_brawl_menu_01.ogg` would be in the `/music/` folder.
The final URL would then be this:

> `https://<base url>/<sha>/<path>/<to>/<file.ext>`
 
Or, populated, as an example:
 
> https://game-assets.brawlstarsgame.com/117431f533a659d4a02a29d2e56b7ef74006d781/music/robot_factory_brawl_menu_01.ogg

For Clash of Clans, here's an example:

> https://game-assets.clashofclans.com/55a54c313c4040c8568df2a58074549818934df2/music/capital_music.ogg

This can be automated within DraggieTools.py by simply searching for the filename, it will download it automatically with no other inputs necessary. You can even type in `/music` or even `.ogg`.


