class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self):
        return f"I am {self.name}"

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{super().__str__()} from {self.house}"

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()} proferssor of {self.subject}"

def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against Dark Arts")
    print(wizard)
    print(student)
    print(professor)

if __name__ == "__main__":
    main()