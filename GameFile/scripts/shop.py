import pygame
import random
import math
import ctypes
import GameFile.scripts.assets as assets
import GameFile.scripts.notification as notific
import GameFile.scripts.progliettili as progliettili
import GameFile.scripts.pygameEventCycles as cicle
import GameFile.scripts.functions as F

banana = random.choice(assets.meow)
ShootColdown = 0
channel = None

def meow(player, screen, enemys):
    global banana
    global channel
    if channel is not None and channel.get_busy() and banana == channel.get_sound():
        width, height = screen.get_size()
        x,y = random.randint(round(width*0.1),round(width*0.7)),random.randint(round(height*0.1),round(height*0.7))
        screen.blit(items["cat"]["image"], (x,y))
        object_rect = pygame.Rect(x, y, 225, 225)
        if random.random() < 0.1:
            for i in enemys:
                if i.rect.colliderect(object_rect):          
                    NewNotification = notific.Notifica(
                            str(1), i.rect.center, (255, 0, 0), 1000)
                    notific.notifiche.append(NewNotification)
                    i.life -= 1
    else:
        if random.random() < 0.001:
            banana =  random.choice(assets.meow)
            channel = banana.play()

def knife(player, screen, enemys):
    coltello = pygame.transform.scale(items["knife"]["image"], (80,80))
    screen.blit(coltello, (player.x,player.y+10))

def longSword(player, screen, enemys):
    coltello = pygame.transform.scale(items["longSword"]["image"], (100,100))
    coltello = pygame.transform.rotate(coltello, random.randint(-10,10))
    screen.blit(coltello, (player.x-10,player.y+10))

def pescio(player, screen, enemys):
    coltello = pygame.transform.scale(items["Pesce Spada"]["image"], (100,100))
    coltello = pygame.transform.rotate(coltello, random.randint(-10,10))
    screen.blit(coltello, (player.x-10,player.y+10))

def gun(player, screen, enemys):
    coltello = pygame.transform.scale(items["gun"]["image"], (80,80))
    screen.blit(coltello, (player.x-30,player.y+10))

def rock(player, screen, enemys):
    coltello = pygame.transform.scale(items["sasso"]["image"], (70,70))
    screen.blit(coltello, (player.x+5,player.y-40))

def scudo(player, screen, enemys):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        player.state = "protected"
    else:
        player.state = "normal"
    if player.state == "protected":
        screen.blit(assets.bobble, (player.x - 60, player.y - 60))

def fireBall(player, screen, enemys):
    global ShootColdown
    if pygame.time.get_ticks() - ShootColdown >= 2000:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            delta_y = mouse_y - player.y
            delta_x = mouse_x - player.x
            angolo_radiani = math.atan2(delta_y, delta_x)
            angolo_gradi = math.degrees(angolo_radiani)
            angolo_gradi = (angolo_gradi + 360) % 360
            NewFireBall = progliettili.Progliettile("fireBall",[player.x,player.y],angolo_gradi)
            progliettili.progliettili.append(NewFireBall)
            ShootColdown = pygame.time.get_ticks()

items = {
    "knife": {
        "type": "weapon",
        "image": pygame.image.load("GameFile/image/items/knife.png").convert_alpha(),
        "cost": 100,
        "addStat": [0, 10, 0, 0, 0, 0, 0, -20, -1],
        "specialScript": [knife],
        "description": "+attacco -range"
    },
    "longSword": {
        "type": "weapon",
        "image": pygame.image.load("GameFile/image/items/longsword.png").convert_alpha(),
        "cost": 250,
        "addStat": [0, 20, 0, 0, 0, 0, 0, 10, -5],
        "specialScript": [longSword],
        "description": "++attacco +range"
    },
    "Pesce Spada": {
        "type": "weapon",
        "image": pygame.image.load("GameFile/image/items/pesceSpada.png").convert_alpha(),
        "cost": 100,
        "addStat": [10, 10, 1, 0, 0, 0, 0, 5, 0],
        "specialScript": [pescio],
        "description": "+vita +attacco +range"
    },
    "sasso": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/sasso.png").convert_alpha(),
        "cost": 150,
        "addStat": [10, 5, 5, -10, 0, 100, 0, -5, -5],
        "specialScript": [rock],
        "description": "+vita +attacco +difesa -velocità -att speed"
    },
    "cat": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/cat.png").convert_alpha(),
        "cost": 150,
        "addStat": [5, 0, 5, -5, 0, 0, 0, 5, -5],
        "specialScript": [meow],
        "description": "+difesa a caso appare e fa danni a caso"
    },
    "acqua": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/water.png").convert_alpha(),
        "cost": 50,
        "addStat": [10, 0, 2, 5, 0, 0, -0.6, 0, 0],
        "specialScript": [],
        "description": "+vita +difesa"
    },
    "gun": {
        "type": "weapon",
        "image": pygame.image.load("GameFile/image/items/gun.png").convert_alpha(),
        "cost": 250,
        "addStat": [0, 0, 0, 0, 0, 0, 0, 500,0],
        "specialScript": [gun],
        "description": "++++++++++++range"
    },
    "fiore": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/fiore.png").convert_alpha(),
        "cost": 25,
        "addStat": [5, 1, 1, 5, 5, 0, -0.01, 0,0],
        "specialScript": [],
        "description": "un poco poco di tutto"
    },
    "papera": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/paperella.png").convert_alpha(),
        "cost": 1000,
        "addStat": [-50, 10, -1, 5, 0, 0, -0.05, -10,-5],
        "specialScript": [],
        "description": "-----vita +attaco -difesa -reg.Speed -range +CritChance"
    },
    "cuore": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/cuore.png").convert_alpha(),
        "cost": 70,
        "addStat": [20, 0, 0, 0, 0, 0, 0, 0,0],
        "specialScript": [],
        "description": "++vita"
    },
    "tonno": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/TONNO.png").convert_alpha(),
        "cost": 70,
        "addStat": [0, 0, 0, 50, 0, 0, 0, 0,0],
        "specialScript": [],
        "description": "+++++ velocità"
    },
    "scudo": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/scudo.png").convert_alpha(),
        "cost": 150,
        "addStat": [0, 0, 1, 0, 0, 0, 0, 0,0],
        "specialScript": [scudo],
        "description": "+difesa quando premi CTRL puoi attivare lo scudo che non ti fa prendere danni ma non puoi attaccare e sei lento"
    },
    "fireBall": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/FireBall.png").convert_alpha(),
        "cost": 250,
        "addStat": [0, 1, 0, 0, 0, 0, 0, 0,0],
        "specialScript": [fireBall],
        "description": "premi E per sparare delle palle di fuoco con danno medio di 50"
    },
    "pinguino carino": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/pinguino.png").convert_alpha(),
        "cost": 400,
        "addStat": [30, 0, 10, 5, 0, 0, -1, 0,-10],
        "specialScript": [],
        "description": "+++vita ++difesa ++++reg.Speed +++CritChance"
    }
    }

