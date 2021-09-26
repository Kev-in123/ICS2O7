import math


def distance(point1, point2):

    
    x1 = point1 [0]
    
    x2 = point2 [0]
    
    y1 = point1 [1]
    
    y2 = point2 [1]
    
    sqaure1 = pow (y2 - y1, 2)
    
    sqaure2 = pow (x2 - x1, 2)
    
    
    return math.sqrt(sqaure1+sqaure2)