from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window setup
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_text = Label(font=("Arial", 18), fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        # Canvas setup
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=250,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # True and false colors
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
            command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
            command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="This is the end of que quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

