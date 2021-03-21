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

def rotateVertex(vertex,point,Angle):
    
    Point1Module = math.sqrt((vertex.p[0].Coords[0]-point.Coords[0])**2+(vertex.p[0].Coords[1]-point.Coords[1])**2)
    Point2Module = math.sqrt((vertex.p[1].Coords[0]-point.Coords[0])**2+(vertex.p[1].Coords[1]-point.Coords[1])**2)
    Point3Module = math.sqrt((vertex.p[2].Coords[0]-point.Coords[0])**2+(vertex.p[2].Coords[1]-point.Coords[1])**2)
    Point1BaseArg = 0
    Point2BaseArg = 0
    Point3BaseArg = 0
    try:
        Point1BaseArg = math.acos((vertex.p[0].Coords[0]-point.Coords[0])/Point1Module)
    except:
        pass
    try:
        Point2BaseArg = math.acos((vertex.p[1].Coords[0]-point.Coords[0])/Point2Module)
    except:
        pass
    try:
        Point3BaseArg = math.acos((vertex.p[2].Coords[0]-point.Coords[0])/Point3Module)
    except:
        pass
    return Mesh.Vertex([
    
        Mesh.Point([Point1Module*math.cos(Point1BaseArg+Angle),Point1Module*math.sin(Point1BaseArg+Angle),vertex.p[0].Coords[2]]),
        Mesh.Point([Point2Module*math.cos(Point2BaseArg+Angle),Point2Module*math.sin(Point2BaseArg+Angle),vertex.p[1].Coords[2]]),
        Mesh.Point([Point3Module*math.cos(Point3BaseArg+Angle),Point3Module*math.sin(Point3BaseArg+Angle),vertex.p[2].Coords[2]])
    
    ])


TranslationMatrix = matrix.mat3x3([
    [0,0,5],
    [0,0,5],
    [0,0,5]

])

TranslationMatrix2 = matrix.mat3x3([
    [-0.5,-0.5,-1.5],
    [-0.5,-0.5,-1.5],
    [-0.5,-0.5,-1.5]

])


Cam = matrix.vector([0,0,0])
Light = matrix.vector([0,-0,-1])
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
        Normal[len(Normal)-1].v[2] *=size
    #Graphics.PrintFPS()

 
  
    #print(theta)
    theta += math.pi/512

    for i in range(len(cube2[0].v)):
        ProjectedCam = matrix.vector([
            cube2[0].v[i].p[0].Coords[0] - Cam.v[0],
            cube2[0].v[i].p[0].Coords[1] - Cam.v[1],
            cube2[0].v[i].p[0].Coords[2] - Cam.v[2]

        ])

        if(matrix.DotProduct(ProjectedCam,Normal[i]) < 0):
            
            #Conversions.DrawVertex(Conversions.ProjectVertex(cube2[0].v[i]),(255,0,0))
            Conversions.FillVertex(Conversions.ProjectVertex(cube2[0].v[i]),Conversions.CalculateVertexColor(cube2[0].v[i],Normal[i],Light,(255,255,255)))
    
    
   


    Graphics.HandleWindowEvents()


