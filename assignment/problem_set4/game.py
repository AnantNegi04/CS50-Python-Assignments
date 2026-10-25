import random

def main():
    game()

def game():
    n = int(input("Level: "))
    while n < 0:
        n = int(input("Level: "))

    ans = random.randint(1, n)
    while True:
        try:
            g = int(input("Guess: "))

            if g < 0:
                continue

            if ans == g:
                print("Just right!")
                break
            elif g > ans:
                print("Too large!")
            else:
                print("Too small!")
        except ValueError:
            pass

if __name__ == "__main__":
    main()

