from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# --------- FLASH CARD CREATION --------- #

words_file = pd.read_csv("data/french_words.csv")
words_dict = words_file.to_dict(orient="records")
current_flashcard = {}


def new_flashcard():
    global current_flashcard, flip_timer
    window.after_cancel(flip_timer)

    # Set right flashcard format
    canvas.itemconfig(flashcard_image, image=card_front_image)
    canvas.itemconfig(language_text, fill="black")
    canvas.itemconfig(word_text, fill="black")

    # Fill flashcard text
    flashcard = random.choice(words_dict)
    current_flashcard = flashcard
    word = flashcard["French"]
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=word)

    # Reset loop
    flip_timer = window.after(3000, flip_flashcard())


# --------- FLASH CARD FLIPPING --------- #
def flip_flashcard():
    # Change flashcard formatting
    canvas.itemconfig(flashcard_image, image=card_back_image)
    canvas.itemconfig(language_text, fill="white")
    canvas.itemconfig(word_text, fill="white")

    # Change text
    translation = current_flashcard["English"]
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=translation)


# ----------------- UI ------------------ #
# Window setup
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_flashcard)

# Flash card canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
flashcard_image = canvas.create_image(400, 263)
language_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR, command=new_flashcard)
wrong_button.grid(column=0, row=1)

# Right button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR, command=new_flashcard)
right_button.grid(column=1, row=1)

new_flashcard()
window.mainloop()

