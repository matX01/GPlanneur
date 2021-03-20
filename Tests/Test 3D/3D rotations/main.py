import Graphics
import Mesh
import Conversions
import pygame
import matrix
import math
import copy
from dataclasses import dataclass
import time

from typing import List
A = matrix.mat3x3([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
B = matrix.mat3x3([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])


@dataclass
class Point:                                                                    # Le point , constitué de 3 valeurs x , y , z
    Coords: List[float]
    
@dataclass
class Vertex:                                                                   # le vertex , un triangle sans volume constitué de trois points
    p: List[Point]
    
@dataclass
class mesh:                                                                     # le mesh , un ensemble de vertex permettant de former un polygone en 3 dimensions.
   v: List[Vertex]

matrix.PrintMatrix(matrix.multiplyMatrix(A,B))
Graphics.init()

"""
for i in range(len(Mesh.cube.v)):
        
        Mesh.cube.v[i] = matrix.multiplyMatrixVertex(
            Mesh.cube.v[i],matrix.RotationMatrix("X",math.pi/6))
    

for vertex in Mesh.cube.v:
        for points in vertex.p:
            points.Coords[2] += 5
            points.Coords[0] += 0
            points.Coords[1] += 0
"""

matrix.PrintVertex(matrix.multiplyMatrixVertex(Mesh.square.v[0],matrix.RotationMatrix("Z",math.pi/6)))

theta = 0

while Graphics.ProgramRunning:
    cube2 = copy.deepcopy([Mesh.cube])

    for i in range(len(cube2[0].v)):
        
        
        cube2[0].v[i] = matrix.multiplyMatrixVertex(
            cube2[0].v[i],matrix.RotationMatrix("Z",theta))
        cube2[0].v[i] = matrix.multiplyMatrixVertex(
            cube2[0].v[i],matrix.RotationMatrix("X",theta))
        cube2[0].v[i] = matrix.multiplyMatrixVertex(
            cube2[0].v[i],matrix.RotationMatrix("Y",theta))


    for vertex in cube2[0].v:
        for points in vertex.p:
            points.Coords[2] += 5
            points.Coords[0] += 0
            points.Coords[1] += 0


    #Graphics.PrintFPS()
    
    print(theta)
    theta += math.pi/256
    
    """
    for vertex in Mesh.ProjectedSquare.v:
        
        Conversions.DrawVertex(vertex,(255,0,0))
"""



    for vertex in cube2[0].v:

        Conversions.DrawVertex(Conversions.ProjectVertex(matrix.multiplyMatrixVertex(vertex,matrix.RotationMatrix("Z",theta))),(255,255,255))


    Graphics.HandleWindowEvents()


