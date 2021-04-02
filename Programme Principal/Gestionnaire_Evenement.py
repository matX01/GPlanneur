import pygame


#le programme va simuler l'input d'un joystick en attendant qu'on en incorpore 1



YaxisStep = 10              #valeur de l'incrément a chaque pression sur la fleche
YaxisValue = 0              #valeur sur Y

af=0
afstep = 1


def begin(RepeatFrequency,step):
    global YaxisStep 
    YaxisStep = step
    pygame.key.set_repeat(RepeatFrequency)
  




                            

    
    
    
    
    
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
                    