def first_last6(lst:list):
    """ returns True if a 6 is the first element or the last element or if both the first and last element are 6. Otherwise, the function returns False. 
    """
    if lst[0]==6 or lst[-1] == 6:
        return True
    return False
lst = [6,1,2,3,4,1]
print (first_last6(lst))