import pygame
import time
import os
ScreenSize = width,height = 1920,1080
window = None
ISRUNNING = True
FPS = 190 # frames per second setting
Offset = [0,0,0,0]
JoystickAxis = [0 for i in range(4)]
joy = None


def init():
    global window
    global ScreenSize
    global JoystickAxis
    global joy
    global Offset
    #os.environ["SDL_VIDEO_DRIVER"] = "directx"
    pygame.init()
    try:
        pygame.joystick.init()
        joy = pygame.joystick.Joystick(0)
        joy.init()
    except:
        print("No joystick")
        pass
    window = pygame.display.set_mode((ScreenSize),pygame.FULLSCREEN | pygame.DOUBLEBUF,16)
    HandleWindowEvents()
    for i in range(4):
        
        Offset[i] = JoystickAxis[i]
    

def HandleWindowEvents():
    global SpaceToken
    global ISRUNNING
    global JoystickAxis
    global Offset
    pygame.display.flip()
    #pygame.display.update()
    #fpsClock.tick(FPS)
    window.fill((0,0,0))
    #PrintFPS()

    
    for event in pygame.event.get():
        if( event.type == pygame.QUIT):
            
            ISRUNNING = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if(joy.get_button(0)):

                for i in range(4):
                    
                    Offset[i] = joy.get_axis(i)
        

        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                ISRUNNING = False
        
        
    if (joy != None):
        for i in range(4):

            JoystickAxis[i] = joy.get_axis(i)-Offset[i]

       
        for i in range(4):
            if(JoystickAxis[i] <= 0.05 and JoystickAxis[i] >= -0.05):
                
                JoystickAxis[i] = 0

    #print(JoystickAxis)
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

