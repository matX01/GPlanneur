from Mesh.Mesh import *
import DisplayHandling.Graphics as Graphics
import DisplayHandling.MatGraph as MatGraph
import math
import copy
import matrix
import pygame
def DrawMesh(M,color):
    
    for i in range(len(M)):

        Graphics.DrawTriangle(MatGraph.ProjectTriangle(M[i]),color,1)


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




def FillMesh(M,color,Camera,LightSource,matView):

    #Msh = PaintingAlgorithm(M)
    Msh = M
    
    Normal = CalculateNormals(Msh)
    #global Normal


    for i in range(len(Msh)):
        ProjectedCam = vector([
            Msh[i].m[0][0] - Cam.v[0],
            Msh[i].m[0][1] - Cam.v[1],
            Msh[i].m[0][2] - Cam.v[2]

        ])
        for j in range(3):

            Msh[i].m[j][0] =  matView.m[0][0] * Msh[i].m[j][0] + matView.m[1][0] * Msh[i].m[j][1] + matView.m[2][0] * Msh[i].m[j][2] 
            Msh[i].m[j][1] =  matView.m[0][1] * Msh[i].m[j][0] + matView.m[1][1] * Msh[i].m[j][1] + matView.m[2][1] * Msh[i].m[j][2] 
            Msh[i].m[j][2] =  matView.m[0][2] * Msh[i].m[j][0] + matView.m[1][2] * Msh[i].m[j][1] + matView.m[2][2] * Msh[i].m[j][2] 

        if(MatGraph.DotProduct(ProjectedCam,Normal[i]) <= 0):

            Graphics.DrawTriangle(MatGraph.ProjectTriangle(Msh[i]),MatGraph.CalculateTriangleColor(Normal[i],LightSource,color),0)
            #Graphics.DrawTriangle(M[i],MatGraph.CalculateTriangleColor(Normal[i],Light,color),0)
    







Light = vector([0,0,-1])

TranslationMatrix = matrix.mat3x3([
        [0,0,20],
        [0,0,20],
        [0,0,20]

])


def PointAt(pos,target,up):
    
    
    NewForward = target-pos
    #print(NewForward.v)
    try:
        size = math.sqrt(NewForward.v[0]**2+NewForward.v[0]**2+NewForward.v[0]**2)
        NewForward.v[0] /= size
        NewForward.v[1] /= size
        NewForward.v[2] /= size
    except:
        pass

    
    
    a = NewForward * MatGraph.DotProduct(up,NewForward)
    NewUp = up - a


    newRight = MatGraph.CrossProduct(NewUp , NewForward)

    return matrix.mat4x4([
        [newRight.v[0],newRight.v[1],newRight.v[2],0],
        [NewUp.v[0],NewUp.v[1],NewUp.v[2],0],
        [NewForward.v[0],NewForward.v[1],NewForward.v[2],0],
        [pos.v[0],pos.v[1],pos.v[2],1]
    ])

def LookatMatrix(m):
   
    return matrix.mat4x4([
        [m.m[0][0],m.m[1][0],m.m[2][0],0],
        [m.m[0][1],m.m[1][1],m.m[2][1],0],
        [m.m[0][2],m.m[1][2],m.m[2][2],0],
        [-(m.m[3][0]*m.m[0][0] + m.m[3][1] * m.m[0][1] + m.m[3][2] * m.m[0][2]),
         -(m.m[3][0]*m.m[1][0] + m.m[3][1] * m.m[1][1] + m.m[3][2] * m.m[1][2]),
         -(m.m[3][0]*m.m[2][0] + m.m[3][1] * m.m[2][1] + m.m[3][2] * m.m[2][2])]
    ])



#if __name__ == "__main__":
def main():   
    import DEBUG
    global Cam
    global Light
    global Light2
    global TranslationMatrix
    
    DEBUG.init()
    Graphics.initDisplayHandler(DEBUG.window,DEBUG.ScreenSize,100,60*math.pi/360)
    DEBUG.HandleWindowEvents()
    theta = math.pi/6
    vtheta = 0
    Test2 = Load3DElement("Tests/Graphipsa3D/MeshFiles/axis.obj")
    #Test2 = Load3DElement("Tests/Graphipsa3D/MeshFiles/teapot.obj")
    #MatGraph.MultiplyMeshAndMatrix(Test2,matrix.RotationMatrix("X",theta))
    #MatGraph.MultiplyMeshAndMatrix(Test2,matrix.RotationMatrix("Y",theta))
    #MatGraph.MultiplyMeshAndMatrix(Test2,matrix.RotationMatrix("Z",theta))
    print(len(Test2))
    
    
    Cam = vector([0,0,1])
    vUp = vector([0,1,0])
    #print(pygame.display.Info())
    while DEBUG.ISRUNNING:

    
        vLookDir = vector([0,0,1])
        
        vTarget = Cam + vLookDir
        
        Cam.v[0] += DEBUG.JoystickAxis[0]/64
        Cam.v[1] += DEBUG.JoystickAxis[1]/64
        Cam.v[2] += DEBUG.JoystickAxis[2]/64
        matView = PointAt(vTarget,vLookDir,vUp)

        
        Test = Test2.copy()

        for i in range(len(Test)):
            for j in range(3):

                Test[i].m[j][0] =  matView.m[0][0] * Test[i].m[j][0] + matView.m[1][0] * Test[i].m[j][1] + matView.m[2][0] * Test[i].m[j][2] 
                Test[i].m[j][1] =  matView.m[0][1] * Test[i].m[j][0] + matView.m[1][1] * Test[i].m[j][1] + matView.m[2][1] * Test[i].m[j][2] 
                Test[i].m[j][2] =  matView.m[0][2] * Test[i].m[j][0] + matView.m[1][2] * Test[i].m[j][1] + matView.m[2][2] * Test[i].m[j][2] 


        MatGraph.AddMeshAndMatrix(Test,TranslationMatrix)

        #FillMesh(Test,(255,255,255),Cam,Light,matView)
        
  
        DrawMesh(Test,(255,255,255))




        DEBUG.HandleWindowEvents()

    DEBUG.quit()

if __name__ == "__main__":
    main()