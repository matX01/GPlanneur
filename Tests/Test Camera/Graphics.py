
import pygame
import matrix
import math
import MatGraph
ScreenSize = None
ScrMeshSize = None
ScrTranslationConstant = None
AspectRatio = None
theta = None
fovConverter = None
window = None
Font = None

def initDisplayHandler(PanelToUse,ScrSize,ScreenMeshSize,FOV):
    global ScreenSize
    global ScrTranslationConstant
    global AspectRatio
    global theta
    global fovConverter
    global window
    global ScrMeshSize
    global Font
    Font = pygame.font.SysFont('Arial', 15)
    ScrTranslationConstant = [ScrSize[0]/2,ScrSize[1]/2]
    AspectRatio = ScrSize[0]/ScrSize[1]
    ScrMeshSize = ScreenMeshSize
    theta = FOV
    fovConverter = 1/math.tan(theta/2)
    ScreenSize = ScrSize
    window = PanelToUse






def DrawTriangle(T,color,FillMode):
    pygame.draw.polygon(window,
    color,
    
        [(T.m[0][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[0][1]*ScrMeshSize + ScrTranslationConstant[1]),
        (T.m[1][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[1][1]*ScrMeshSize + ScrTranslationConstant[1]),
        (T.m[2][0]*ScrMeshSize + ScrTranslationConstant[0],T.m[2][1]*ScrMeshSize + ScrTranslationConstant[1]),
        
        ],FillMode)




def drawAxis():
    pygame.draw.line(window,(255,0,0),(ScrTranslationConstant[0], ScrTranslationConstant[1]),(ScrTranslationConstant[0], ScrTranslationConstant[1]+ScrMeshSize),2)
    pygame.draw.line(window,(0,255,0),(ScrTranslationConstant[0], ScrTranslationConstant[1]),(ScrTranslationConstant[0]+ScrMeshSize, ScrTranslationConstant[1]),2)

def drawPoint(pos,color,Text):
    textsurface = Font.render(Text, False, color)
    pygame.draw.line(window,color,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize-10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize-10),(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+10),2)
    pygame.draw.line(window,color,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize-10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+10),(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize-10),2)
    window.blit(textsurface,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+13, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+13))

def drawVector(pos,vec,color,ArrowColor,Text):
    textsurface = Font.render(Text, False, color)
    pygame.draw.line(window,color,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize),(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+vec.v[0]*ScrMeshSize, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+vec.v[1]*ScrMeshSize),2)
    pygame.draw.line(window,ArrowColor,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+vec.v[0]*ScrMeshSize*0.90, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+vec.v[1]*ScrMeshSize*0.90),(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+vec.v[0]*ScrMeshSize, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+vec.v[1]*ScrMeshSize),2)
    window.blit(textsurface,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+13, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+13))