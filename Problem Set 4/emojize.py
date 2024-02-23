from emoji import emojize


input = input("What emoji do you want to see?")
emojized_input = emojize(input, language="alias")
print(
    f"Input: {input}\n"
    f"Output: {emojized_input}"
    )