import Graphics
import matrix 
import DEBUG
import MatGraph
import math
from Mesh import *
import random
DEBUG.init()
Graphics.initDisplayHandler(DEBUG.window,(1920,1080),100,70*math.pi/180)


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

class Point:
    p = []
    def __init__(self,p):
        self.p = p
    def __add__(self,p):
        return Point([self.p[0]+p.p[0],self.p[1]+p.p[1]])
    def __str__(self):
        returnValue = "[ "
        for El in self.p:
            returnValue += str(El) + " "
        return returnValue + "]"
       


m = matrix.mat3x3([
    [1,1,0],
    [1,2,0],
    [2,1,0]
])



def ProjectIntoSubReference(xvec,yvec,RefPos,PointToProject):
    
    return Point([PointToProject.p[0] * xvec.v[0]+PointToProject.p[1] * yvec.v[0]+RefPos.p[0],PointToProject.p[0] * xvec.v[1]+PointToProject.p[1] * yvec.v[1]+RefPos.p[1]])

def ProjectIntoMainReference(xvec,yvec,RefPos,PointToProject):
    det = 1/(xvec.v[0]*yvec.v[1]-xvec.v[1]*yvec.v[0])

    return Point([det * (PointToProject.p[0] * yvec.v[1] - yvec.v[0]*PointToProject.p[1]+(yvec.v[0]*RefPos.p[1]-yvec.v[1]*RefPos.p[0])*det),det * (-PointToProject.p[0]*xvec.v[1] + PointToProject.p[1]*xvec.v[0]) + (xvec.v[1]*RefPos.p[0] - xvec.v[0]*RefPos.p[1])*det])




P = Point([5,3])
CameraPosition = Point([0,0])
LookingVector = vector([1,0])
DownVec = vector([0,1])

theta = 0

CLOUDY = []

for i in range (50):
    CLOUDY.append(Point([random.randint(-10,10),random.randint(-10,10)]))

def actualiseCameraPosition():
    global CameraPosition
    global LookingVector
    global theta
    global DownVec

    theta += DEBUG.JoystickAxis[2]/32
    LookingVector = vector([math.cos(theta),math.sin(theta)])
    DownVec = vector([-math.sin(theta),math.cos(theta)])

while DEBUG.ISRUNNING:

    CameraVector = vector([CameraPosition.p[0],CameraPosition.p[1]]) + LookingVector


    
    NewForwardVec = LookingVector

    CameraPosition += Point([DownVec.v[0]*DEBUG.JoystickAxis[1]/8,DownVec.v[1]*DEBUG.JoystickAxis[1]/8])
    CameraPosition += Point([LookingVector.v[0]*DEBUG.JoystickAxis[0]/8,LookingVector.v[1]*DEBUG.JoystickAxis[0]/8])
    
    CLOUDYProjected = []

    for El in CLOUDY:
        bt = ProjectIntoMainReference(NewForwardVec,DownVec,CameraPosition,El)
        CLOUDYProjected.append(bt)
    
    

    Q = ProjectIntoSubReference(CameraVector,DownVec,CameraPosition,P)
    Q2 = ProjectIntoMainReference(CameraVector,DownVec,CameraPosition,Q)

    for i in range(len(CLOUDYProjected)):
        Graphics.drawPoint(CLOUDYProjected[i],(255,255,255),("Q"+str(i)))

    

    Graphics.drawVector(Point([0,0]),NewForwardVec,(255,0,0),(0,255,255),"Cam")
    Graphics.drawVector(Point([0,0]),DownVec,(255,0,0),(0,255,255),"DOWN")
    Graphics.drawAxis()
    #Graphics.drawPoint(P,(255,255,255),"P")
    
    
    
    
    
    actualiseCameraPosition()
    DEBUG.HandleWindowEvents()