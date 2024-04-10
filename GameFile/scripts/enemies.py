import pygame
import math
import random
import GameFile.scripts.cutSceen as CutSceen
import GameFile.scripts.notification as notific
import GameFile.scripts.assets as assets
import GameFile.scripts.shop as shop

def BaseAttack(self, player):
    attack = EnemyType[self.type]["stat"][1] + random.randint(-1, 1)
    player.life -= attack
    NewNotification = notific.Notifica(
        str(round(attack)), player.rect.center, (255, 0, 0), 1000)
    notific.notifiche.append(NewNotification)


def rickAttack(self, screen, player):
    CutSceen.ViewCutSceen(screen, "GameFile/CutSceen/meme.mp4")
    self.state = "stun"
    player.life -= EnemyType[self.type]["stat"][1] + random.randint(-1, 1)

def NormalAttack(self, screen, player):
    self.state = "stun"
    BaseAttack(self,player)

def SteveAttack(self, screen, player):
    self.state = "stun/2"
    BaseAttack(self,player)
    assets.hit.play()

def SUSAttack(self, screen, player):
    assets.vent.play()
    width, height = screen.get_size()
    BaseAttack(self,player)
    self.x = random.randint(0,width)
    self.y = random.randint(0,height)
    

EnemyType = {"rick": {"stat": [100, 10, 5, 20], "image": pygame.image.load("GameFile/image/enemies/rick.jpg"), "attack": rickAttack, "exp": 40, "baseMoney":15},
             "GINO": {"stat": [150, 30, 5, 25], "image": pygame.image.load("GameFile/image/enemies/EvilGino.png"), "attack": NormalAttack, "exp": 100, "baseMoney":30},
             "bidoof": {"stat": [35, 3, 0, 10], "image": pygame.image.load("GameFile/image/enemies/bidoof.png"), "attack": NormalAttack, "exp": 10,"baseMoney":1},
             "sonic": {"stat": [70, 7, 5, 500], "image": pygame.image.load("GameFile/image/enemies/sonic.png"), "attack": NormalAttack, "exp": 50,"baseMoney":17},
             "gold": {"stat": [50, 10, 10, 30], "image": pygame.image.load("GameFile/image/enemies/gold.png"), "attack": NormalAttack, "exp": 30,"baseMoney":100},
             "steeve": {"stat": [200, 45, 0, 30], "image": pygame.image.load("GameFile/image/enemies/steeve.png"), "attack": SteveAttack, "exp": 30,"baseMoney":20},
             "SUS": {"stat": [100, 55, 0, 40], "image": pygame.image.load("GameFile/image/enemies/red.png"), "attack": SUSAttack, "exp": 33,"baseMoney":21},
             "bradbug": {"stat": [1000, 70, 10, 50], "image": pygame.image.load("GameFile/image/enemies/breadbug.png"), "attack": NormalAttack, "exp": 200,"baseMoney":100}}


class Enemy:
    def __init__(self, position, type, player):
        self.x = position[0]
        self.type = type
        self.y = position[1]
        if player.rect.collidepoint(self.x, self.y):
            self.x, self.y = random.randint(
                0, self.x), random.randint(0, self.y)
        self.life = EnemyType[self.type]["stat"][0]
        self.state = "normal"
        self.image = EnemyType[self.type]["image"]
        self.rect = EnemyType[self.type]["image"].get_rect()

    def move_towards_player(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance != 0:
            dx /= distance
            dy /= distance
        self.x += dx * (0.1 * (EnemyType[self.type]["stat"][3] / 10))
        if dx < 0:
            self.image = pygame.transform.flip(
                EnemyType[self.type]["image"], True, False)
        else:
            self.image = EnemyType[self.type]["image"]
        self.y += dy * (0.1 * (EnemyType[self.type]["stat"][3] / 10))
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, screen, player):
        _, Height = screen.get_size()
        if self.life <= 0:
            player.kill(self, Height)
            Enemys.remove(self)
            return
        if self.state == "normal":
            self.move_towards_player(player)
            if self.rect.colliderect(player.rect):
                EnemyType[self.type]["attack"](self, screen, player)
        elif self.state == "stun":
            if random.randint(0, 1000) == 10:
                self.state = "normal"
        elif self.state == "stun/2":
            if random.randint(0, 500) == 10:
                self.state = "normal"
        screen.blit(self.image, (self.x, self.y))


Enemys = []


def EnemyUpdate(screen, player):
    if len(Enemys) == 0:
        assets.round += 1
        Width, Height = screen.get_size()
        for i in assets.rounds[assets.round]:
            if i == "shop":
                shop.shop(screen, player)
                break
            if i == "heal":
                player.life = player.playerStat["stat"][0]
                break
            for b in range(len(i)):
                probability = 1 / (assets.rounds[assets.round].index(i) + 1)
                if random.random() < probability:
                    a = Enemy((random.randint(0, Width),
                            random.randint(0, Height)), i[b], player)
                    Enemys.append(a)
        NewNotification = notific.Notifica(
            "round:"+str(assets.round+1), (0, Height/2-100), (0, 0, 0), 3000,1, True)
        notific.notifiche.append(NewNotification)
    for i in Enemys:
        i.update(screen, player)
