def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
            
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()