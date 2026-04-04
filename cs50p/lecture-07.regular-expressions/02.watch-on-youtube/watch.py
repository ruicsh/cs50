import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url_matches := re.search(r"src=['|\"](.+)['|\"]", s):
        (url,) = url_matches.groups()

        if url and (slug_matches := re.search(r"embed/(.+)", url)):
            (slug,) = slug_matches.groups()

            if slug:
                return f"https://youtu.be/{slug}"


if __name__ == "__main__":
    main()
