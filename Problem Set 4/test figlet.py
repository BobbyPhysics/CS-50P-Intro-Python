from pyfiglet import Figlet

figlet = Figlet(width=200)
font_list = figlet.getFonts()

try:
    with open("c:\\Users\\rxhac\\OneDrive\\Desktop\\figlet_fonts.txt", "w", encoding="utf-8") as file:
        for font_name in font_list:
            figlet.setFont(font=font_name)
            rendered_text = figlet.renderText(font_name[:8])
            if rendered_text.strip():  # Check if rendered text is not empty
                file.write(f"Font name: {font_name}\n"
                           f"{rendered_text} + \n\n")
except Exception as e:
    print(f"An error occurred: {e}")
