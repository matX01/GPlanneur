import math
import time
import numpy as np
TimeStep = 0



m=500 
#poids du planeur
g=9.81
rho = 1.3
S = 16
h = 0.1

A = [0,0,30,-1]



def SetTimeStep(t):
    global TimeStep
    global h
    global ExecutionTime
    h = t
    ExecutionTime = time.time() + t




def Cz(alpha)  :
    return 0.15*(alpha + 4)

def Cx(Cz0) :
    return  0.03+0.01*(Cz0**2)


def ExecuteEuler(theta):
    #compteur pour choisir la position dans la liste 
    
    global A
    global m
    global S
    global g
    global rho
    
    gamma = np.arctan(A[3]/A[2])
    alpha = theta - gamma
    Cz0 = Cz(alpha)
    Cx0 = Cx(Cz0)
    
    vx_new = A[2]
    vy_new = A[3]
    
    
    
    ax_new = (1/(2*m))*rho*S*Cz0*(vx_new**2)*np.sin(gamma*np.pi/180)-(1/(2*m))*rho*S*Cx0*vx_new**2*np.cos(gamma*np.pi/180)
    ay_new = -g + (1/(2*m))*rho*S*Cz0*vy_new**2*np.cos(gamma*np.pi/180)+(1/(2*m))*rho*S*Cx0*vy_new**2*np.sin(gamma*np.pi/180)
    
    A_new = [vx_new, vy_new, ax_new, ay_new]
    
    A = A+h*np.array(A_new)
    
 
    return A





    
    
    
    
    
    
    
    
    