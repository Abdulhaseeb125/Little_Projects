from tkinter import *

def to_km():
    number = float(input.get())
    number *= 1.605
    result.config(text=number)


screen = Tk()
screen.config(padx=10, pady=10)

Title = Label(text="Miles to Km")
Title.grid(column=1)

input = Entry(width=4)
input.grid(row=1, column=1)

label1 = Label(text="is equal to")
label1.grid(column=0)

result = Label(text="0")
result.grid(row=2, column=1)

Km = Label(text=" Km")
Km.grid(row=2, column=3)

button = Button(text="Calculate", command=to_km)
button.grid(column=1)

screen.mainloop()
