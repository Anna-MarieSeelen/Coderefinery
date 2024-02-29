
def fizz_buzz(value):
    if value <= 0:
        raise ValueError("Input number higher than zero")
    elif value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return value
