from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


# Function used to generate a random word from the japanese_words csv file when one of the buttons is pressed
words = pandas.read_csv("data/japanese_words.csv")
words_list = words.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list)
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    canvas.itemconfig(word_text, text=current_card["Japanese"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# Window
window = Tk()
window.title("Flashy Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.config(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.config(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
