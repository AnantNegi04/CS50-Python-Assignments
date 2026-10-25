from jar import Jar
import pytest

def test_init():
    jar1 = Jar(30)
    assert jar1.capacity == 30
    jar2 = Jar()
    assert jar2.capacity == 12
    assert jar1.size == 0
    assert jar2.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(capacity=5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():
    jar = Jar(capacity=10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3