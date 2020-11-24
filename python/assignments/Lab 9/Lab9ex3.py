def has22(lst:list):
    """
    """
    for i in lst:
        if lst[i] == lst[i+1]:
            return True
    return False
lst = [4,2,2,3,0]
print(has22(lst))

