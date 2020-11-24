def sum_x(s):
    """returns the sum of all the x coordinates"""
    sum = 0
    for i in s:
        sum += i[0]
    return sum
s = {(2,3), (4,6), (4,1)}
print (sum_x(s))