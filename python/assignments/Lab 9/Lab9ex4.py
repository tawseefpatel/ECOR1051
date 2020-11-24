def centered_average(new_list:list):
    """
    """
    n = len(new_list)
    
    return sum(new_list)/n

lst = [1,1,5,5,10,8,7]
new_list = sorted(lst)
del(new_list[0], new_list[-1])
print(centered_average(new_list))
