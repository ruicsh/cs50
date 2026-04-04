import re
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit()

    url = sys.argv[1].strip()

    rg = r"^(?:https?://)?(?:www.)?twitter.com\/(\w+)$"
    if matches := re.search(rg, url, re.IGNORECASE):
        (username,) = matches.groups()

        print(username)


main()
