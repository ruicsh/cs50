def main():
    percent = get_percent()
    print(f"{percent:.0f}%")


def get_percent():
    while True:
        try:
            fraction = input("Fraction: ")
            return convert(fraction)
        except ValueError, ZeroDivisionError:
            pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x > y:
            raise ValueError

        if y == 0:
            raise ZeroDivisionError

        return round((x / y) * 100)
    finally:
        ...


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
