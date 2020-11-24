#Step1
points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}
print (points)

point1 = (1.0, 2.0) 
point2 = (4.0, 6.0) 
point3 = (10.0, -2.0) 
points = {point1, point2, point3}
print (points)

points = set() 
points.add(point1) 
points.add(point2) 
points.add(point3)
print(points)

#Step 2
points.add(point2) 
print (points) 

#Step3
"""print(points[0])""" #doesnt work

#Step4
for point in points:
    print(point)