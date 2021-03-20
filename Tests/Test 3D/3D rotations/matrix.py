from dataclasses import dataclass
from typing import List
import math
import Mesh

class mat3x3:
    m = [[]]

    def __init__(self,mat):
        
        self.m = mat


def multiplyMatrix(A,B):
    
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
def multiplyMatrixPoint(A,B):
    
    return Mesh.Point([
        A.Coords[0]*B.m[0][0]+A.Coords[1]*B.m[1][0]+A.Coords[2]*B.m[2][0],
        A.Coords[0]*B.m[0][1]+A.Coords[1]*B.m[1][1]+A.Coords[2]*B.m[2][1],
        A.Coords[0]*B.m[0][2]+A.Coords[1]*B.m[1][2]+A.Coords[2]*B.m[2][2],
    ])
"""
def multiplyMatrixVertex(A,B):
    return Mesh.Vertex([
        multiplyMatrixPoint(A.p[0],B),
        multiplyMatrixPoint(A.p[1],B),
        multiplyMatrixPoint(A.p[2],B)
    ])
"""
def multiplyMatrixVertex(A,B):
    return Mesh.Vertex([
        multiplyMatrixPoint(A.p[0],B),
        multiplyMatrixPoint(A.p[1],B),
        multiplyMatrixPoint(A.p[2],B),
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
