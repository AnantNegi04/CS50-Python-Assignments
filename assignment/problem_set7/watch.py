import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        
        matches = re.search(r'src="https?://(www\.)?youtube\.com/embed/(.+?)"', s)

        if matches:
            return f"https://youtu.be/{matches.group(2)}"

        return ""

    except ValueError:
        sys.exit()


if __name__ == "__main__":
    main()