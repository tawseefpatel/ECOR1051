def bakers_party(number_of_pastries:int, day_of_week:bool):
    """ returns True if a party with the given arguments is successful, otherwise it will return False; True if it's the weekend, False if the day is a weekday.
    """
    if day_of_week:
        if number_of_pastries in range(40,61):
            return True
    else:
        if number_of_pastries >=40:
            return True
    return False
        
print(bakers_party(100,False))