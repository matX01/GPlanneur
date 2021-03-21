import pygame
import time

ScreenSize = width,height = 1280,720
window = None

ProgramRunning = True 

def init():
    
    global window
    global ScreenSize
    
    pygame.init()
    window = pygame.display.set_mode(ScreenSize)

def displayCenter():

    pygame.draw.line(window,(255,0,0),((width/2-20),(height/2)),((width/2+20),(height/2)))
    pygame.draw.line(window,(255,0,0),((width/2),(height/2-20)),((width/2),(height/2+20)))



def HandleWindowEvents():
    global SpaceToken
    global ProgramRunning
    
    pygame.display.flip()
    pygame.display.update()
    window.fill(0)
    for event in pygame.event.get():
        if( event.type == pygame.QUIT):
            ProgramRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SpaceToken = True

        else:
            SpaceToken = False


oldTime = 0
def PrintFPS():
    global oldTime
    print(1/(time.time()-oldTime))
    
    oldTime = time.time()