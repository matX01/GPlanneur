import pygame
import Gestionnaire_Evenement as WindowEvent
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time



ExecutionTime = 0
TimeStep = 0.1

A = [0, 0, 0, 0]

def begin():
    Physics.SetTimeStep(TimeStep)
    GraphicPane.begin(500,500)
    WindowEvent.begin(10,0.01)



def __main__():
    global ExecutionTime
    global TimeStep
    global A
    
    if(time.time() >= ExecutionTime):
        ExecutionTime = time.time() + TimeStep
 
        A = Physics.ExecuteEuler(WindowEvent.YaxisValue)
    
  
    GraphicPane.Display(WindowEvent.YaxisValue,A[3],A[2],A[1])
    WindowEvent.Actualise()
    
    

    
begin()
while True:
    
    __main__();

