import pygame
import math
import copy
import time
from dataclasses import dataclass


from typing import List
import Autre as WHandler
import time
import random


# définissons les structures de données nous permettant de stocker le maillage a l'origine de toutes les formes.

ScrMeshSize = 100

ScrTranslationConstant = [WHandler.ScreenSize[0]/2,WHandler.ScreenSize[1]/2]


AspectRatio = WHandler.ScreenSize[0]/WHandler.ScreenSize[1]

theta = 30*math.pi/180
fovConverter = 1/math.tan(theta/2)


@dataclass
class Point:                                                                    # Le point , constitué de 3 valeurs x , y , z
    Coords: List[float]
    
@dataclass
class Vertex:                                                                   # le vertex , un triangle sans volume constitué de trois points
    p: List[Point]
    
@dataclass
class mesh:                                                                     # le mesh , un ensemble de vertex permettant de former un polygone en 3 dimensions.
    v: List[Vertex]
    



cube = mesh([
    #South
    Vertex([
        Point([0,0,0]),
        Point([0,1,0]),
        Point([1,1,0])
    ]),
    Vertex([
        Point([0,0,0]),
        Point([1,1,0]),
        Point([1,0,0])
    ]),
    
    #east
    Vertex([
        Point([1,0,0]),
        Point([1,1,0]),
        Point([1,1,1])
    ]),
    Vertex([
        Point([1,0,0]),
        Point([1,1,1]),
        Point([1,0,1])
    ]),
    
    #north
    Vertex([
        Point([1,0,1]),
        Point([1,1,1]),
        Point([0,0,1])
    ]),
    Vertex([
        Point([1,0,1]),
        Point([0,1,1]),
        Point([0,0,1])
    ]),
    
    #west
    Vertex([
        Point([0,0,1]),
        Point([0,1,1]),
        Point([0,1,0])
    ]),
    Vertex([
        Point([0,0,1]),
        Point([0,1,0]),
        Point([0,0,0])
    ]),
    
    #top
    Vertex([
        Point([0,1,0]),
        Point([0,1,1]),
        Point([1,1,1])
    ]),
    Vertex([
        Point([0,1,0]),
        Point([1,1,1]),
        Point([1,1,0])
    ]),
    
    #bottom
    Vertex([
        Point([1,0,1]),
        Point([0,0,1]),
        Point([0,0,0])
    ]),
    Vertex([
        Point([1,0,1]),
        Point([0,0,0]),
        Point([1,0,0])
    ])
])

testFloor = mesh([])




Ymove = 5
oldTime = 0

deplacementX = 0.0
deplacementY = -0.0
deplacementZ = 0.0

for z in range(1,10):
    step = 1
    size = 1

        
    for x in range(-30,30,step):
        

        
        V = Vertex([
                Point([x,Ymove,z]),
                Point([x,Ymove,z+1]),
                Point([x+size,Ymove,z])
            ])
        Vtwo = Vertex([
                Point([x+size,Ymove,z]),
                Point([x,Ymove,z+1]),
                Point([x+size,Ymove,z+1])
    
            ])
        
        
        
        testFloor.v.append(V)
        testFloor.v.append(Vtwo)
    
for z in range(10,25,2):
    step = 2
    size = 2

        
    for x in range(-30,30,step):
        
        V = Vertex([
                Point([x,Ymove,z]),
                Point([x,Ymove,z+2]),
                Point([x+size,Ymove,z])
            ])
        Vtwo = Vertex([
                Point([x+size,Ymove,z]),
                Point([x,Ymove,z+2]),
                Point([x+size,Ymove,z+2])
    
            ])
        
        
        
        testFloor.v.append(V)
        testFloor.v.append(Vtwo)
        
for z in range(25,50,5):
    step = 5
    size = 5

        
    for x in range(-30,30,step):
        
        V = Vertex([
                Point([x,Ymove,z]),
                Point([x,Ymove,z+size]),
                Point([x+size,Ymove,z])
            ])
        Vtwo = Vertex([
                Point([x+size,Ymove,z]),
                Point([x,Ymove,z+size]),
                Point([x+size,Ymove,z+size])
    
            ])
        
        
        
        testFloor.v.append(V)
        testFloor.v.append(Vtwo)
        
print(len(testFloor.v))


for vertex in cube.v:
    for points in vertex.p:
        for i in points.Coords:
            i *= 100

def ProjectVertex(v):
    #a = v.p[0].Coords[2]*ZConverterCoef-ZConverterResizer
    #b = v.p[1].Coords[2]*ZConverterCoef-ZConverterResizer
    #c = v.p[2].Coords[2]*ZConverterCoef-ZConverterResizer
    a = v.p[0].Coords[2]
    b = v.p[1].Coords[2]
    c = v.p[2].Coords[2]
    return Vertex([
    Point([(v.p[0].Coords[0]*fovConverter)/a,(v.p[0].Coords[1]*fovConverter)/a,a]),
    Point([(v.p[1].Coords[0]*fovConverter)/b,(v.p[1].Coords[1]*fovConverter)/b,b]),
    Point([(v.p[2].Coords[0]*fovConverter)/c,(v.p[2].Coords[1]*fovConverter)/c,c]),
    ])
    
def DrawVertex(v,color):
    
    pygame.draw.line(WHandler.window,color,(v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),(v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))
    pygame.draw.line(WHandler.window,color,(v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),(v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))
    pygame.draw.line(WHandler.window,color,(v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),(v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))



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




    return Vertex([
    
        Point([Point1Module*math.cos(Point1BaseArg+Angle),Point1Module*math.sin(Point1BaseArg+Angle),vertex.p[0].Coords[2]]),
        Point([Point2Module*math.cos(Point2BaseArg+Angle),Point2Module*math.sin(Point2BaseArg+Angle),vertex.p[1].Coords[2]]),
        Point([Point3Module*math.cos(Point3BaseArg+Angle),Point3Module*math.sin(Point3BaseArg+Angle),vertex.p[2].Coords[2]])
    
    ])





