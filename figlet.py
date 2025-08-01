import sys
import random
from pyfiglet import Figlet



def main():
    figlet = Figlet()
    fonts = figlet.getFonts()


    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3:
        option = sys.argv[1]
        font = sys.argv[2]
        if option not in ["-f", "--font"]:
            sys.exit("Invalid usage: Use -f or --font to specify font")
        if font not in fonts:
            sys.exit("Invalid font name")
    else:
        sys.exit("Usage: python figlet.py [-f fontname]")
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
