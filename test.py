import pygame,sys
from pygame.locals import *

win = pygame.display.set_mode((800, 500),0,32)

gnome = pygame.image.load("sprite.png")

while True:
    win.blit(gnome, (300,300))
    pygame.display.flip()
    pygame.display.update()

