import random


def main():
    l = get_level()
    marks = 0

    count = 10
    while count > 0:

        x, y = generate_integer(l)
        expAns = x + y
        retry = 3

        while retry > 0:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == expAns:
                    count -= 1
                    if retry == 3:
                        marks += 1
                    break
                else:
                    retry -= 1
                    print("EEE")
            except ValueError:
                print("EEE")
                retry -= 1

        if retry == 0:
            print(f"{x} + {y} = {expAns}")

    print("Score:", marks)

def get_level():
    while True:
        try:
            l = int(input("Level: "))

            if l in {1, 2, 3}:
                return l
        except ValueError:
            pass



def generate_integer(level):
    n = 10
    digits = pow(n, level) - 1
    return random.randint(1, digits), random.randint(1, digits)


if __name__ == "__main__":
    main()