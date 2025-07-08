def get_number():
    while True:
        n = int(input("How many meows?"))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

def main():
    number = get_number()
    meow(number)

if __name__ == "__main__":
    main()