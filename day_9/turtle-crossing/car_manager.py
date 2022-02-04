from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_array = []
        self.speed = STARTING_MOVE_DISTANCE
        self.car_chance = 10

    def create_car(self):
        if random.randrange(100) < self.car_chance:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.x_pos = 300
            new_car.y_pos = random.randint(-250, 250)
            new_car.goto(new_car.x_pos, new_car.y_pos)
            self.cars_array.append(new_car)

    def move_cars(self):
        for car in self.cars_array:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.y_pos)

    def level_up(self):
        self.speed += MOVE_INCREMENT
        self.car_chance += 5


