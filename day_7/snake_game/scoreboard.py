from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.setpos(0, 270)
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.print_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
