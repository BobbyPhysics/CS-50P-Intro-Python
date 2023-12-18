def main():
    percent = get_percent()

    match percent:
        case 99 | 100:
            print("F")
        case 0 | 1:
            print("E")
        case _:
            print(f"{percent}%")

def get_percent():
    while True:
        try:
            fraction = input("What fraction of the tank is full?").split("/")
            numerator = int(fraction[0])
            denominator = int(fraction[1])
            if (numerator > denominator) :
                raise ValueError()
            return round((numerator/denominator)*100)
        except (ValueError, ZeroDivisionError, IndexError)  :
            print("That was not an acceptable fraction. Please try again.")


main()