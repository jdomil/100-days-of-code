from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y = -110
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(f"{color}")
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y)
    turtles.append(new_turtle)
    y += 45

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner_color = turtle.pencolor()
            is_race_on = False
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winner_color == user_bet:
    print(f"You've won! The {winner_color} turtle is the winner.")
else:
    print(f"You've lost... The {winner_color} turtle is the winner.")

screen.exitonclick()
