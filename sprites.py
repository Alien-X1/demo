# Sprite Class

import pygame as pg
import pygame.math.Vector2 as vec
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
        self.rect.center = (WIDTH/2,550)
        self.vec(0,0)
        self.acc = 0.5
        self.grav = 0.5
        self.fric = 0.25
        self.falling = True
    def update(self):
        # self.vx = 0
        # self.vy = 0
        keys = pg.key.get_pressed()
        # move left
        if keys[pg.K_LEFT] and self.vx > -10:
            self.vec.x = -self.acc
        # move right
        if keys[pg.K_RIGHT] and self.vx < 10:
            self.vec.x = self.acc
        # Jump
        self.jump()
        # Gravity
        self.gravity()
        # Friction
        self.friction()
        print("Player Coordinates (%d,%d)" % (self.rect.x,self.rect.y))
        self.rect.x += self.vx
        self.rect.y += self.vy
    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.vy < 10 and self.falling == False:
            self.falling = True
            for i in range(20):
                self.vy -= self.acc
    def gravity(self):
        keys = pg.key.get_pressed()
        if self.vy < 10 or (self.rect.y >= HEIGHT-50):
            self.vy += self.grav
        if (self.rect.y >= HEIGHT-50) and not keys[pg.K_UP]:
            self.vy = 0
            self.rect.y = HEIGHT-50
            self.falling = False
    def friction(self):
        keys = pg.key.get_pressed()
        if self.vx > 0 and not keys[pg.K_RIGHT]:
            self.vx -= self.fric
        if self.vx < 0 and not keys[pg.K_LEFT]:
            self.vx += self.fric
    # def collision(self):
    #     sprite.groupcollide()


class Immovable(Sprite):
    def __init__(self, sizex, sizey, placex, placey):
        Sprite.__init__(self)
        self.image = pg.Surface((sizex,sizey))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (placex,placey)
