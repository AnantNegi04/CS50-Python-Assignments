import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = []
    matches = re.findall(r"(\bum,?)\ ?", s, re.IGNORECASE)
    print(matches)
    return len(matches)

...


if __name__ == "__main__":
    main()