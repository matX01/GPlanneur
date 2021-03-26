from dataclasses import dataclass
from typing import List
import math
@dataclass
class Point:                                                                    # Le point , constitué de 3 valeurs x , y , z
    Coords: List[float]
    
@dataclass
class Vertex:                                                                   # le vertex , un triangle sans volume constitué de trois points
    p: List[Point]
    
@dataclass
class mesh:                                                                     # le mesh , un ensemble de vertex permettant de former un polygone en 3 dimensions.
    v: List[Vertex]




cube = mesh([
    #Front
    Vertex([
        Point([0,0,0]),
        Point([0,1,0]),
        Point([1,1,0])
    ]),
    Vertex([
        Point([0,0,0]),
        Point([1,1,0]),
        Point([1,0,0])
    ]),
    
    #Right
    Vertex([
        Point([1,0,0]),
        Point([1,1,0]),
        Point([1,1,1])
    ]),
    Vertex([
        Point([1,0,0]),
        Point([1,1,1]),
        Point([1,0,1])
    ]),
    
    #Back
    Vertex([
        Point([1,0,1]),
        Point([1,1,1]),
        Point([0,0,1])
    ]),
    Vertex([
        Point([1,1,1]),
        Point([0,1,1]),
        Point([0,0,1])
    ]),
    
    #Left
    Vertex([
        Point([0,0,1]),
        Point([0,1,1]),
        Point([0,1,0])
    ]),
    Vertex([
        Point([0,0,1]),
        Point([0,1,0]),
        Point([0,0,0])
    ]),
    
    #bottom
    Vertex([
        Point([0,1,0]),
        Point([0,1,1]),
        Point([1,1,1])
    ]),
    Vertex([
        Point([0,1,0]),
        Point([1,1,1]),
        Point([1,1,0])
    ]),
    
    #top
    Vertex([
        Point([1,0,1]),
        Point([0,0,1]),
        Point([0,0,0])
    ]),
    Vertex([
        Point([1,0,1]),
        Point([0,0,0]),
        Point([1,0,0])
    ])
])

square = mesh([
    
    Vertex([
        Point([0,0,0]),
        Point([0,1,0]),
        Point([1,1,0])
    ]),
    
    Vertex([
        Point([0,0,0]),
        Point([1,0,0]),
        Point([0,1,0])
    ])
])

pyramid = mesh([
    
    Vertex([
        Point([0,0,0]),
        Point([1,0,0]),
        Point([0,0,1])
    ]),
    Vertex([
        Point([0,0,0]),
        Point([1,0,0]),
        Point([0,0,1])
    ]),
    Vertex([
        Point([0,0,0]),
        Point([1,0,0]),
        Point([0,0,1])
    ]),
    Vertex([
        Point([0,0,0]),
        Point([1,0,0]),
        Point([0.5,0.5,0.707])
    ]),
    Vertex([
        Point([1,0,0]),
        Point([1,0,1]),
        Point([0.5,0.5,0.707])
    ]),
    Vertex([
        Point([1,0,1]),
        Point([0,0,1]),
        Point([0.5,0.5,0.707])
    ]),
        Vertex([
        Point([0,0,1]),
        Point([1,0,0]),
        Point([0.5,0.5,0.707])
    ]),



])


ProjectedSquare = mesh([
    #South
    Vertex([
        Point([0,0,0]),
        Point([1/2,math.sqrt(3)/2,0]),
        Point([((1+math.sqrt(3))/2),(math.sqrt(3)-1)/2,0])
    ]),
    Vertex([
        Point([0,0,0]),
        Point([((1+math.sqrt(3))/2),((math.sqrt(3)-1)/2),0]),
        Point([(math.sqrt(3)/2),-1/2,0])
    ])
])
