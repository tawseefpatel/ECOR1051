def same_first_last(lst:list):
    """ The function returns True if the list is not empty and if the first and last elements are equal. Otherwise, the function returns False. 
    >>> lst = [1,2,1,3,2,1]
    True
    >>> lst = ['']
    True
    >>> lst = [1,2,3,4,5,6]
    Flase
    """
    if lst != [''] or lst[0] == lst[-1]:
        return True
    return False
lst = [1,2,3,3,4,5]
print(same_first_last(lst))
    