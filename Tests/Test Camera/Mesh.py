from dataclasses import dataclass
from typing import List
import matrix
import MatGraph as MatGraph


class vector:
    v = []

    def __sub__(self,B):
        return vector([
        self.v[0] - B.v[0],
        self.v[1] - B.v[1],
        ])

    def __mul__(self,B):
        return (vector([self.v[0]*B,self.v[1]*B]))
    
    def __add__(self,B):

        return (vector([self.v[0] + B.v[0],self.v[1] + B.v[1]]))

    def __init__(self,vector):

        self.v = vector
        





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

