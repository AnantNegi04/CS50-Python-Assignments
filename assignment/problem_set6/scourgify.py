import csv
import sys

def main():
    scourgify()

def scourgify():
    names = []
    try:
        if len(sys.argv) < 3:
            print("Too few arguments")
            sys.exit()

        elif len(sys.argv) > 3:
            print("Too many arguments")
            sys.exit()

        elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
            print("Not a valid file")
            sys.exit()

        with open(sys.argv[1], "r") as input_file:
            reader = csv.DictReader(input_file)

            for row in reader:
                last, first = row["name"].split(",")
                names.append({
                    "first": first.strip(), 
                    "last": last.strip(),
                    "house": row["house"]
                })
                    
        with open(sys.argv[2], "w", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])

            writer.writeheader()

            for row in names:
                writer.writerow(row)

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit()

if __name__ == "__main__":
    main()