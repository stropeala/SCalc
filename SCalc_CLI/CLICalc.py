from math_utils import addition, division, multiplication, percentage, subtraction
from parser import parser

if __name__ == "__main__":
    # Math Utilities test
    print("#---------------------------------------------------------------------#")
    print(addition(10, 2))
    print(subtraction(10, 2))
    print(multiplication(10, 2))
    print(division(10, 2))
    print(percentage(50, 144))

    # Parser test
    print("#---------------------------------------------------------------------#")
    print(parser("25% * 250"))
    print(parser("79 + -5"))
    print(parser("(18/(2+2x2))"))
    print(parser("18/2+2x2"))
    print(parser("1/100+2+3/2"))
