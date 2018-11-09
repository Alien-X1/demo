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
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.ground = Immovable()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ground)
        self.run()
        # create new object
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            self.collision_check(self.player,self.ground)
        # game loop
    def update(self):
        self.all_sprites.update()
        # updates sprites
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
        # listening for events
    def draw(self):
        self.screen.fill(REDDISH)
        self.all_sprites.draw(self.screen)
        # double buffer
        pg.display.flip()
        # screen creation
    def show_start_screen(self):
        # self explanitory
        pass
    def show_go_screen(self):
        # show game over screen
        pass
    def collision_check(self,sprite1,sprite2):
        collision = py.sprite.collde_rect(sprite1,sprite2)
        if collision == true:
            sys.exit()
    # init sound mixer

g=Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen
pg.quit()