import pygame



pygame.init()

w = pygame.display.set_mode((1000,1000))



class Point:
    p = []

    def __init__(self,p):
        self.p = p

UI = True
A = Point([1,2])
B = Point([6,0])
C = Point([2.5,-1])
D = Point([3.5,2])
ScrTranslationConstant = [500,500]
ScrMeshSize = 100

def DrawLine(P1,P2):
    
    pygame.draw.line(w,(255,255,255),(P1.p[0]*100+500,P1.p[1]*100+500),(P2.p[0]*100+500,P2.p[1]*100+500),1)

def drawPoint(pos,color):

    pygame.draw.line(w,color,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize-10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize-10),(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+10),2)
    pygame.draw.line(w,color,(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize-10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize+10),(ScrTranslationConstant[0]+pos.p[0]*ScrMeshSize+10, ScrTranslationConstant[1]+pos.p[1]*ScrMeshSize-10),2)


def FindInter(P0,P1,P2,P3):
    A1 = P1.p[1]-P0.p[1]
    B1 = P0.p[0]-P1.p[0]
    C1 = A1 * P0.p[0] + B1 * P0.p[1]
    A2 = P3.p[1] - P2.p[1]
    B2 = P2.p[0] - P3.p[0]
    C2 = A2 * P2.p[0] + B2 * P2.p[1]
    print(A1,"* x + ",B1," * y = ",C1," ",A2,"* x + ",B2," * y = ",C2)
    #A2 = 0
    #B2 = 1
    #C2 = 0
    den = A1 * B2 - A2 * B1

 
    return Point([(B2*C1-B1*C2)/den,(A1*C2-A2*C1)/den])
while(UI):
    DrawLine(A,B)
    DrawLine(C,D)

    print(FindInter(A,B,C,D).p)
    drawPoint(FindInter(A,B,C,D),(255,255,0))
   


    














    for event in pygame.event.get():
        if( event.type == pygame.QUIT):
            
            UI = False

    pygame.display.flip()