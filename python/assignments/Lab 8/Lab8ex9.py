def sum2(lst:list):
    """
    """
    return (lst[0] if len(lst) else 0) + (lst[1] if len(lst)>1 else 0)
lst = [1]
print (sum2(lst))
       