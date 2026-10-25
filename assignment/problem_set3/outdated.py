def main():
    dates()

def dates():
    d = [
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
        "December"
    ]

    while True:
        try:
            date = input("Date: ")

            if "/" in date:
                day, month, year = date.split("/")

            else:
                day, month, year = date.replace(",", "").split()
                month = d.index(month) + 1

            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
            
        except (ValueError, IndexError):
            pass


if __name__ == "__main__":
    main()