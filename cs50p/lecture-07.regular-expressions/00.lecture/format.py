import re
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit()

    name = sys.argv[1].strip()
    if matches := re.search(r"(^.+), *(.+)$", name):
        last, first = matches.groups()
        name = f"{first} {last}"

    print(f"hello, {name}")


main()
