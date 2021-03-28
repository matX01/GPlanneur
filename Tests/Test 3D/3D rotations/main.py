import Graphics
import Mesh
import ConversionsTo3D as Conversions
import pygame
import matrix
import math
import copy
from dataclasses import dataclass
import time
from typing import List




TranslationMatrix = matrix.mat3x3([
    [0,0,8],
    [0,0,8],
    [0,0,8]

])



TranslationMatrix2 = matrix.mat3x3([
    [-0,0,0],
    [-0,0,0],
    [-0,0,0],

])


Cam = matrix.vector([0,0,0])
Light = matrix.vector([0,-0,-1])

Graphics.init()

theta = math.pi/3
spd = 0.01
Test = Mesh.Load3DElement("Tests/Test 3D/3D rotations/GAMIIIING.obj")
#print(Test.v)
while Graphics.ProgramRunning :
    
    cube2 = copy.deepcopy([Test])

    Graphics.PrintFPS()

    if(Graphics.SpaceToken):
        theta += math.pi/8
    else:
        theta += math.pi/512



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
    NonSortedZ = []
    SortedZ = []
    NonSortedIndex = []
    SortedIndex = []
    for i in range(len(cube2[0].v)):

        SortedZ.append((cube2[0].v[i].p[0].Coords[2] +cube2[0].v[i].p[1].Coords[2] + cube2[0].v[i].p[2].Coords[2])/3)
        NonSortedZ.append(SortedZ[i])
        NonSortedIndex.append(i)

    SortedZ.sort(reverse=True)
    
    for E in SortedZ:
        SortedIndex.append(NonSortedZ.index(E))
    
    #print(SortedIndex)
    Cube3 = Mesh.mesh([])
    for e in SortedIndex:

        Cube3.v.append(cube2[0].v[e])
    


    cube2 = copy.deepcopy([Cube3])

    for vertex in cube2[0].v:

        Normal.append(matrix.CrossProduct(

            matrix.vector([vertex.p[1].Coords[0]-vertex.p[0].Coords[0],
            vertex.p[1].Coords[1]-vertex.p[0].Coords[1],
            vertex.p[1].Coords[2]-vertex.p[0].Coords[2]]),

            matrix.vector([vertex.p[2].Coords[0]-vertex.p[0].Coords[0],
            vertex.p[2].Coords[1]-vertex.p[0].Coords[1],
            vertex.p[2].Coords[2]-vertex.p[0].Coords[2]])
            ))
        
        size = math.sqrt((Normal[len(Normal)-1].v[0])**2 + (Normal[len(Normal)-1].v[1])**2 + (Normal[len(Normal)-1].v[2])**2)
        if(not(size == 0)):
            Normal[len(Normal)-1].v[0] /= size
            Normal[len(Normal)-1].v[1] /= size
            Normal[len(Normal)-1].v[2] /= size
    


    for i in range(len(cube2[0].v)):
        ProjectedCam = matrix.vector([
            cube2[0].v[i].p[0].Coords[0] - Cam.v[0],
            cube2[0].v[i].p[0].Coords[1] - Cam.v[1],
            cube2[0].v[i].p[0].Coords[2] - Cam.v[2]

        ])
    
        if(matrix.DotProduct(ProjectedCam,Normal[i]) < 0):
           
            Conversions.FillVertex(Conversions.ProjectVertex(cube2[0].v[i]),Conversions.CalculateVertexColor(Normal[i],Light,(255,255,255)))
        #Conversions.DrawVertex(Conversions.ProjectVertex(cube2[0].v[i]),(255,255,255))
    
    Graphics.HandleWindowEvents()




 