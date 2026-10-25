from plates import is_valid

def main():
    test_plates()

def test_plates():
    assert is_valid("CS50") == True