# This file was created by Cal
''' Sources:
KidsCanCode  Chris Bradfield
'''
import pygame as pg
import random
from settings import *
from sprites import *
from time import sleep

class Game:
    def __init__ (self):
        # init game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True
        self.alive = True
        # init pygame and create window
    def new(self):
        # Groups
        self.players = pg.sprite.Group()
        self.immovables = pg.sprite.Group()
        self.traps = pg.sprite.Group()
        self.hiddens = pg.sprite.Group()
        self.baddies = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        # Player[s]
        self.gamer = Player()
        # Platforms
        self.g1 = Immovable(60, 2, 29.5, 22)
        self.p1 = Immovable(12, 1, 5.5, 17)
        self.u1 = Immovable(1, 1, 78, 23)
        # Hidden Platforms
        self.h1 = Hidden(1, 1, 16, 13)
        self.h2 = Hidden(1, 1, 70, 15)
        self.h3 = Hidden(1, 1, 85, 15)
        # Traps
        self.t1 = Trap(1, 1, 14, 18)
        self.t2 = Trap(20, 2, 69.5, 22)
        # Enemies
        self.b1 = Baddie()
        # Powerups
        self.pu1 = Powerup(1, 1, 0, 18, "jump")
        self.pu2 = Powerup(1, 1, 2, 18, "speed")
        self.pu3 = Powerup(1, 1, 4, 18, "death")
        self.pu4 = Powerup(1, 1, 6, 18, "jump")
        self.pu5 = Powerup(1, 1, 8, 18, "death")
        self.pu6 = Powerup(1, 1, 10, 18, "clear")
        self.pu7 = Powerup(1, 22, 59, 0, "clear")
        # Adding to the Groups
        self.players.add(self.gamer)
        self.immovables.add(self.g1)
        self.immovables.add(self.p1)
        self.immovables.add(self.u1)
        self.traps.add(self.t1)
        self.traps.add(self.t2)
        self.hiddens.add(self.h1)
        self.hiddens.add(self.h2)
        self.hiddens.add(self.h3)
        self.baddies.add(self.b1)
        self.powerups.add(self.pu1)
        self.powerups.add(self.pu2)
        self.powerups.add(self.pu3)
        self.powerups.add(self.pu4)
        self.powerups.add(self.pu5)
        self.powerups.add(self.pu6)
        self.powerups.add(self.pu7)
        # create new object
    def run(self):
        while self.playing:
            self.new()
            while self.alive:
                self.clock.tick(TICKS)
                self.events()
                self.update()
                self.draw()
                self.collision()
                self.scrolling()
                self.death()
            self.reset()
        # game loop
    def reset(self):
        for i in self.hiddens:
            self.hiddens.remove(i)
        for i in self.players:
            self.players.remove(i)
        for i in self.immovables:
            self.immovables.remove(i)
        for i in self.traps:
            self.traps.remove(i)
        for i in self.baddies:
            self.baddies.remove(i)
        for i in self.powerups:
            self.powerups.remove(i)
        self.alive = True
        
    def update(self):
        self.hiddens.update()
        self.players.update()
        self.immovables.update()
        self.traps.update()
        self.baddies.update()
        self.powerups.update()
        # updates sprites
    def collision(self):
        gamer_hits_g = pg.sprite.spritecollide(self.gamer, self.immovables, False)
        gamer_hits_t = pg.sprite.spritecollide(self.gamer, self.traps, False)
        gamer_hits_h = pg.sprite.spritecollide(self.gamer, self.hiddens, False)
        block_hit_g = pg.sprite.spritecollideany(self.gamer, self.immovables, False)
        block_hit_t = pg.sprite.spritecollideany(self.gamer, self.traps, False)
        block_hit_h = pg.sprite.spritecollideany(self.gamer, self.hiddens, False)
        if gamer_hits_g:
            print(block_hit_g)
            if self.gamer.rect.bottom < block_hit_g.rect.top + 29:     
                self.gamer.pos.y = block_hit_g.rect.top + 1
                self.gamer.vel.y = 0
                self.gamer.collide_g = True
            elif self.gamer.rect.top > block_hit_g.rect.bottom - 29:
                self.gamer.vel.y = 0
                self.gamer.collide_g = False
                self.gamer.jumps = self.gamer.max_jumps
        if gamer_hits_t:
            print(block_hit_t)
            if self.gamer.rect.bottom < block_hit_t.rect.top + 29:
                self.gamer.pos.y = block_hit_t.rect.top - 1    
                self.gamer.vel.y = 0
                self.gamer.collide_g = False
                block_hit_t.acc.y = GRAVITY
            elif self.gamer.rect.top > block_hit_t.rect.bottom - 29:
                self.gamer.vel.y = 0
                self.gamer.collide_g = False
                self.gamer.jumps = self.gamer.max_jumps
        if gamer_hits_h:
            print(block_hit_h)
            if self.gamer.rect.bottom < block_hit_h.rect.top + 29:     
                self.gamer.pos.y = block_hit_h.rect.top + 1
                self.gamer.vel.y = 0
                self.gamer.collide_g = True
            # elif self.gamer.rect.top > block_hit_h.rect.bottom - 29 and not block_hit_h.color == RED:
            #     self.hiddens.remove(block_hit_h)
            #     block_hit_h.color = RED
            #     print(block_hit_h.color)
            #     self.hiddens.add(block_hit_h)
                
        elif not gamer_hits_g or gamer_hits_t or gamer_hits_h:
            self.gamer.collide_g = False

        b1_hits_g = pg.sprite.spritecollide(self.b1, self.immovables, False)
        b1_hits_t = pg.sprite.spritecollide(self.b1, self.traps, False)
        if b1_hits_g:
            self.b1.pos.y = b1_hits_g[0].rect.top + 1
            self.b1.vel.y = 0
            self.b1.collide_g = True
        if b1_hits_t:
            self.b1.pos.y = b1_hits_t[0].rect.top + 1
            self.b1.vel.y = 0
            self.b1.collide_g = True
        elif not b1_hits_g or b1_hits_t:
            self.b1.collide_g = False
        # sprite collision
    def scrolling(self):
        if self.gamer.pos.x >= WIDTH / 2 and self.gamer.vel.x > 0:
            for i in self.immovables:
                i.vel.x = -self.gamer.vel.x
            for i in self.traps:
                i.vel.x = -self.gamer.vel.x
            for i in self.hiddens:
                i.vel.x = -self.gamer.vel.x
            for i in self.powerups:
                i.vel.x = -self.gamer.vel.x
            for i in self.baddies:
                i.vel.x = -self.gamer.vel.x - 5
            self.gamer.pos.x = WIDTH / 2
        elif self.gamer.pos.x < WIDTH / 2:
            for i in self.immovables:
                i.vel.x = 0
            for i in self.traps:
                i.vel.x = 0
            for i in self.hiddens:
                i.vel.x = 0
            for i in self.powerups:
                i.vel.x = 0
            for i in self.baddies:
                i.vel.x = -5
        # Map scrolling
    def death(self):
        player_deathblow = pg.sprite.spritecollideany(self.gamer, self.baddies, False)
        player_item_collect = pg.sprite.spritecollideany(self.gamer, self.powerups, False)
        if player_deathblow:
            print(player_deathblow)
            self.alive = False
            self.gamer.vel = vec(0,0)
        if self.gamer.pos.y > HEIGHT + 60:
            self.alive = False
            self.gamer.vel = vec(0,0)
        if player_item_collect:
            self.powerups.remove(player_item_collect)
            if player_item_collect.type == "death":
                self.alive = False
            elif player_item_collect.type == "jump":
                self.gamer.max_jumps += 1
            elif player_item_collect.type == "speed":
                self.gamer.max_vel += 10
            elif player_item_collect.type == "clear":
                self.gamer.max_vel = PLAYER_MAX_VEL
                self.gamer.max_jumps = PLAYER_MAX_JUMPS
        # Player, Enemy, and Powerup removal
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.alive = False
                    self.running = False
        # listening for events
    def draw(self):
        # self.screen.fill(RED)
        self.screen.fill(NAVY)
        self.hiddens.draw(self.screen)
        self.players.draw(self.screen)
        self.immovables.draw(self.screen)
        self.traps.draw(self.screen)
        self.baddies.draw(self.screen)
        self.powerups.draw(self.screen)
        # double buffer
        pg.display.flip()
        # screen creation
    def show_start_screen(self):
        # self explanitory
        pass
    def show_go_screen(self):
        self.screen.fill(BLACK)

        # show game over screen
        pass
    # init sound mixer

g=Game()
g.show_start_screen()

while g.running:
    g.run()
    g.show_go_screen
pg.quit()