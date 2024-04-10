import os
import GameFile.scripts.assets as assets


def saveLoad():
    pass


def loadSetting():
    if os.path.exists("GameFile/settings.txt"):
        with open("GameFile/settings.txt", 'r') as file:
            assets.screen_width = int(file.readline().strip())
            assets.screen_height = int(file.readline().strip())
    else:
        print("Missing settings")
        assets.screen_width = input("inserire larghezza dello schermo")
        assets.screen_height = input("inserire altezza del tuo schermo")
        with open("GameFile/settings.txt", 'w') as file:
            contenuto = [assets.screen_width +
                         '\n', assets.screen_height + '\n']
            file.writelines(contenuto)
