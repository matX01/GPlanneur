# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:30:31 2020

@author: Eyokus
"""
import GraphIpsa






largeur=500 
longueur=500

#ScreenSize = width,height = largeur,longueur

black = 0, 0, 0
sky=135,206,235
dirt=91,60,17
positionY = 0


def initialiser_Horizon(taille_X,taille_Y):
    global largeur
    global longueur
    largeur = taille_X
    longueur = taille_Y
    


def Tracer_horizon(positionY):
    global sky
    global dirt
    global largeur
    global longueur
    GraphIpsa.Tracer_Rectangle(dirt,0,largeur/2+positionY,longueur,largeur)
    GraphIpsa.Tracer_Rectangle(sky,0,0,longueur,largeur/2+positionY)
    


