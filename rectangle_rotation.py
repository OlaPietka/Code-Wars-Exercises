import math

def rectangle_rotation(a, b):
    ai = (a/2) * math.cos(math.radians(45))
    bi = (b/2) * math.sin(math.radians(45))
    
    x1 = -ai - bi
    y1 = -ai + bi
    
    x2 = ai - bi
    y2 = ai + bi

    n1 = math.floor((x1*y2 - x2*y1)/(x1-x2))
    n2 = math.floor((x2*x2 - y2*y2)/(x2-y2))
    
    points_num = math.ceil((2*n1+1)*(2*n2+1)/2)

    return  points_num if points_num % 2 == 1 else points_num - 1
    