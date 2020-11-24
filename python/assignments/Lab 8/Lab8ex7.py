lst = [1,2,3]
def reverse3(lst:list):
    """
    """
    if len(lst) == 3:
        a,b,c = lst[0], lst[1], lst[2]
        value = [c, b, a]
    return value    
print(reverse3(lst))