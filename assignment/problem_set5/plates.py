def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    string = str(s)
    
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    if not s.isalnum():
        return False
    

    # If there are numbers, they must all be at the end
    # and the first number cannot be 0
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and i == 2:
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


if __name__ == "__main()__":
    main()