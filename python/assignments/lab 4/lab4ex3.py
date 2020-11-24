import math

#Exercise 3
def area_of_circle(xc: float, yc:float, xp:float, yp:float) -> float:
    """ Return the area of a cirlce by using the radius as a distance between two points
    
    >>>area = area_of_circle(1,1,2,2)
    print (area)
6.283185307179588
   
    >>>area = area_of_circle(2,2,4,4)
    print (area)
25.132741228718352
    """
    radius = (math.sqrt((xp - xc)**2 + (yp - yc)**2))    
    return math.pi * pow(radius,2)
area = area_of_circle(2,2,4,4)
print (area)