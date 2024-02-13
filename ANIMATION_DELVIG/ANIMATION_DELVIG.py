# Delvig Diego 1G7

import pygame
from pygame import *
from pygame.gfxdraw import *
from pygame.time import *
from random import random

def move_ball(x: int, dx: int, y: int, dy:int, speed: float) -> tuple:

    if x <= 0:
        dx *= -1
    if x >= 700:
        dx *= -1
    if y <= 0:
        dy *= -1
    if y >= 500:
        dy *= -1

    x = x + speed * dx

    y = y + speed * dy

    return x, dx, y, dy

def display_image(active_player: bool) -> None:
    screen.blit(bg, (0, 0))
    screen.blit(ball, (x_ball, y_ball))
    
    if active_player:
        screen.blit(player, (x_player, y_player))

    return active_player

width, height = 800, 600

# initialise pygame et l'écran
pygame.init()           
screen = pygame.display.set_mode((width, height))

# stocke les images dans les variables
bg = image.load('images/espace.jpeg').convert()
bg = transform.scale(bg, (800, 600))
ball = image.load('images/ball.png').convert_alpha()
player = image.load('images/player.png').convert_alpha()

# variables de la balle
x_ball = 50
dx_ball = random()
y_ball = 50
dy_ball = random()

# variables du joueur
x_player = 100
y_player = 300
width_player = 100
height_player = 133
active_player = False
mode = False


running = 1

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if active_player:
                    active_player = False
                else:
                    active_player = True


            if mode == False:
                if event.key == K_LEFT:
                    x_player = x_player - 10
                if event.key == K_RIGHT:
                    x_player = x_player + 10
                if event.key == K_UP:
                    y_player = y_player - 10
                if event.key == K_DOWN:
                    y_player = y_player + 10

            if event.key == K_w:
                if mode == True:
                    mode = False
                else:
                    mode = True

        if mode:
            pos = mouse.get_pos()
            x_player = pos[0] - width_player / 2
            y_player = pos[1] - height_player / 2
                
    # fait bouger la balle
    x_ball, dx_ball, y_ball, dy_ball = move_ball(x_ball, dx_ball, y_ball, dy_ball, 0.5)
    
    # affiche les images
    display_image(active_player)
    display.flip()
    
    time.delay(2)
    
    if active_player == True and mode == False:
        key.set_repeat(10, 0)


pygame.quit()



