import turtle
import random

my_timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

my_timmy.shape("turtle")
my_timmy.pensize(4)
my_timmy.speed("fastest")


def color_random():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def turtle_random_path():
    while True:
        movement = random.randint(0, 1)
        my_timmy.color(color_random())
        angle = random.choice([90, 180, 270, -90, -180, -270])
        if movement == 0:
            my_timmy.right(angle)
        else:
            my_timmy.left(angle)
        my_timmy.forward(10)


turtle_random_path()
screen.exitonclick()
