import pytest
from fizz_buzz import fizz_buzz

def test_fizz_buzz():
    with pytest.raises(ValueError):
        assert fizz_buzz(-10) == ValueError("Input a number higher than zero")
    assert fizz_buzz(9) == "Fizz"
    assert fizz_buzz(50) == "Buzz"
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(1) == 1