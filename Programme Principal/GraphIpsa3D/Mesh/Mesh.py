from dataclasses import dataclass
from typing import List
import matrix
import GraphIpsa3D.DisplayHandling.MatGraph as MatGraph


class vector:
    v = []

    def __sub__(self,B):
        return vector([
        self.v[0] - B.v[0],
        self.v[1] - B.v[1],
        self.v[2] - B.v[2]
        ])

    def __mul__(self,B):
        return (vector([self.v[0]*B,self.v[1]*B,self.v[2]*B]))
    
    def __add__(self,B):

        return (vector([self.v[0] + B.v[0],self.v[1] + B.v[1],self.v[2] + B.v[2]]))

    def __init__(self,vector):

        self.v = vector

    def __str__(self):
        ReturnValue = "[ "
        for i in range(3):
            ReturnValue += str(self.v[i]) + " "

        return ReturnValue + "]"






def Load3DElement(Path):
    f = open(Path,"r")
    Points = []
    MeshElement = []
    for Line in f:
        
        SplitedVar = Line.split(" ")
          
        if(Line[0] == "v"):
       
            Points.append([float(SplitedVar[1]),float(SplitedVar[2]),float(SplitedVar[3])])
        
        if(Line[0] == "f"):
           
            MeshElement.append(matrix.mat3x3([Points[int(SplitedVar[1])-1],Points[int(SplitedVar[2])-1],Points[int(SplitedVar[3])-1]]))



    f.close()
    return MeshElement

