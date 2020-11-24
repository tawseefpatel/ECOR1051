import math 
 
def area_of_disk(radius): 
    return math.pi * radius ** 2 

def area_of_ring(outer, inner): 
    return area_of_disk(outer) - area_of_disk(inner)

area = area_of_disk(5)
print (area)

area = area_of_disk(10)
print (area)

area = area_of_ring(10,5)
print (area)

area = area_of_ring(10.0,5.0)
print (area)