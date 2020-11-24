#Step 1
point1 = [1.0,2.0]
print (point1)

#Step2
point1.append(3.0)
print (point1)

point1.pop(0)
print(point1)

point1.pop()
print(point1)

#Step3
point1 = (1.0, 2.0)
print(type(point1))
print (point1)

point1 = 1.0, 2.0
print(point1)

#Step4
x = point1[0]
y = point1[1]
print (x,y)

point2 = (4.0, 6.0)
x,y = point2
print(x,y)

#Step 5
point2[0] = 2.0
point2.appened(4.0)
point2.pop(0)

#Step 6
points = [(1.0,5,0), (2.0,8,0), (3.5,12,5)]
point1, point2, point3 = points
print (point1, point2, point3)


