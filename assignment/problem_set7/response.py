from validator_collection import validators

def main():
    email = input("What's your email address? ")
    validate(email)

def validate(s):
    try:
        email_address = validators.email(s, allow_empty = True)
        if email_address:
            print("valid")
        else:
            print("invalid")
    except ValueError:
        print("invalid")

if __name__ == "__main__":
    main()
