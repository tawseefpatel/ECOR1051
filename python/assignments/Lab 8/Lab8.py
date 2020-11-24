"""Need help fixing exercise 6,7,9"""
#Exercise 1
def first_last6(lst:list):
    if lst[0] or lst[-1] == 6:
        return True
    return False
lst = [6,1,2,3,4,1]
print (first_last6(lst))
 
    
#Exercise 2
def same_first_last(lst:list):
    if lst == [''] or lst[0] == lst[-1]:
        return True
    else:
        return False
lst = [1,2,3,3,4,5]
print(same_first_last(lst))


#Exercise 3
import math
def make_pi():
    return [3,1,4]
print (make_pi())


#Exercise 4
def common_end(lst1:list, lst2:list):
    if (lst1[0] == lst2[0]) and (lst1[-1] == lst2[-1]): 
        return True
    if (lst1[0] == lst2[0]) or (lst1[-1] == lst2[-1]):
        return True
    else:
        return False
lst1 = [1,2,3,4,5,0]
lst2 = [0,2,3,4,5,1]
print (common_end(lst1,lst2))
    

#Exercise 5
def sum3(lst:list):
    return sum(lst)
lst = [1,2,3,4,5]
print(sum3(lst))


#Exercise 6
def rotate_left3(lst:list):
    return lst[1:] + lst[:1] #cant use slicing 
lst = [1,2,3,4]
print(rotate_left3(lst))


#Exercise 7
lst = [1,2,3]
def reverse3(lst:list):
    return lst.reverse() #cant use reverse
(reverse3(lst))
print(lst)


#Exercise 8
def max_end3(lst:list)-> list:
    if lst[0] > lst[-1]:
        return [lst[0]] * len(lst)
    return [lst[-1]] * len(lst)
lst = [2,2,4]
print (max_end3(lst))


#Exercise 9
def sum2(lst:list):
    if len(lst) == 0 and 1:
        return [0] * len(lst)
    return sum(lst[:-1]) #cant use slicing
lst = [1,2,3]
print (sum2(lst))


#Exercise 10
def middle_way(lst1:list, lst2:list):
    return [lst1[1], lst2[1]]
lst1 = [1,2,3]
lst2 = [4,5,6]
print (middle_way(lst1,lst2))


#Exercise 11
def make_ends(lst:list):
    return [lst[0],lst[-1]]
lst = [4,5,6,7]
print (make_ends(lst))


#Exercise 12
def has23(lst:list):
    if 2 or 3 in lst:
        return True
    return False
lst = [1,2,3]
print(has23(lst))