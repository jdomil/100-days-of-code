from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 46, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scores()

    def print_middle_line(self):
        self.width(10)
        self.goto(0, 300)
        self.setheading(270)

        while self.ycor() > -300:
            self.pd()
            self.forward(20)
            self.pu()
            self.forward(40)

    def update_scores(self):
        self.clear()
        self.goto(-75, 220)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(75, 220)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)
        self.print_middle_line()

    def increase_left_score(self):
        self.left_score +=1
        self.update_scores()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scores()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)




