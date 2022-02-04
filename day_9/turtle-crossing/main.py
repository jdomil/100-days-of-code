import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    screen.update()
    car_manager.create_car()

    # Detect when player passes level
    if turtle.ycor() > turtle.finish_line:
        turtle.reset_turtle()
        car_manager.level_up()
        scoreboard.update_level()

    # Detect car collision
    for car in car_manager.cars_array:
        if car.ycor() + 20 > turtle.ycor() > car.ycor() - 20 and turtle.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()




