def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting):.02f}")


def value(greeting):
    word = greeting.lower()
    if word.startswith("hello"):
        return 0
    elif word.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
