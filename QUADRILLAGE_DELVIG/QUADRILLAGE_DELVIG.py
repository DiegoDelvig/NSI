import pygame
from pygame import *
from pygame.gfxdraw import *
from random import randint

width, height = 601, 801

pygame.init()           
screen = pygame.display.set_mode((height, width))
clicked = False
boxs = []
tresor_pos = (randint(0, 7), randint(0, 5))
found = False
tresor = image.load('trésor.jpg').convert()

running = 1
while running:


    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            running = 0

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()

            if mouse_pos[0] // 100 == tresor_pos[0] and mouse_pos[1] // 100 == tresor_pos[1]:
                found = True
            boxs.append((mouse_pos[0] // 100 , mouse_pos[1] // 100))


    screen.fill((0, 0, 0))

    # affiche toutes les boites jaune
    for box_pos in boxs:
        box(screen, (box_pos[0] * 100, box_pos[1] * 100, 100, 100), (255, 255, 0))

    if found:
        # afficher l'image
        tresor = transform.scale(tresor, (100, 100))
        screen.blit(tresor, (tresor_pos[0] * 100, tresor_pos[1] * 100))

    # affichage du quadrillage
    for i in range (0, 601, 100):
        line(screen, 0, i, height, i, (0, 0, 255))
    for j in range (0, 801, 100):
        line(screen, j, 0, j, height, (0, 0, 255))

    pygame.display.flip()

pygame.quit()


















