from typing import Set, Tuple
file = input("What text file do you want to open: ")

def read_points(file:str) -> Set[Tuple[float, float]]:
    """Return the points in the selected file
    """
    infile = open(file,"r")
    points = []
    for line in infile:
        points.append((float(line.split()[0]), float(line.split()[1])))
    infile.close()
    return set(points)

def fit_line_to_points(points: Set[Tuple[float, float]]) -> Tuple[float, float]:
    """returns a tuple, which contains the slope and intercept of the best-fit straight line through the points
    >>>fit_line_to_points(get_points())
    >>> 3.0,2.0
    """
    n = len(points)
    sumx = 0
    sumy = 0 
    sumxx = 0
    sumxy = 0
    for (x , y) in points:
        sumx +=x
        sumy +=y
        sumxx += x**2
        sumxy += x*y
    m = (sumx * sumy - n * sumxy) / (sumx * sumx - n * sumxx)
    b = (sumx * sumxy - sumxx * sumy) / (sumx * sumx - n * sumxx)  
    return  m,b

m,b = fit_line_to_points(read_points(file))
print("The best-fit line is y =", m, "x +", b)