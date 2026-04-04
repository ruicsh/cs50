import pathlib
import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not get_file_extension(filename) == ".py":
        sys.exit("Not a Python file")

    print(count_lines_of_code(filename))


def get_file_extension(filename):
    file_path = pathlib.Path(filename)
    return file_path.suffix


def count_lines_of_code(filename):
    lines_of_code = 0
    try:
        with open(filename) as file:
            for line in file:
                if is_line_of_code(line):
                    lines_of_code += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return lines_of_code


def is_line_of_code(line):
    trimmed = line.strip()

    if len(trimmed) == 0:
        return False

    if trimmed[0] == "#":
        return False

    return True


main()
