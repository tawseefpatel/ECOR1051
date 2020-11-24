def repeat(s: str, n:int) -> int:
    """Return s repeated n times; if n is negative return an empty string
    
    >>>repeat ('yes' , 4)
    yesyesyesyes
    >>>repeat('no', 0)
    '' 
    >>>repeat('no', -2)
    ''
    >>>repeat('yesnomaybe' , 3)
    yesnomaybeyesnomaybeyesnomaybe
    """
    return (s * n)
statement = input("write statement here: ")
repeats_required = 4 #change this value in accordance to how many repeats you want
repeat_statement = repeat(statement, repeats_required)

#print (repeat_statement)




def total_length(s1: str, s2: str) -> int:
    """ Return the sum of the lengths in strings s1 and s2.
    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    14
    """
    return len(s1 + s2)
s1 = input("write your choice of word here: ")
s2 = input("write your second choice of word here: ")  
length = total_length(s1,s2)

#print (length)






def replicate(arg:str) -> str:
    """returns a new string that contains copies of arg; the nummber of copies is equal to the number of characters in arg 
    >>>replicate('a')
    'a'
    >>>replicate('abc')
    'abcabcabc'
    """
    return (arg * (len(arg)))
replication_word = input ("what do you want to replicate: ")
word = replicate(replication_word)

#print(word)
