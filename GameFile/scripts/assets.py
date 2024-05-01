import pygame
import os

pygame.font.init()
pygame.mixer.init()

yee = pygame.image.load("GameFile/image/yee.png").convert_alpha()
SartButton = pygame.image.load("GameFile/image/start.png").convert_alpha()
QuitButton = pygame.image.load("GameFile/image/quit.png").convert_alpha()
MenuButton = pygame.image.load("GameFile/image/menu.png").convert_alpha()
PlayerButton = pygame.image.load("GameFile/image/player.png").convert_alpha()
back = pygame.image.load("GameFile/image/background.png").convert_alpha()
player = pygame.image.load("GameFile/image/player/catto.png").convert_alpha()
bobble = pygame.image.load("GameFile/image/bobble.png").convert_alpha()

attack = pygame.mixer.Sound("GameFile/sound/attack1.mp3")
LevelUp = pygame.mixer.Sound("GameFile/sound/LevelUp.mp3")
meow = []
for filename in os.listdir("GameFile/sound/meow"):
    if filename.endswith(".wav") or filename.endswith(".mp3"):
        filepath = os.path.join("GameFile/sound/meow", filename)
        meow.append(pygame.mixer.Sound(filepath))

font = pygame.font.SysFont(None, 64)

width = 800
height = 600
mode = "menu"
round = 0
rounds = [#["shop"],    
          [["TheBidoof"],["Tree","Tree"]],
          [["bidoof","rick","Tree"],["bidoof","bidoof","Tree"],[],["GINO"],["bidoof"],["gold"]],
          [["rick", "rick", "rick", "bidoof"],["sonic","Tree","Tree"],["bidoof","Tree"],["gold"]],
          [["GINO", "rick","Tree"],["rick","rick","Tree"],["sonic","Tree"],["rick","Tree"],["gold","Tree"]],
          ["shop"],
          [["GINO", "sonic"],["sonic","Tree"],["sonic"],["gold","Tree"]],
          [["bidoof"],[],[],["gold"]],
          [["bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof"],
           ["bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","Tree","Tree"],
           ["bidoof","bidoof","bidoof","bidoof","Tree"],["gold"]],
          ["shop"],
          [["rick","rick","rick","rick","GINO","GINO","Tree"],
           ["bidoof","bidoof","bidoof","DancingGhost"],
           ["rick","steeve","SUS","DancingGhost"],["gold","PurpleGuy","DancingGhost"]],
          [["GINO","GINO","steeve","sonic"],
           ["steeve","sonic","SUS","SUS"],
           ["steeve","DancingGhost","Tree"],["gold","PurpleGuy","DancingGhost"],["SUS","DancingGhost"],["DragoGomma","DancingGhost"]],
          [["SUS","SUS","SUS","GINO","sonic","steeve"],
           ["DancingGhost","bidoof","steeve","sonic","Tree","Tree"],
           ["SUS","GINO","gold","PurpleGuy","DancingGhost"],["DragoGomma","DancingGhost"]],
          ["shop"],
          ["heal"],
          [["breadbug"],["bidoof","bidoof","bidoof","bidoof","chicken","chicken","chicken"]],
          ["heal"],
          ["shop"],
          [["PurpleGuy","SUS","PurpleGuy","steeve","Tree"],
           ["SUS","PurpleGuy","steeve","GINO","bidoof","DancingGhost","chicken","chicken"],
           ["bidoof","rick","DragoGomma","DancingGhost"],["gold","DancingGhost","calziniShooter"],["calziniShooter"]],
          [["sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic"],["chicken"]],
          ["shop"],
          [["PurpleGuy","DragoGomma","DragoGomma","SUS","steeve","chicken","chicken","chicken","chicken","chicken"],
           ["PurpleGuy","DragoGomma","chicken","chicken","chicken","chicken","chicken","chicken","SUS","steeve","calziniShooter"]],
          [["Tree","DragoGomma","DragoGomma","DragoGomma","PurpleGuy","chicken","chicken","chicken","chicken"],
           ["calziniShooter","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","SUS","steeve"],
           ["gold","calziniShooter"]],
          ["shop"],
          ["heal"],
          [["calziniShooter","chicken","chicken","chicken","chicken","chicken","chicken","chicken","calziniShooter","calziniShooter","calziniShooter"],
           ["calziniShooter","chicken","chicken","chicken","chicken","chicken","chicken","calziniShooter",],
           ["chicken","chicken","chicken","calziniShooter","calziniShooter","calziniShooter","calziniShooter","calziniShooter"]],
          [["DragoGomma","calziniShooter","calziniShooter","calziniShooter","calziniShooter","calziniShooter","SUS","chicken","chicken","chicken"],
           ["chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"],
           ["chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"],
           ["SUS","SUS","SUS","SUS","PurpleGuy","chicken","chicken","chicken","chicken""PurpleGuy","steeve"],
           ["gold","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"]],
          ["shop"],
          ["heal"],
          [["doge"],
           ["chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"],
           ["chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"],
           ["chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"],
           ["chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"],
           ["chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken","chicken"]],
          ["shop"],
          ["heal"],
          [["UgKnukles","UgKnukles","Charizard"],["UgKnukles","PurpleGuy","Mario"],["UgKnukles"],["Charizard","UgKnukles","gold"]],
          [["UgKnukles","UgKnukles","UgKnukles","UgKnukles","Mario"],["UgKnukles","UgKnukles","UgKnukles","UgKnukles","Mario"],
           ["gold","UgKnukles","UgKnukles","UgKnukles","UgKnukles","UgKnukles"]],
          ["shop"],
          [["bidoof"],
           ["Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree"],
           ["Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree","Tree"]]]