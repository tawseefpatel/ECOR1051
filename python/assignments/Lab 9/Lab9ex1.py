print("Beginning Test")
print("Testing first in for-loop")
print ("Testing values from lst")
def count_evens(lst:list):
    """
    """
    for num in lst:
        if num % 2 == 0:
            print (num, end = ' ')
lst = [1,2,3,4,5,6,7,8]
print (count_evens(lst))
print("Test complete")
    