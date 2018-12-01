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
        # init pygame and create window
    def new(self):
        # Groups
        self.players = pg.sprite.Group()
        self.immovables = pg.sprite.Group()
        self.baddies = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        # Player[s]
        self.gamer = Player()
        # Platforms
        self.ground = Immovable(4 * WIDTH, 30, 3 * WIDTH / 4, HEIGHT - 30)
        self.platform = Immovable(WIDTH / 3, 30, 2 * WIDTH / 3, HEIGHT - 180)
        # Enemies
        self.b1 = Baddie()
        # Powerups
        self.jump_boost1 = Powerup(1, 1, 6, 18)
        self.jump_boost2 = Powerup(1, 1, 6, 20)
        self.jump_boost3 = Powerup(1, 1, 9, 18)
        self.jump_boost4 = Powerup(1, 1, 16, 18)
        self.jump_boost5 = Powerup(1, 1, 1, 18)
        # Adding to the Groups
        self.players.add(self.gamer)
        self.immovables.add(self.ground)
        self.immovables.add(self.platform)
        self.baddies.add(self.b1)
        self.powerups.add(self.jump_boost1)
        self.powerups.add(self.jump_boost2)
        self.powerups.add(self.jump_boost3)
        self.powerups.add(self.jump_boost4)
        self.powerups.add(self.jump_boost5)
        self.run()
        # create new object
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(TICKS)
            self.events()
            self.update()
            self.draw()
            self.collision()
            self.scrolling()
            self.death()
        # game loop
    def update(self):
        self.players.update()
        self.immovables.update()
        self.baddies.update()
        self.powerups.update()
        # updates sprites
    def collision(self):
        gamer_hits = pg.sprite.spritecollide(self.gamer, self.immovables, False)
        if gamer_hits:
            self.gamer.pos.y = gamer_hits[0].rect.top + 1
            self.gamer.vel.y = 0
            self.gamer.collide_g = True
        elif not gamer_hits:
            self.gamer.collide_g = False

        b1_hits = pg.sprite.spritecollide(self.b1, self.immovables, False)
        if b1_hits:
            self.b1.pos.y = b1_hits[0].rect.top + 1
            self.b1.vel.y = 0
            self.b1.collide_g = True
        elif not b1_hits:
            self.b1.collide_g = False
        # sprite collision
    def scrolling(self):
        if self.gamer.pos.x >= WIDTH / 2 and self.gamer.vel.x > 0:
            for i in self.immovables:
                i.vel.x = -self.gamer.vel.x
            for i in self.powerups:
                i.vel.x = -self.gamer.vel.x
            self.gamer.pos.x = WIDTH / 2
        elif self.gamer.pos.x < WIDTH / 2:
            for i in self.immovables:
                i.vel.x = 0
        for i in self.powerups:
                i.vel.x = 0
        # Map scrolling
    def death(self):
        player_deathblow = pg.sprite.spritecollideany(self.gamer, self.baddies, False)
        player_item_collect = pg.sprite.spritecollideany(self.gamer, self.powerups, False)
        if player_deathblow:
            print(player_deathblow)
            self.players.remove(self.gamer)
            self.running = False
        if self.gamer.pos.y > HEIGHT + 60:
            self.players.remove(self.gamer)
            self.running = False
        if player_item_collect:
            self.powerups.remove(player_item_collect)
        # Player, Enemy, and Powerup removal
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
        # listening for events
    def draw(self):
        self.screen.fill(REDDISH)
        self.players.draw(self.screen)
        self.immovables.draw(self.screen)
        self.baddies.draw(self.screen)
        self.powerups.draw(self.screen)
        # double buffer
        pg.display.flip()
        # screen creation
    def show_start_screen(self):
        # self explanitory
        pass
    def show_go_screen(self):
        # show game over screen
        pass
    # init sound mixer

g=Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen
pg.quit()