from Mesh.Mesh import *
import DisplayHandling.Graphics as Graphics
import DisplayHandling.MatGraph as MatGraph
import math
import copy
import matrix
import pygame
import threading
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
    
    #Normal = CalculateNormals(Msh)
    #global Normal

    for i in range(len(Msh)):

        M2 = matrix.mat3x3([[0,0,0],[0,0,0],[0,0,0]])
        #print("\n\n\n",Msh)
        """
        M2.m[0][0] = -1 * Msh[i].m[0][2]
        M2.m[0][1] = 1 * Msh[i].m[0][1]
        M2.m[0][2] = 1 * Msh[i].m[0][0]
 
        M2.m[1][0] =  -1 * Msh[i].m[1][2]
        M2.m[1][1] =  1 * Msh[i].m[1][1]
        M2.m[1][2] =  1 * Msh[i].m[1][0]   

        M2.m[2][0] =  -1 * Msh[i].m[2][2]
        M2.m[2][1] =  1 * Msh[i].m[2][1]
        M2.m[2][2] =  1 * Msh[i].m[2][0]
        """
        #print(matView)

    
        #print(M2.m)
        
        
        M2.m[0][0] =  matView.m[0][0] * Msh[i].m[0][0] + matView.m[1][0] * Msh[i].m[0][1] + matView.m[2][0] * Msh[i].m[0][2] + matView.m[3][0]
        M2.m[0][1] =  matView.m[0][1] * Msh[i].m[0][0] + matView.m[1][1] * Msh[i].m[0][1] + matView.m[2][1] * Msh[i].m[0][2] + matView.m[3][1]
        M2.m[0][2] =  matView.m[0][2] * Msh[i].m[0][0] + matView.m[1][2] * Msh[i].m[0][1] + matView.m[2][2] * Msh[i].m[0][2] + matView.m[3][2]
            
        M2.m[1][0] =  matView.m[0][0] * Msh[i].m[1][0] + matView.m[1][0] * Msh[i].m[1][1] + matView.m[2][0] * Msh[i].m[1][2] + matView.m[3][0]
        M2.m[1][1] =  matView.m[0][1] * Msh[i].m[1][0] + matView.m[1][1] * Msh[i].m[1][1] + matView.m[2][1] * Msh[i].m[1][2] + matView.m[3][1]
        M2.m[1][2] =  matView.m[0][2] * Msh[i].m[1][0] + matView.m[1][2] * Msh[i].m[1][1] + matView.m[2][2] * Msh[i].m[1][2] + matView.m[3][2]

        M2.m[2][0] =  matView.m[0][0] * Msh[i].m[2][0] + matView.m[1][0] * Msh[i].m[2][1] + matView.m[2][0] * Msh[i].m[2][2] + matView.m[3][0]
        M2.m[2][1] =  matView.m[0][1] * Msh[i].m[2][0] + matView.m[1][1] * Msh[i].m[2][1] + matView.m[2][1] * Msh[i].m[2][2] + matView.m[3][1]
        M2.m[2][2] =  matView.m[0][2] * Msh[i].m[2][0] + matView.m[1][2] * Msh[i].m[2][1] + matView.m[2][2] * Msh[i].m[2][2] + matView.m[3][2]
        
        #print("after: ",Msh[i])
        ProjectedCam = vector([
            M2.m[0][0] - Camera.v[0],
            M2.m[0][1] - Camera.v[1],
            M2.m[0][2] - Camera.v[2]

        ])
        
        


        
        if(M2.m[0][0] <  1.24 *  (M2.m[0][2]) and M2.m[1][0] <  1.24 *  (M2.m[1][2]) and M2.m[2][0] <  1.24 *  (M2.m[2][2]) 
        and M2.m[0][0] > - 1.24 *  (M2.m[0][2]) and M2.m[1][0] > - 1.24 *  (M2.m[1][2]) and M2.m[2][0] > - 1.24 *  (M2.m[2][2]) 
        and M2.m[0][1] <  0.7 *  (M2.m[0][2]) and M2.m[1][1] <  0.7 *  (M2.m[1][2]) and M2.m[2][1] <  0.7 *  (M2.m[2][2])
        and M2.m[0][1] > - 0.7 *  (M2.m[0][2]) and M2.m[1][1] > - 0.7 *  (M2.m[1][2]) and M2.m[2][1] > - 0.7 *  (M2.m[2][2])  ) :
        
     
        #print(M2[i])
            #if(MatGraph.DotProduct(ProjectedCam,Normal[i]) <= 0):
         
            #Graphics.DrawTriangle(MatGraph.ProjectTriangle(M2[i]),MatGraph.CalculateTriangleColor(Normal[i],LightSource,color),0)
        
        
        #if(M2.m[0][2] >= 0.7 and M2.m[1][2] >= 0.7 and M2.m[2][2] >= 0.7):
            Graphics.DrawTriangle(MatGraph.ProjectTriangle(M2),(0,0,0),1)
            #Graphics.DrawTriangle(M2[i],color,0)

        """
        else :
            tri = MatGraph.ProjectTriangle(Msh[i])
            
            Graphics.drawPoint(tri.m[0],(255,255,255))
            Graphics.drawPoint(tri.m[1],(255,255,255))
            Graphics.drawPoint(tri.m[2],(255,255,255))
        """




