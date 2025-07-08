# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case 
# and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.

text = input("write in camelCase: ")

for i in text:
    if i.isupper():
       text = text.replace(i, "_"+i.lower()) # replaces uppercase with _lowercase

print(text)