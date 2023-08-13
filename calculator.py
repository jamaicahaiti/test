import tkinter as tk
import math

def button_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(num))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_sin():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_cos():
    try:
        angle = float(entry.get())
        result = math.cos(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("sin", 5, 0), ("cos", 5, 1), ("Clear", 5, 2)
]

for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, width=10, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)

    if button_text.isnumeric() or button_text == ".":
        button.config(command=lambda num=button_text: button_click(num))

    elif button_text == "=":
        button.config(command=calculate)

    elif button_text == "Clear":
        button.config(command=clear)

    elif button_text == "sin":
        button.config(command=calculate_sin)

    elif button_text == "cos":
        button.config(command=calculate_cos)

root.mainloop()
