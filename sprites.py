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
        self.image = pg.Surface((PIX, 2 * PIX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 60)
        self.pos = vec(40, HEIGHT - 60)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.collide_g = False
        self.max_jumps = PLAYER_MAX_JUMPS
        self.max_vel = PLAYER_MAX_VEL
        self.jump_vel = PLAYER_JUMP_VEL
        self.jumps = 0

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.vel.x > -self.max_vel:
            self.acc.x =  -ACCELERATION
        if keys[pg.K_RIGHT] and self.vel.x < self.max_vel:
            self.acc.x = ACCELERATION
        self.jump()
        self.gravity()
        self.friction()
        self.edge()
        # self.collision()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        print(self.pos)
    
    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and (self.collide_g == True or self.jumps < self.max_jumps) and self.vel.y >= 0:
            self.collide = False
            self.jumps += 1
            self.vel.y -= self.jump_vel
        if self.collide_g == True :
            self.jumps = 0

    def gravity(self):
        if self.collide_g == False and self.vel.y < 15:
            self.acc.y = GRAVITY

    def collision(self):
        if self.pos.y >= HEIGHT - 20:
            self.collide = True
    
    def edge(self):
        if self.pos.x < 15:
            self.vel.x = 0
            self.pos.x = 15
        # elif self.pos.x > WIDTH + 15:
        #     self.pos.x = -15
    
    def friction(self):
        keys = pg.key.get_pressed()
        if self.vel.x > 0 and not (keys[pg.K_LEFT] or keys[pg.K_RIGHT]):
            self.acc.x = -FRICTION
        elif self.vel.x < 0 and not (keys[pg.K_RIGHT] or keys[pg.K_LEFT]):
            self.acc.x = FRICTION

class Baddie(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH, HEIGHT / 2)
        self.pos = vec(WIDTH, HEIGHT / 2)
        self.vel = vec(-5, 0)
        self.acc = vec(0, 0)
        self.collide_g = False
        self.max_jumps = 1
        self.jumps = 0

    def update(self):
        self.gravity()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
    
    def gravity(self):
        if self.collide_g == False and self.vel.y < 15:
            self.acc.y = GRAVITY

class Immovable(Sprite):
    def __init__(self, w, h, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((w * PIX, h * PIX))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
        # print(str(self.image)+" "+str(self.pos))

class Trap(Sprite):
    def __init__(self, w, h, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((w * PIX, h * PIX))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
        if self.pos.y > HEIGHT:
            self.kill()

class Powerup(Sprite):
    def __init__(self, w, h, x, y, t):
        Sprite.__init__(self)
        self.image = pg.Surface((w * PIX, h * PIX))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.type = t
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos