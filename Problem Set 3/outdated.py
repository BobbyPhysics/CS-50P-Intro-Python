months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def format_date():
    while True:
        # get user input in form mm/dd/yyyy or month dd, yyyy
        date = input("Date: ")
        try:
            # for the first case, split on /
            month, day, year = date.split("/")
            if 1 <= int(month) <= 12 and 1<= int(day) <= 31:
                break
        # nesting another "try" for the second case
        except:
            try:
                # for the second case, remove comma and split on spaces
                date = date.replace(",", "")
                string_month, day, year = date.split(" ")
                string_month = string_month.capitalize()
                # compare string_month to the list of months
                for i in range(len(months)):
                    if string_month == months[i]:
                        month = i + 1
                if 1<= int(month) <= 12 and 1 <= int(day) <= 31:
                    break
            except:
                break
    print(f"{year}-{int(month):02}-{int(day):02}")

def main():
    format_date()

if __name__ == "__main__":
    main()