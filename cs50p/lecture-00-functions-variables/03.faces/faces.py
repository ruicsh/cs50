def main():
    str = input()
    print(convert(str))


def convert(input):
    return input.replace(":)", "🙂").replace(":(", "🙁")


main()
