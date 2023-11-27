def main():
    fraction = input("What fraction of the tank is full?").split("/")
    try:
        numerator = int(fraction[0])
        denominator = int(fraction[1])
    except (ValueError, ZeroDivisionError):
        print("That was not an acceptable fraction. Please try again.")

    print(f"{fuel_percentage(numerator, denominator)}%")


def fuel_percentage(x, y):
    try:
        percentage = int(x/y)
        return percentage
    except (ValueError, ZeroDivisionError):
        print("That was not an acceptable fraction. Please try again.")


main()