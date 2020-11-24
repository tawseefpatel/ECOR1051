def great_42(a:int, b:int):
    """ returns True if either a or b is 42, or if their sum or difference is 42
    """
    if a and b == 42:
        return True
    else:
        if abs(a+b) and abs(a-b) == 42:
            return True
    return False

print (great_42(80,38))