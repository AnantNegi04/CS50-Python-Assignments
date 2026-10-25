import csv

students = []

# with open("namesAndHouse.csv", "r") as file:
#     names = csv.reader(file)
#     for row in names:
#         students.append({"name":row[0], "home":row[1]})

# for s in sorted(students, key=lambda s: s["home"]):
#     print(f"{s['name']} lives in {s['home']}")

# with open("namesAndHouse.csv", "r") as file:
#     names = csv.DictReader(file)
#     for row in names:
#         students.append({"name":row["names"], "home":row["home"]})

# for s in sorted(students, key=lambda s: s["home"]):
#     print(f"{s['name']} lives in {s['home']}")

# name = input("What's your name? ")
# home = input("What's your home? ")

# with open("students.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})
