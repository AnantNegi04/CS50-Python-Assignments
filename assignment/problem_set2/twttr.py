def main():
    string = input("Input: ")
    string
    print("Output: ", ommit(string))

def ommit(s):
    result = ""
    for c in s:
        if is_vowel(c):
            continue
        else: 
            result += c
    return result
        

def is_vowel(s):
    if s == "A" or s == "E" or s == "I" or s == "O" or s == "U":
        return True
    elif s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
        return True
    else:
        return False

if __name__ == "__main__":
    main()