import tkinter as tk
from tkinter import messagebox
import json
import os


# ---------------- DATA STORAGE ----------------

FILE = "contacts.json"


def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


contacts = load_contacts()



def save_contacts():
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)



# ---------------- FUNCTIONS ----------------


def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()


    if name == "" or phone == "":
        messagebox.showwarning(
            "Missing Information",
            "Name and Phone are required"
        )
        return


    contacts.append({
        "name":name,
        "phone":phone,
        "email":email,
        "address":address
    })


    save_contacts()

    messagebox.showinfo(
        "Success",
        "Contact Added Successfully"
    )

    clear_fields()
    display_contacts()



def display_contacts():

    contact_list.delete(0,tk.END)


    for c in contacts:

        contact_list.insert(
            tk.END,
            f"{c['name']}  |  {c['phone']}"
        )



def search_contact():

    value = search_entry.get().lower()


    contact_list.delete(0,tk.END)


    for c in contacts:

        if value in c["name"].lower() or value in c["phone"]:

            contact_list.insert(
                tk.END,
                f"{c['name']}  |  {c['phone']}"
            )



def delete_contact():

    selected = contact_list.curselection()


    if not selected:
        messagebox.showwarning(
            "Select",
            "Select a contact first"
        )
        return


    contacts.pop(selected[0])

    save_contacts()

    display_contacts()



    messagebox.showinfo(
        "Deleted",
        "Contact Deleted"
    )



def update_contact():

    selected = contact_list.curselection()


    if not selected:
        messagebox.showwarning(
            "Select",
            "Select a contact first"
        )
        return



    index = selected[0]


    contacts[index] = {

        "name":name_entry.get(),
        "phone":phone_entry.get(),
        "email":email_entry.get(),
        "address":address_entry.get()

    }


    save_contacts()

    display_contacts()


    messagebox.showinfo(
        "Updated",
        "Contact Updated"
    )



def clear_fields():

    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)



def select_contact(event):

    selected = contact_list.curselection()

    if selected:

        c = contacts[selected[0]]


        name_entry.delete(0,tk.END)
        name_entry.insert(0,c["name"])


        phone_entry.delete(0,tk.END)
        phone_entry.insert(0,c["phone"])


        email_entry.delete(0,tk.END)
        email_entry.insert(0,c["email"])


        address_entry.delete(0,tk.END)
        address_entry.insert(0,c["address"])




# ---------------- GUI ----------------


root = tk.Tk()

root.title("Contact Management System")

root.geometry("750x650")

root.resizable(False,False)

root.configure(bg="#121212")



title = tk.Label(

    root,

    text="CONTACT MANAGEMENT SYSTEM",

    font=("Arial",22,"bold"),

    bg="#121212",

    fg="white"

)

title.pack(pady=20)




frame = tk.Frame(
    root,
    bg="#121212"
)

frame.pack()



def create_label(text,row):

    tk.Label(

        frame,

        text=text,

        font=("Arial",12),

        bg="#121212",

        fg="white"

    ).grid(
        row=row,
        column=0,
        padx=10,
        pady=8
    )



create_label("Name",0)
create_label("Phone",1)
create_label("Email",2)
create_label("Address",3)



name_entry=tk.Entry(frame,width=40)

name_entry.grid(row=0,column=1)



phone_entry=tk.Entry(frame,width=40)

phone_entry.grid(row=1,column=1)



email_entry=tk.Entry(frame,width=40)

email_entry.grid(row=2,column=1)



address_entry=tk.Entry(frame,width=40)

address_entry.grid(row=3,column=1)





# BUTTONS


button_frame=tk.Frame(

    root,

    bg="#121212"

)

button_frame.pack(pady=20)



def button(text,cmd,col):

    tk.Button(

        button_frame,

        text=text,

        width=15,

        height=2,

        bg="#1f6feb",

        fg="white",

        font=("Arial",10,"bold"),

        command=cmd

    ).grid(
        row=0,
        column=col,
        padx=8
    )



button("Add",add_contact,0)

button("Update",update_contact,1)

button("Delete",delete_contact,2)

button("Clear",clear_fields,3)




# SEARCH


search_entry=tk.Entry(

    root,

    width=40

)

search_entry.pack(pady=5)



tk.Button(

    root,

    text="Search",

    width=15,

    bg="#238636",

    fg="white",

    command=search_contact

).pack()




# LIST


contact_list=tk.Listbox(

    root,

    width=65,

    height=12,

    font=("Arial",12)

)

contact_list.pack(pady=20)


contact_list.bind(
    "<<ListboxSelect>>",
    select_contact
)



footer=tk.Label(

    root,

    text="Python GUI Project | CODSOFT",

    bg="#121212",

    fg="gray"

)

footer.pack(side="bottom",pady=10)



display_contacts()


root.mainloop()