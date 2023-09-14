from turtle import Turtle

# Constants
MAX_LIMIT = 270
MIN_LIMIT = -270


# Class TurtleRunner. Player's class
class TurtleRunner:

    def __init__(self):
        self.runner = Turtle()
        self.runner.shape("turtle")
        self.runner.color("black")
        self.runner.penup()
        self.runner.goto(x=0, y=-280)
        self.runner.setheading(90)
        self.velocity = 20

    # Player's up movement method
    def up(self):
        if self.runner.ycor() < MAX_LIMIT:
            self.runner.goto(x=self.runner.xcor(), y=(self.runner.ycor() + self.velocity))

    # Player's left movement method
    def left(self):
        if self.runner.xcor() > MIN_LIMIT:
            self.runner.goto(x=(self.runner.xcor() - self.velocity), y=self.runner.ycor())

    # Player's right movement method
    def right(self):
        if self.runner.xcor() < MAX_LIMIT:
            self.runner.goto(x=(self.runner.xcor() + self.velocity), y=self.runner.ycor())

    # Player's down movement method
    def down(self):
        if self.runner.ycor() > MIN_LIMIT:
            self.runner.goto(x=self.runner.xcor(), y=(self.runner.ycor() - self.velocity))

    # When the player level up, has to reset his position to the beginning
    def reset_position(self):
        self.runner.goto(x=0, y=-280)

    # Gets
    def get_turtle_runner(self):
        return self.runner
