import pygame


pygame.font.init()
pygame.init()


class Notifica:
    def __init__(self, testo, posizione, colore, durata,dimension=1, Center=False):
        self.testo = testo
        self.posizione = posizione
        self.colore = colore
        self.durata = durata
        self.speed = 5
        self.dimension = dimension
        self.center = Center
        self.tempo_inizio = pygame.time.get_ticks()

    def controlla(self):
        tempo_trascorso = pygame.time.get_ticks() - self.tempo_inizio
        if tempo_trascorso >= self.durata:
            return True
        return False

    def aggiorna(self, schermo):
        width, height = schermo.get_size()
        posizione_x, posizione_y = self.posizione
        posizione_y -= self.speed
        if self.speed > 0:
            self.speed -= 0.1
        else:
            self.speed = 0.1
        font = pygame.font.Font(None, round(height / 15*self.dimension))
        testo_renderizzato = font.render(self.testo, True, self.colore)
        larghezza, _ = testo_renderizzato.get_size()
        if self.center:
            posizione_x = width / 2 - larghezza / 2
        self.posizione = (posizione_x, posizione_y)
        schermo.blit(testo_renderizzato, self.posizione)


notifiche = []


def notification(screen):
    for notifica in notifiche[:]:
        notifica.aggiorna(screen)
        if notifica.controlla():
            notifiche.remove(notifica)

# NewNotification = notific.Notifica("mi dispiace ma il gioco ancora non esiste", [100,altezza/2+50], (0,0,0), 2000)
# notific.notifiche.append(NewNotification)
