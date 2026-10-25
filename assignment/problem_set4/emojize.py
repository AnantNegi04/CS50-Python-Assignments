import emoji  # type: ignore


def main():
    emo = input("Input: ")
    emojizey(emo)


def emojizey(e):
    print(f"Output: {emoji.emojize(e)}")


if __name__ == "__main__":
    main() 