def dollars_to_float(d):
    # remove $ sign
    d = d.replace('$', '')
    return float(d)

def percent_to_float(p):
    # remove % sign
    p = float(p.replace('%', ''))
    # convert to percent
    p = p/100
    return float(p)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()