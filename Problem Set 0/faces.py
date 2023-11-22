def main():
    print(convert(input))

def convert(input):
    input = input("Please provide input")
    input = input.replace(':)', '🙂')
    input = input.replace(':(', '🙁')
    return input

main()