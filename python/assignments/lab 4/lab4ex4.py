import math
#Exercise 4

L = LENGTH_OF_LADDER = (3) #length in meters when angle is 0
a = 30 #change the value of a with the corresponsing angle you want to test

def height (LENGTH_OF_LADDER:float, angle_with_ground:float)-> float:
    """return the height reached by the ladder and what minimum angle with the ground can be used to reach the top of the wall
    
    a = 45
    >>> height_reached = height(L,a)
    2.121320343559643
    
    a = 60
    >>>height_reached = height(L,a)
    1.5000000000000004
    """      
    return LENGTH_OF_LADDER * (math.sin(math.radians(angle_with_ground))) 

height_reached = height(L,a)
print ("the height reached by the ladder is",  height_reached, "m.")