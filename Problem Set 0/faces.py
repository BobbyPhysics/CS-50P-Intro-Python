def convert(input): # convert text into emoji
    input = input("Please provide input")
    input = input.replace(':)', '🙂')
    input = input.replace(':(', '🙁')
    return input

def main():
    print(convert(input))

main()