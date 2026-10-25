import sys

def main():
    print(read_lines())

def read_lines():
    try:
          
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit()
        if not sys.argv[1].endswith(".py"):
            print("Not a python file")
            sys.exit()

        with open(sys.argv[1]) as file:
            count = 0
            for row in file:
                if row.startswith("#") or row.isspace():
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

    return count

if __name__ == "__main__":
    main()