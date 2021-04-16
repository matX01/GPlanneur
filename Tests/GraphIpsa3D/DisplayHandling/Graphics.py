
import pygame
from Mesh import *
import math
import DisplayHandling.MatGraph
import DEBUG
ScreenSize = None
ScrMeshSize = None
ScrTranslationConstant = None
AspectRatio = None
theta = None
fovConverterX = None
fovConverterY = None
window = None


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
    theta = FOV
    fovConverterX = 1/math.tan(theta/2)
    fovConverterY = 1/math.tan(theta/2)

    ScreenSize = ScrSize
    window = PanelToUse






def DrawTriangle(T,color,FillMode):
    pygame.draw.polygon(window,
    color,
    
        [(T.m[0][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[0][1]*ScrMeshSize + ScrTranslationConstant[1]),
        (T.m[1][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[1][1]*ScrMeshSize + ScrTranslationConstant[1]),
        (T.m[2][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[2][1]*ScrMeshSize + ScrTranslationConstant[1]),
        
        ],FillMode)