from tabulate import tabulate
import csv
import sys

def main():
    table()

def table():
    table = []
    
    if len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit()

    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit()

    if sys.argv[1] == "regular.csv":
        header = ["Regular Pizza", "Small", "Large"]
    elif sys.argv[1] == "sicilian.csv":
        header = ["Sicilian Pizza", "Small", "Large"]
    else:
        print("Invalid file")
        sys.exit()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)

            for row in reader:
                table.append(row)

        print(tabulate(table, headers=header, tablefmt="grid"))

    except FileNotFoundError:
        print("File not found")
        sys.exit()

if __name__ == "__main__":
    main()