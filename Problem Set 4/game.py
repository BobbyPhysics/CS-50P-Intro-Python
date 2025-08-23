# prompt user for a level, n
# close if user does not enter a positive integer
# generate a random integer between 1 and n
# prompt user to guess the number. reprompt until user guesses a positive integer

import random

# Prompt user for "Level" n and check that it's a positive integer
while True:
    try:
        n = int(input("Level:"))
    except ValueError:
        continue
    if n > 0:
        break
    else:
        continue

# Generate random integer between 1 and n
target = random.randrange(1,n+1)

# Prompt user to guess a positive integer
while True:
    try:
        user_guess = int(input("Guess:"))
    except ValueError:
        continue
    if user_guess > 0:
        if user_guess == target:
            print("Just right!")
            break
        elif user_guess < target:
            print("Too small!")
        elif user_guess > target:
            print("Too large!")
    else:
        continue

