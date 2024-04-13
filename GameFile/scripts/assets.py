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
Screenmode = "normal"
mode = "menu"
round = -1
rounds = [#["shop"],
          [["bidoof"]],
          [["bidoof","rick"],["bidoof","bidoof"],[],["GINO"],["bidoof"],["gold"]],
          [["rick", "rick", "rick", "bidoof"],["sonic"],["bidoof"],["gold"]],
          [["GINO", "rick"],["rick","rick"],["sonic"],["rick"],["gold"]],
          [["GINO", "sonic"],["sonic"],["sonic"],["gold"]],
          ["shop"],
          [["bidoof"],[],[],["gold"]],
          [["bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof"],["bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof", "bidoof","bidoof"],["bidoof"],["gold"]],
          ["shop"],
          [["rick","rick","rick","rick","GINO","GINO"],["bidoof","bidoof","bidoof","DancingGhost"],["rick","steeve","SUS","DancingGhost"],["gold","PurpleGuy","DancingGhost"]],
          [["GINO","GINO","steeve","sonic"],["steeve","sonic","SUS","SUS"],["steeve","DancingGhost"],["gold","PurpleGuy","DancingGhost"],["SUS","DancingGhost"],["DragoGomma","DancingGhost"]],
          [["SUS","SUS","SUS","GINO","sonic","steeve"],["DancingGhost","bidoof","steeve","sonic"],["SUS","GINO","gold","PurpleGuy","DancingGhost"],["DragoGomma","DancingGhost"]],
          ["shop"],
          ["heal"],
          [["breadbug"],["bidoof","bidoof","bidoof","bidoof"]],
          ["shop"],
          ["heal"],
          [["PurpleGuy","SUS","PurpleGuy","steeve"],["SUS","PurpleGuy","steeve","GINO","bidoof","DancingGhost"],["bidoof","rick","DragoGomma","DancingGhost"],["gold","DancingGhost"]],
          [["sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic","sonic"]],
          [["PurpleGuy","DragoGomma","DragoGomma","SUS","steeve"],["PurpleGuy","DragoGomma","SUS","steeve","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof"],["gold","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof"],["gold","bidoof","bidoof","bidoof","bidoof","bidoof","bidoof"]]]

def BasePygameCicle(event, screen):
    global screen_width, screen_height , Screenmode, width, height
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            if Screenmode == "normal":
                screen = pygame.display.set_mode(
                    (screen_width, screen_height), pygame.FULLSCREEN)
                Screenmode = "full"
            else:
                screen = pygame.display.set_mode(
                    (width, height), pygame.RESIZABLE)
                Screenmode = "normal"
    elif event.type == pygame.VIDEORESIZE and Screenmode == "normal":
        width, height = screen.get_size()
