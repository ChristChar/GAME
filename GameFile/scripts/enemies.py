import pygame
import math
import random
import GameFile.scripts.cutSceen as CutSceen
import GameFile.scripts.notification as notific
import GameFile.scripts.assets as assets
import GameFile.scripts.shop as shop
import GameFile.scripts.progliettili as progliettili
import GameFile.scripts.finals as end


def BaseAttack(self, player):
    baseAttack = EnemyType[self.type]["stat"][1]
    attack = max(1, random.randint(round(baseAttack*0.8),
                 round(baseAttack*1.2)) - player.playerStat["stat"][2])
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
    BaseAttack(self, player)

def GhostAttack(self, screen, player):
    self.state = "stun/2"
    BaseAttack(self, player)
    player.state = "speed/2"

def SteveAttack(self, screen, player):
    hit = pygame.mixer.Sound("GameFile/sound/minecraft_hit.mp3")
    self.state = "stun/2"
    BaseAttack(self, player)
    hit.play()

def SUSAttack(self, screen, player):
    vent = pygame.mixer.Sound("GameFile/sound/vent.mp3")
    vent.play()
    width, height = screen.get_size()
    BaseAttack(self, player)
    self.x = random.randint(0, width)
    self.y = random.randint(0, height)

def Purpleguy(self, screen, player):
    purple = pygame.mixer.Sound("GameFile/sound/theMan.mp3")
    purple.play()
    self.state = "stun/2"
    BaseAttack(self, player)
    player.state = "purple"


def CasualTp(self, screen, player):
    if random.random() < 0.01:
        width, height = screen.get_size()
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

def move_towards_player(self, screen, player):
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

def casualMove(self, screen, player):
    W,H = screen.get_size()
    if not hasattr(self, "direction"):
        self.direction = random.randint(0,360)
    if random.random() < 0.4:
        self.direction += random.randint(-3, 3)
        self.direction %= 360
    angle_radians = math.radians(self.direction)
    dx = math.cos(angle_radians)
    dy = math.sin(angle_radians)
    if dx < 0:
        self.image = pygame.transform.flip(
            EnemyType[self.type]["image"], True, False)
    else:
        self.image = EnemyType[self.type]["image"]
    self.x += dx
    self.y += dy
    IW, IH = self.image.get_size()
    if self.x < 0 - IW or self.x > W or self.y < 0 - IH or self.y > H:
        self.direction = (self.direction + 180) % 360


def DoYouKnowTheWay(self,screen,player):
    if random.random() < 0.01:
        suono = pygame.mixer.Sound("GameFile/sound/DUKYW.mp3")
        suono.play()

def SpawnBidoof(self, screen, player):
    if random.random() < 0.005:
        bidoof = pygame.mixer.Sound("GameFile/sound/bidoof.mp3")
        Width, Height = screen.get_size()
        a = Enemy((random.randint(0, Width),
                   random.randint(0, Height)), "bidoof", player)
        Enemys.append(a)
        bidoof.play()


def shootCalzo(self, screen, player):
    if random.random() < 0.005:
        a = random.choice(["casualShoot", "MirateShoot"])
        if a == "casualShoot":
            for i in range(random.randint(1, 3)):
                progliettili.progliettili.append(progliettili.Progliettile(
                    "calzino", [self.x, self.y], random.randint(0, 360), False))
        elif a == "MirateShoot":
            delta_y = player.y - self.y
            delta_x = player.x - self.x
            angolo_radiani = math.atan2(delta_y, delta_x)
            angolo_gradi = math.degrees(angolo_radiani)
            angolo_gradi = (angolo_gradi + 360) % 360
            progliettili.progliettili.append(progliettili.Progliettile(
                "calzino", [self.x, self.y], angolo_gradi, False))

def dash(self, screen, player):
    if random.random() < 0.01:
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance != 0:
            dx /= distance
            dy /= distance
        self.x += dx * (0.1 * (EnemyType[self.type]["stat"][3]*2))
        if dx < 0:
            self.image = pygame.transform.flip(
                EnemyType[self.type]["image"], True, False)
        else:
            self.image = EnemyType[self.type]["image"]
        self.y += dy * (0.1 * (EnemyType[self.type]["stat"][3] / 10))

def duplicate(self, screen, player):
    if random.random() < 0.001:
        Width, Height = screen.get_size()
        a = Enemy((random.randint(0, Width), random.randint(
            0, Height)), self.type, player)
        Enemys.append(a)

