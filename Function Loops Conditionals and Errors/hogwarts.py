# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])
"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor", 
    "Ron": "Gryffindord", 
    "Draco": "Slytherin" 
}
"""

students = [
    {"Name" : "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name" : "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name" : "Ron", "House": "Gryffindor", "Patronus": "Jack Russell terrier"},
    {"Name" : "Draco", "House": "Slytherin", "Patronus": None}

]

for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep=", ")

