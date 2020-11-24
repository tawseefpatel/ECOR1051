def average(lst:list)-> list:
    """returns a new list of tuples. The three numbers in each tuple are the integer average values of the numbers in the tuple at the same position in the original list
    >>>average(27,219,134)
    >>>(126,126,126)
    """
    y = 0 
    for i in lst:
        avg = sum(i)//len(i)
        lst[y] = (avg,avg,avg)
        y = y+1
    return lst

lst = [(27,219,134),(2,4,6),(10,12,14)]
print(average(lst))