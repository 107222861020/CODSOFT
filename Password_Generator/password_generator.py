import tkinter as tk
from tkinter import messagebox
import random
import string


# Password Generator Function
def generate_password():

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Warning",
                "Password length should be at least 4"
            )
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if number_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation


        if characters == "":
            messagebox.showwarning(
                "Warning",
                "Select password complexity"
            )
            return


        password = ""

        for i in range(length):
            password += random.choice(characters)


        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)


    except:
        messagebox.showerror(
            "Error",
            "Enter valid password length"
        )


# Copy password
def copy_password():

    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

    messagebox.showinfo(
        "Copied",
        "Password copied!"
    )


# Main Window

root = tk.Tk()

root.title("Password Generator")
root.geometry("450x500")
root.resizable(False,False)


# Background

root.configure(bg="#1e1e2f")


title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial",22,"bold"),
    bg="#1e1e2f",
    fg="white"
)

title.pack(pady=20)



label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial",13),
    bg="#1e1e2f",
    fg="white"
)

label.pack()



length_entry = tk.Entry(
    root,
    font=("Arial",14),
    width=15,
    justify="center"
)

length_entry.pack(pady=10)



# Options

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()


tk.Checkbutton(
    root,
    text="Uppercase Letters",
    variable=upper_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#33334d"
).pack()


tk.Checkbutton(
    root,
    text="Lowercase Letters",
    variable=lower_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#33334d"
).pack()


tk.Checkbutton(
    root,
    text="Numbers",
    variable=number_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#33334d"
).pack()


tk.Checkbutton(
    root,
    text="Symbols",
    variable=symbol_var,
    bg="#1e1e2f",
    fg="white",
    selectcolor="#33334d"
).pack()



generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial",14,"bold"),
    bg="#4CAF50",
    fg="white",
    command=generate_password
)

generate_btn.pack(pady=20)



password_entry = tk.Entry(
    root,
    font=("Arial",15),
    width=30,
    justify="center"
)

password_entry.pack()



copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial",12),
    bg="#2196F3",
    fg="white",
    command=copy_password
)

copy_btn.pack(pady=15)



footer = tk.Label(
    root,
    text="Python GUI Password Generator",
    bg="#1e1e2f",
    fg="gray"
)

footer.pack(side="bottom",pady=20)



root.mainloop()