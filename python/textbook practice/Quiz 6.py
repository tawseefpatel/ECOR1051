'''
number = 5
while number > 0:
    number -= 1
    print (number)

number = 5
while number > 0:
    print (number)
    number -= 1
    
my_list = [1,2,3]
i = 1
while (i < len(my_list)):
    print (my_list[i], end="" )
    
x = "abcdef"
i = "a"
while i in x:
    x = x[:-1]
    print(i, end = " ")

password = input("Please enter your password ")
while (password != 'python'):
    print ("Try again")
    password = input ("Please enter your password")
print ("Welcome")

my_list = [1,2,3]
# Version 1
for item in my_list:
    print (item)
# Version 2    
i=0
while (i < len(my_list)):
    print (my_list[i])
    i += 1

my_list = [1,2,3]
while (i < len(my_list)):
    print (my_list[i])
    i += 1
    
x = {1,2,3}
value = x(0)
print(value)

z = [1,2,3,1,2,3]
print (len(z))

x = [1,2,3]
a = 4
x[0] = a
a = x[2]
print (a)
print(x)

x = (1,2,3)
a = 4
x[0] = a
a = x[2]'''
password = input("Please enter your password ")
while (password != 'python'):
    print ("Try again")
    password = input ("Please enter your password")
print ("Welcome")