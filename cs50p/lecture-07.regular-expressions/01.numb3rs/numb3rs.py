import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip):
        is_valid = True
        for n in matches.groups():
            is_valid = is_valid and is_valid_number(n)
        return is_valid
    return False


def is_valid_number(n):
    return 0 <= int(n) <= 255


if __name__ == "__main__":
    main()
