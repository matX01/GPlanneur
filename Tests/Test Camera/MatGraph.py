

import Mesh 
import Graphics
import matrix
import math
Sin = []
Cos = []


def ProjectTriangle(T):
        return matrix.mat3x3([
            [(T.m[0][0]*Graphics.fovConverter)/T.m[0][2],
             (T.m[0][1]*Graphics.fovConverter)/T.m[0][2],
             T.m[0][2]],

            [(T.m[1][0]*Graphics.fovConverter)/T.m[1][2],
             (T.m[1][1]*Graphics.fovConverter)/T.m[1][2],
             T.m[1][2]],

            [(T.m[2][0]*Graphics.fovConverter)/T.m[2][2],
             (T.m[2][1]*Graphics.fovConverter)/T.m[2][2],
             T.m[2][2]]
        ])


def CalculateTriangleColor(Normal,LightSource,Color):

    conversion = DotProduct(LightSource,Normal)

    if(conversion < 0):
        
        conversion = 0

    return (Color[0]*conversion,Color[1]*conversion,Color[2]*conversion)



def MultiplyMeshAndMatrix(Mesh,Matrix):
    for i in range(len(Mesh)):
        
        Mesh[i] *= Matrix





def AddMeshAndMatrix(Mesh,Matrix):
    for i in range(len(Mesh)):
        
        Mesh[i] += Matrix







def CrossProduct(A,B):
    return Mesh.vector([
        A.v[1]*B.v[2] - A.v[2]*B.v[1],
        A.v[2]*B.v[0] - A.v[0]*B.v[2],
        A.v[0]*B.v[1] - A.v[1]*B.v[0]
    ])

def DotProduct(A,B):
    
    return A.v[0]*B.v[0]+A.v[1]*B.v[1]+A.v[2]*B.v[2]
















