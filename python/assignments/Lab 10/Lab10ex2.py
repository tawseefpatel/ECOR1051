def divisors(n:int)->list:
    """returns a list containing all the positive divisors of n. 
    >>> divsors(6)
    >>>[1,2,3,6]
    >>>divisors(9)
    >>>[1,3,9]
    """
    i = 1
    return [i for i in range (1,n+1) if n%i == 0]
print(divisors(6))  