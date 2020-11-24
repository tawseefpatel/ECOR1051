def sum_unique(a:int, b:int, c:int):
    """return the sum of a b c however, if the same value is used twice that value is not considered
    >>>sum_unique(3,2,3)
    2
    >>>sum_unique(3,3,3)
    0
    """
    if lst[0] == lst[1]:
        return lst[2]
    if lst[0] == lst[2]:
        return lst[1]
    if lst[1] == lst[2]:
        return lst[0]
    return sum(lst)

lst = [3,1,2]
num1 = lst [0]
num2 = lst [1]
num3 = lst [2]
summed = sum_unique(num1,num2,num3)
print (summed)


'''
#can create a for-loop
def sum_unique2(a:int, b:int, c:int):
    for i in lst:
        return 

'''