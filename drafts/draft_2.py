import re


def calculator():
    # We start by doing a small introduction and then
    # asking the user for an equation
    print("Welcome to the Calculator, to exit type 'Go to sleep!' or Ctrl + C")

    while True:
        try:
            input1 = input("Enter an equation (maximum of 6 numbers): ")

        except KeyboardInterrupt:
            print("\nExiting Calculator...")
            break

        if input1.lower() in ["go to sleep!", "quit", "go to sleep", "gts", "exit"]:
            print("Exiting Calculator...")
            break

        # We check if the user's equation is in our 6 nr. limit
        # and if the syntax is correct
        try:
            # We use RegEx (Regular Expression Operations) to check
            # r"" → a raw string, so \d+\.?\d* is treated correctly by Python
            # \d+ - one or more digits
            # \.? - optional decimal point (the ? means 0 or 1)
            # \d* - zero or more digits after the decimal (the * means 0 or more)
            numbers1 = re.findall(r"\d+\.?\d*", input1)

            if len(numbers1) > 6:
                print(f"{len(numbers1)} exceeds the max numbers (6)")

            else:
                equation1 = input1
                print(f"This is your equation: {equation1}")
                # We replace any x's from the syntax with *
                # and then we get the result using eval
                result1 = round(eval(input1.replace("x", "*")), 3)
                print(f"Result: {result1}")

                while True:
                    # We make a loop so the user can keep making
                    # equations user the last operation's result
                    while True:
                        try:
                            q = input(
                                f"Do you want to continue with the previous result({result1})? (Y/N): "
                            )
                            if q == "y":
                                break
                            elif q == "n":
                                print("Going back...")
                                break
                            else:
                                print("Please type 'Y' for yes or 'N' for no.")

                        except KeyboardInterrupt:
                            print("\nExiting Calculator...")
                            return

                    if q.lower() == "n":
                        break

                    try:
                        input2 = input(
                            f"Enter an equation to add to {result1} (maximum of 5 numbers), start with either +, -, *, /: "
                        )

                    except KeyboardInterrupt:
                        print("\nGoing back...")
                        break

                    if input2.lower() in [
                        "go to sleep!",
                        "quit",
                        "go to sleep",
                        "gts",
                        "exit",
                    ]:
                        print("Going back...")
                        break

                    numbers2 = re.findall(r"\d+\.?\d*", input2)

                    # This makes sure the second input starts with a symbol
                    # so eval can calculate
                    if not input2 or input2[0] not in ["+", "-", "*", "/"]:
                        print("Equation must start with +, -, *, or /")

                    elif len(numbers2) > 5:
                        print(f"{len(numbers2)} exceeds the max numbers (5)")

                    # We combine the previous result with the new input
                    # and replace the previous result so the loop continues
                    else:
                        equation2 = f"({result1}) {input2}"
                        print(f"This is your equation: {equation2}")
                        try:
                            result1 = round(eval(equation2.replace("x", "*")), 3)
                            print(f"Result: {result1}")
                        except (
                            ValueError,
                            SyntaxError,
                            ZeroDivisionError,
                            NameError,
                        ) as error:
                            print(f"Invalid equation: {error}")

        except (ValueError, SyntaxError, ZeroDivisionError, NameError) as error:
            print(f"Invalid equation: {error}")


calculator()
