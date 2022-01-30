import random
import turtle as t

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

"""Array of colors obtained with script above less white-y colors"""
RGB_COLORS = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

"""Define art piece constants"""
DOT_SIZE = 20
DOT_SEPARATION = 50
DOTS_PER_ROW = 10

"""Create turtle instance with desired params"""
t.colormode(255)
turtle = t.Turtle()
turtle.shape("circle")
turtle.speed("fastest")
turtle.up()
turtle.hideturtle()

"""Set start position"""
start_position = - ((DOTS_PER_ROW * DOT_SEPARATION - DOT_SEPARATION) / 2)
start_coordinates = (start_position, start_position)
turtle.setpos(start_coordinates)


def draw_row(dots_num):
    for _ in range(dots_num):
        turtle.dot(DOT_SIZE, random.choice(RGB_COLORS))
        turtle.forward(DOT_SEPARATION)


def new_row(dots_num, separation):
    current_position = turtle.pos()
    current_x = current_position[0]
    current_y = current_position[1]
    turtle.setpos(current_x - dots_num * separation, current_y + separation)


for _ in range(DOTS_PER_ROW):
    draw_row(DOTS_PER_ROW)
    new_row(DOTS_PER_ROW, DOT_SEPARATION)


screen = t.Screen()
screen.exitonclick()
