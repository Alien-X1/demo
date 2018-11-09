# Sprite Class

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *
from time import sleep

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0,HEIGHT/2)
        self.vx = 0
        self.vy = 0
        self.grav = 1
    def update(self):
        # self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        # move left
        if keys[pg.K_LEFT]:
            self.vx = -5
        # move right
        if keys[pg.K_RIGHT]:
            self.vx = 5
        # Jump
        if keys[pg.K_UP]:
            self.vy = 10
        # Fall
        # if not collide_rect(self,Immovable()):
        #     self.vy += self.grav

        self.rect.x += self.vx
        self.rect.y += self.vy

class Immovable(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((480,10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,595)