def main():
    print_row(4)
    print_column(3)
    print_square(3)


def print_row(width):
    print("#" * width)


def print_column(height):
    for _ in range(height):
        print("#")


def print_square(size):
    for row in range(size):
        print_row(size)


main()
