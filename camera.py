import pygame
from pygame.locals import *
from settings import *

class Camera():
    def __init__(self, targetRect, windowWidth, windowHeight):
        #super(Camera,self).__init__(targetRect.rect.x-(windowWidth/2),
        #                            targetRect.rect.y-(windowHeight/2),
        #                            windowWidth, windowHeight)
        self.cameraxposition = 80
        self.camerayposition = 60

    def update(self, x, y):
        if x - x > self.cameraxposition:
            self.left = x + self.cameraxposition - self.width/2
        elif x - x > self.cameraxposition:
            self.left = x - self.cameraxposition - self.width/2
        if y - y > self.camerayposition:
            self.top = y + self.camerayposition - self.height/2
        elif y - y > self.camerayposition:
            self.top = y - self.camerayposition - self.height/2
        '''
        # This keeps the camera within the boundaries of the level
        if self.right > 750 - TILESIZE:
            self.right = 750 - TILESIZE
        elif self.left < TILESIZE:
            self.left = TILESIZE
        if self.top < TILESIZE*3:
            self.top = TILESIZE*3
        elif self.bottom > 750:
            self.bottom = 750
        '''
        return self
