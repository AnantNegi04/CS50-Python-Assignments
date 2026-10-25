def main():
    coke_price = 50
    coke(coke_price)

def coke(price):
    priceLeft = price
    while True:
        input_money = int(input("Insert Coin: "))
        if input_money == 25 or input_money == 10 or input_money == 5:
            priceLeft = priceLeft - input_money
            if priceLeft > 0:
                print("Amount Due: ", priceLeft)
                print("Change Owed: 0")
            elif priceLeft < 0:
                print("Amount Due: 0")
                print("Change Owed:", -(priceLeft))
                break
            else:
                print("Amount Due: 0")
                print("Change Owed: 0")
                break
        else:
            continue
        

if __name__ == "__main__":
    main()