def jump(self, screen, player):
    if self.image == EnemyType[self.type]["image"] or self.image == pygame.transform.flip(EnemyType[self.type]["image"], True, False):
        if random.random() < 0.001:
            self.image = pygame.image.load(
                "GameFile/image/enemies/"+self.type+"2.png")
            self.x = player.x + 40 + random.randint(-20, 20)
            self.y = player.y + 40 + random.randint(-20, 20)
    else:
        if random.random() < 0.1:
            self.image = EnemyType[self.type]["image"]


def trensform(self, screen, player):
    a = Enemy((self.x,self.y), EnemyType[self.type]["trasformIn"], player)
    if EnemyType[a.type]["IsEnemy?"]:
        Enemys.append(a)
    else:
        NotEnemys.append(a)


EnemyType = {"rick":
             {
              "stat": [100, 10, 5, 20],
              "image": pygame.image.load("GameFile/image/enemies/rick.jpg"),
              "attack": rickAttack,
              "exp": 40,
              "baseMoney": 15,
              "Script": [move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "GINO": 
             {
              "stat": [150, 30, 5, 25],
              "image": pygame.image.load("GameFile/image/enemies/EvilGino.png"), 
              "attack": NormalAttack, 
              "exp": 100, 
              "baseMoney": 20, 
              "Script": [move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "bidoof": 
             {
              "stat": [35, 3, 0, 10], 
              "image": pygame.image.load("GameFile/image/enemies/bidoof.png"), 
              "attack": NormalAttack, 
              "exp": 10, 
              "baseMoney": 1, 
              "Script": [move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
              "TheBidoof": 
             {
              "stat": [35, 3, 0, 10], 
              "image": pygame.image.load("GameFile/image/enemies/bidoof.png"), 
              "attack": NormalAttack, 
              "exp": 0, 
              "baseMoney": 0, 
              "Script": [move_towards_player],
              "DeadScripts": [trensform],
              "trasformIn": "GodBidoof",
              "IsEnemy?":True
              },
              "GodBidoof": 
             {
              "stat": [5000, 200, 10, 150], 
              "image": pygame.image.load("GameFile/image/enemies/BiGod.png"), 
              "attack": NormalAttack, 
              "exp": 500, 
              "baseMoney": 300, 
              "Script": [move_towards_player, SpawnBidoof],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "UgKnukles": 
             {
              "stat": [40, 5, 2, 30], 
              "image": pygame.image.load("GameFile/image/enemies/ugandaknucleO.png"), 
              "attack": NormalAttack, 
              "exp": 30, 
              "baseMoney": 10, 
              "Script": [move_towards_player, duplicate, DoYouKnowTheWay],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "sonic":
               {
                "stat": [70, 7, 5, 500], 
                "image": pygame.image.load("GameFile/image/enemies/sonic.png"), 
                "attack": NormalAttack, 
                "exp": 50, 
                "baseMoney": 17, 
                "Script": [move_towards_player],
                "DeadScripts": ["kill"],
                "IsEnemy?":True
                },
             "gold": 
             {
              "stat": [50, 10, 10, 30], 
              "image": pygame.image.load("GameFile/image/enemies/gold.png"), 
              "attack": NormalAttack, 
              "exp": 30, 
              "baseMoney": 100, 
              "Script": [move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "steeve": 
             {
              "stat": [200, 45, 0, 30], 
              "image": pygame.image.load("GameFile/image/enemies/steeve.png"), 
              "attack": SteveAttack, 
              "exp": 30, 
              "baseMoney": 20, 
              "Script": [move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "SUS": 
             {
              "stat": [100, 55, 0, 40], 
              "image": pygame.image.load("GameFile/image/enemies/red.png"), 
              "attack": SUSAttack, 
              "exp": 33, 
              "baseMoney": 21, 
              "Script": [move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "PurpleGuy": 
             {
              "stat": [150, 40, 10, 50], 
              "image": pygame.image.load("GameFile/image/enemies/purple_guy.png"), 
              "attack": Purpleguy, 
              "exp": 33, 
              "baseMoney": 21, 
              "Script": [move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "DragoGomma": 
             {
              "stat": [200, 30, 35, 70], 
              "image": pygame.image.load("GameFile/image/enemies/DragoGomma.png"), 
              "attack": NormalAttack, 
              "exp": 40, 
              "baseMoney": 25, 
              "Script": [CasualTp, move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "Charizard": 
             {
              "stat": [500, 50, 10, 100], 
              "image": pygame.image.load("GameFile/image/enemies/chorizard.png"), 
              "attack": NormalAttack, 
              "exp": 60, 
              "baseMoney": 30, 
              "Script": [CasualTp, move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "Mario": 
             {
              "stat": [300, 30, 5, 80], 
              "image": pygame.image.load("GameFile/image/enemies/Mario.png"), 
              "attack": NormalAttack, 
              "exp": 40, 
              "baseMoney": 27, 
              "Script": [casualMove, jump],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "DancingGhost": 
             {
              "stat": [100, 10, 5, 150], 
              "image": pygame.image.load("GameFile/image/enemies/Dance.png"), 
              "attack": GhostAttack, 
              "exp": 28, 
              "baseMoney": 18, 
              "Script": [CasualTp, move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "calziniShooter": 
             {
              "stat": [150, 10, 7, 5], 
              "image": pygame.image.load("GameFile/image/enemies/calzino.png"), 
              "attack": NormalAttack, 
              "exp": 28, 
              "baseMoney": 18, 
              "Script": [shootCalzo, move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "breadbug": 
             {
              "stat": [1500, 90, 20, 35], 
              "image": pygame.image.load("GameFile/image/enemies/breadbug.png"), 
              "attack": NormalAttack, 
              "exp": 200, 
              "baseMoney": 100, 
              "Script": [SpawnBidoof, move_towards_player],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "doge": 
             {
              "stat": [2500, 140, 20, 50], 
              "image": pygame.image.load("GameFile/image/enemies/doge.png"), 
              "attack": NormalAttack, 
              "exp": 400, 
              "baseMoney": 200, 
              "Script": [dash, move_towards_player, CasualTp],
              "DeadScripts": ["kill"],
              "IsEnemy?":True
              },
             "Tree": 
             {
              "stat": [200, 0, 30, 0], 
              "image": pygame.image.load("GameFile/image/enemies/tree.png"), 
              "attack": None, 
              "exp": 10, 
              "baseMoney": 100, 
              "Script": [],
              "DeadScripts": ["kill"],
              "IsEnemy?":False
              },
             "chicken": 
             {
              "stat": [50, 0, 5, 100], 
              "image": pygame.image.load("GameFile/image/enemies/chiken.png"), 
              "attack": None, 
              "exp": 50, 
              "baseMoney": 0, 
              "Script": [casualMove],
              "DeadScripts": ["kill"],
              "IsEnemy?":False
              }}


class Enemy:
    def __init__(self, position, type, player):
        self.x = position[0]
        self.type = type
        self.y = position[1]
        self.life = EnemyType[self.type]["stat"][0]
        self.state = "stun/4"
        self.image = EnemyType[self.type]["image"]
        self.rect = EnemyType[self.type]["image"].get_rect()
        self.rect.x = self.x  
        self.rect.y = self.y  

    def update(self, screen, player):
        _, Height = screen.get_size()
        if self.life <= 0:
            for event in EnemyType[self.type]["DeadScripts"]:
                if event == "kill":
                    player.kill(self, Height)
                else:
                    event(self, screen, player)
            if EnemyType[self.type]["IsEnemy?"]:
                Enemys.remove(self)
            else:
                NotEnemys.remove(self)
            return
        if self.state == "normal":
            for i in EnemyType[self.type]["Script"]:
                i(self, screen, player)
            if self.rect.colliderect(player.rect) and player.state != "protected" and  EnemyType[self.type]["IsEnemy?"]:
                EnemyType[self.type]["attack"](self, screen, player)
        elif self.state == "stun":
            if random.randint(0, 1000) == 10:
                self.state = "normal"
        elif self.state == "stun/2":
            if random.randint(0, 500) == 10:
                self.state = "normal"
        elif self.state == "stun/4":
            if random.randint(0, 250) == 10:
                self.state = "normal"
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image, (self.x, self.y))

Enemys = []
NotEnemys = []

def spawnEnemys(screen, player):
    Width, Height = screen.get_size()
    if len(assets.rounds) == assets.round:
        end.FINE(screen)
        return
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
                if EnemyType[i[b]]["IsEnemy?"]:
                    Enemys.append(a)
                else:
                    NotEnemys.append(a)


def EnemyUpdate(screen, player):
    global NotEnemys
    if len(Enemys) == 0:
        assets.round += 1
        Width, Height = screen.get_size()
        NotEnemys = []
        spawnEnemys(screen, player)
        NewNotification = notific.Notifica(
            "round:"+str(assets.round+1), (0, Height/2-100), (0, 0, 0), 3000, 1, True)
        notific.notifiche.append(NewNotification)
    for i in Enemys:
        i.update(screen, player)
    for i in NotEnemys:
        i.update(screen, player)
