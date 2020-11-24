def factorial (n:int) -> int:
    """ return n! for positive values of n."""
    fact = 1
    for i in range (2, n+1):
        fact = fact * n  
    return fact

def test_int(string:str, argument:int, expected:int):
    """
    Returns 1 if the test passes the actual/expected comparison and returns
    0 if it does not.
    """
    actual = factorial(argument)
    print ("testing factorial", "(", argument, ")")
    print("Expected result:", expected , "Actual result:", actual)     
    if actual == expected:     
        return 1
    else:     
        return 0
test1 = test_int(factorial, 1, 1)
test2 = test_int(factorial, 2, 2)
test3 = test_int(factorial, 3, 6)
test4 = test_int(factorial, 4, 24)
test_results = [test1, test2, test3, test4]
print(test_results)
print ("The test passed", test_results.count(1), "times.")
print ("The test failed", test_results.count(0), "times.")

