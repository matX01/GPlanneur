# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:44:57 2020

@author: Eyokus
"""
import schedule

import pygame
import time
pygame.init()

def actualise():
    global h   
    global vitesseHorizontale
    global vitesseVerticale 
    global positonY
    h=altitude(positionY/10,h)
    vitesseVerticale = VitesseV(positionY/10)
    vitesseHorizontale = VitesseH(positionY/10)
    


largeur=500 
longueur=500

ScreenSize = width,height = largeur,longueur

black = 0, 0, 0
sky=135,206,235
dirt=91,60,17
positionY = 0.0


window_surface=pygame.display.set_mode(ScreenSize)

window_surface.fill(sky)


#image = pygame.image.load("condor-cockpit.jpg").convert_alpha()

schedule.every(1).seconds.do(actualise)


vitesseVerticale = 0
vitesseHorizontale = 0
continuer = True
refreshRate = 1
t = 1 / refreshRate
h=1000

pygame.key.set_repeat(50)
  
def VitesseV(positionY) :
    Vv=0.0001*(positionY**4)-0.004*(positionY**3)-0.04*(positionY**2)-0.07*(positionY)-1.35
    return(Vv)
    
def VitesseH(positionY) :
    Vh=0.0059*(positionY**4)+0.0128*(positionY**3)+1.22*(positionY**2)+8.42*(positionY)+113.31
    return(Vh)

def altitude(assiete, h0, t=t):
    Vv = VitesseV(assiete)
    h = h0 + t*Vv
    return h

while 1:
    
   # window_surface.blit(image, (0, 50))
    #for event in pygame.event.get():
        #if event.type == pygame.KEYDOWN:
            #continuer = False
    #pygame.display.flip()
    
    #Handle 
    schedule.run_pending()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if(positionY > -100):
                        positionY -= 1
                    
                if event.key == pygame.K_DOWN:
                    if(positionY < 100):
                        positionY += 1
    
    rect_form=pygame.Rect(0,largeur/2+positionY,longueur,largeur)
    
    pygame.draw.rect(window_surface,dirt,rect_form)
    
    rect_sky=pygame.Rect(0,0,longueur,largeur/2+positionY)
    
    pygame.draw.rect(window_surface,sky,rect_sky)
    
    pygame.draw.line(window_surface,black,[0,largeur/2+positionY],[longueur,largeur/2+positionY],5)

    # display text
    
    arial_font = pygame.font.SysFont("arial", 30)
    
    vitesse_verticale = arial_font.render('VS: {}'.format(vitesseVerticale), True, (0,0,0) )
    
    window_surface.blit(vitesse_verticale,(30,30))

    vitesse_horizontal = arial_font.render('VH: {}'.format(vitesseHorizontale), True, (0,0,0) )
    
    window_surface.blit(vitesse_horizontal,(30,70))

    
    
    Haltitude = arial_font.render('H: {}'.format(h), True, (0,0,0) )
    
    window_surface.blit(Haltitude,(30,110))
 

    assiette = arial_font.render('H: {}'.format(positionY), True, (0,0,0) )
    
    window_surface.blit(assiette,(30,160))


   
    
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
        