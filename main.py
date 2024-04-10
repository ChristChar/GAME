import pygame
screen = pygame.display.set_mode(
    (800, 600), pygame.RESIZABLE)
import random
import GameFile.scripts.assets as assets
import GameFile.scripts.saveload as save
import GameFile.scripts.notification as notific
import GameFile.scripts.cutSceen as CutSceen
import GameFile.scripts.player as player
import GameFile.scripts.enemies as enemy

#C:\Users\chris\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\pyinstaller.exe --onefile --icon=yee.ico main.py

pygame.font.init()
pygame.init()

save.loadSetting()

pygame.display.set_caption("giuoco")
pygame.display.set_icon(assets.yee)
screen = pygame.display.set_mode(
    (assets.width, assets.height), pygame.RESIZABLE)

startRect = pygame.rect.Rect(1, 1, 1, 1)
quitRect = pygame.rect.Rect(1, 1, 1, 1)

def drawnBtton(ScW, ScH, button, rect, position):
    NewScalY = ScH / 10
    rect.height = NewScalY
    NewScalX = NewScalY * 3
    rect.width = NewScalX
    buttonR = pygame.transform.scale(button, (NewScalX, NewScalY))
    posX = ScW / 2 - NewScalX / 2
    rect.x = posX
    posY = ScH / 2 - NewScalY / 2
    rect.y = posY + position
    screen.blit(buttonR, (posX, posY + position))


while True:
    larghezza, altezza = assets.yee.get_size()
    Width, Height = screen.get_size()
    for event in pygame.event.get():
        assets.BasePygameCicle(event, screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if assets.mode == "menu":
                    if startRect.collidepoint(mouse_x, mouse_y):
                        assets.mode = "game"
                        player.Player = player.player(
                            (300, 300), assets.player)
                    if quitRect.collidepoint(mouse_x, mouse_y):
                        pygame.quit()
                        quit()
                elif assets.mode == "game" and player.Player.state != "protected":
                    for i in enemy.Enemys:
                        if i.rect.collidepoint(mouse_x, mouse_y):
                            player.Player.attack(i)
    if assets.mode == "menu":
        screen.fill((255, 255, 255))
        pos_y = Height - altezza
        screen.blit(assets.yee, (0, pos_y))
        drawnBtton(Width, Height, assets.SartButton, startRect, 0)
        drawnBtton(Width, Height, assets.QuitButton, quitRect, 150)
    if assets.mode == "game":
        back = pygame.transform.scale(assets.back, (Width, Height))
        screen.blit(back, (0, 0))
        enemy.EnemyUpdate(screen, player.Player)
        player.Player.update(screen)
    notific.notification(screen)
    pygame.display.update()
