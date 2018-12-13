# This file was made by Cal
import pygame as pg

TITLE = "Rage It"
# Screen Dimensions
WIDTH = 1200
HEIGHT = 720
# Frames Per Second
TICKS = 60
# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
ORANGE = (255,155,0)
# REDDISH = (240,55,66)

L_BLUE = (0,179,233)
TEAL = (0,108,144)
NAVY = (0,14,76)
SEA = (0,173,136)
# Player game settings
FRICTION = 1
ACCELERATION = 1
GRAVITY = 1
PLAYER_JUMP_VEL = 15
PLAYER_MAX_VEL = 10
PLAYER_MAX_JUMPS = 1
PIX = 30

b1_mask = pg.image.load("v2_images\Baddie_block_1.png")
b2_mask = pg.image.load("v2_images\Baddie_block_2.png")
b_masks = [b1_mask,b2_mask]
f_mask = pg.image.load("v2_images\Flag_block.png")
s_top_mask = pg.image.load("v2_images\Solid_block.png")
t_top_mask = pg.image.load("v2_images\Trap_block.png")
p_walk_mask = pg.image.load("v2_images\Player_block_1.png")
p_jump_mask = pg.image.load("v2_images\Player_block_4.png")
h_mask =  pg.image.load("v2_images\Hidden_block.png")
pow_mask =  pg.image.load("v2_images\Power_block.png")