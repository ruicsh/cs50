import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    filename_in = sys.argv[1]
    filename_out = sys.argv[2]

    students = []

    try:
        with open(filename_in) as file:
            reader = csv.DictReader(file)
            for row in reader:
                first, last = row["name"].split(",")
                student = {
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"],
                }
                students.append(student)
    except FileNotFoundError:
        sys.exit(f"Could not read {filename_in}")

    with open(filename_out, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


main()
