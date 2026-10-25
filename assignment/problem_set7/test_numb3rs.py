from numb3rs import validate

def main():
    test_all_ip()
    test_invalid_ip()

def test_all_ip():
    assert validate("192.168.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("8.8.8.8") == True

def test_invalid_ip():
    assert validate("Cat") == False
    assert validate("999.999.999.999") == False
    assert validate("256.0.0.0") == False
    assert validate("255.255.255.256") == False

if __name__ == "__main__":
    main()