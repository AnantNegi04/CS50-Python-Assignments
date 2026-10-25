import inflect

def main():
    adieu()

def adieu():
    p = inflect.engine()
    list = []
    
    while True:
        try:
            s = input("Name: ")
            list.append(s)
        except KeyboardInterrupt:
            print()
            print("Adieu, adiue, to", p.join((list), final_sep=""))
            break


if __name__ == "__main__":
    main()
            
