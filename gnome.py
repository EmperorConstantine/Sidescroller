import pygame,sys
from pygame.locals import*

class gnome:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xvel, self.yvel = 0, 0
        self.w = 50
        self.h = 50
        self.x_velocity = 0
        self.y_velocity = 0
        self.onGround = False
        self.i1 = pygame.image.load('spriterun1.png')
        self.i2 = pygame.image.load('spriterun2.png')
        self.timeTarget = 5
        self.timeNum = 0
        self.currentImage = 0
    def update(self, win):
        if self.onGround:
            self.yvel -= 10
        self.timeNum += 1
        if (self.timeNum == self.timeTarget):
            if (self.currentImage == 0):
                self.currentImage += .5
            else:
                self.currentImage = 0
            self.timeNum = 0
        self.render(win)

    def render(self, win):
        if (self.currentImage == 0):
            win.blit(self.i1, (self.x, self.y))
        else:
            win.blit(self.i2, (self.x, self.y))
            
            
            
                                    
                                    
        
