import turtle
import random

my_timmy = turtle.Turtle()
screen = turtle.Screen()
my_timmy.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


for n in range(1, 180):
    for angle in range(1, 180, n):
        my_timmy.color(random_color())
        my_timmy.right(angle)
        my_timmy.circle(100)

screen.exitonclick()
