# In deep.py, implement a program that prompts the user for the answer to
# the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or forty-two or forty two (case-insensitively).
# Otherwise output No.

def main():
    response = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    match response:
        case "42" | "Forty Two" | "forty-two":
            print("yes")
        case _:
            print("no")

main()