import math
import MatGraph as MatGraph
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
    
class mat4x4:
    m = None

  

    def __init__(self,m=None):
        
        self.m = m

    def __add__(self,B):

        return mat4x4([

        
        [self.m[0][0]+B.m[0][0],self.m[0][1]+B.m[0][1],self.m[0][2]+B.m[0][2],self.m[0][3]+B.m[0][3]],
        [self.m[1][0]+B.m[1][0],self.m[1][1]+B.m[1][1],self.m[1][2]+B.m[1][2],self.m[1][3]+B.m[1][3]],
        [self.m[2][0]+B.m[2][0],self.m[2][1]+B.m[2][1],self.m[2][2]+B.m[2][2],self.m[2][3]+B.m[2][3]]
        [self.m[3][0]+B.m[3][0],self.m[3][1]+B.m[3][1],self.m[3][2]+B.m[2][2],self.m[3][3]+B.m[3][3]],


    ])

    
    def __mul__(self,B):
    
        return mat4x4([

        [self.m[0][0]*B.m[0][0]+self.m[0][1]*B.m[1][0]+self.m[0][2]*B.m[2][0]+self.m[0][3]*B.m[3][0],
        self.m[0][0]*B.m[0][1]+self.m[0][1]*B.m[1][1]+self.m[0][2]*B.m[2][1]+self.m[0][3]*B.m[3][1],
        self.m[0][0]*B.m[0][2]+self.m[0][1]*B.m[1][2]+self.m[0][2]*B.m[2][2]+self.m[0][3]*B.m[3][2]],
        
        
        [self.m[1][0]*B.m[0][0]+self.m[1][1]*B.m[1][0]+self.m[1][2]*B.m[2][0]+self.m[1][3]*B.m[3][0],
        self.m[1][0]*B.m[0][1]+self.m[1][1]*B.m[1][1]+self.m[1][2]*B.m[2][1]+self.m[1][3]*B.m[3][1],
        self.m[1][0]*B.m[0][2]+self.m[1][1]*B.m[1][2]+self.m[1][2]*B.m[2][2]+self.m[1][3]*B.m[3][2]],


        [self.m[2][0]*B.m[0][0]+self.m[2][1]*B.m[1][0]+self.m[2][2]*B.m[2][0]+self.m[2][3]*B.m[3][0],
        self.m[2][0]*B.m[0][1]+self.m[2][1]*B.m[1][1]+self.m[2][2]*B.m[2][1]+self.m[2][3]*B.m[3][1],
        self.m[2][0]*B.m[0][2]+self.m[2][1]*B.m[1][2]+self.m[2][2]*B.m[2][2]+self.m[2][3]*B.m[3][2]],

        
        [self.m[3][0]*B.m[0][0]+self.m[3][1]*B.m[1][0]+self.m[3][2]*B.m[2][0]+self.m[3][3]*B.m[3][0],
        self.m[3][0]*B.m[0][1]+self.m[3][1]*B.m[1][1]+self.m[3][2]*B.m[2][1]+self.m[3][3]*B.m[3][1],
        self.m[3][0]*B.m[0][2]+self.m[3][1]*B.m[1][2]+self.m[3][2]*B.m[2][2]+self.m[3][3]*B.m[3][2]]

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





def PointAt(pos,target,up):
    
    
    NewForward = target-pos
    try:
        size = math.sqrt(NewForward.v[0]**2+NewForward.v[0]**2+NewForward.v[0]**2)
        NewForward.v[0] /= size
        NewForward.v[1] /= size
        NewForward.v[2] /= size
    except:
        pass

    
    
    a = NewForward * MatGraph.DotProduct(up,NewForward)
    NewUp = up - a


    newRight = MatGraph.CrossProduct(NewUp , NewForward)

    return mat4x4([
        [newRight.v[0],newRight.v[1],newRight.v[2],0],
        [NewUp.v[0],NewUp.v[1],NewUp.v[2],0],
        [NewForward.v[0],NewForward.v[1],NewForward.v[2],0],
        [pos.v[0],pos.v[1],pos.v[2],1]
    ])

def LookatMatrix(m):
   
    return mat4x4([
        [m.m[0][0],m.m[1][0],m.m[2][0],0],
        [m.m[0][1],m.m[1][1],m.m[2][1],0],
        [m.m[0][2],m.m[1][2],m.m[2][2],0],
        [-(m.m[3][0]*m.m[0][0] + m.m[3][1] * m.m[0][1] + m.m[3][2] * m.m[0][2]),
         -(m.m[3][0]*m.m[1][0] + m.m[3][1] * m.m[1][1] + m.m[3][2] * m.m[1][2]),
         -(m.m[3][0]*m.m[2][0] + m.m[3][1] * m.m[2][1] + m.m[3][2] * m.m[2][2])]
    ])