def rotate_left3(lst:list):
    """
    """
    if len(lst) == 3:
        a,b,c = lst[0], lst[1], lst[2]
        value = [b, c, a]
    return value
lst = [1,2,3]
print(rotate_left3(lst))