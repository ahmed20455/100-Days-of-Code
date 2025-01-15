import tkinter
from tkinter import PhotoImage, Button, Canvas
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_car={}
to_learn={}
#---------------------READING DATA----------------#
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    french = current_card["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_text,text=french,fill="black")
    canvas.itemconfig(card_background,image=my_front)
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    English = current_card["English"]
    canvas.itemconfig(card_text,text=English,fill="white")
    canvas.itemconfig(card_background,image=my_back)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window= tkinter.Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer=window.after(3000, func=flip_card)
canvas = Canvas(height=526, width=800)
my_front=PhotoImage(file="images/card_front.png")
my_back=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=my_front)
card_title = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_text = canvas.create_text(400,263,text="", font=("Ariel",60,"italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0,)
canvas.grid(row=0,column=0,columnspan=2)
my_image=PhotoImage(file="images/right.png")
wrong_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
correct_button = Button(image=my_image,highlightthickness=0,command=is_known)
correct_button.grid(row=1,column=1)
next_card()
window.mainloop()
