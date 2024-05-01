from os import error
import pygame



screen = pygame.display.set_mode(
    (800, 600), pygame.RESIZABLE)
import time
import ctypes
import GameFile.scripts.saveload as save
import GameFile.scripts.assets as assets
import GameFile.scripts.notification as notific
import GameFile.scripts.cutSceen as CutSceen
import GameFile.scripts.player as player
import GameFile.scripts.enemies as enemy
import GameFile.scripts.progliettili as progliettili
import GameFile.scripts.pygameEventCycles as cicles
import GameFile.scripts.finals as end
import GameFile.scripts.buttons as buttons
from GameFile.scripts.shop import shop

pygame.display.quit()

save.loadSetting()
save.saveLoad()

screen = pygame.display.set_mode(
    (800, 600), pygame.RESIZABLE)

pygame.font.init()
pygame.init()

pygame.display.set_caption("giuoco")
pygame.display.set_icon(assets.yee)
screen = pygame.display.set_mode(
    (assets.width, assets.height), pygame.RESIZABLE)

clock = pygame.time.Clock()
Fpss = []
lastFPS = 0
fps = assets.font.render("FPS: ", True, (0,0,0))

def writeStat(self):
    Level = assets.font.render(
        "L: "+str(self.playerStat["L"]), True, (0, 0, 0))
    hp = assets.font.render(
        "vita: "+str(self.life)+"/"+str(self.playerStat["stat"][0]), True, (0, 0, 0))
    att = assets.font.render(
        "attacco: "+str(self.playerStat["stat"][1]), True, (0, 0, 0))
    dif = assets.font.render(
        "difesa: "+str(self.playerStat["stat"][2]), True, (0, 0, 0))
    vel = assets.font.render(
        "velocità: "+str(self.playerStat["stat"][3]), True, (0, 0, 0))
    Msta = assets.font.render(
        "Max stanima: "+str(self.playerStat["stat"][4]), True, (0, 0, 0))
    attSp = assets.font.render(
        "velocità di attacco: "+str(self.playerStat["stat"][5]/1000)+"s", True, (0, 0, 0))
    regSp = assets.font.render(
        "velocità di rigenerazione: "+str(round(self.playerStat["stat"][6],2))+"s", True, (0, 0, 0))
    Attdist = assets.font.render(
        "distanza min. di attacco: "+str(self.playerStat["stat"][7])+"px", True, (0, 0, 0))
    CrtChan = assets.font.render(
        "possibilità si colpo critico: "+str(round(1 / self.playerStat["stat"][8] * 100,2))+"%", True, (0, 0, 0))
    death = assets.font.render(
        "morti: "+str(self.death), True, (0, 0, 0))
    stat = [Level,hp, regSp, att, attSp, Attdist, CrtChan, dif, vel, Msta, death]
    return stat

while True:
    clock.tick()
    Width, Height = screen.get_size()
    cicles.pygameEventCicles()
    if assets.mode == "menu":
        larghezza, altezza = assets.yee.get_size()
        screen.fill((255, 255, 255))
        buttons.updateButtons(screen)
        pos_y = Height - altezza
        screen.blit(assets.yee, (0, pos_y))
    elif assets.mode == "game":
        back = pygame.transform.scale(assets.back, (Width, Height))
        screen.blit(back, (0, 0))
        enemy.EnemyUpdate(screen, player.Player)
        player.Player.update(screen)
        progliettili.progliettiliUpdate(screen, enemy.Enemys, player.Player)
    elif assets.mode == "gameMenu":
        back = pygame.transform.scale(assets.back, (Width, Height))
        screen.blit(back, (0, 0))
        pygame.draw.rect(screen, (150,150,150), (Width/6, Height/6, Width/1.5, Height/1.5))
        buttons.updateButtons(screen)
    elif assets.mode == "statView":
        screen.fill((50,255,50))
        stat = writeStat(player.Player)
        for i in range(len(stat)):
            screen.blit(stat[i], (0 + 50,
                        0 + i * (Height/11)+20))
    elif assets.mode == "custom":
        screen.fill((255, 255, 255))
        buttons.updateButtons(screen)
    notific.notification(screen)
    if pygame.time.get_ticks() - lastFPS >= 1000 and len(Fpss) > 0:
        FPS = sum(Fpss) / len(Fpss)
        fps = assets.font.render("FPS: "+str(round(FPS)), True, (0,0,0))
        lastFPS = pygame.time.get_ticks()
        Fpss = []
    else:
        Fpss.append(clock.get_fps())
    A,L = fps.get_size()
    screen.blit(fps, (Width-10-A,0+10+L))
    pygame.display.update()
