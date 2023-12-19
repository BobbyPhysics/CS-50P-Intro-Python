def main():
    get_item()

def get_item():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError: #press CTRL+Z in VS Code
            for key in sorted(grocery_list.keys()):
                print(f"{grocery_list[key]} {key}\n")
            break


main()