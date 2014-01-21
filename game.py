import pygame,sys
from pygame.locals import *
from gnome import *
clock = pygame.time.Clock()


pygame.init()

bg = pygame.image.load("wallpaper.png")
bgsize = bg.get_size()

win = pygame.display.set_mode(bgsize)

movex,movey = 0,0
x,y = 0,0
Gnome = gnome(88, 88)

        
    


true = True
while true:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            true = False

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                movex = - 5
            if (event.key == pygame.K_RIGHT):
                movex =5
            if (event.key == pygame.K_UP):
                movey = -5
            if (event.key == pygame.K_DOWN):
                movey = 5
                
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT):
                movex = 0
            if (event.key == pygame.K_RIGHT):
                movex = 0
            if (event.key == pygame.K_UP):
                movey = 0
            if (event.key == pygame.K_DOWN):
                movey = 0

    win.blit(bg, (0,0))
    Gnome.x += movex
    Gnome.y += movey
    Gnome.update(win)
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(100)
    
pygame.quit()     
                
    
