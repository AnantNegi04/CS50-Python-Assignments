import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
            for i in matches.groups():
                i = int(i)
                if i > 255:
                    return False
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()