Light = vector([0,-0.7,-0.7])

TranslationMatrix = matrix.mat3x3([
        [0,3,15],
        [0,3,15],
        [0,3,15]

])


def PointAt(pos,target,up):
    
    #print(target," ",pos)
    NewForward = target-pos

   
    
    size = math.sqrt(NewForward.v[0]**2+NewForward.v[1]**2+NewForward.v[2]**2)
    NewForward.v[0] /= size
    NewForward.v[1] /= size
    NewForward.v[2] /= size
    #print(NewForward.v)
    
    
    a = NewForward * MatGraph.DotProduct(up,NewForward)
    NewUp = up - a
    
    size2 = math.sqrt(NewUp.v[0]**2+NewUp.v[1]**2+NewUp.v[2]**2)
    NewUp.v[0] /= size2
    NewUp.v[1] /= size2
    NewUp.v[2] /= size2


    newRight = MatGraph.CrossProduct(NewUp , NewForward)

    #print(newRight.v)
    return matrix.mat4x4([
        [newRight.v[0],newRight.v[1],newRight.v[2],0],
        [NewUp.v[0],NewUp.v[1],NewUp.v[2],0],
        [NewForward.v[0],NewForward.v[1],NewForward.v[2],0],
        [pos.v[0],pos.v[1],pos.v[2],1]
    ])

def LookAtMatrix(m):
    return matrix.mat4x4([

        [m.m[0][0],m.m[1][0],m.m[2][0],0],
        [m.m[0][1],m.m[1][1],m.m[2][1],0],
        [m.m[0][2],m.m[1][2],m.m[2][2],0],
        [-(m.m[3][0]*m.m[0][0] + m.m[3][1] * m.m[0][1] + m.m[3][2] * m.m[0][2]),
         -(m.m[3][0]*m.m[1][0] + m.m[3][1] * m.m[1][1] + m.m[3][2] * m.m[1][2]),
         -(m.m[3][0]*m.m[2][0] + m.m[3][1] * m.m[2][1] + m.m[3][2] * m.m[2][2]),
         1]

    ])




