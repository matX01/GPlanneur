import Graphics
import Mesh
import ConversionsTo3D as Conversions
import pygame
import matrix
import math
import copy
from dataclasses import dataclass
import time
from numba import jit, cuda 
from typing import List




TranslationMatrix = matrix.mat3x3([
    [0,0,5],
    [0,0,5],
    [0,0,5]

])

TranslationMatrix2 = matrix.mat3x3([
    [-0.5,-0.5,-0.5],
    [-0.5,-0.5,-0.5],
    [-0.5,-0.5,-0.5]

])


Cam = matrix.vector([0,0,0])
Light = matrix.vector([0,-.66,-.75])

Graphics.init()

theta = 0



while Graphics.ProgramRunning:
    
    Graphics.displayCenter()

    cube2 = copy.deepcopy([Mesh.cube])

    

    for i in range(len(cube2[0].v)):

        #Calcul effectué : ((translationMatrix2 + cube2[0].v[i]) * RotationMatrix("X",theta)) + translationMatrix
        
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(matrix.AddMatrix(TranslationMatrix2,matrix.ConvertVertexToMatrix(cube2[0].v[i])))
        
        
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(
            matrix.MultiplyMatrix(
                matrix.ConvertVertexToMatrix(cube2[0].v[i]),
                matrix.RotationMatrix("X",theta)))
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(
            matrix.MultiplyMatrix(
                matrix.ConvertVertexToMatrix(cube2[0].v[i]),
                matrix.RotationMatrix("Y",theta)))
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(
            matrix.MultiplyMatrix(
                matrix.ConvertVertexToMatrix(cube2[0].v[i]),
                matrix.RotationMatrix("Z",theta)))
        
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(matrix.AddMatrix(TranslationMatrix,matrix.ConvertVertexToMatrix(cube2[0].v[i])))

    Normal = []

    for vertex in cube2[0].v:

        Normal.append(matrix.CrossProduct(

            matrix.vector([vertex.p[1].Coords[0]-vertex.p[0].Coords[0],
            vertex.p[1].Coords[1]-vertex.p[0].Coords[1],
            vertex.p[1].Coords[2]-vertex.p[0].Coords[2]]),

            matrix.vector([vertex.p[2].Coords[0]-vertex.p[0].Coords[0],
            vertex.p[2].Coords[1]-vertex.p[0].Coords[1],
            vertex.p[2].Coords[2]-vertex.p[0].Coords[2]])
            ))
        
        size = 1/math.sqrt((Normal[len(Normal)-1].v[0])**2 + (Normal[len(Normal)-1].v[1])**2 + (Normal[len(Normal)-1].v[2])**2)
        Normal[len(Normal)-1].v[0] *= size
        Normal[len(Normal)-1].v[1] *= size
        Normal[len(Normal)-1].v[2] *= size
    

    #Graphics.PrintFPS()

 
  
    #print(theta)
    if(Graphics.SpaceToken):
        pass
    else:
        theta += math.pi/512

    for i in range(len(cube2[0].v)):
        ProjectedCam = matrix.vector([
            cube2[0].v[i].p[0].Coords[0] - Cam.v[0],
            cube2[0].v[i].p[0].Coords[1] - Cam.v[1],
            cube2[0].v[i].p[0].Coords[2] - Cam.v[2]

        ])

        if(matrix.DotProduct(ProjectedCam,Normal[i]) < 0):
          
            Conversions.FillVertex(Conversions.ProjectVertex(cube2[0].v[i]),Conversions.CalculateVertexColor(cube2[0].v[i],Normal[i],Light,(255,255,255)))
        #Conversions.DrawVertex(cube2[0].v[i],(255,0,0))
            #Conversions.DrawVertex(Conversions.ProjectVertex(cube2[0].v[i]),(255,255,255))
    
   


    Graphics.HandleWindowEvents()


