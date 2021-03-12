import pygame

ScreenSize = width,height = 1280,720
window = None

ProgramRunning = True 

White = 255,255,255
SpaceToken = False



def init():
    
    global window
    global ScreenSize
    
    pygame.init()
    window = pygame.display.set_mode(ScreenSize)

def HandleWindowEvents():
    global SpaceToken
    global ProgramRunning
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if( event.type == pygame.QUIT):
            ProgramRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SpaceToken = True

        else:
            SpaceToken = False



init()



