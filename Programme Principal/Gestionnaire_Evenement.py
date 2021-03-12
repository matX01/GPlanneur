import pygame


#le programme va simuler l'input d'un joystick en attendant qu'on en incorpore 1



YaxisStep = 10              #valeur de l'incrément a chaque pression sur la fleche
YaxisValue = 0              #valeur sur Y


def begin(RepeatFrequency,step):
    global YaxisStep 
    YaxisStep = step
    pygame.key.set_repeat(RepeatFrequency)
  




                            

    
    
    
    
    
def Actualise():           #méthode pour actualiser les actions sur le clavier et la fenetre

    global YaxisValue
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                YaxisValue -= YaxisStep
                    
            if event.key == pygame.K_DOWN:
             
                YaxisValue += YaxisStep
    