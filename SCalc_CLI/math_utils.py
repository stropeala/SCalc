def addition(a: float, b: float) -> float:
    # We made a function for addition
    return a + b


def subtraction(a: float, b: float) -> float:
    # We made a function for subtraction
    return a - b


def multiplication(a: float, b: float) -> float:
    # We made a function for multiplication
    return a * b


def division(a: float, b: float) -> float:
    # We made a function for division
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def percentage(percent: float, b: float) -> float:
    # We made a function for percentages
    return (percent / 100) * b


print(addition(10, 2))
print(subtraction(10, 2))
print(multiplication(10, 2))
print(division(10, 2))
print(percentage(50, 250))
