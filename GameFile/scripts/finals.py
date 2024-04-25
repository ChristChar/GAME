import pygame
import time
import ctypes
import random
import GameFile.scripts.player as player
import GameFile.scripts.assets as assets
import GameFile.scripts.cutSceen as CutSceen

def FINE(screen):
    if "papera" in player.Player.items:
        CutSceen.ViewCutSceen(screen, "GameFile/CutSceen/quak.mp4")
    elif random.random() < 0.1:
        CutSceen.ViewCutSceen(screen, "GameFile/CutSceen/crash.mp4")
        ctypes.windll.user32.MessageBoxW(0, 'Fatal Error', 'Error', 0x10)
        W,H = screen.get_size()
        pygame.display.quit()
        time.sleep(3)
        screen = pygame.display.set_mode(
            (W, H), pygame.RESIZABLE)
        CutSceen.ViewCutSceen(screen, "GameFile/CutSceen/crash2.mp4")
    else:
        CutSceen.ViewCutSceen(screen, "GameFile/CutSceen/normal.mp4")
    assets.mode = "menu"
    assets.round = 0