import pygame
from pygame.locals import *
import GameFile.scripts.assets as assets
import GameFile.scripts.pygameEventCycles as cicle
from moviepy.editor import VideoFileClip
import numpy as np


def ViewCutSceen(screen, video_path):
    video_clip = VideoFileClip(video_path)
    video_fps = video_clip.fps
    duration = video_clip.duration
    lista = list(video_path)
    lista[-1] = '3'
    audioFile = ''.join(lista)

    pygame.init()
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load(audioFile)
    pygame.mixer.music.play()

    for t in range(0, int(duration * 1000), int(1000 / video_fps)):
        frame = video_clip.get_frame(t / 1000)
        # Converti in RGB e rovescia l'immagine per Pygame
        frame_rgb = np.flip(frame, axis=0)
        # Ruota il frame di 90 gradi in senso antiorario tre volte
        frame_rgb = np.rot90(frame_rgb, k=3)
        frame_surface = pygame.surfarray.make_surface(frame_rgb)
        larghezza, altezza = frame_surface.get_size()
        # Ottieni solo la larghezza dello schermo
        screen_width, screen_height = screen.get_size()
        # Calcola il rapporto di scala utilizzando la larghezza dello schermo
        scale_ratio = screen_width / larghezza
        frame_surface = pygame.transform.scale(frame_surface, (round(
            larghezza * scale_ratio), round(altezza * scale_ratio)))
        posY = screen_height / 2 - round(altezza * scale_ratio) / 2
        screen.fill((0, 0, 0))
        screen.blit(frame_surface, (0, posY))
        pygame.display.flip()
        for event in pygame.event.get():
            cicle.BaseCicle(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    pygame.mixer.music.stop()
                    return
        clock.tick(video_fps)
