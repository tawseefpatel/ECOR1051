#the values that were used in the example were reused to test 

def accumulated_amount(principal, rate, n, time):
    return principal*(1+(rate/n))**(n*time)

print (accumulated_amount (1500, 0.043,4,6)) 

print (accumulated_amount (0, 0.043,4,6))

print (accumulated_amount (1500, 0,4,6))