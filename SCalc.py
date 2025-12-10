from tkinter import *

# We create the root window
scalc = Tk()

# Root window title and dimensions
scalc.title("SCalc")
scalc.geometry("600x500")

# We create the buttons
btn1 = Button(scalc, text="1", fg="black")
btn2 = Button(scalc, text="2", fg="black")
btn3 = Button(scalc, text="3", fg="black")
btn4 = Button(scalc, text="4", fg="black")
btn5 = Button(scalc, text="5", fg="black")
btn6 = Button(scalc, text="6", fg="black")
btn7 = Button(scalc, text="7", fg="black")
btn8 = Button(scalc, text="8", fg="black")
btn9 = Button(scalc, text="9", fg="black")
btn0 = Button(scalc, text="0", fg="black")
btnDot = Button(scalc, text=".", fg="black")
btnC = Button(scalc, text="C", fg="black")
btnPlusMinus = Button(scalc, text="+/-", fg="black")
btnPercent = Button(scalc, text="%", fg="black")
btnDivision = Button(scalc, text="/", fg="black")
btnMultiplication = Button(scalc, text="*", fg="black")
btnSubtraction = Button(scalc, text="-", fg="black")
btnAddition = Button(scalc, text="+", fg="black")
btnResult = Button(scalc, text="=", fg="black")

# We create the grid positions
btn1.grid(column=0, row=4)
btn2.grid(column=1, row=4)
btn3.grid(column=2, row=4)
btn4.grid(column=0, row=3)
btn5.grid(column=1, row=3)
btn6.grid(column=2, row=3)
btn7.grid(column=0, row=2)
btn8.grid(column=1, row=2)
btn9.grid(column=2, row=2)
btn0.grid(column=0, row=5)
btnDot.grid(column=2, row=5)
btnC.grid(column=0, row=1)
btnPlusMinus.grid(column=1, row=1)
btnPercent.grid(column=2, row=1)
btnDivision.grid(column=3, row=1)
btnMultiplication.grid(column=3, row=2)
btnSubtraction.grid(column=3, row=3)
btnAddition.grid(column=3, row=4)
btnResult.grid(column=3, row=5)

# F

# Execute Tkinter
scalc.mainloop()
