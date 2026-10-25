from bank import value

def main():
    test_bank()

def test_bank():
    assert value("Hello") == "$0"
    assert value("Hieee") == "$20"
    assert value("hihh") == "$20"
    assert value("morning") == "$100"


if __name__ == "__main__":
    main()