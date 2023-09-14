from turtle import Turtle, Screen
import time

# Creating a Turtle object
timmy = Turtle()

# Printing Turtle object memory address
print(timmy)

# Timmy shape
timmy.shape("turtle")
# Timmy Color
timmy.color("chartreuse1")
# Timmy size
timmy.shapesize(10)
# Waiting 1 second
time.sleep(1)
# Movement
timmy.forward(100)

# Creating a screen
my_screen = Screen()
# Printing the screen
print(my_screen.canvwidth)

# Creating a command to exit the screen
my_screen.exitonclick()