# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:41:06 2020

@author: julia
"""
#Résolution des équations différentielles

import numpy as np

m=500 
#poids du planeur
g=9.81
rho = 1.3
S = 16

theta = np.pi/6



def Cz(alpha)  :
    return 0.15*(alpha + 4)

def Cx(alpha,Cz0) :
    return  0.03+0.01*(Cz0**2)


A=[0, 0, 5, 5]
#Liste qui va contenir les positions, vitesses et l'angle (à ajouter)

h = 0.1
#Pas de la méthode d'Euler
t = 10 
#temps d'étude
iteration = int(t/h)
#Nombre d'itération des calculs


def Fonction(A, m, g, gamma, rho, S, Cx0, Cz0, theta, alpha):
    #compteur pour choisir la position dans la liste 
    vx_new = A[2]
    vy_new = A[3]
    
    
    
    ax_new = (1/(2*m))*rho*S*Cz0*(vx_new**2)*np.sin(gamma)-(1/(2*m))*rho*S*Cx0*vx_new**2*np.cos(gamma)
    ay_new = -g + (1/(2*m))*rho*S*Cz0*vy_new**2*np.cos(gamma)+(1/(2*m))*rho*S*Cx0*vy_new**2*np.sin(gamma)
    
    A_new = [vx_new, vy_new, ax_new, ay_new]
    
    return np.array(A_new)

#Test
X_prim = []
Y_prim = []



def execute(theta):
    gamma = np.arctan(A[3]/A[2])
    alpha = theta - gamma
    Cz0 = Cz(alpha)
    Cx0 = Cx(alpha,Cz0)
    A= A+h*Fonction(A, m, g, gamma, rho, S, Cx0, Cz0, theta, alpha)
    X_prim.append(A[0])
    Y_prim.append(A[1])


for i in range (0, iteration):
    
    gamma = np.arctan(A[3]/A[2])
    alpha = theta - gamma
    Cz0 = Cz(alpha)
    Cx0 = Cx(alpha,Cz0)
    A= A+h*Fonction(A, m, g, gamma, rho, S, Cx0, Cz0, theta, alpha)
    X_prim.append(A[0])
    Y_prim.append(A[1])
    
    
    
    
    #On récupère les positions à chaque itération
    print(int(i*100/iteration), "%")

  
np.plot(X_prim,Y_prim)

