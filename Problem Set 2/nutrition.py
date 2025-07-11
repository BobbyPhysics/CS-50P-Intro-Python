# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and 
# then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. 
# Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). 
# Ignore any input that isn’t a fruit.

fruits = [ # dictionary of fruits
    {"fruit":"apple", "calories":130},
    {"fruit":"avocado", "calories":50},
    {"fruit":"banana", "calories":110},
    {"fruit":"cantaloupe", "calories":50},
    {"fruit":"grapefruit", "calories":60},
    {"fruit":"grapes", "calories":90},
    {"fruit":"honeydew melon", "calories":50},
    {"fruit":"kiwifruit", "calories":90},
    {"fruit":"lemon", "calories":15},
    {"fruit":"lime", "calories":20},
    {"fruit":"nectarine", "calories":60},
    {"fruit":"orange", "calories":80},
    {"fruit":"peach", "calories":60},
    {"fruit":"pear", "calories":100},
    {"fruit":"pineapple", "calories":50},
    {"fruit":"plums", "calories":70},
    {"fruit":"strawberries", "calories":50},
    {"fruit":"sweet cherries", "calories":100},
    {"fruit":"tangerine", "calories":50},
    {"fruit":"watermelon", "calories":80},
]


def calories_in_fruit(i):
    for fruit in fruits:
         if fruit["fruit"]==i:
               print(fruit["calories"])

def main():
    item = input("Item: ").lower()
    return calories_in_fruit(item)

if __name__ == "__main__":
    main()