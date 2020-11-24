"""
OPERATIONS ON LISTS
noble_gases = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'R']
gas = input("enter element here: ")
if 'gas' in noble_gases :
    print (gas, 'is noble.')
else: 
    print (gas, 'is a metal.')
"""

"""
SLICING A LIST
my_exes = ['maham', 'wajiha', 'aafia', 'anna']
actual_exes = my_exes[:2]
fake_exes = my_exes[2:]
print ('my real exes are', actual_exes)
print ('my fake exes are', fake_exes)
"""

"""
from typing import List, Any
#Aliasing
list1 = [1,2,3,4,5]
list2 = list1
#del list1[:2]
#print (list2)

def remove_last(l1:List[Any]) -> list:
    'return the list without the last item
    Precondition: len(L) >= 0
    >>>remove_last([1,2,3,4])
    [1, 2, 3]
    '
    del l1[-1]
print ((remove_last(list1)))
"""

list1 = [1,2,3,4,5]
L.index(list1)