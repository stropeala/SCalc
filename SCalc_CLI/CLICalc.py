from math_utils import addition, division, multiplication, percentage, subtraction
from parser import parser

if __name__ == "__main__":
    print(addition(10, 2))
    print(subtraction(10, 2))
    print(multiplication(10, 2))
    print(division(10, 2))
    print(percentage(50, 144))
    print(parser("25% * 250"))
    print(parser("(18/(2+2x2))"))
    print(parser("18/2+2x2"))
    print(parser("1/100+2+3/2"))
    print(parser(input("Please enter an equation: ")))
