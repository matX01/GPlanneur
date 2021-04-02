import MoteurV2.Graphics as Graphics
import MoteurV2.Mesh as Mesh
import MoteurV2.ConversionsTo3D as Conversions
import pygame
import MoteurV2.matrix as matrix
import math
import copy
from dataclasses import dataclass
import time
from typing import List




TranslationMatrix = matrix.mat3x3([
    [0,3,8],
    [0,3,8],
    [0,3,8]

])



TranslationMatrix2 = matrix.mat3x3([
    [-0,0,0],
    [-0,0,0],
    [-0,0,0],

])


Cam = matrix.vector([0,0,0])
Light = matrix.vector([0,-.7,-.7])

def init(Pane):
    Graphics.window = Pane

theta = math.pi/3
spd = 0.01

Test = Mesh.Load3DElement("GPlanneur/Tests/Test Rassemblement des deux programmes/MoteurV2/Modèle.obj")

#print(Test.v)
def Disp(Y):
    
    cube2 = copy.deepcopy([Test])

    Graphics.PrintFPS()




    for i in range(len(cube2[0].v)):


    
        #Calcul effectué : ((translationMatrix2 + cube2[0].v[i]) * RotationMatrix("X",theta)) + translationMatrix
        
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(matrix.AddMatrix(TranslationMatrix2,matrix.ConvertVertexToMatrix(cube2[0].v[i])))
        
  
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(
            matrix.MultiplyMatrix(
                matrix.ConvertVertexToMatrix(cube2[0].v[i]),
                matrix.RotationMatrix("X",Y)))

        
        cube2[0].v[i] = matrix.ConvertMatrixToVertex(matrix.AddMatrix(TranslationMatrix,matrix.ConvertVertexToMatrix(cube2[0].v[i])))

    Normal = []
    
    NonSortedZ = []
    SortedZ = []
    NonSortedIndex = []
    SortedIndex = []
    for i in range(len(cube2[0].v)):

        SortedZ.append( ((cube2[0].v[i].p[0].Coords[2] +cube2[0].v[i].p[1].Coords[2] + cube2[0].v[i].p[2].Coords[2])/3,i) )
        NonSortedZ.append(SortedZ[i][0])
        NonSortedIndex.append(i)

    SortedZ.sort(key=lambda tup: tup[0],reverse=True)

   
    Cube3 = Mesh.mesh([])
    for e in SortedZ:

        Cube3.v.append(cube2[0].v[e[1]])
    


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
            pass
            Conversions.FillVertex(Conversions.ProjectVertex(cube2[0].v[i]),Conversions.CalculateVertexColor(Normal[i],Light,(255,255,255)))
        #Conversions.DrawVertex(Conversions.ProjectVertex(cube2[0].v[i]),(255,255,255))
    
    Graphics.HandleWindowEvents()




 