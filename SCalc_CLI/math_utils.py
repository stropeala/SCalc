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
