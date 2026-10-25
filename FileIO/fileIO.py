students = []

with open("names.csv", "r") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]


for s in sorted(students, key=get_house):
    print(f"{s['name']} is in {s['house']}")






