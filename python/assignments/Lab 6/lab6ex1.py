#Excercise 1

def factorial (n:int) -> int:
    """ return n! for positive values of n.
    >>> factorial (1)
    1
    >>>factorial (2)
    2
    >>>factorial (3)
    6
    >>>factorial (4)
    24
    """
    fact = 1
    for i in range (2, n+1):
        fact = fact * n  
    return fact
test1 = factorial(1)
test2 = factorial(2)
test3 = factorial(3)
test4 = factorial(4)
test_passed = 0
test_failed = 0

#Test 1
print ("testing factorial (1) ")
print ("expected result: 1 , Actual result: ", test1)
if test1 == 1:
    print ("Test Passed")
    test_passed += 1
else:
    print ("Test Failed")
    test_failed += 1

#Test 2
print ("testing factorial (2) ")
print ("expected result: 2 , Actual result: ", test2)
if test2 == 2:
    print ("Test Passed")
    test_passed += 1
else:
    print ("Test Failed") 
    test_failed += 1

#Test 3
print ("testing factorial (3) ")
print ("expected result: 6 , Actual result: ", test3)
if test3 == 6:
    print ("Test Passed")
    test_passed += 1
else:
    print ("Test Failed")
    test_failed += 1

#Test 4    
print ("testing factorial (4) ")
print ("expected result: 24 , Actual result: ", test4)
if test4 == 24:
    print ("Test Passed")
    test_passed += 1
else:
    print ("Test Failed")
    test_failed += 1
     
print (test_passed, "tests passed for exercise 1")
print (test_failed, "tests failed for exercise 1")
