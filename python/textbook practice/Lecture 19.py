grades = {10:55, 23:66.7, 14:87}

grades.update({99:55})
def check():
    for student in grades:
        if 38 in grades.keys(): 
            print()
        return 
print('3:', check())
print('4:',grades.get(10))
print('5:',grades.get(38))

for mark in grades:
    if 50 in grades.values():
        print('6:',student)

n=0   
for mark in grades.values():
    if mark == 55:
        n+=1   
print('7:' ,n)

gradelist = list(grades.values())
print("8:",gradelist.count(55))


for mark in grades.values():
    if mark >=50:
        print('9:', True)
    
n=0
for mark in grades.values():
    if mark >= 50:
        n+=1
print('10:',n)


grades.pop(23)
gradeslist = sorted(list(grades.items()))
print('12:', gradeslist)