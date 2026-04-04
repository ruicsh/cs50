import re
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit()

    email = sys.argv[1].strip()

    if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")


main()
