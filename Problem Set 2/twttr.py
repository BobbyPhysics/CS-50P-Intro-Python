# Implement a program that prompts the user for a str of text 
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

vowels = ["A", "E", "I", "O", "U"]

user_input = input("Input:")

def vowel_remover(string):
    output=""
    for letter in string:
        if letter.upper() not in vowels:
            output += letter
    print(output)

vowel_remover(user_input)