# ------------------Imports-------------
import random
from tkinter import *
import pandas as pd
learned_words = []
BACKGROUND_COLOR = "#B1DDC6"
# --------------------CSV READER--------------------
data_csv = pd.read_csv("data/french_words.csv")
dict_data = data_csv.to_dict(orient="records")


def next_card():
    global rand_record, flip_timer
    window.after_cancel(flip_timer)
    rand_record = random.randint(0, len(dict_data))
    canvas.itemconfig(front, image=canvas_front_image)
    canvas.itemconfig(title, text="French", font=("Arial", 40, "italic"), fill="black")
    canvas.itemconfig(word, text=dict_data[rand_record]["French"], font=("Arial", 40, "italic"), fill='black')
    flip_timer = window.after(3000, flip_card)

def learned():
    dict_data.remove(dict_data[rand_record])
    next_card()



def flip_card():
    canvas.itemconfig(front, image=canvas_back_image)
    canvas.itemconfig(title, text="English", font=("Arial", 40, "italic"), fill="white")
    canvas.itemconfig(word, text=dict_data[rand_record]["English"], font=("Arial", 40, "italic"), fill="white")


# --------------------UI-------------------
window = Tk()
flip_timer = window.after(3000, flip_card)

window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_back_image = PhotoImage(file="images/card_back.png")
canvas_front_image = PhotoImage(file="images/card_front.png")
front = canvas.create_image(400, 263, image=canvas_front_image)
title = canvas.create_text(400, 203, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 293, text="", font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Mark button
wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)
# Right Mark button
right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, borderwidth=0, highlightthickness=0, command=learned)
right.grid(row=1, column=1)
next_card()

window.mainloop()