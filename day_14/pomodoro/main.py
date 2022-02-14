from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES -------------------------- #
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    ticks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = str(math.floor(count / 60)).zfill(2)
    count_sec = str(count % 60).zfill(2)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        global reps
        if reps % 2 == 0:
            ticks_label['text'] += "✔︎"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Title
title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Start button
start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

# Pomodoro ticks
ticks_label = Label(fg=GREEN, bg=YELLOW)
ticks_label.grid(row=3, column=1)

window.mainloop()
