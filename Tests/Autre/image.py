# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:44:57 2020

@author: Eyokus
"""


import pygame

pygame.init()

largeur=500 
longueur=500

ScreenSize = width,height = largeur,longueur

black = 0, 0, 0
sky=135,206,235
dirt=91,60,17
positionY = 0

window_surface=pygame.display.set_mode(ScreenSize)
window_surface.fill(sky)
ecran = pygame.display.set_mode((942,332))
#image = pygame.image.load("condor-cockpit.jpg").convert_alpha()

continuer = True

pygame.key.set_repeat(10)

while 1:
    
    #window_surface.blit(image, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    positionY -= 1
                if event.key == pygame.K_DOWN:
                    positionY += 1
    rect_form=pygame.Rect(0,largeur/2+positionY,longueur,largeur)
    pygame.draw.rect(window_surface,dirt,rect_form)
    rect_sky=pygame.Rect(0,0,longueur,largeur/2+positionY)
    pygame.draw.rect(window_surface,sky,rect_sky)
    pygame.draw.line(window_surface,black,[0,largeur/2+positionY],[longueur,largeur/2+positionY],5)
    pygame.draw.circle(window_surface, dirt, (300, 50), 20, 0)
    pygame.display.flip()


pygame.quit()
        
























import pygame

pygame.init()

ecran = pygame.display.set_mode((942,332))
image = pygame.image.load("condor-cockpit1.jpg").convert_alpha()

continuer = True

while continuer:
    ecran.blit(image, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

pygame.quit()
        