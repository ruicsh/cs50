import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(.+) to (.+)", s):
        am, pm = matches.groups()
        am = convert_time(am)
        pm = convert_time(pm)

        return f"{am} to {pm}"


def convert_time(time):
    if matches := re.search(r"(\d{1,2}):?(\d{2})?\s?([A|P]M)", time):
        hours, minutes, meridiem = matches.groups()
        hours = int(hours)

        if minutes is not None:
            minutes = int(minutes)
        else:
            minutes = 0

        if not 0 <= minutes < 60:
            raise ValueError

        if meridiem == "PM":
            if not 0 <= hours <= 12:
                raise ValueError

            hours += 12

        return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
