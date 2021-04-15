from Mesh.Mesh import *
import DisplayHandling.Graphics as Graphics
import DisplayHandling.MatGraph as MatGraph
import math
import copy
import matrix
from ctypes import c_float, c_int32, cast, byref, POINTER
import numpy as np
import pygame
def DrawMesh(M,color):
    
    for i in range(len(M)):

        Graphics.DrawTriangle(M[i],color,1)


def CalculateNormals(Msh):
    Normal = [0 for i in range(len(Msh))]
    for i in range(len(Msh)):
    #for M[i] in M:
        Normal[i] = MatGraph.CrossProduct(

            vector([Msh[i].m[1][0]-Msh[i].m[0][0],
            Msh[i].m[1][1]-Msh[i].m[0][1],
            Msh[i].m[1][2]-Msh[i].m[0][2]]),

            vector([Msh[i].m[2][0]-Msh[i].m[0][0],
            Msh[i].m[2][1]-Msh[i].m[0][1],
            Msh[i].m[2][2]-Msh[i].m[0][2]])
            )
        #print((Normal[len(Normal)-1].v[0])**2 + (Normal[len(Normal)-1].v[1])**2 + (Normal[len(Normal)-1].v[2])**2)
        try:
            size = ((Normal[i].v[0])**2 + (Normal[i].v[1])**2 + (Normal[i].v[2])**2)**-0.5
            Normal[i].v[0] *= size
            Normal[i].v[1] *= size
            Normal[i].v[2] *= size
        except:
            pass
    
    return Normal

def PaintingAlgorithm(M):
    NonSortedZ = [0 for i in range(len(M))]
    SortedZ = [0 for i in range(len(M))]
    NonSortedIndex = [i for i in range(len(M))]
    SortedIndex = [0 for i in range(len(M))]
    Msh = []

    for i in range(len(M)):

        NonSortedZ[i] = SortedZ[i] = ((M[i].m[0][2] +M[i].m[1][2] +M[i].m[2][2])/3)
        
   

    SortedZ.sort(reverse=True)
    #print(NonSortedIndex)
    for i in range(len(SortedZ)):
        
        SortedIndex[i] = NonSortedZ.index(SortedZ[i])
    
    #print(SortedIndex)

    
    for e in SortedIndex:

        Msh.append(M[e])
    

    
    return Msh

def FillMesh(M,color,Camera,LightSource):
    """
    NonSortedZ = [0 for i in range(len(M))]
    SortedZ = [0 for i in range(len(M))]
    NonSortedIndex = [i for i in range(len(M))]
    SortedIndex = [0 for i in range(len(M))]
    Msh = []

    for i in range(len(M)):

        NonSortedZ[i] = SortedZ[i] = ((M[i].m[0][2] +M[i].m[1][2] +M[i].m[2][2])/3)
        
   

    SortedZ.sort(reverse=True)
    #print(NonSortedIndex)
    for i in range(len(SortedZ)):
        
        SortedIndex[i] = NonSortedZ.index(SortedZ[i])
    
    #print(SortedIndex)

    
    for e in SortedIndex:

        Msh.append(M[e])
    
    """
    Msh = PaintingAlgorithm(M)
    
    Normal = CalculateNormals(Msh)
    #global Normal
    """
    for i in range(len(Msh)):
    #for M[i] in M:
        Normal[i] = MatGraph.CrossProduct(

            vector([Msh[i].m[1][0]-Msh[i].m[0][0],
            Msh[i].m[1][1]-Msh[i].m[0][1],
            Msh[i].m[1][2]-Msh[i].m[0][2]]),

            vector([Msh[i].m[2][0]-Msh[i].m[0][0],
            Msh[i].m[2][1]-Msh[i].m[0][1],
            Msh[i].m[2][2]-Msh[i].m[0][2]])
            )
        #print((Normal[len(Normal)-1].v[0])**2 + (Normal[len(Normal)-1].v[1])**2 + (Normal[len(Normal)-1].v[2])**2)
        try:
            size = ((Normal[i].v[0])**2 + (Normal[i].v[1])**2 + (Normal[i].v[2])**2)**-0.5
            Normal[i].v[0] *= size
            Normal[i].v[1] *= size
            Normal[i].v[2] *= size
        except:
            pass
    

    """

    for i in range(len(Msh)):
        ProjectedCam = vector([
            Msh[i].m[0][0] - Cam.v[0],
            Msh[i].m[0][1] - Cam.v[1],
            Msh[i].m[0][2] - Cam.v[2]

        ])
        if(MatGraph.DotProduct(ProjectedCam,Normal[i]) < 0):

            Graphics.DrawTriangle(MatGraph.ProjectTriangle(Msh[i]),MatGraph.CalculateTriangleColor(Normal[i],Light,color),0)
            #Graphics.DrawTriangle(M[i],MatGraph.CalculateTriangleColor(Normal[i],Light,color),0)
    


Cam = vector([0,0,0])
Light = vector([0,-0,-1])
TranslationMatrix = matrix.mat3x3([
        [0,0,6],
        [0,0,6],
        [0,0,6]

])
#if __name__ == "__main__":
def main():   
    import DEBUG
    global Cam
    global Light
    global TranslationMatrix



    

    
    DEBUG.init()
    Graphics.initDisplayHandler(DEBUG.window,DEBUG.ScreenSize,100,70*math.pi/360)
    theta = math.pi/6
    Test2 = Load3DElement("Gplanneur/Tests/Test 3D/3D rotations/GAMIIIING.obj")
    """
    MatGraph.MultiplyMeshAndMatrix(Test2,matrix.RotationMatrix("X",theta))
    MatGraph.MultiplyMeshAndMatrix(Test2,matrix.RotationMatrix("Y",theta))
    MatGraph.MultiplyMeshAndMatrix(Test2,matrix.RotationMatrix("Z",theta))
    MatGraph.AddMeshAndMatrix(Test2,TranslationMatrix)
    """        
    print(pygame.display.Info())
    while DEBUG.ISRUNNING:
        
        
        theta += math.pi/256

        Test = Test2.copy()
     
        
        MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("X",theta))
        MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("Y",theta))
        MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("Z",theta))

        MatGraph.AddMeshAndMatrix(Test,TranslationMatrix)
    
        
        FillMesh(Test,(255,255,255),Cam,Light)

  
        #DrawMesh(Test2,(255,255,255))




        DEBUG.HandleWindowEvents()

    DEBUG.quit()

if __name__ == "__main__":
    main()