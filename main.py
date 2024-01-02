import turtle as t
import pandas as pd
import time
# Screen setup

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
tim = t.Turtle()
tim.hideturtle()
tim.penup()
red = t.Turtle()
red.hideturtle()
red.penup()
red.color("red")
# data extraction

data = pd.read_csv("50_states.csv", index_col=False)
states = data.state.to_list()

# game setup

game_is_on = True
correct_list = []

while game_is_on:
    tim.color("black")

    if len(correct_list) != 50:
        answer_state = str(screen.textinput(title=f"{len(correct_list)}/50 States Correct",
                                            prompt="What's a state's name?")).title()
        if answer_state == "Exit":
            missed_list = [state for state in states if state not in correct_list]

            missed_states_csv = pd.DataFrame(missed_list)
            missed_states_csv.to_csv("missed_states.csv")
            break
        if answer_state in states:
            if not (answer_state in correct_list):
                row = data[data.state == answer_state]
                x = int(data[data.state == answer_state].x.iloc[0])
                y = int(data[data.state == answer_state].y.iloc[0])
                tim.goto(x, y)
                tim.write(answer_state, align='center', font=('Arial', 10, 'normal'))
                correct_list.append(answer_state)
            else:
                tim.goto(0, 0)
                red.write("Already Guessed State!", align='center', font=('Arial', 30, 'bold'))
                time.sleep(1)
                red.clear()
        else:
            tim.goto(0, 0)
            red.write("Not a state!", align='center', font=('Arial', 30, 'bold'))
            time.sleep(1)
            red.clear()
    else:
        tim.goto(0, 0)
        tim.color("green")
        red.write("You won! Congratulations!", align='center', font=('Arial', 30, 'bold'))
        time.sleep(3)
        red.clear()
        game_is_on = False
