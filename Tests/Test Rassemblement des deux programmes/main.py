import pygame
import Gestionnaire_Evenement as WindowEvent
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time
import MoteurV2.main as Graph
import math


ExecutionTime = 0
TimeStep = 0.1

A = [0, 0, 0, 0]

def begin():
    Physics.SetTimeStep(TimeStep)
    GraphicPane.begin(1280,720)
    WindowEvent.begin(10,0.1)
    Graph.init(GraphicPane.window_surface)


def __main__():
    global ExecutionTime
    global TimeStep
    global A
    
    if(time.time() >= ExecutionTime):
        ExecutionTime = time.time() + TimeStep
 
        A = Physics.ExecuteEuler(WindowEvent.YaxisValue)
    
    Graph.Disp(-WindowEvent.YaxisValue * math.pi/180)
    GraphicPane.Display(WindowEvent.YaxisValue,A[3],A[2],A[1])
    WindowEvent.Actualise()
    
    

    
begin()
while True:
    
    __main__()

