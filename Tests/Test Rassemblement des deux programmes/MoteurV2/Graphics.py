ScreenSize = width,height = 1280,720
window = None
import pygame
import time
import MoteurV2.Graphics as Graphics
import MoteurV2.Mesh as Mesh
import MoteurV2.ConversionsTo3D as Conversions
import pygame
import MoteurV2.matrix as matrix
import math
import copy
from dataclasses import dataclass
import time
from typing import List



ProgramRunning = True 

#ScreenZBuffering = [0 for i in range(width)][0 for j in range(height)]


SpaceToken = False
def init():
    
    global window

    

def displayCenter():

    pygame.draw.line(window,(255,0,0),((width/2-20),(height/2)),((width/2+20),(height/2)))
    pygame.draw.line(window,(255,0,0),((width/2),(height/2-20)),((width/2),(height/2+20)))



def HandleWindowEvents():
    global SpaceToken
    global ProgramRunning
    
    pygame.display.flip()
    pygame.display.update()
    window.fill((0,0,0))



oldTime = 0
It = 0
def PrintFPS():
    global It
    global oldTime
    It += 1
    
    if(oldTime < time.time()*1000):
        print(It)
        It = 0
        oldTime = time.time()*1000+ 1000
    
    
    #print(1/(time.time()-oldTime))
    
    