import Mesh
import Graphics
import math
import pygame
from dataclasses import dataclass
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
        (v.p[1].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],v.p[1].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        (v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))

    pygame.draw.line(Graphics.window,
        color,
        (v.p[2].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[2].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]),
        (v.p[0].Coords[0]*ScrMeshSize + ScrTranslationConstant[0],
        v.p[0].Coords[1]*ScrMeshSize + ScrTranslationConstant[1]))

