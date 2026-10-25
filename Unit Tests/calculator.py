
#z = round(x + y)
#print(f"{z:,}")

#z = round(x / y, 2)

#print(f"{z:.2f}")

def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "___main___":
    main()