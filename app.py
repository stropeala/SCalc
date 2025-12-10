def calculator():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    calcul = input("Enter the operation you want to make(+, -, /, * ): ")

    try:
        a = float(a)
    except ValueError:
        print("First input was not a number")
    try:
        b = float(b)
    except ValueError:
        print("Second input was not a number")

    for calcul in calcul:
        if calcul == "+":
            print(float(a) + float(b))
        elif calcul == "-":
            print(float(a) - float(b))
        elif calcul == "*":
            print(float(a) * float(b))
        elif calcul == "/":
            print(float(a) / float(b))
        else:
            print("Not a valid operation")


calculator()
