balance = 0

def deposit(n):
    global balance 
    balance += n

def withdraw(n):
    global balance
    balance -= n

def main():
    deposit(100)
    withdraw(20)
    print(balance)

if __name__ == "__main__":
    main()