import sys
import re

from datetime import date

import inflect


class DateOfBirth:
    def __init__(self, input_date):
        if matches := re.search(r"(\d{4})-(\d{2})-(\d{2})", input_date):
            year, month, day = matches.groups()
            try:
                self.date = date(int(year), int(month), int(day))
                self.minutes = self.date
            except ValueError:
                raise ValueError("Invalid Date")
        else:
            raise ValueError("Invalid date")

    def __str__(self):
        p = inflect.engine()
        words = p.number_to_words(self.minutes, andword="")  # type: ignore
        return f"{words} minutes"

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, date):
        self._minutes = (date.today() - date).days * 24 * 60


def main():
    if len(sys.argv) != 2:
        sys.exit()

    dob = DateOfBirth(sys.argv[1])
    print(dob)


if __name__ == "__main__":
    main()
