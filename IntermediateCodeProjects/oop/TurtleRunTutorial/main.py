import turtle
from turtle import Turtle, Screen
import random

race_start = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
runners = []
start_point = -100

for color in colors:
    new_runner = Turtle(shape="turtle")
    new_runner.color(color)
    new_runner.shapesize(2)
    new_runner.penup()
    new_runner.goto(x=-230, y=start_point)
    start_point += 50
    runners.append(new_runner)

if user_bet:
    race_start = True

while race_start:

    for runner in runners:
        if runner.xcor() > 230:
            winner = runner.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You Loose! The {winner} turtle is the winner!")
            race_start = False
            break
        rand_distance = random.randint(0, 50)
        runner.forward(rand_distance)


screen.exitonclick()