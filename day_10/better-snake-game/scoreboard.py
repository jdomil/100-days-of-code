from turtle import Turtle

FILE = open("data.txt", mode="r+")

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.setpos(0, 270)
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.print_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.print_scoreboard()

