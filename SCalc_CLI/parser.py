def parser(equation: str):
    # We will make a fucntion that goes through the users input string(equation)
    # and analyses each index of the equation
    indexes = []
    position = 0

    # We make a loop that checks each character and position from the user input string(equation)
    # until it reaches len limit
    while position < len(equation):
        character = equation[position]

        # If the parser finds a character that is a space,
        # it skips it and goes to the next position
        if character.isspace():
            position += 1
            continue

        # If the parser goes thruogh the user input and if it finds a "-" symbol
        # We know that a number is negative only if it is before a number and
        # if it has another symbol before (or is at the start)
        # The parser then checks to see if it has/has not another symbol before the "-"
        # and we get the last digit(last_neg_pos) and the first digit(last known position)
        # and make a negative number from the first digit to the last
        # and add that negative number to the index list
        if character == "-" and (
            len(indexes) == 0 or indexes[-1] in ["+", "-", "*", "x", "X", "/", "("]
        ):
            # The pasrser starts from the first character after "-"
            neg_last_pos = position + 1

            # We make a loop that after it finds a "-" and another symbol before or not it
            # checks if every "last" character is a digit or a dot so its added to the negative number
            # It's something like:
            # this is the user input string(equation): "-1.23"
            # the parser goes throug each character/position
            #
            # ˅˅˅˅˅˅˅˅˅˅˅(finds digits and it goes neg_last_pos(-),neg_last_pos(1),neg_last_pos(.),neg_last_pos(2),neg_last_pos(3))
            # -1.23
            #
            # Then gets all those neg_last_pos characters and appends them to
            # to the position last known before it turns to neg_last_pos, i.e. when it detects a digit
            # to form the number
            while neg_last_pos < len(equation) and (
                equation[neg_last_pos].isdigit() or equation[neg_last_pos] == "."
            ):
                neg_last_pos += 1
            indexes.append(float(equation[position:neg_last_pos]))
            position = neg_last_pos
            continue

        # If the character is a digit or a dot
        # we get the last digit(last_pos) and the first digit(last known position)
        # and make a number from the first digit to the last
        # and add that number to the index list
        if character.isdigit() or character == ".":
            last_pos = position

            # We make a loop that checks if every "last" character is a digit or a dot
            # so its added to the number
            # It's something like:
            # this is the input string: "1.23"
            # the parser goes throug each character/position
            #
            # ˅˅˅˅˅˅˅˅(finds digits and it goes last_pos(1),last_pos(.),last_pos(2),last_pos(3))
            # 1.23
            #
            # Then gets all those last_pos characters and appends them to
            # to the position last known before it turns to last_pos, i.e. when it detects a digit
            # to form the number
            while last_pos < len(equation) and (
                equation[last_pos].isdigit() or equation[last_pos] == "."
            ):
                last_pos += 1

            number = float(equation[position:last_pos])
            position = last_pos  # We make the position of the parser the positon after the number

            # We immediately check for a % symbol after the formed number above
            # If there is a % we add it to the number
            if position < len(equation) and equation[position] == "%":
                indexes.append(("PERCENT", number))
                position += 1
            else:
                indexes.append(number)
            continue

        # If the parser finds one of these characters,
        # it adds them to the index list
        if character in ["+", "-", "*", "x", "X", "/", "(", ")"]:
            indexes.append(character)
            position += 1
            continue

        # If it detects anything other than what is specified it raises a ValueError
        raise ValueError(f"Invalid character: {character}")

    # We return the parsed index list from the input string
    return indexes
