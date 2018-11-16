# This file was created by Cal
''' Sources:
KidsCanCode  Chris Bradfield
'''
import pygame as pg
import random
from settings import *
from sprites import *

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
        self.players = pg.sprite.Group()
        self.immovables = pg.sprite.Group()
        self.gamer = Player()
        self.ground = Immovable(WIDTH, 10, WIDTH / 4, HEIGHT - 5)
        self.platform = Immovable(WIDTH / 3, 10, 2 * WIDTH / 3, 3 * WIDTH / 4)
        self.players.add(self.gamer)
        self.immovables.add(self.ground)
        self.immovables.add(self.platform)
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
        # game loop
    def update(self):
        self.players.update()
        self.immovables.update()
        # updates sprites
    def collision(self):
        if pg.sprite.spritecollide(self.gamer, self.immovables, False):
            self.gamer.collide = True
        elif not pg.sprite.spritecollide(self.gamer, self.immovables, False):
            self.gamer.collide = False
        # sprite collision
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