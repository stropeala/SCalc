def calculator():
    # We ask the use to input two numbers and an operation
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    calcul = input("Enter the operation you want to make(+, -, /, * ): ")

    # We verify if the input of the user is indeed a number
    try:
        a = float(a)
    except ValueError:
        print("First input was not a number")
    try:
        b = float(b)
    except ValueError:
        print("Second input was not a number")

    # We make the app calculate the users desired operation if it's correct
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
