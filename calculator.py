from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    e.insert(END, str(number))

def button_clear():
    e.delete(0, END)

def button_operator(op):
    current = e.get()
    if current and current[-1] not in "+-*/":
        e.insert(END, op)

def button_equal():
    expression = e.get()
    try:
        # Evaluate safely using eval (better: use parser)
        result = eval(expression)
        e.delete(0, END)
        e.insert(0, result)
    except Exception:
        e.delete(0, END)
        e.insert(0, "Error")

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text in "0123456789.":
        Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t)).grid(row=row, column=col)
    elif text == "=":
        Button(root, text=text, padx=40, pady=20, command=button_equal).grid(row=row, column=col)
    else:
        Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_operator(t)).grid(row=row, column=col)

# Clear button
Button(root, text="Clear", padx=150, pady=20, command=button_clear).grid(row=5, column=0, columnspan=4)

root.mainloop()
