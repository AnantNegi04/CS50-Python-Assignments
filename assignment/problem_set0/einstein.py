def main():
    takeInput = int(input("m: "))
    print("e:", energy(takeInput))

def energy(m):
    return m * 300000000 * 300000000 

main()