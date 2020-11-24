def bank_statement(nums:list)-> list:
    """ returns a new list of three numbers: the first will be the sum of the deposits, the second (a negative number) will be the sum of the withdrawals, and the third will be the current account balance.  """
    deposit = 0
    withdrawl = 0
    for transaction in statement:
        if transaction > 0:
            deposit += round(transaction,2)
        else:
            withdrawl += round(transaction,2)  
    balance = round(deposit + withdrawl, 2)    
    return [deposit, withdrawl, balance]

statement= [30.95, -15.67, 45.565, -55.00, 43.78]
print (bank_statement(statement))   