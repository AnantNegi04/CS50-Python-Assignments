from pyfiglet import Figlet
import random
import sys

def main():
    s = input("Input: ")
    font_change(s)

def font_change(s):
    figlet = Figlet()

    l = figlet.getFonts()

    if len(sys.argv) == 1:

        r = random.choice(l)
        figlet.setFont(font=r)
        
    elif len(sys.argv) == 3:
            
        if sys.argv[1] not in ("--font", "-f"):
            sys.exit("Invalid usage")

        if sys.argv[2] not in l:
            sys.exit("Invalid usage")      

        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid usage") 

    print(figlet.renderText(s))

if __name__ == "__main__":
    main()

