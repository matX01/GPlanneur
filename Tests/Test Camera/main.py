import Graphics
import matrix 
import DEBUG
import MatGraph
import math
from Mesh import *
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


forwardVec = vector([1,0,0])
downVec = vector([0,1,0])
P = Point([-3,-3])
Position = Point([1,0])
def ProjectIntoSubReference(xvec,yvec,RefPos,PointToProject):
    
    return Point([PointToProject.p[0] * xvec.v[0]+PointToProject.p[1] * yvec.v[0]+RefPos.p[0],PointToProject.p[0] * xvec.v[1]+PointToProject.p[1] * yvec.v[1]+RefPos.p[1]])

def ProjectIntoMainReference(xvec,yvec,RefPos,PointToProject):
    det = 1/(xvec.v[0]*yvec.v[1]-xvec.v[1]*yvec.v[0])

    return Point([det * (PointToProject.p[0] * yvec.v[1] - yvec.v[0]*PointToProject.p[1]+(yvec.v[0]*RefPos.p[1]-yvec.v[1]*RefPos.p[0])*det),det * (-PointToProject.p[0]*xvec.v[1] + PointToProject.p[1]*xvec.v[0]) + (xvec.v[1]*RefPos.p[0] - xvec.v[0]*RefPos.p[1])*det])


theta = 0
while DEBUG.ISRUNNING:

    Position.p[0] += DEBUG.JoystickAxis[2]/32
    Position.p[1] += DEBUG.JoystickAxis[3]/32

    theta += DEBUG.JoystickAxis[0]/64
    forwardVec = vector([math.cos(theta),math.sin(theta)])
    downVec = vector([-math.sin(theta),math.cos(theta)])

    Q = ProjectIntoSubReference(forwardVec,downVec,Position,P)
    Q2 = ProjectIntoMainReference(forwardVec,downVec,Position,P)
    m = matrix.mat3x3([
        [Position.p[0],Position.p[1],0],
        [Position.p[0]+math.cos(theta+math.pi/12)*10,Position.p[1]+math.sin(theta+math.pi/12)*10,0],
        [Position.p[0]-math.sin(theta-math.pi/12)*10,Position.p[1]+math.cos(theta-math.pi/12)*10,0]

    ])
    #print(Q)
    
    
    PointAt = vector([(Q2.p[0]) , (Q2.p[1])])


    

    Graphics.DrawTriangle(m,(50,50,50),0)
    Graphics.drawVector(Position,vector([forwardVec.v[0]*10,forwardVec.v[1]*10]),(0,0,255),(255,0,0),"forward")
    Graphics.drawVector(Position,vector([downVec.v[0]*10,downVec.v[1]*10]),(0,255,0),(0,0,255),"down")
    Graphics.drawAxis()
    #Graphics.drawPoint(Q2,(255,255,255),"Normalized Q2")
    #Graphics.drawPoint(Q,(255,255,255),"Q")
    
    if((PointAt.v[0]*0.26 < PointAt.v[1]) and (PointAt.v[1]*0.26< PointAt.v[0])):
        #Graphics.drawPoint(Q2,(255,255,255),"Q'")
        Graphics.drawPoint(P,(255,255,255),"P")
    #Graphics.DrawTriangle(m,(255,255,255),1)
    

    
    DEBUG.HandleWindowEvents()