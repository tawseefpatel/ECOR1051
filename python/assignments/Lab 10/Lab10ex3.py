def reverse(lst:list):
    """ returns a new list that contains all the elements of the original list in reverse order"""
    l = len(lst)
    new = [None]*l
    for i in lst:
        l = l - 1
        new [l] = i
    return new

lst = [1,2,3,4,5,6,7,8,9,10]
print(reverse(lst))