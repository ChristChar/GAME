import pygame
import math
import random
import GameFile.scripts.notification as notific
import GameFile.scripts.enemies as enemy

types = {"fireBall":{"speed":3,"BaseDamage": 50,"image":pygame.image.load("GameFile/image/items/FireBall.png")},
         "calzino":{"speed":5,"BaseDamage": 40,"image":pygame.image.load("GameFile/image/calzino.png")}}

class Progliettile:
    def __init__(self,type,position, direction, BY= True):
        self.type = type
        self.x = position[0]
        self.y = position[1]
        self.direction = direction
        self.by =BY
        self.image = pygame.transform.scale(types[type]["image"], (80,80))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()

    def move(self, screenDimension):
        angle_radians = math.radians(self.direction)
        vel_x = types[self.type]["speed"] * math.cos(angle_radians)
        vel_y = types[self.type]["speed"] * math.sin(angle_radians)
        self.x += vel_x
        self.y += vel_y
        if self.x > screenDimension[0] or self.x < 0 or self.y < 0 or self.y > screenDimension[1]:
            if random.random() < 0.8:
                del self
                return
            self.direction = (self.direction + 180) % 360

    def collisioni(self, enemys,player):
        if self.by:
            for i in enemys:
                if self.rect.colliderect(i.rect):
                    attack = max(types[self.type]["BaseDamage"] + random.randint(-3, 3) - enemy.EnemyType[i.type]["stat"][2],1)
                    i.life -= attack
                    NewNotification = notific.Notifica(
                        str(round(attack)), i.rect.center, (255, 0, 0), 1000)
                    notific.notifiche.append(NewNotification)
                    progliettili.remove(self)
                    return
        else:
            if self.rect.colliderect(player.rect):
                if player.state != "protected":
                    attack = max(types[self.type]["BaseDamage"] + random.randint(-3, 3) - player.playerStat["stat"][2],1)
                    player.life -= attack
                    NewNotification = notific.Notifica(
                        str(round(attack)), player.rect.center, (255, 0, 0), 1000)
                    notific.notifiche.append(NewNotification)
                    progliettili.remove(self)
                    return

    def update(self,screen,enemys,player):
        width, heigth = screen.get_size()
        self.move([width, heigth])
        self.rect.x = self.x
        self.rect.y = self.y
        self.collisioni(enemys,player)
        image = pygame.transform.rotate(self.image, self.direction)
        screen.blit(image, (self.x, self.y))

progliettili = []

def progliettiliUpdate(screen,enemys,player):
    for  i in progliettili:
        i.update(screen,enemys,player)

