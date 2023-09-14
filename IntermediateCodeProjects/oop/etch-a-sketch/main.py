import turtle
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(50)


def move_backwards():
    pen.backward(50)


def move_clockwise():
    pen.right(10)


def move_counterclockwise():
    pen.left(10)


def cleaning():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=cleaning)


screen.exitonclick()
    
