from pyfiglet import Figlet
import sys

figlet = Figlet(width=200)

try:
    if(sys.argv[1]=="-f" or sys.argv[1]=="--font"):
        f = sys.argv[2] #big #bulbhead #3d-ascii #caligraphy #calgphy2 #doh #doom
        figlet.setFont(font=f)
    else:
        raise ValueError("Invalid usage")
except:
    print("Invalid usage")
    sys.exit(1)

s = sys.argv[3] #input("Input: ")

print(figlet.renderText(s))

