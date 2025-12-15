from tkinter import *

# We create the root window
scalc = Tk()

# Root window title and dimensions
scalc.title("SCalc")
scalc.geometry("800x600")

# We create the frames
equationFrame = Frame(scalc, background="black")
equationFrame.pack(fill=BOTH, expand=True)
buttonsFrame1 = Frame(scalc, background="gray15")
buttonsFrame1.pack(fill=BOTH, expand=True)
buttonsFrame2 = Frame(scalc, background="gray15")
buttonsFrame2.pack(fill=BOTH, expand=True)
buttonsFrame3 = Frame(scalc, background="gray15")
buttonsFrame3.pack(fill=BOTH, expand=True)
buttonsFrame4 = Frame(scalc, background="gray15")
buttonsFrame4.pack(fill=BOTH, expand=True)
buttonsFrame5 = Frame(scalc, background="gray15")
buttonsFrame5.pack(fill=BOTH, expand=True)

# We create a text widget for the equation frame
equationText = Entry(
    equationFrame, fg="white", background="black", font=("Calibri 30"), justify="right"
)
equationText.pack(side=LEFT, fill=BOTH, expand=True)


# We create the functions
def add_to_equation(equationText, button_input):
    # We create a function that gets the user Entry input and
    # appends the button input to it

    current_equation = equationText.get()
    equationText.delete(0, END)  # Deletes the Entry box
    equationText.insert(END, current_equation + button_input)


def equation():
    # We create a function that gets the string from the Entry box and
    # calculates the qeuation if its valid using eval

    current_equation = equationText.get()
    equationText.delete(0, END)
    try:
        result = eval(current_equation)  # dont type: __import__('os').system('reboot')
        equationText.insert(END, result)
    except (ValueError, SyntaxError, ZeroDivisionError) as error:
        equationText.insert(END, f"Invalid equation: {error}")


def plus_minus():
    # We create a function that changes
    # wether the number is positive or negative

    # We delete the last number in the Entry box
    current_equation = equationText.get()
    equationText.delete(len(current_equation) - len(current_equation.split()[-1]), END)

    # We now check to see if the number is positive or negative
    number = current_equation.split()[-1]
    if number.startswith("(-") and number.endswith(")"):
        equationText.insert(END, number[2:-1])
    else:
        equationText.insert(END, f"(-{number})")


def delete_equation():
    equationText.delete(0, END)


def delete_last_char():
    equationText.delete(len(equationText.get()) - 1, END)


# We create the buttons
btn1 = Button(
    buttonsFrame4,
    text="1",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "1"),
)
btn2 = Button(
    buttonsFrame4,
    text="2",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "2"),
)
btn3 = Button(
    buttonsFrame4,
    text="3",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "3"),
)
btn4 = Button(
    buttonsFrame3,
    text="4",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "4"),
)
btn5 = Button(
    buttonsFrame3,
    text="5",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "5"),
)
btn6 = Button(
    buttonsFrame3,
    text="6",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "6"),
)
btn7 = Button(
    buttonsFrame2,
    text="7",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "7"),
)
btn8 = Button(
    buttonsFrame2,
    text="8",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "8"),
)
btn9 = Button(
    buttonsFrame2,
    text="9",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "9"),
)
btn0 = Button(
    buttonsFrame5,
    text="0",
    font=("Calibri 15"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "0"),
)
btnDot = Button(
    buttonsFrame5,
    text=".",
    font=("Calibri 12"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "."),
)

btnParenthesesLeft = Button(
    buttonsFrame5,
    text="(",
    font=("Calibri 12"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, "("),
)
btnParenthesesRight = Button(
    buttonsFrame5,
    text=")",
    font=("Calibri 12"),
    fg="white",
    background="gray15",
    command=lambda: add_to_equation(equationText, ")"),
)

btnC = Button(
    buttonsFrame1,
    text="C",
    font=("Calibri 12"),
    fg="white",
    background="gray30",
    command=delete_equation,
)
btnBackspace = Button(
    buttonsFrame1,
    text="<-",
    font=("Calibri 12"),
    fg="white",
    background="gray30",
    command=delete_last_char,
)
btnPlusMinus = Button(
    buttonsFrame5,
    text="+/-",
    font=("Calibri 12"),
    fg="white",
    background="gray15",
    command=plus_minus,
)
btnPercent = Button(
    buttonsFrame1,
    text="%",
    font=("Calibri 12"),
    fg="white",
    background="gray30",
    command=lambda: add_to_equation(equationText, " /100 * "),
)
btnDivision = Button(
    buttonsFrame1,
    text="/",
    font=("Calibri 12"),
    fg="white",
    background="darkorange3",
    command=lambda: add_to_equation(equationText, " / "),
)
btnMultiplication = Button(
    buttonsFrame2,
    text="*",
    font=("Calibri 12"),
    fg="white",
    background="darkorange3",
    command=lambda: add_to_equation(equationText, " * "),
)
btnSubtraction = Button(
    buttonsFrame3,
    text="-",
    font=("Calibri 12"),
    fg="white",
    background="darkorange3",
    command=lambda: add_to_equation(equationText, " - "),
)
btnAddition = Button(
    buttonsFrame4,
    text="+",
    font=("Calibri 12"),
    fg="white",
    background="darkorange3",
    command=lambda: add_to_equation(equationText, " + "),
)
btnResult = Button(
    buttonsFrame5,
    text="=",
    font=("Calibri 12"),
    fg="white",
    background="darkorange3",
    command=equation,
)

# We create the pack positions
btn1.pack(side=LEFT, fill=BOTH, expand=True)
btn2.pack(side=LEFT, fill=BOTH, expand=True)
btn3.pack(side=LEFT, fill=BOTH, expand=True)
btn4.pack(side=LEFT, fill=BOTH, expand=True)
btn5.pack(side=LEFT, fill=BOTH, expand=True)
btn6.pack(side=LEFT, fill=BOTH, expand=True)
btn7.pack(side=LEFT, fill=BOTH, expand=True)
btn8.pack(side=LEFT, fill=BOTH, expand=True)
btn9.pack(side=LEFT, fill=BOTH, expand=True)
btnPlusMinus.pack(side=LEFT, fill=BOTH, expand=True)
btn0.pack(side=LEFT, fill=BOTH, expand=True)
btnDot.pack(side=LEFT, fill=BOTH, expand=True)
btnParenthesesLeft.pack(side=LEFT, fill=BOTH, expand=True)
btnParenthesesRight.pack(side=LEFT, fill=BOTH, expand=True)
btnBackspace.pack(side=LEFT, fill=BOTH, expand=True)
btnC.pack(side=LEFT, fill=BOTH, expand=True)
btnPercent.pack(side=LEFT, fill=BOTH, expand=True)
btnDivision.pack(side=LEFT, fill=BOTH, expand=True)
btnMultiplication.pack(side=LEFT, fill=BOTH, expand=True)
btnSubtraction.pack(side=LEFT, fill=BOTH, expand=True)
btnAddition.pack(side=LEFT, fill=BOTH, expand=True)
btnResult.pack(side=LEFT, fill=BOTH, expand=True)

# Execute Tkinter
scalc.mainloop()
