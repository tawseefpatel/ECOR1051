def max_end3(lst:list)-> list:
    """
    """
    if lst[0] > lst[-1]:
        return [lst[0]] * len(lst)
    return [lst[-1]] * len(lst)
lst = [3,2,2]
print (max_end3(lst))