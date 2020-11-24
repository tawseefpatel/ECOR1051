import math 
from math import pi
#Exercise 1
def area_of_disk(radius:float)-> float: 
    """ Return the area_of_disk when evaluated at a non-negative radius
    Precondition: radius > 0
    >>>area = area_of_disk(5)
        print (area)
    78.53981633974483
    
    >>>area = area_of_disk(10)
        print (area)
    314.1592653589793
    """
    return math.pi * radius ** 2 
area = (area_of_disk(10))
print (area)
