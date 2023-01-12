import random
from tkinter import *
from tkinter import messagebox as mb
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '#', '$', '%', '&',
             '?', '@', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '']


def Password_generator():
    Password_entry.delete(0, END)
    password = ""
    for letter in range(12):
        password += random.choice(alphabets)
    Password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def Data_Saving():
    if len(Website_entry.get()) == 0 or len(Password_entry.get()) == 0 or len(Password_entry.get()) == 0:
        mb.showinfo("ERROR", "Please fill all fields.")
    else:
        is_ok = mb.askokcancel(title=Website_entry.get(),
                               message=f"Email: {Email_entry.get()} \nPassword: {Password_entry.get()}\n\n Do you want to save this informatoin?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{Website_entry.get()}, {Email_entry.get()},{Password_entry.get()} \n")
                Website_entry.delete(0, END)
                Password_entry.delete(0, END)
                Email_entry.delete(0, END)
                Email_entry.insert(END, "@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas()
lock_logo = PhotoImage(file="logo.png")
canvas.config(width=200, height=189)
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)

# ---------------Website entry----------------
Website_label = Label(text="Website")
Website_label.grid(row=1, column=0)

Website_entry = Entry(width=35)
Website_entry.focus()
Website_entry.grid(row=1, column=1, columnspan=2)
# --------------Email/Username---------------------
Email_label = Label(text="Email/Username")
Email_label.grid(row=2, column=0)

Email_entry = Entry(width=35)
Email_entry.insert(0, "@gmail.com")
Email_entry.grid(row=2, column=1, columnspan=2)

# -------------------Password------------------
Password_label = Label(text="Password")
Password_label.grid(row=3, column=0)

Password_entry = Entry(width=22)
Password_entry.grid(row=3, column=1)

Generate_button = Button(text="Generate", width=10, command=Password_generator)
Generate_button.grid(row=3, column=2)

# --------------Add button-----------------------
Add_button = Button(width=30, text="add", command=Data_Saving)
Add_button.grid(column=1, columnspan=2)

screen.mainloop()
