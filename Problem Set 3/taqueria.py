menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    get_order()

def get_order():
    total = 0
    while True:
        try:
            order = input("What would you like to order?\n").title()
            total += menu[order]
            print(f"Total: ${total:.2f}")
        except EOFError: #press CTRL+Z in VS Code
            print(f"Your total is ${total:.2f}.")
            break
        except KeyError:
            print("We don't have those.")


main()