for vertex in cube.v:
        for points in vertex.p:
            points.Coords[2] += 5
            points.Coords[0] -= 5
            points.Coords[1] +=0
    

cube2 = copy.deepcopy([cube])

theta = 0
spd = 5
ui = True
while WHandler.ProgramRunning:
    WHandler.HandleWindowEvents()
 
    print(1/(time.time()-oldTime))
    oldTime = time.time()


    
    WHandler.window.fill(0)
    """
    for vertex in cube2[0].v:
        for points in vertex.p:
            points.Coords[0] += deplacementX
            points.Coords[1] += deplacementY
            points.Coords[2] += deplacementZ
            #print(points.Coords[2])

    if((cube.v[0].p[0].Coords[0] >=30) or (cube.v[0].p[0].Coords[0] <= -30)):
        deplacementX = -deplacementX
    if((cube.v[0].p[0].Coords[1] >= Ymove) or (cube.v[0].p[0].Coords[1] <= -10)):
        deplacementY = -deplacementY
    if((cube.v[0].p[0].Coords[2] >= 50) or (cube.v[0].p[0].Coords[2] <= 2)):
        deplacementZ = -deplacementZ
    
    
    if(not(cube2[0].v[0].p[0].Coords[1] > 10)):
        deplacementY += 9.81 * (time.time()-oldTime)
    else:
        
        deplacementY = -deplacementY * 0.90
      

    
    if(deplacementZ > 0):

        deplacementZ -= 0.005
    

    
    """
    for vertex in testFloor.v:
        
        DrawVertex(ProjectVertex(vertex),(0,100,0))
        
    """
    for vertex in cube2[0].v:
        
        DrawVertex(ProjectVertex(vertex),WHandler.White)
    
    """
    """
    theta += math.pi/256
    for vertex in cube.v:
        
        DrawVertex(ProjectVertex(rotateVertex(vertex,Point([-5,0,5]),theta)),WHandler.White)
    
    """
    for vertex in cube.v:
        
        DrawVertex(rotateVertex(vertex,Point([-5,0,5]),theta),WHandler.White)
    
    """
    if(WHandler.SpaceToken):
        
        cube2 = copy.deepcopy([cube])
        deplacementX = 0.0
        deplacementY = -0.2
        deplacementZ = 0.5 
        """
    
    
    #WHandler.window.blit(text,(150,300))
    

    
    
    
    
    
    
    
    pygame.display.update()

    
    

"""

def DrawVertex(v,color):
    
    pygame.draw.line(WHandler.window,color,(v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),(v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))
    pygame.draw.line(WHandler.window,color,(v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),(v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))
    pygame.draw.line(WHandler.window,color,(v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),(v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))


rectangle = mesh([
    Vertex([
        Point([0,0,0]),
        Point([1,0,0]),
        Point([0,1,0])
    ]),
    Vertex([
        Point([1,0,0]),
        Point([0,1,0]),
        Point([1,1,0])
    ])

])

rectangle2 = mesh([
    Vertex([
        Point([0,0,0]),
        Point([math.sqrt(3),1,0]),
        Point([-1/2,math.sqrt(3)/2,0])
    ])

])

Vertex([
    Point([0,1,0]),
    Point([1,0,0]),
    Point([1,1,0])
]),

def rotateVertex(vertex,point,Angle):
    Point1Module = math.sqrt((vertex.p[0].Coords[0]-point.Coords[0])**2+(vertex.p[0].Coords[1]-point.Coords[1])**2)
    Point2Module = math.sqrt((vertex.p[1].Coords[0]-point.Coords[0])**2+(vertex.p[1].Coords[1]-point.Coords[1])**2)
    Point3Module = math.sqrt((vertex.p[2].Coords[0]-point.Coords[0])**2+(vertex.p[2].Coords[1]-point.Coords[1])**2)
    Point1BaseArg = 0
    try:
        Point1BaseArg = math.acos((vertex.p[0].Coords[0]-point.Coords[0])/Point1Module)
    except:
        pass

    Point2BaseArg = math.acos((vertex.p[1].Coords[0]-point.Coords[0])/Point2Module)
    Point3BaseArg = math.acos((vertex.p[2].Coords[0]-point.Coords[0])/Point3Module)
    return Vertex([
        Point([Point1Module*math.cos(Point1BaseArg+Angle),Point1Module*math.sin(Point1BaseArg+Angle),vertex.p[0].Coords[2]]),
        Point([Point2Module*math.cos(Point2BaseArg+Angle),Point2Module*math.sin(Point2BaseArg+Angle),vertex.p[1].Coords[2]]),
        Point([Point3Module*math.cos(Point3BaseArg+Angle),Point3Module*math.sin(Point3BaseArg+Angle),vertex.p[2].Coords[2]])
    ])



theta = 0

while WHandler.ProgramRunning:
    WHandler.HandleWindowEvents()
    WHandler.window.fill(0)
    
    theta += math.pi/256
    for triangles in rectangle.v:
        
        DrawVertex(triangles,(255,255,255))

    
    for triangles in rectangle.v:
        
        DrawVertex(rotateVertex(triangles,Point([-1,0,0]),theta),(255,0,0))

    
    for triangles in rectangle2.v:
        
        DrawVertex(triangles,(0,255,0))




"""


pygame.quit()


























