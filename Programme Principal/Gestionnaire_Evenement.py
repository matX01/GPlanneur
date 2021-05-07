import pygame
import time

#le programme va simuler l'input d'un joystick en attendant qu'on en incorpore 1



YaxisStep = 10              #valeur de l'incrément a chaque pression sur la fleche
YaxisValue = 0              #valeur sur Y

af=0
afstep = 1

axis_value=[0 for i in range(4)]
joysticks=[]
offset=[0 for i in range(4)]
begin_time=0

def begin(RepeatFrequency,step):
    global YaxisStep 
    YaxisStep = step
    pygame.key.set_repeat(RepeatFrequency)
    pygame.joystick.init()
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
    for i in range (4):
        offset[i]=joysticks[0].get_axis(i)
  


                            

    
    
    
    
    
def Actualise():           #méthode pour actualiser les actions sur le clavier et la fenetre

    global YaxisValue
    global af
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                YaxisValue -= YaxisStep
                    
            if event.key == pygame.K_DOWN:
             
                YaxisValue += YaxisStep
            
    
           
            if event.key == pygame.K_h:
                
                if af < 100 :
                    af += afstep
                
            if event.key == pygame.K_j:
                
                if af > 0:
                    af -= afstep
            if event.type==pygame.JOYAXISMOTION:
                for i in range (4):
                    axis_value[i]=joysticks[0].get_axis(i)-offset[i]
    if axis_value[1]>0.1 or axis_value[1]<-0.1:
        YaxisValue += axis_value[1]*delta_time           