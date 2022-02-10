import turtle
import pandas as pd

# Create screen with blank picture of US states
screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read csv data and create list of state
states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()

# Create another instance of Turtle to move around writing correct states where they belong
pointer = turtle.Turtle()
pointer.pu()
pointer.hideturtle()

# Initialize correct guesses score and list of guesses
guessed_list = []

# Main game logic
while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 states", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in guessed_list:
        guessed_list.append(answer_state)
        state_data = states_data[states_data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        pointer.goto(x_cor, y_cor)
        pointer.write(answer_state, align="center", font="Arial")

missed_states = []
for state in states_list:
    if state not in guessed_list:
        missed_states.append(state)

missed_states_series = pd.DataFrame(missed_states)
missed_states_series.to_csv("states_to_learn.csv")

