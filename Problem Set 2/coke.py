# In a file called coke.py, implement a program that prompts the user to insert a coin, 
# one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

payment = 0
amount_due = 50
refund = 0
currency = [5, 10, 25]

while payment < 50:
    coin = int(input("Insert Coin:"))

    if coin in currency: # rebalance payment and amount_due
        payment = payment + coin
        amount_due = amount_due - coin

    if amount_due > 0:
        print("Amount Due:", amount_due)
    else:
        print("Change Owed:", -1*amount_due)