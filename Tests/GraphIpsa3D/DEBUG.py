import pygame
import time
import os
ScreenSize = width,height = 1920,1080
window = None
ISRUNNING = True
FPS = 190 # frames per second setting
fpsClock = pygame.time.Clock()

def init():
    global window
    global ScreenSize
    os.environ["SDL_VIDEO_DRIVER"] = "directx"
    pygame.init()
    window = pygame.display.set_mode((ScreenSize),pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE,16)


def HandleWindowEvents():
    global SpaceToken
    global ISRUNNING
    
    pygame.display.flip()
    #pygame.display.update()
    #fpsClock.tick(FPS)
    window.fill((0,0,0))
    PrintFPS()

    
    for event in pygame.event.get():
        if( event.type == pygame.QUIT):
            
            ISRUNNING = False

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                ISRUNNING = False



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
    
    

def quit():

    pygame.quit()

