def main():
    greeting = input("greeting: ")
    print(value(greeting))

def value(greeting):
    if greeting.startswith("Hello"):
        return "$0"
    elif "h" in greeting or "H" in greeting:
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()