import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
my_image = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526)
img = canvas.create_image(400, 263, image=my_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

t = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
w = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
new_img = PhotoImage(file="images/card_back.png")

r = {}
l = []

try:
    data = pandas.read_csv("words_to_learn.csv")
    d = data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("data/french_words.csv")
    d = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    d = data.to_dict(orient="records")


def is_known():
    global r
    d.remove(r)
    print(len(d))
    data = pandas.DataFrame(d)
    data.to_csv("words_to_learn.csv", index=False)
    generate()


def generate():
    global r
    r = random.choice(d)
    canvas.itemconfig(img, image=my_image)
    canvas.itemconfig(t, text="French", fill="black")
    canvas.itemconfig(w, text=r["French"], fill="black")
    window.after(3000, func=pull)


def pull():
    canvas.itemconfig(img, image=new_img)
    canvas.itemconfig(t, text="English", fill="white")
    canvas.itemconfig(w, text=r["English"], fill="white")


right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=generate)
wrong_button.grid(row=1, column=0)

generate()

window.mainloop()
