def date(date2):
    """return a value of true or false when the function date is evaluated to determine if January (01) is apart of the date
    >>>date(0o1,01,2001) 
    true  
    >>>date(0o1,02,2001) 
    false
    """
    date2 = (0o2, 0o1, 2001) #leading zeros cannot be evaluated without prefix '0o'
    return ('0o1' in 'date2')
print(date)
