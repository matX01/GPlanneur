from dataclasses import dataclass
from typing import List
import math
import Graphics as Graphics
import Mesh as Mesh
import ConversionsTo3D as Conversions
import pygame
import matrix as matrix
import math
import copy
from dataclasses import dataclass
import time
from typing import List

class mat3x3:
    m = [[]]

    def __init__(self,mat):
        
        self.m = mat

    
class vector:
    v = []

    def __init__(self,vector):

        self.v = vector


def MultiplyMatrix(A,B):
    
    return mat3x3([

        [A.m[0][0]*B.m[0][0]+A.m[0][1]*B.m[1][0]+A.m[0][2]*B.m[2][0],
        A.m[0][0]*B.m[0][1]+A.m[0][1]*B.m[1][1]+A.m[0][2]*B.m[2][1],
        A.m[0][0]*B.m[0][2]+A.m[0][1]*B.m[1][2]+A.m[0][2]*B.m[2][2]],
        
        
        [A.m[1][0]*B.m[0][0]+A.m[1][1]*B.m[1][0]+A.m[1][2]*B.m[2][0],
        A.m[1][0]*B.m[0][1]+A.m[1][1]*B.m[1][1]+A.m[1][2]*B.m[2][1],
        A.m[1][0]*B.m[0][2]+A.m[1][1]*B.m[1][2]+A.m[1][2]*B.m[2][2]],


        [A.m[2][0]*B.m[0][0]+A.m[2][1]*B.m[1][0]+A.m[2][2]*B.m[2][0],
        A.m[2][0]*B.m[0][1]+A.m[2][1]*B.m[1][1]+A.m[2][2]*B.m[2][1],
        A.m[2][0]*B.m[0][2]+A.m[2][1]*B.m[1][2]+A.m[2][2]*B.m[2][2]],

    ])

def AddMatrix(A,B):
    return mat3x3([
        [A.m[0][0]+B.m[0][0],A.m[0][1]+B.m[0][1],A.m[0][2]+B.m[0][2]],
        [A.m[1][0]+B.m[1][0],A.m[1][1]+B.m[1][1],A.m[1][2]+B.m[1][2]],
        [A.m[2][0]+B.m[2][0],A.m[2][1]+B.m[2][1],A.m[2][2]+B.m[2][2]],


    ])


def CrossProduct(A,B):
    return vector([
        A.v[1]*B.v[2] - A.v[2]*B.v[1],
        A.v[2]*B.v[0] - A.v[0]*B.v[2],
        A.v[0]*B.v[1] - A.v[1]*B.v[0]
    ])
def DotProduct(A,B):
    
    return A.v[0]*B.v[0]+A.v[1]*B.v[1]+A.v[2]*B.v[2]












def ConvertMatrixToVertex(A):
    return Mesh.Vertex([

        Mesh.Point([A.m[0][0],A.m[0][1],A.m[0][2]]),
        Mesh.Point([A.m[1][0],A.m[1][1],A.m[1][2]]),
        Mesh.Point([A.m[2][0],A.m[2][1],A.m[2][2]]),

    ])



def ConvertVertexToMatrix(A):
    return mat3x3([
        [A.p[0].Coords[0],A.p[0].Coords[1],A.p[0].Coords[2]],
        [A.p[1].Coords[0],A.p[1].Coords[1],A.p[1].Coords[2]],
        [A.p[2].Coords[0],A.p[2].Coords[1],A.p[2].Coords[2]]
    ])
    


def PrintMatrix(A):
    for M in A.m:
        print(M)
    print("")

def PrintVertex(A):
    for M in A.p:
        print(M.Coords)
    print("")




def RotationMatrix(R,Theta):
    if(R == "X"):
        return mat3x3([
            [1,0,0],
            [0,math.cos(Theta),-math.sin(Theta)],
            [0,math.sin(Theta),math.cos(Theta)]
        ])
    if(R == "Y"):
        return mat3x3([
            [math.cos(Theta),0,math.sin(Theta)],
            [0,1,0],
            [-math.sin(Theta),0,math.cos(Theta)]
        ])
    if(R == "Z"):
        return mat3x3([
            [math.cos(Theta),-math.sin(Theta),0],
            [math.sin(Theta),math.cos(Theta),0],
            [0,0,1]
        ])
