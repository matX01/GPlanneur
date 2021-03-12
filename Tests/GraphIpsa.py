# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:39:36 2020

@author: mathi
"""
import pygame

Screen = 0

def Initialiser_Ecran(Width,Height):
    
    
    global Screen 
    Screen = pygame.display.set_mode([Width,Height])
    #pygame.key.set_repeat(10)
    return Screen
    
    
    
def Tracer_Rectangle(color,X,Y,XSize,YSize):
    global Screen
    rect_form=pygame.Rect(X,Y,XSize,YSize)
    pygame.draw.rect(Screen,color,rect_form)


    
def Couleur_arriere_plan(Color,X,Y,XSize,YSize):
    
    Screen.fill(Color,rect=[X,Y,XSize,YSize])
        
    
    
    
def Actualiser_La_Fenetre():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        
        
    pygame.display.update()
            
                
            
            
     
                
        
        