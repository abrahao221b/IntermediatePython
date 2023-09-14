from turtle import Turtle, Screen
import random

color = ["red", "blue", "yellow", "green", "purple", "grey", "black"]

turtle_timmy = Turtle()
turtle_timmy.shape("classic")

turtle_timmy.penup()
turtle_timmy.left(90)
turtle_timmy.forward(400)
turtle_timmy.right(90)
turtle_timmy.pendown()


def convex_angle(faces):
    angle_sum = (faces - 2) * 180
    return angle_sum / faces


for step in range(3, 52):
    angle = convex_angle(step)
    turtle_timmy.color(random.choice(color))
    for i in range(step):
        turtle_timmy.forward(50)
        turtle_timmy.right(180 - angle)

screen = Screen()
screen.exitonclick()
