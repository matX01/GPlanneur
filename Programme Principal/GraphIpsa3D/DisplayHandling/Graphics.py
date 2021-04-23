
import pygame
from GraphIpsa3D.Mesh import *
import math
import GraphIpsa3D.DisplayHandling.MatGraph

ScreenSize = None
ScrMeshSize = None
ScrTranslationConstant = None
AspectRatio = None
theta = None
fovConverterX = None
fovConverterY = None
window = None

def drawVector(pos,vec,color,ArrowColor):
    
    pygame.draw.line(window,color,(ScrTranslationConstant[0]+pos[0]*ScrMeshSize, ScrTranslationConstant[1]+pos[1]*ScrMeshSize),(ScrTranslationConstant[0]+pos[0]*ScrMeshSize+vec.v[0]*ScrMeshSize, ScrTranslationConstant[1]+pos[1]*ScrMeshSize+vec.v[2]*ScrMeshSize),2)
    pygame.draw.line(window,ArrowColor,(ScrTranslationConstant[0]+pos[0]*ScrMeshSize+vec.v[0]*ScrMeshSize*0.90, ScrTranslationConstant[1]+pos[1]*ScrMeshSize+vec.v[2]*ScrMeshSize*0.90),(ScrTranslationConstant[0]+pos[0]*ScrMeshSize+vec.v[0]*ScrMeshSize, ScrTranslationConstant[1]+pos[1]*ScrMeshSize+vec.v[2]*ScrMeshSize),2)
 
def initDisplayHandler(PanelToUse,ScrSize,ScreenMeshSize,FOV):
    global ScreenSize
    global ScrTranslationConstant
    global AspectRatio
    global theta
    global fovConverterX
    global fovConverterY
    global window
    global ScrMeshSize
    
    ScrTranslationConstant = [ScrSize[0]/2,ScrSize[1]/2]
    AspectRatio = ScrSize[0]/ScrSize[1]
    ScrMeshSize = ScreenMeshSize
    #theta = FOV
    fovConverterX = (1/math.tan(FOV/2))
    fovConverterY = (1/math.tan(FOV/2))

    ScreenSize = ScrSize
    window = PanelToUse



def drawPoint(pos,color):
    pygame.draw.line(window,color,(ScrTranslationConstant[0]+pos[0]*ScrMeshSize-10, ScrTranslationConstant[1]+pos[1]*ScrMeshSize-10),(ScrTranslationConstant[0]+pos[0]*ScrMeshSize+10, ScrTranslationConstant[1]+pos[1]*ScrMeshSize+10),2)
    pygame.draw.line(window,color,(ScrTranslationConstant[0]+pos[0]*ScrMeshSize-10, ScrTranslationConstant[1]+pos[1]*ScrMeshSize+10),(ScrTranslationConstant[0]+pos[0]*ScrMeshSize+10, ScrTranslationConstant[1]+pos[1]*ScrMeshSize-10),2)


def DrawTriangle(T,color,FillMode):
    pygame.draw.polygon(window,
    color,
    
        [(T.m[0][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[0][1]*ScrMeshSize + ScrTranslationConstant[1]),
        (T.m[1][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[1][1]*ScrMeshSize + ScrTranslationConstant[1]),
        (T.m[2][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[2][1]*ScrMeshSize + ScrTranslationConstant[1]),
        
        ],FillMode)