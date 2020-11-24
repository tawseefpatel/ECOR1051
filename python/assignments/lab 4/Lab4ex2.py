import math

#Exercise 2
def distance(x1:float, y1:float, x2:float, y2: float) -> float:
    """ Returns the distance between two points, given by the coordinates 
    (x1, y1) and (x2, y2)
    
    >>> distance(3,3,6,7)
    5.0
   
    >>> distance (3,3,8,9)
    7.81
    """    
    x = (x2 - x1)
    y = (y2 - y1)    
    return math.sqrt((pow(x,2) + (pow(y,2))))
dist = distance (3,3,6,7)   
print ("The distance between the two points is:" , dist, "units")
