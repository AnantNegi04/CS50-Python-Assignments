from twttr import ommit

def main():
    test_ommit()
    test_case()


def test_ommit():
    assert ommit("Anant") == "nnt"
    assert ommit("twttr") == "twttr" 
    assert ommit("hello") == "hll"
    assert ommit("AEIOU") == ""
    assert ommit("aeiou") == ""

def test_case():
    assert ommit("HELLO") == "HLL"
    assert ommit("Hello World") == "Hll Wrld"


if __name__ == "__main__":
    main()