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
P = Point([3,3])

def ProjectIntoSubReference(xvec,yvec,PointToProject):
    return Point([PointToProject.p[0] * xvec.v[0]+PointToProject.p[1] * yvec.v[0],PointToProject.p[0] * xvec.v[1]+PointToProject.p[1] * yvec.v[1]])


theta = 0
while DEBUG.ISRUNNING:
    theta += math.pi/512
    forwardVec = vector([2*math.cos(theta),math.sin(theta)])
    downVec = vector([-math.sin(theta),math.cos(theta)])

    Q = ProjectIntoSubReference(forwardVec,downVec,P)
    print(Q)
    
    Graphics.drawAxis()




    Graphics.drawVector(Point([0,0]),forwardVec,(0,0,255),(255,0,0),"forward")
    Graphics.drawVector(Point([0,0]),downVec,(0,255,0),(0,0,255),"down")
    Graphics.drawPoint(P,(255,255,255),"P")
    Graphics.drawPoint(Q,(255,255,255),"Q")
    #Graphics.DrawTriangle(m,(255,255,255),1)
    

    
    DEBUG.HandleWindowEvents()