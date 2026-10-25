def main():
    
    camel_case()


def camel_case():
    takeInput = input("camelCase: ")
    print("snake_case: ", end="" )
    for c in takeInput:
        if c.isupper():
            print(f"_{c.lower()}", end="")
        else:
            print(c, end="")

main()