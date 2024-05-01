import pygame
import ctypes
import GameFile.scripts.assets as assets
import GameFile.scripts.progliettili as progliettili
import GameFile.scripts.player as player
import GameFile.scripts.enemies as enemy
import GameFile.scripts.functions as F
import GameFile.scripts.loadImage as image

class button:
    def __init__(self, text, color, script, ScriptVariable = None):
        self.text = text
        self.color = color
        self.script = script
        if ScriptVariable is not None:
            self.scriptVariable = ScriptVariable
        self.rect = pygame.rect.Rect(0,0,150,50)

    def draw(self, screen, i):
        ScW, ScH = screen.get_size()
        NewScalY = ScH / 10
        self.rect.height = NewScalY
        NewScalX = NewScalY * 3
        self.rect.width = NewScalX
        posX = ScW / 2 - NewScalX / 2
        self.rect.x = posX
        posY = ScH / 2 - NewScalY / 2
        self.rect.y = posY + i * ScH / 9
        pygame.draw.rect(screen, self.color, self.rect)
        TeW, TeH = 999, 999
        D = round(NewScalY)
        if F.is_color_light(self.color):
            color = (0,0,0)
        else:
            color = (255,255,255)
        font = pygame.font.SysFont(None, D)
        text = font.render(self.text, True, color)
        TeW, TeH = text.get_size()
        if TeW+5 > self.rect.width:
            D = round(NewScalY / 2)     
            font = pygame.font.SysFont(None, D)
            text = font.render(self.text, True, color)
            TeW, TeH = text.get_size()
        screen.blit(text, (self.rect.x + self.rect.width/2 - TeW/2, self.rect.y + self.rect.height/2 - TeH/2))
    
    def WhenClicked(self):
        if isinstance(self.script, str):
            assets.mode = self.script
        else:
            self.script()

    def ControllClicked(self, event):
        mouse_x, mouse_y = event.pos
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.WhenClicked()

def quit():
    pygame.quit()
    quit()

def resetMenu():
    assets.round -= 1
    player.Player.life = player.Player.playerStat["stat"][0]
    player.Player.stanima = player.Player.playerStat["stat"][4]
    enemy.Enemys = []
    progliettili.progliettili = []
    assets.mode = "menu"

def changePlayerSprite():
    PlayerImage = image.loadImage(1)
    if PlayerImage is None:
        return
    input = ctypes.windll.user32.MessageBoxW(None, "vuoi ridimensare l'immagine?", "Reisize?", 0x00000004)
    if input == 6:
        PlayerImage = pygame.transform.scale(PlayerImage, (80,80))
    ctypes.windll.user32.MessageBoxW(None, "lo sprite non verrà cambiato nelle cutsceen finali, sono prerenderizzate in mp4, non possiamo farlo", "informazione", 0x00000004)
    player.Player.image = PlayerImage
    player.Player.imageToView = PlayerImage

def changeBackgroundSprite():
    PlayerImage = image.loadImage(1)
    if PlayerImage is None:
        return
    assets.back = PlayerImage


start = button("START", (255,0,0),"game")
quitB = button("QUIT", (0,255,255),quit)
Customize = button("CUSTOM", (255,255,0),"custom")
menu = button("MENU", (100,200,255), resetMenu)
PlayerStat = button("VIEW STAT", (0,255,0),"statView")
playerB = button("Change Player", (255, 250,100), changePlayerSprite)
Back = button("Change Bacground", (100, 255,100), changeBackgroundSprite)

Buttons = {"menu":[start,Customize,quitB],"gameMenu":[PlayerStat,menu], "custom":[playerB, Back]}

def updateButtons(screen):
    for i, Butt in enumerate(Buttons[assets.mode]):
        Butt.draw(screen, i)

def ControllButtons(event):
    for Butt in Buttons[assets.mode]:
        Butt.ControllClicked(event)
