import turtle
import pandas

screen = turtle.Screen()
screen.title("Brazil, States Game")

img = "./Img/blank_states_img.gif"

screen.addshape(img)

turtle.shape(img)

states_data = pandas.read_csv("./data/50_states.csv")
states_list = states_data.state.to_list()

state_pen = turtle.Turtle()
state_pen.color("blue")
state_pen.hideturtle()

game_on = True
guess_right = []

while game_on:
    answer_state = screen.textinput(title=f"{len(guess_right)}/{len(states_list)}Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    elif answer_state in states_list:
        if answer_state not in guess_right:
            guess_right.append(answer_state)
            state_pen.penup()
            state = states_data[states_data.state == answer_state]
            state_pen.goto(float(state.x), float(state.y))
            state_pen.pendown()
            state_pen.write(f'{answer_state}', align="center", font=("Courier", 8, "normal"))

    if len(guess_right) == len(states_list):
        game_on = False

for state in guess_right:
    states_list.remove(state)

print(f"You miss: {states_list}")
new_data = pandas.DataFrame(states_list)
new_data.to_csv("./data/states_to_learn.csv")