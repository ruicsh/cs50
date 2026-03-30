def main():
    fraction = get_fraction()
    percent = fraction * 100
    print(f"{percent:.0f}%")


def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
            return int(numerator) / int(denominator)
        except (ValueError, ZeroDivisionError):
            pass


main()
