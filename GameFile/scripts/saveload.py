import os
import GameFile.scripts.assets as assets
import GameFile.scripts.player as player
import GameFile.scripts.assets as assets

def saveLoad():
    files = os.listdir("saves")
    saves =  [file for file in files if os.path.isfile(os.path.join("saves", file))]
    saves = [os.path.splitext(file)[0] for file in saves]
    if len(saves) > 0:
        print(saves)
        print("scrivendo il nome quale salvataggio vuoi caricare?")
        print("se vuoi creare un nuovo salvataggio scrivi new")
        print("se vuoi cancellare un salvataggio scrivi del")
        scelta = input()
        if scelta == "new":
            name = input("come vuoi chiamare il salvataggio?")
            with open("saves/"+name+".save", "w") as file:
                pass
            player.Player = player.player(
                                (300, 300), assets.player, "saves/"+name+".save")
        elif scelta == "del":
            name = input("quale salvataggio vuoi cancellare?")
            if name in saves:
                os.remove("saves/"+name+".save")
            else:
                print("il salvataggio digitato non esiste")
                saveLoad()
                return
        elif scelta in saves:
            player.Player = player.player(
                            (300, 300), assets.player, "saves/"+scelta+".save", True)
        else:
            print("il file non esiste")
            saveLoad()
            return
    else:
        name = input("come vuoi chiamare il salvataggio?")
        with open("saves/"+name+".save", "w") as file:
            pass
        player.Player = player.player(
                            (300, 300), assets.player, "saves/"+name+".save")

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
