from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 1000
HEIGHT = 600

RIGHT_PADDLE_LOCATION = (470, 0)
LEFT_PADDLE_LOCATION = (-470, 0)

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_LOCATION)
left_paddle = Paddle(LEFT_PADDLE_LOCATION)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

balls_counter = 1
while balls_counter <= 9:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 440 or ball.distance(left_paddle) < 50 and ball.xcor() < -440:
        ball.bounce_x()
        ball.move_speed *= 0.85

    # Detect ball going out of bounds
    if ball.xcor() > 480:
        score.increase_left_score()
        ball.reset_position()
        balls_counter += 1
        time_delay = 0.1

    if ball.xcor() < -480:
        score.increase_right_score()
        ball.reset_position()
        balls_counter += 1
        ball.move_speed = 0.1

score.game_over()
screen.exitonclick()
