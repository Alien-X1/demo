# sprite classes for game
# i used some ideas from CodePylet https://www.youtube.com/watch?v=osDofIdja6s&t=1038s
# i also borrowed pretty much all of this from kids can code - thanks!
# on acceleration https://www.khanacademy.org/science/physics/one-dimensional-motion/kinematic-formulas/v/average-velocity-for-constant-acceleration 
# on vectors: https://www.youtube.com/watch?v=ml4NSzCQobk 


import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.collide = False
        self.jumps = 0

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.vel.x > -10:
            self.acc.x =  -ACCELERATION
        if keys[pg.K_RIGHT] and self.vel.x < 10:
            self.acc.x = ACCELERATION
        self.jump()
        self.gravity()
        self.edge()
        self.friction()
        # self.collision()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        print(self.pos)
    
    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and (self.collide == True or self.jumps < 2) and self.vel.y >= 0:
            self.collide = False
            self.jumps += 1
            self.vel.y -= 10
            
    def gravity(self):
        if self.collide == False and self.vel.y < 10:
            self.acc.y = GRAVITY
        if self.collide == True:
            self.vel.y = 0
            self.acc.y = 0
            self.jumps = 0

    def collision(self):
        if self.pos.y >= HEIGHT - 20:
            self.collide = True
    
    def edge(self):
        if self.pos.x < -15:
            self.pos.x = WIDTH + 15
        elif self.pos.x > WIDTH + 15:
            self.pos.x = -15
    
    def friction(self):
        keys = pg.key.get_pressed()
        if self.vel.x > 0 and not (keys[pg.K_LEFT] or keys[pg.K_RIGHT]):
            self.acc.x = -FRICTION
        elif self.vel.x < 0 and not (keys[pg.K_RIGHT] or keys[pg.K_LEFT]):
            self.acc.x = FRICTION

class Immovable(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = ""
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = ""
        self.pos = ""
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)