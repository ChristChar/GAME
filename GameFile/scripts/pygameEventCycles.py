import pygame
import GameFile.scripts.assets as assets
import GameFile.scripts.player as player
import GameFile.scripts.enemies as enemy
import GameFile.scripts.buttons as buttons

def BaseCicle(event):
    if event.type == pygame.QUIT:
        player.Player.saveProgres()
        pygame.quit()
        quit()

def MenuCicles():
    for event in pygame.event.get():
        BaseCicle(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                buttons.ControllButtons(event)

def CustomCicles():
    for event in pygame.event.get():
        BaseCicle(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                buttons.ControllButtons(event)
        elif event.type == pygame.KEYDOWN:               
            if event.key == pygame.K_ESCAPE:
                assets.mode = "menu"

def GameMenuCicles():
    for event in pygame.event.get():
        BaseCicle(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                buttons.ControllButtons(event)
        elif event.type == pygame.KEYDOWN:               
            if event.key == pygame.K_ESCAPE:
                assets.mode = "game"

def StatViewCicles():
    for event in pygame.event.get():
        BaseCicle(event)
        if event.type == pygame.KEYDOWN:               
            if event.key == pygame.K_ESCAPE:
                assets.mode = "gameMenu"

def GameCicles():
    for event in pygame.event.get():
        BaseCicle(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   
                mouse_x, mouse_y = event.pos
                if player.Player.state != "protected":
                    for i in enemy.Enemys:
                        if i.rect.collidepoint(mouse_x, mouse_y):
                            player.Player.attack(i)
        elif event.type == pygame.KEYDOWN:               
            if event.key == pygame.K_ESCAPE:
                assets.mode = "gameMenu"

cicles = {"menu":MenuCicles, "gameMenu":GameMenuCicles, "game":GameCicles,"statView":StatViewCicles, "custom":CustomCicles}

def pygameEventCicles():
    cicles[assets.mode]()
                    