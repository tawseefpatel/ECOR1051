LITRES_PER_GALLON = 4.54609 
KMS_PER_MILE = 1.60934 

def convert_to_litres_per_100_km (mpg):  
    return (LITRES_PER_GALLON)/(mpg*KMS_PER_MILE)*100


thirty_two = convert_to_litres_per_100_km(32)
print (thirty_two)

negative_five = convert_to_litres_per_100_km(-5)
print (abs(negative_five)) 
#this results in a negative value and therefore the abs function was added \n
#because fuel consumption cannot be negative and if it is negative that means \n
#fuel is being added not taken away


zero = convert_to_litres_per_100_km(0) #this is not able to be called as it is division by 0
print (zero) 


