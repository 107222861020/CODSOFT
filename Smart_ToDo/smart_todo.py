import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3


# DATABASE

db = sqlite3.connect("todo.db")
cursor = db.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT,
password TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
username TEXT,
task TEXT,
date TEXT,
priority TEXT,
status TEXT
)
""")


db.commit()


current_user = ""


# ---------- LOGIN ----------


def register():

    u = username.get()
    p = password.get()

    if u == "" or p == "":
        messagebox.showwarning(
            "Warning",
            "Fill all fields"
        )
        return


    cursor.execute(
        "INSERT INTO users VALUES(?,?)",
        (u,p)
    )

    db.commit()


    messagebox.showinfo(
        "Success",
        "Account Created"
    )




def login():

    global current_user


    u=username.get()
    p=password.get()


    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (u,p)
    )


    if cursor.fetchone():

        current_user=u

        login_window.destroy()

        app()


    else:

        messagebox.showerror(
            "Error",
            "Invalid Login"
        )




# ---------- TASK FUNCTIONS ----------


def add_task():

    task = task_entry.get()

    priority = priority_var.get()


    if task == "":
        return


    date=datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )


    cursor.execute(
        "INSERT INTO tasks VALUES(?,?,?,?,?)",
        (
        current_user,
        task,
        date,
        priority,
        "Pending"
        )
    )


    db.commit()

    load_tasks()

    task_entry.delete(
        0,
        tk.END
    )




def load_tasks():

    task_list.delete(
        0,
        tk.END
    )


    cursor.execute(
        "SELECT * FROM tasks WHERE username=?",
        (current_user,)
    )


    data=cursor.fetchall()


    for t in data:

        task_list.insert(

        tk.END,

        f"{t[1]} | {t[2]} | {t[3]} | {t[4]}"

        )


    counter.config(
        text=f"Total: {len(data)}"
    )





def complete_task():

    selected=task_list.curselection()


    if selected:


        text=task_list.get(
            selected[0]
        )


        name=text.split("|")[0].strip()


        cursor.execute(

        """
        UPDATE tasks
        SET status='Completed'
        WHERE username=? AND task=?
        """,

        (
        current_user,
        name
        )

        )


        db.commit()

        load_tasks()




def delete_task():

    selected=task_list.curselection()


    if selected:


        text=task_list.get(
            selected[0]
        )


        name=text.split("|")[0].strip()


        cursor.execute(

        """
        DELETE FROM tasks
        WHERE username=? AND task=?
        """,

        (
        current_user,
        name
        )

        )


        db.commit()

        load_tasks()




def search_task():

    word=search.get()


    task_list.delete(
        0,
        tk.END
    )


    cursor.execute(

    """
    SELECT * FROM tasks
    WHERE username=? AND task LIKE ?
    """,

    (
    current_user,
    "%"+word+"%"
    )

    )


    for t in cursor.fetchall():

        task_list.insert(

        tk.END,

        f"{t[1]} | {t[2]} | {t[3]} | {t[4]}"

        )





# ---------- MAIN APP ----------


def app():

    global task_entry
    global task_list
    global priority_var
    global search
    global counter


    window=tk.Tk()

    window.title(
        "Smart To-Do Manager"
    )


    window.geometry(
        "850x650"
    )


    window.configure(
        bg="#121212"
    )



    tk.Label(

    window,

    text="SMART TO-DO MANAGER",

    font=("Arial",25,"bold"),

    bg="#121212",

    fg="white"

    ).pack(
        pady=20
    )



    task_entry=tk.Entry(

    window,

    width=40,

    font=("Arial",13)

    )

    task_entry.pack()



    priority_var=tk.StringVar()

    priority_var.set(
        "Medium"
    )



    tk.OptionMenu(

    window,

    priority_var,

    "High",

    "Medium",

    "Low"

    ).pack()



    tk.Button(

    window,

    text="Add Task",

    width=18,

    command=add_task

    ).pack(
        pady=5
    )



    search=tk.Entry(

    window,

    width=30

    )

    search.pack()



    tk.Button(

    window,

    text="Search",

    command=search_task

    ).pack()



    task_list=tk.Listbox(

    window,

    width=95,

    height=18

    )

    task_list.pack(
        pady=15
    )



    tk.Button(

    window,

    text="Complete",

    bg="green",

    fg="white",

    command=complete_task

    ).pack()



    tk.Button(

    window,

    text="Delete",

    bg="red",

    fg="white",

    command=delete_task

    ).pack(
        pady=5
    )



    counter=tk.Label(

    window,

    bg="#121212",

    fg="white"

    )

    counter.pack()



    load_tasks()


    window.mainloop()





# ---------- LOGIN UI ----------


login_window=tk.Tk()


login_window.title(
    "Login"
)


login_window.geometry(
    "400x400"
)


login_window.configure(
    bg="#121212"
)



tk.Label(

login_window,

text="SMART LOGIN",

font=("Arial",25,"bold"),

bg="#121212",

fg="white"

).pack(
    pady=40
)



username=tk.Entry(
    login_window
)

username.pack(
    pady=10
)



password=tk.Entry(

login_window,

show="*"

)

password.pack(
    pady=10
)



tk.Button(

login_window,

text="LOGIN",

width=20,

command=login

).pack(
    pady=10
)



tk.Button(

login_window,

text="CREATE ACCOUNT",

width=20,

command=register

).pack()



login_window.mainloop()