from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.hideturtle()
        self.goto(-200, 250)
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
