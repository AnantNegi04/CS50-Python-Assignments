#name = input("What's your name?")

#remove white space from string & capitalize user's name
#name = name.strip().title()

#first, last = name.split(" ")

#print("hello,", name, end="", sep='???')

def main():
    hello()
    name = input("What's your name?")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()