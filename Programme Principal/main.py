import pygame
import Gestionnaire_Evenement as WindowEvent
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time



ExecutionTime = 0
TimeStep = 0.001

A = [0,0,0,0]


def begin():
    Physics.SetTimeStep(TimeStep)
    GraphicPane.begin(500,500)
    WindowEvent.begin(10,1)



def __main__():
    global A
    global ExecutionTime
    global TimeStep
    
    if(time.time() >= ExecutionTime):
        ExecutionTime = time.time() + TimeStep
 
        A = Physics.ExecuteEuler(WindowEvent.YaxisValue)
    
    
    
    print(A)
    GraphicPane.Display(WindowEvent.YaxisValue/100,1000,1000,1000)
    WindowEvent.Actualise()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
begin()
while True:
    
    __main__();

