# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials##
import colorgram
import turtle
import random

my_timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
my_timmy.speed("fastest")
my_timmy.pensize(10)
my_timmy.hideturtle()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

position_color = 0

def fixing_position():
    my_timmy.penup()
    my_timmy.left(90)
    my_timmy.forward(200)
    my_timmy.left(90)
    my_timmy.forward(300)
    my_timmy.right(180)

def drawing_million_dollars_piece(position_color):
    for _ in range(10):
        distance = 0
        for _ in range(10):
            my_timmy.pendown()
            my_timmy.color(random.choice(rgb_colors))
            my_timmy.dot(15)
            my_timmy.penup()
            distance += 40
            my_timmy.forward(40)
            position_color += 1
        jumping(distance)
   
def jumping(distance):
    my_timmy.penup()
    my_timmy.backward(distance)
    my_timmy.right(90)
    my_timmy.forward(40)
    my_timmy.left(90)
    
    
        
    
fixing_position()
drawing_million_dollars_piece(position_color)
screen.exitonclick()
