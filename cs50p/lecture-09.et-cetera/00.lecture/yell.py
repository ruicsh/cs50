def main():
    yell("This", "is", "cs50")
    yell2("This", "is", "cs50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


# list comprehensions
def yell2(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
