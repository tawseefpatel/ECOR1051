from typing import Set, Tuple
file = (open('data.txt', 'r'))

def read_points(filename:str) -> Set[Tuple[float, float]]:
        file = open('data.txt', 'r') 
        for line in file:
                print(line)
        return(str(line.split))
                
file.close

point1, point2, point3 = read_points(file)

print(point1,point2, point3)
