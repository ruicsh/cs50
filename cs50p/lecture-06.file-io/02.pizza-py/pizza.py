import csv
import pathlib
import sys

from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]
    if not get_file_extension(filename) == ".csv":
        sys.exit("Not a CSV file")

    table = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for line in reader:
                table.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers="keys", tablefmt="grid"))


def get_file_extension(filename):
    file_path = pathlib.Path(filename)
    return file_path.suffix


main()
