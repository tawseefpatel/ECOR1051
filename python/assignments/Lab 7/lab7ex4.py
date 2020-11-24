def blackjack(a:int, b:int):
    """return whatever value is closest to 21. with values not exceeding 21.
    >>>blackjack(19,20)
    20
    >>>blackjack(17,22)
    17
    """ 
    if a<= 21 and b<=21:
        return max(a,b)
    if a<=21 or b<21:
        return a and b
    return 0
card_number1 = int(input("Choose your first card value:"))
card_number2 = int(input("Choose your second card value:"))

card_numbers = (blackjack(card_number1,card_number2))
print (card_numbers)

        