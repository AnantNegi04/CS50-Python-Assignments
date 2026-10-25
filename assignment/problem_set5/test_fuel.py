from fuel import convert, gauge

def main():
    test_fuel()

def test_fuel():
    assert convert("1/4") == 25 
    assert gauge(25) == "25%"
    assert convert("2/4") == 50
    assert gauge(50) == "50%"
    assert convert("0/4") == 0
    assert gauge(0) == "E"
    assert convert("1/0") == "tank capacity cannot be zero"
    assert convert("cat") == "Input should be positive integer"
