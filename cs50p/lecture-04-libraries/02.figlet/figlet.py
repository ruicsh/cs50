import sys

import pyfiglet
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3 and sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid font")

    text = input("Input: ")

    f = pyfiglet.figlet_format(text, font=sys.argv[2])
    print(f)


main()
