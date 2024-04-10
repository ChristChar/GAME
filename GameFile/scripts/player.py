import pygame
import math
import random
import ctypes
import GameFile.scripts.assets as assets
import GameFile.scripts.notification as notific
import GameFile.scripts.enemies as enemy
import GameFile.scripts.shop as shop

pygame.init()
pygame.mixer.init()
pygame.font.init()

class player:
    def __init__(self, position, image):
        self.playerStat = {
            "BaseStat": [100, 10, 5, 10, 100, 1000, 10, 150, 100], "exp": 0, "expToLevelUp": 100, "L": 1} #vita attacco difesa velocità stanima attColdown regenerationSpeed(s) attDistant CritChanche
        self.x = position[0]
        self.y = position[1]
        self.items = []
        self.playerStat["stat"] = self.playerStat["BaseStat"].copy()
        for i in self.items:
            for a in  range(len(shop.items[i]["addStat"])):
                self.playerStat["stat"][a] += shop.items[i]["addStat"][a]
        self.stamina = self.playerStat["stat"][4]
        self.life = self.playerStat["stat"][0]
        self.image = image
        self.rect = image.get_rect()
        self.imageToView = image
        self.attack_cooldown = 0
        self.regeneration_cooldown = [0, 0]
        self.money = 0
        self.state = "normal"
    
    def statCalcolate(self):
        self.playerStat["stat"] = self.playerStat["BaseStat"].copy()
        for i in self.items:
            for a in  range(len(shop.items[i]["addStat"])):
                self.playerStat["stat"][a] += shop.items[i]["addStat"][a]
    
    def itemsUpdate(self,screen):
        for i in self.items:
            for b in shop.items[i]["specialScript"]:
                b(self, screen)

            
    def regeneration(self):
        if self.regeneration_cooldown[0] <= 0 and self.life < self.playerStat["stat"][0]:
            self.life += 1
            self.regeneration_cooldown[0] = self.playerStat["stat"][6]*1000
        else:
            self.regeneration_cooldown[0] -= pygame.time.get_ticks() - \
                self.regeneration_cooldown[1]
            self.regeneration_cooldown[1] = pygame.time.get_ticks()

    def drawThings(self, screen):
        Width, Height = screen.get_size()
        Level = assets.font.render(
            "L: "+str(self.playerStat["L"]), True, (0, 0, 0))
        stamina = assets.font.render(
            "stamina: "+str(round(self.stamina)), True, (200, 100, 200))
        life = assets.font.render(
            "vita: "+str(round(self.life)), True, (255, 0, 0))
        money = assets.font.render(
            "€"+str(self.money), True, (255, 255, 0))
        stat = [Level,money, stamina, life]
        MaxLarg = 0
        for i in stat:
            larghezza, _ = i.get_size()
            if larghezza > MaxLarg:
                MaxLarg = larghezza
        for i in range(len(stat)):
            screen.blit(stat[i], (Width - MaxLarg - 50,
                        Height - (len(stat) - i) * 100))

    def update(self, screen):
        width, height = screen.get_size()
        if self.state == "purple":
            if random.random() < 0.05:
                life = random.randint(1,2)
                self.life -= life
                NewNotification = notific.Notifica(
                        str(life), self.rect.center, (255, 0, 255), 1000)
                notific.notifiche.append(NewNotification)
            elif random.random() < 0.005:
                self.state = "normal"
        if self.life <= 0:
            assets.mode = "menu"
            assets.round = -1
            NewNotification = notific.Notifica(
                "GAME OVER", (100, 200), (255, 0, 0), 2000,4, True)
            notific.notifiche.append(NewNotification)
            del self
            enemy.Enemys = []
            return
        self.regeneration()
        keys = pygame.key.get_pressed()
        speed = self.playerStat["stat"][3] / 10
        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and self.stamina >= 0.4:
            speed *= 3
            self.stamina -= 0.04
        else:
            if self.stamina < self.playerStat["stat"][4]:
                self.stamina += 0.01
        speed /= 3
        if self.state == "protected":
            speed /= 2
        print(speed)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= speed
            self.imageToView = pygame.transform.flip(self.image, True, False)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += speed
            self.imageToView = self.image
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += speed
        if self.x > width or self.x < -80 or self.y > height or self.y < -80:
            ctypes.windll.user32.MessageBoxW(0, 'Ehy thise is illigal!', 'Cheating Error', 0x10)
            self.x = width // 2 -40
            self.y = height // 2 - 40
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.imageToView, (self.x, self.y))
        self.itemsUpdate(screen)
        self.drawThings(screen)

    def attack(self, Enemy):
        if self.attack_cooldown <= 0:
            distance = math.sqrt((Enemy.rect.center[0] - self.rect.center[0])**2 + (
                Enemy.rect.center[1] - self.rect.center[1])**2)
            if distance <= self.playerStat["stat"][7]:
                attack = self.playerStat["stat"][1] + \
                    random.randint(-2, 2) - \
                    enemy.EnemyType[Enemy.type]["stat"][2] / 2
                if random.random() < 1 / self.playerStat["stat"][8]:
                    attack *= 2
                    NewNotification = notific.Notifica(
                        str(round(attack)), Enemy.rect.center, (255, 255, 0), 1000, 3)
                    notific.notifiche.append(NewNotification)
                else:
                    NewNotification = notific.Notifica(
                        str(round(attack)), Enemy.rect.center, (255, 0, 0), 1000)
                    notific.notifiche.append(NewNotification)
                Enemy.life -= attack
                assets.attack.play()
                self.attack_cooldown = self.playerStat["stat"][5]
        else:
            self.attack_cooldown -= pygame.time.get_ticks()

    def kill(self, Enemy, Height):
        baseMoney = enemy.EnemyType[Enemy.type]["baseMoney"]
        MONEY = max(0,baseMoney + random.randint(round(baseMoney*-0.4),round(baseMoney*0.4)))
        if MONEY > 0:
            assets.purchase.play()
        self.money += MONEY
        NewNotification = notific.Notifica(
                    "€"+str(MONEY), Enemy.rect.center, (255, 255, 0), 1000)
        notific.notifiche.append(NewNotification)
        self.playerStat["exp"] += enemy.EnemyType[Enemy.type]["exp"]
        if self.playerStat["exp"] >= self.playerStat["expToLevelUp"]:
            NewNotification = notific.Notifica(
                "Level UP!!!", (0, Height/2-100), (0, 200, 255), 2000,1, True)
            notific.notifiche.append(NewNotification)
            assets.LevelUp.play()
            self.playerStat["exp"] -= self.playerStat["expToLevelUp"]
            self.playerStat["expToLevelUp"] *= 1.5
            self.playerStat["L"] += 1
            self.playerStat["BaseStat"][0] += 10
            self.life = min(self.life+10, self.playerStat["BaseStat"][0])
            self.playerStat["BaseStat"][1] += 5
            self.playerStat["BaseStat"][2] += 1
            self.playerStat["BaseStat"][3] += 3
            self.statCalcolate()
