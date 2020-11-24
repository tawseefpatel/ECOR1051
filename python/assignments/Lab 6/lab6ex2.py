import math
cost = int(input("what was the cost of the meal?: "))
sat_level = int(input("what is your sat level?: "))
one = cost * 0.2
two = cost * 0.15
three = cost * 0.05 

def tip (cost: float, sat:float) -> float:
    "Precondition: satisfaction must be between 0 and 3"
    """return the amount that the waiter should be tipped based on the cost and satisfaction (sat) on a scale from 1-3, 3 being the lowest and 1 being the highest. 
    return a 20% tip for a sat of 1, 15% tip for a sat of 2 and tip of 5% for a sat of 3
    >>>tip(100,1)
    The total is $120
    >>>tip(100,2)
    The total is $115
    >>>tip(100,3)
    The total is $105
    """
    return sat_level

#Test 1
print ("Checking if Satisfaction level is 1")
if sat_level == 1:
    sat_level = one
    print ("satisfaction level is 1")
else:
    print("satisfaction level is not 1")

#Test2
print ("checking if satisfaction level is 2")
if sat_level == 2:
    sat_level = two
    print ("satisfaction level is 2")
else:
    print("satisfaction level is not 2")

#Test 3
print ("checking if satisfaction level is 3")
if sat_level == 3:
    sat_level = three
    print ("satisfaction level is 3")
else:
    print("satisfaction level is not 3")
#Test 4
print("checking if satisfaction level is out of range")
if sat_level < 0 and sat_level > 3:
    sat_level = 0
    print ("sat level is out of range")
else:
    print("sat level is in range")


print ("The total is: $", tip(cost, sat_level))