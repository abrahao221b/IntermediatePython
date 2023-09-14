from turtle import Turtle
import random

# Constants
POSSIBLE_POSITIONS = [-230, -170, -140, -110, -50, -10, 10, 35, 70, 130, 160, 190, 230]
POSSIBLE_COLORS = ["black", "green", "red", "grey", "purple", "yellow", "blue", "medium blue", "lime", "orange"]

SPEED_UP = 1
LIMIT_LEFT = -320
LIMIT_RIGHT = 310


# Class Car
class Car(Turtle):

    def __init__(self, velocity):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(POSSIBLE_COLORS))
        self.penup()
        self.position_start_y = random.choice(POSSIBLE_POSITIONS)
        self.goto(x=310, y=self.position_start_y)
        self.velocity = velocity
        self.movement_forward = True

    # Car's movement method
    def move(self):
        if self.movement_forward:
            self.forward_move()
        else:
            self.reverse_move()

    # Car's movement forward method
    def forward_move(self):
        if self.xcor() > LIMIT_LEFT:
            position_x = self.xcor() - self.velocity
            self.goto(x=position_x, y=self.position_start_y)
        else:
            self.new_ycor()
            self.movement_forward = False

    # Car's movement reversed method
    def reverse_move(self):
        if self.xcor() < LIMIT_RIGHT:
            position_x = self.xcor() + self.velocity
            self.goto(x=position_x, y=self.position_start_y)
        else:
            self.movement_forward = True

    # Choosing a new y coordinate for the car
    def new_ycor(self):
        self.position_start_y = random.choice(POSSIBLE_POSITIONS)

    # Setting a new velocity
    def set_velocity(self):
        self.velocity += SPEED_UP
