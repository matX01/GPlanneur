import math
class MatrixCalculusException(Exception):
    def __init__(self,E):
        print(E)
    

class mat3x3:
    m = None

  

    def __init__(self,m=None):
        
        self.m = m

    def __add__(self,B):

        return mat3x3([

        
        [self.m[0][0]+B.m[0][0],self.m[0][1]+B.m[0][1],self.m[0][2]+B.m[0][2]],
        [self.m[1][0]+B.m[1][0],self.m[1][1]+B.m[1][1],self.m[1][2]+B.m[1][2]],
        [self.m[2][0]+B.m[2][0],self.m[2][1]+B.m[2][1],self.m[2][2]+B.m[2][2]],


    ])

    
    def __mul__(self,B):
    
        return mat3x3([

        [self.m[0][0]*B.m[0][0]+self.m[0][1]*B.m[1][0]+self.m[0][2]*B.m[2][0],
        self.m[0][0]*B.m[0][1]+self.m[0][1]*B.m[1][1]+self.m[0][2]*B.m[2][1],
        self.m[0][0]*B.m[0][2]+self.m[0][1]*B.m[1][2]+self.m[0][2]*B.m[2][2]],
        
        
        [self.m[1][0]*B.m[0][0]+self.m[1][1]*B.m[1][0]+self.m[1][2]*B.m[2][0],
        self.m[1][0]*B.m[0][1]+self.m[1][1]*B.m[1][1]+self.m[1][2]*B.m[2][1],
        self.m[1][0]*B.m[0][2]+self.m[1][1]*B.m[1][2]+self.m[1][2]*B.m[2][2]],


        [self.m[2][0]*B.m[0][0]+self.m[2][1]*B.m[1][0]+self.m[2][2]*B.m[2][0],
        self.m[2][0]*B.m[0][1]+self.m[2][1]*B.m[1][1]+self.m[2][2]*B.m[2][1],
        self.m[2][0]*B.m[0][2]+self.m[2][1]*B.m[1][2]+self.m[2][2]*B.m[2][2]],

    ])


    def __str__(self):
        returnValue = ""
        for Column in self.m:
            returnValue += "[ "
            for Row in Column:
                returnValue += str(Row) + " " 
            returnValue += "]\n"

        return returnValue
    

def RotationMatrix(R,Theta):
    if(R == "X"):
        return mat3x3([
            [1,0,0],
            [0,math.cos(Theta),-math.sin(Theta)],
            [0,math.sin(Theta),math.cos(Theta)]
        ])
    if(R == "Y"):
        return mat3x3([
            [math.cos(Theta),0,math.sin(Theta)],
            [0,1,0],
            [-math.sin(Theta),0,math.cos(Theta)]
        ])
    if(R == "Z"):
        return mat3x3([
            [math.cos(Theta),-math.sin(Theta),0],
            [math.sin(Theta),math.cos(Theta),0],
            [0,0,1]
        ])







