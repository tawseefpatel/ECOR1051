#Exercise 1
days_in_numbers = [0,1,1,1,1,1,0]
day = int(input("What is the day of the week? (Enter 1 for weekday, 0 for weekend):"))
number_of_pastries_wd = range(40,60)
number_of_pastries_we = range(40,99999)

if day ==1:
    number_of_pastries = number_of_pastries_wd 
else:
    number_of_pastries = number_of_pastries_we


if day == 1:
    weekday = 1
    weekend = None
else:
    weekday = None
    weekend = 0
    
if day == weekend:
    print (True)  
    day_of_the_week = True
else: 
    print (False)
    day_of_the_week = False

    
def bakers_party(number_of_pastries:int, day_of_the_week:bool):
    if day_of_the_week == True:
        print (True)
    else:
        print (False)

party = bakers_party(number_of_pastries, day)
print (party)
