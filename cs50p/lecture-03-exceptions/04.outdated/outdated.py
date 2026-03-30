months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    year, month, day = get_user_date()
    iso_date = get_iso_date(year, month, day)
    print(iso_date)


def get_user_date():
    while True:
        try:
            date = input("Date: ")
            if date.find("/") > -1:
                month, day, year = date.split("/")
            else:
                monthday, year = date.split(",")
                month_str, day = monthday.split(" ")
                month_str = month_str.strip()
                month = months.index(month_str.title()) + 1

                day = day.strip()

                year = year.strip()

            year = int(year)
            month = int(month)
            day = int(day)

            if month > 12:
                raise ValueError
            if int(day) > 31:
                raise ValueError

            return year, month, day
        except ValueError:
            pass


def get_iso_date(year, month, day):
    return f"{year}-{month:02}-{day:02}"


main()
