import MoteurV2.Graphics as Graphics
import MoteurV2.Mesh as Mesh
import MoteurV2.ConversionsTo3D as Conversions
import pygame
import MoteurV2.matrix as matrix
import math
import copy
from dataclasses import dataclass
import time
from typing import List












ScrMeshSize = 100

ScrTranslationConstant = [Graphics.ScreenSize[0]/2,Graphics.ScreenSize[1]/2]


AspectRatio = Graphics.ScreenSize[0]/Graphics.ScreenSize[1]

theta = 30*math.pi/180
fovConverter = 1/math.tan(theta/2)




def ProjectVertex(v):

    return Mesh.Vertex([
            Mesh.Point([(v.p[0].Coords[0]*fovConverter)/v.p[0].Coords[2],
                (v.p[0].Coords[1]*fovConverter)/v.p[0].Coords[2],
                v.p[0].Coords[2]]),

            Mesh.Point([(v.p[1].Coords[0]*fovConverter)/v.p[1].Coords[2],
                (v.p[1].Coords[1]*fovConverter)/v.p[1].Coords[2],
                v.p[1].Coords[2]]),

            Mesh.Point([(v.p[2].Coords[0]*fovConverter)/v.p[2].Coords[2],
                (v.p[2].Coords[1]*fovConverter)/v.p[2].Coords[2],
                v.p[2].Coords[2]])
        ])

def DrawVertex(v,color):
    
    pygame.draw.line(Graphics.window,
        color,
        (v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        (v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))

    pygame.draw.line(Graphics.window,
        color,
        (v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        (v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))

    pygame.draw.line(Graphics.window,
        color,
        (v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        (v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))


def FillVertex(v,color):
    pygame.draw.polygon(Graphics.window,
    color,
    
        [(v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        (v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        (v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        
        ])


def Display3DMesh(Mesh):
    for vertex in Mesh.v:

        DrawVertex(ProjectVertex(vertex),(255,255,255))


def CalculateVertexColor(Normal,LightSource,Color):

    conversion = matrix.DotProduct(LightSource,Normal)
    
    if(conversion < 0):
        conversion = 0

    return (Color[0]*conversion,Color[1]*conversion,Color[2]*conversion)