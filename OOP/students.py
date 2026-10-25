def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("What's your name: ")
    house = input("What's your house: ")
    return (name, house)

if __name__ == "__main__":
    main()