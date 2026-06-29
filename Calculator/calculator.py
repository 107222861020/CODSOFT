import tkinter as tk
from tkinter import messagebox


# Calculator functions
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2

        else:
            messagebox.showerror("Error", "Select an operation")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")


# Window
window = tk.Tk()
window.title("Professional Calculator")
window.geometry("400x450")
window.resizable(False, False)


# Heading
title = tk.Label(
    window,
    text="Calculator",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)


# Number 1
tk.Label(window, text="Enter First Number").pack()

entry1 = tk.Entry(
    window,
    width=25,
    font=("Arial",14)
)

entry1.pack(pady=5)



# Number 2
tk.Label(window, text="Enter Second Number").pack()

entry2 = tk.Entry(
    window,
    width=25,
    font=("Arial",14)
)

entry2.pack(pady=5)



# Operation
tk.Label(window, text="Select Operation").pack()


operation_var = tk.StringVar()

operation_menu = tk.OptionMenu(
    window,
    operation_var,
    "+",
    "-",
    "*",
    "/"
)

operation_menu.pack(pady=10)



# Button

calculate_button = tk.Button(
    window,
    text="Calculate",
    font=("Arial",14),
    command=calculate
)

calculate_button.pack(pady=15)



# Result

result_label = tk.Label(
    window,
    text="Result:",
    font=("Arial",16)
)

result_label.pack(pady=20)



window.mainloop()