def shop(screen, player):
    shop = pygame.image.load("GameFile/image/shop.png").convert_alpha()
    purchase = pygame.mixer.Sound("GameFile/sound/purchase.mp3")
    itemsInShop = []
    rects = []
    itemsKeys = list(items.keys())  
    for i in range(6):
        itemsInShop.append(random.choice(itemsKeys))
        rects.append(pygame.rect.Rect(0,0,255,255))
    while True:
        screen.fill((255, 255, 255))
        larghezza, altezza = shop.get_size()
        screen_width, screen_height = screen.get_size()
        scale_ratio = screen_width / larghezza * 0.6
        frame_surface = pygame.transform.scale(shop, (round(larghezza * scale_ratio), round(altezza * scale_ratio)))
        posY = screen_height - round(altezza * scale_ratio)
        posX = screen_width / 2 - round(larghezza * scale_ratio) / 2
        screen.blit(frame_surface, (posX, posY))
        grid_width = screen_width // 3 
        grid_height = screen_height // 2
        horizontal_space = (grid_width * 0.1) // (3 - 1)
        vertical_space = -100 // (2 - 1)
        itemN = 0
        for row in range(2):
            for col in range(3):
                if itemsInShop[itemN] is not None:
                    x = col * (grid_width + horizontal_space)
                    y = row * (grid_height + vertical_space)
                    screen.blit(items[itemsInShop[itemN]]["image"], (x, y)) 
                    rects[itemN].x, rects[itemN].y = x,y 
                    cost = assets.font.render(str(items[itemsInShop[itemN]]["cost"]), True, (50,50,20))
                    larghezza, _ = cost.get_size()
                    posizione_x = x + 225 / 2 - larghezza / 2
                    posizione = (posizione_x, y + 170)
                    screen.blit(cost, posizione)
                itemN += 1
        money = assets.font.render(
            "€"+str(player.money), True, (255, 255, 0))
        enter = assets.font.render(
            "press enter for exit", True, (0, 0, 0))
        wiii, _ = money.get_size()
        screen.blit(money, (10,10)) 
        screen.blit(enter, (20+ wiii,10)) 
        notific.notification(screen)
        for i, rect in enumerate(rects):
            if rect is not None:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if rect.collidepoint(mouse_x, mouse_y):
                    dimension = screen_height / 6
                    description_box = pygame.Rect(mouse_x+10, mouse_y+10, dimension*1.7, dimension)
                    pygame.draw.rect(screen, (0, 0, 0), description_box) 
                    font = pygame.font.SysFont(None, int(dimension / 4.5))
                    description_text = itemsInShop[i]+": "+items[itemsInShop[i]]["description"]
                    description_box = pygame.Rect(mouse_x+15, mouse_y+15, dimension*1.65, dimension*0.95)
                    F.draw_text_within(screen, description_text, description_box, font, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            cicle.BaseCicle(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    for i in range(6):
                        if rects[i] is not None:
                            if rects[i].collidepoint(mouse_x, mouse_y):
                                if player.money >= items[itemsInShop[i]]["cost"]:
                                    if items[itemsInShop[i]]["type"] == "weapon":
                                        weapon = None
                                        for w in player.items:
                                            if items[w]["type"] == "weapon":
                                                weapon = w
                                                break
                                        if weapon is not None:
                                            input = ctypes.windll.user32.MessageBoxW(None, "hai già un'arma, vuoi sostiture la tua corrente arma: "+weapon+" con "+itemsInShop[i], 'there is a little problem', 0x00000004)
                                            if input == 6:
                                                player.items.remove(weapon)
                                            else:
                                                break
                                    purchase.play()
                                    player.money -= items[itemsInShop[i]]["cost"]
                                    player.items.append(itemsInShop[i])
                                    itemsInShop[i] = None
                                    rects[i] = None
                                    player.statCalcolate()
                                else:
                                    NewNotification = notific.Notifica("sei povero!!!", [100,altezza/2-50], (40,0,0), 2500,3, True)
                                    notific.notifiche.append(NewNotification)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return