#if __name__ == "__main__":
def main():   
    import DEBUG
    global Cam
    global Light
    
    

    #t = threading.Thread(target = ui)
    #t.start()






    sol = []
    
    Step = 2
    Size = 30
    for i in range(-Size,Size,Step):
        for j in range(-Size,Size,Step):
            sq1 = matrix.mat3x3([
                [i,j,3],
                [i,j+Step,3],
                [i+Step,j,3]
            ])
            """
            sq2 = matrix.mat3x3([
                [i,j+Step,1],
                [i+Step,j+Step,1],
                [i+Step,j,1]
            ])
            """
            sol.append(sq1)
            #sol.append(sq2)
    
    MatGraph.MultiplyMeshAndMatrix(sol,matrix.RotationMatrix("X",math.pi/2))
   

    global TranslationMatrix
    
    DEBUG.init()
    Graphics.initDisplayHandler(DEBUG.window,DEBUG.ScreenSize,100,15*math.pi/180)
    DEBUG.HandleWindowEvents()
    theta = 0
    phi = 0
    vtheta = 0
    Test2 = Load3DElement("Tests/Graphipsa3D/MeshFiles/GAMIIIING.obj")
    
            
    #MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("Y",theta))
    #MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("X",math.pi/6))
    #MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("Z",math.pi/6))

    
    
    #Test2 = Load3DElement("Tests/Graphipsa3D/MeshFiles/teapot.obj")

    
    
    Cam = vector([0,0,0])
    vUp = vector([0,1,0])
    vLookDir = vector([0,0,1])
    vTarget = vector([0,0,1])

    #print(pygame.display.Info())
    Step = 2
    Size = 60
    offset = 0
    LastCamPos = 0
    miniOffset = 0
    while DEBUG.ISRUNNING:

        #thetaa += math.pi/512
        
        #Cam.v[2] -= DEBUG.JoystickAxis[3]/16
        
    
        
        
        
        
     
        phi += DEBUG.JoystickAxis[1]/32

        vForward = vector([(-vLookDir.v[0])*DEBUG.JoystickAxis[3]/1,(-vLookDir.v[1])*DEBUG.JoystickAxis[3]/1,(-vLookDir.v[2])*DEBUG.JoystickAxis[3]/1])



        
        Cam += vForward
        
        #print(Cam)
        #vTarget = ([0,0,1])
        vLookDir = vector([0,math.sin(phi),math.cos(phi)])
        #vLookDir = vector([-math.sin(theta),0,math.cos(theta)])
        #vLookDir = vector([1,0,0])
        
        vTarget = Cam + vLookDir
        
        subMat = PointAt(Cam,vTarget,vUp)
    
        mtView = LookAtMatrix(subMat)
        
           


        #print(vTarget)
        sol = []

        #print(offset)
        
        if Cam.v[2] > Size+offset-60:
            
            offset = int(Cam.v[2])
            miniOffset = Cam.v[2] - offset
       



        for i in range(-30,30,Step):
            for j in range(offset,Size+offset,Step):
            
                sq1 = matrix.mat3x3([
                    [i,6,j-miniOffset],
                    [i+Step,6,j-miniOffset],
                    [i,6,j+Step-miniOffset]
                ])

                sol.append(sq1)
        


       
        #Tst2 = sol.copy()
        #MatGraph.MultiplyMeshAndMatrix(Tst2,matrix.RotationMatrix("X",math.pi/2))
        #MatGraph.AddMeshAndMatrix(Tst2,matrix.mat3x3([[0,3,0],[0,3,0],[0,3,0]]))
        #MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("Y",-thetaa))
        #MatGraph.AddMeshAndMatrix(Test,TranslationMatrix)
        #MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("X",thetaa))

        #MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("X",math.pi/6))
        #MatGraph.MultiplyMeshAndMatrix(Test,matrix.RotationMatrix("Z",math.pi/6))

       
        
        #FillMesh(Test,(255,255,255),Cam,Light,matView)
        #FillMesh(Tst2,(0,255,0),Cam,Light,matView)
        
        FillMesh(sol,(255,255,255),Cam,Light,mtView)
        
        #DrawMesh(Test,(255,255,255))




        DEBUG.HandleWindowEvents()

    DEBUG.quit()


if __name__ == "__main__":
    main()