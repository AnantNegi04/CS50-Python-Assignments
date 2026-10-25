import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    from_time = ""
    to_time = ""
    matches = re.search(r"^(([0-9]+)(?::([0-9]{2}))?\ (AM|PM))\ to\ (([0-9]+)(?::([0-9]{2}))?\ (AM|PM))$", s, re.IGNORECASE)

    if matches:
        f_hour = matches.group(2)
        f_minute = matches.group(3)
        f_m = matches.group(4).upper()

        t_hour = matches.group(6)
        t_minute = matches.group(7)
        t_m = matches.group(8).upper()

        # Validate hours
        if not 1 <= int(f_hour) <= 12:
            return ""

        if not 1 <= int(t_hour) <= 12:
            return ""

        # Missing minutes = 00
        if f_minute is None:
            f_minute = "00"

        if t_minute is None:
            t_minute = "00"

        # Validate minutes
        if int(f_minute) > 59 or int(t_minute) > 59:
            return ""

        # Convert first hour
        f_hour = int(f_hour)

        if f_m == "AM":
            if f_hour == 12:
                f_hour = 0
        else:
            if f_hour != 12:
                f_hour += 12

        # Convert second hour
        t_hour = int(t_hour)

        if t_m == "AM":
            if t_hour == 12:
                t_hour = 0
        else:
            if t_hour != 12:
                t_hour += 12

        from_time = f"{f_hour:02}:{int(f_minute):02}"
        to_time = f"{t_hour:02}:{int(t_minute):02}"

    return f"{from_time} to {to_time}"


if __name__ == "__main__":
    main()