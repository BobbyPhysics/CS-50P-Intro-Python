def get_names(list):
    """get a list of names from user input until EOF"""

    print("To whom do you say 'adieu'?")
    try:
        while True:
            names = input()
            list.append(names)
    except EOFError:
        pass

def bid_adieu(list):
    """join names in a list with commas and 'and' before the last item"""

    joined_names = ", ".join(list[:-1])

    if len(list) == 1:
        print(f"Adieu, adieu, to {list[0]}.")
    elif len(list) == 2:
        print(f"Adieu, adieu, to {list[0]} and {list[1]}.")
    else:
        print(f"Adieu, adieu, to {joined_names}, and {list[-1]}.")

def main():
    name_list = []
    get_names(name_list)
    bid_adieu(name_list)

if __name__ == "__main__":
    main()
