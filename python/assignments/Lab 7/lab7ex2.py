def squirrel_play(temp:int, season:bool):
    """ returns True if the squirrels are playing, given the temperature and the season; otherwise it returns False;(True if it's summer, otherwise False)
    """
    if (season):
        if temp in range (60,91):
            return True
    else:
        if (temp <= 100):
            return True
    return False
print (squirrel_play(100,False))