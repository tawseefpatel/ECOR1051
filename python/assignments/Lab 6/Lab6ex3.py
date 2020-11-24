amount_spent = int(input("What is your total?: "))
coupon_percent = 1
def coupon(amount_spent:float, coupon_percent:float) -> float:
    """return the value of the coupon that the customer recieves based on the amount they spent
    >>>coupon(50)
    $4
    >>>coupon(100)
    $10
    """
    return amount_spent * coupon_percent

#Test 1
print ("Checking if amount is below $10.")
if amount_spent <10 :
    print ("No coupon")

#Test 2
print ("Checking if amount is between $11 to $60")
if amount_spent in (range(11,61)):
    coupon_percent = 0.08
    print ("Coupon is worth 8%")
else:
    print ("Amount is not in bracket 2")

#Test 3
print("Checking if amount is between $61 to $150")
if amount_spent in (range(61,150)):
    coupon_percent = 0.10
    print ("Coupon is worth 10%")
else:
    print ("Amount is not in bracket 3")

#Test 3
print("Checking if amount is between $151 to $210")
if amount_spent in (range(151,210)):
    coupon_percent = 0.12
    print ("Coupon is worth 12%")
else:
    print ("Amount is not in bracket 4")

#Test 4
print ("Checking if amount is above $210")
if amount_spent >210:
    coupon_percent = 0.14
    print ("Coupon is worth 14%")

reward = coupon(amount_spent, coupon_percent)
print ("Your coupon is worth: $", reward)

