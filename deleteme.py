from tkinter import *

# We create the root window
scalc = Tk()

# Root window title and dimensions
scalc.title("SCalc")
scalc.geometry("600x500")

# We create the frames
equationFrame = Frame(scalc, background="white")
equationFrame.pack(fill=BOTH, expand=True)
buttonsFrame1 = Frame(scalc, background="gray")
buttonsFrame1.pack(fill=BOTH, expand=True)
buttonsFrame2 = Frame(scalc, background="gray")
buttonsFrame2.pack(fill=BOTH, expand=True)
buttonsFrame3 = Frame(scalc, background="gray")
buttonsFrame3.pack(fill=BOTH, expand=True)
buttonsFrame4 = Frame(scalc, background="gray")
buttonsFrame4.pack(fill=BOTH, expand=True)
buttonsFrame5 = Frame(scalc, background="gray")
buttonsFrame5.pack(fill=BOTH, expand=True)

# We create a text widget for the equation frame
equationText = Entry(equationFrame)
equationText.pack(side=LEFT, fill=BOTH, expand=True)

# We create the buttons
btn1 = Button(buttonsFrame4, text="1", fg="black", background="gray")
btn2 = Button(buttonsFrame4, text="2", fg="black", background="gray")
btn3 = Button(buttonsFrame4, text="3", fg="black", background="gray")
btn4 = Button(buttonsFrame3, text="4", fg="black", background="gray")
btn5 = Button(buttonsFrame3, text="5", fg="black", background="gray")
btn6 = Button(buttonsFrame3, text="6", fg="black", background="gray")
btn7 = Button(buttonsFrame2, text="7", fg="black", background="gray")
btn8 = Button(buttonsFrame2, text="8", fg="black", background="gray")
btn9 = Button(buttonsFrame2, text="9", fg="black", background="gray")
btn0 = Button(buttonsFrame5, text="0", fg="black", background="gray")
btnDot = Button(buttonsFrame5, text=".", fg="black", background="gray")
btnC = Button(buttonsFrame1, text="C", fg="black", background="darkgray")
btnPlusMinus = Button(buttonsFrame1, text="+/-", fg="black", background="darkgray")
btnPercent = Button(buttonsFrame1, text="%", fg="black", background="darkgray")
btnDivision = Button(buttonsFrame1, text="/", fg="black", background="darkgray")
btnMultiplication = Button(buttonsFrame2, text="*", fg="black", background="darkgray")
btnSubtraction = Button(buttonsFrame3, text="-", fg="black", background="darkgray")
btnAddition = Button(buttonsFrame4, text="+", fg="black", background="darkgray")
btnResult = Button(buttonsFrame5, text="=", fg="black", background="darkgray")


# We create the functions
def clicked():
    equation = equationText.get()
    equationText.append(equation)


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
btn0.pack(side=LEFT, fill=BOTH, expand=True)
btnDot.pack(side=LEFT, fill=BOTH, expand=True)
btnC.pack(side=LEFT, fill=BOTH, expand=True)
btnPlusMinus.pack(side=LEFT, fill=BOTH, expand=True)
btnPercent.pack(side=LEFT, fill=BOTH, expand=True)
btnDivision.pack(side=LEFT, fill=BOTH, expand=True)
btnMultiplication.pack(side=LEFT, fill=BOTH, expand=True)
btnSubtraction.pack(side=LEFT, fill=BOTH, expand=True)
btnAddition.pack(side=LEFT, fill=BOTH, expand=True)
btnResult.pack(side=LEFT, fill=BOTH, expand=True)

# Execute Tkinter
scalc.mainloop()
