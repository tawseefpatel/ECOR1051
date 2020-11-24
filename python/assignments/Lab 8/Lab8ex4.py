def common_end(lst1:list, lst2:list):
    """
    """
    if (lst1[0] == lst2[0]) or (lst1[-1] == lst2[-1]):
        return True
    return False
lst1 = [1,2,3,4,5,0]
lst2 = [0,2,3,4,5,1]
print (common_end(lst1,lst2))