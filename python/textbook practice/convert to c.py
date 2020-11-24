def convert_to_c(degree_f:float)-> float:
    """return the temperature from farenheit to celsius as a float
    convert_to_c(100)
    212
    """
    return (degree_f -32)*5/9

print(convert_to_c(212))
