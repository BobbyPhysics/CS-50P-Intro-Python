# prompt user for a level, n
# generate 10 addition problems (X + Y = )
# where X and Y are both non-negative integers

import random


def main():
    num_problems = 10
    level = get_level()
    attempt = 0
    num_attempts = 3
    score = 0

    for _ in range(num_problems):
        X = generate_integer(level)
        Y = generate_integer(level)
        while attempt < num_attempts:
            try:
                answer = int(input(f'{X} + {Y} = '))
            except ValueError:
                print('EEE')
                attempt += 1
                continue
            else:
                if answer == X + Y:
                    score += 1
                    attempt = 0
                    break
                else:
                    print('EEE')
                    attempt += 1
                    continue
        if attempt >= num_attempts:
            print(f'{X} + {Y} = {X + Y}')
            attempt = 0
    print(f'Score: {score}')


def get_level():
    level_list = [1, 2, 3]
    while True:
        try:
            level = int(input("Level:"))
        except ValueError:
            continue
        if level in level_list:
            break
        else:
            continue
    return level


def generate_integer(level):
    # get random ranges from 0-9, 10-99, 100-999 depending on level
    integer = random.randint((10**(level-1)-(0**(level-1))), (10**level-1)) # this depends on 0^0 = 1 so that level 1 starts at 0 instead of 1.
    return integer


if __name__ == "__main__":
    main()
