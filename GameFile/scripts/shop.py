import pygame
import random
import GameFile.scripts.assets as assets
import GameFile.scripts.notification as notific

banana = random.choice(assets.meow)
channel = None

def meow(player, screen):
    global banana
    global channel
    if channel is not None and channel.get_busy() and banana == channel.get_sound():
        width, height = screen.get_size()
        screen.blit(items["cat"]["image"], (random.randint(round(width*0.1),round(width*0.7)),random.randint(round(height*0.1),round(height*0.7))))
    else:
        if random.random() < 0.001:
            banana =  random.choice(assets.meow)
            channel = banana.play()

def knife(player, screen):
    coltello = pygame.transform.scale(items["knife"]["image"], (80,80))
    screen.blit(coltello, (player.x,player.y+10))

def longSword(player, screen):
    coltello = pygame.transform.scale(items["longSword"]["image"], (100,100))
    coltello = pygame.transform.rotate(coltello, random.randint(-10,10))
    screen.blit(coltello, (player.x-10,player.y+10))

def gun(player, screen):
    coltello = pygame.transform.scale(items["gun"]["image"], (80,80))
    screen.blit(coltello, (player.x-30,player.y+10))

def rock(player, screen):
    coltello = pygame.transform.scale(items["sasso"]["image"], (70,70))
    screen.blit(coltello, (player.x+5,player.y-40))


items = {
    "knife": {
        "type": "weapon",
        "image": pygame.image.load("GameFile/image/items/knife.png").convert_alpha(),
        "cost": 100,
        "addStat": [0, 10, 0, 0, 0, 0, 0, -10, -1],
        "specialScript": [knife]
    },
    "longSword": {
        "type": "weapon",
        "image": pygame.image.load("GameFile/image/items/longsword.png").convert_alpha(),
        "cost": 250,
        "addStat": [0, 20, 0, 0, 0, 0, 0, 10, -5],
        "specialScript": [longSword]
    },
    "sasso": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/sasso.png").convert_alpha(),
        "cost": 150,
        "addStat": [10, 5, 5, -10, 0, 100, 0, -5, -5],
        "specialScript": [rock]
    },
    "cat": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/cat.png").convert_alpha(),
        "cost": 100,
        "addStat": [10, 0, 10, -5, 0, 0, 0, 5, -10],
        "specialScript": [meow]
    },
    "acqua": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/water.png").convert_alpha(),
        "cost": 50,
        "addStat": [10, 0, 1, 0, 0, 0, -0.5, 0, 0],
        "specialScript": []
    },
    "gun": {
        "type": "weapon",
        "image": pygame.image.load("GameFile/image/items/gun.png").convert_alpha(),
        "cost": 250,
        "addStat": [0, 5, 0, 0, 0, 0, 0, 500,0],
        "specialScript": [gun]
    },
    "fiore": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/fiore.png").convert_alpha(),
        "cost": 25,
        "addStat": [5, 1, 1, 5, 5, 0, -0.01, 0,0],
        "specialScript": []
    },
    "papera": {
        "type": "roba",
        "image": pygame.image.load("GameFile/image/items/paperella.png").convert_alpha(),
        "cost": 500,
        "addStat": [40, 10, 5, 0, 0, 0, -0.05, 0,-5],
        "specialScript": []
    }
}

def shop(screen, player):
    itemsInShop = []
    rects = []
    itemsKeys = list(items.keys())  
    for i in range(6):
        itemsInShop.append(random.choice(itemsKeys))
        rects.append(pygame.rect.Rect(0,0,255,255))
    while True:
        screen.fill((255, 255, 255))
        larghezza, altezza = assets.shop.get_size()
        screen_width, screen_height = screen.get_size()
        scale_ratio = screen_width / larghezza * 0.6
        frame_surface = pygame.transform.scale(assets.shop, (round(larghezza * scale_ratio), round(altezza * scale_ratio)))
        posY = screen_height - round(altezza * scale_ratio)
        posX = screen_width / 2 - round(larghezza * scale_ratio) / 2
        screen.blit(frame_surface, (posX, posY))
        grid_width = screen_width // 3 
        grid_height = screen_height // 2
        horizontal_space =  (grid_width * 0.1) // (3 - 1)
        vertical_space =    -100 // (2 - 1)
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
        pygame.display.update()
        for event in pygame.event.get():
            assets.BasePygameCicle(event, screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    for i in range(6):
                        if rects[i] is not None:
                            if rects[i].collidepoint(mouse_x, mouse_y):
                                if player.money >= items[itemsInShop[i]]["cost"]:
                                    assets.purchase.play()
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


