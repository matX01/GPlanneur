import Gestionnaire_Evenement as WindowEvent
import Moteur_Graphique as GraphicPane
import Moteur_Physique as Physics
import time
from matplotlib import pyplot as plt
import numpy as np



ExecutionTime = 0
TimeStep = 0.1

A = [0, 0, 0, 0]

i = 0#compteur

def begin():
    Physics.SetTimeStep(TimeStep)
    GraphicPane.begin(500,500)
    WindowEvent.begin(1,0.01)
It = 0
oldTime = 0
def PrintFPS():
    global It
    global oldTime
    It += 1
    
    if(oldTime < time.time()*1000):
        
        print(It)
        
        It = 0
        oldTime = time.time()*1000+ 1000
    
    


def __main__():
    global ExecutionTime
    global TimeStep
    global A
    global i
    
    if(time.time() >= ExecutionTime):
        ExecutionTime = time.time() + TimeStep
 
        A = Physics.ExecuteEuler(WindowEvent.YaxisValue)
    
  
    GraphicPane.Display(WindowEvent.YaxisValue,A[3],A[2],A[1],WindowEvent.af)
    WindowEvent.Actualise()
    
'''    
    if i%100 == 0 :
        plt.scatter(i,A[1], c='black')
        plt.pause(0.0001)

    i+=1
    plt.xlabel("Temps")
    plt.ylabel("Altitude (m)")
    plt.show()
'''
    
    

    
begin()
while True:
    
    __main__()

