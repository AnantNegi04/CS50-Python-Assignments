def main():
    great_question()

def great_question():
    answer = input("What's the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer == "42" or answer == "forty two" or answer == "forty-two" or answer == "Forty two":
        print("Yes")
    else:
        print("No")

main()