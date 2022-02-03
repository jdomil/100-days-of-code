from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.setpos(location)

    def up(self):
        y_cor = self.ycor()
        if y_cor < 230:
            self.sety(y_cor + 20)

    def down(self):
        y_cor = self.ycor()
        if y_cor > -230:
            self.sety(y_cor - 20)




