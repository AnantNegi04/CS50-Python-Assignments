from hello import hello

def main():
    test_default()
    test_arguments()

def test_default():
    assert hello() == "hello, world"

def test_arguments():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

if __name__ == "__main__":
    main()