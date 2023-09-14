from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8)
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed = 0.04

    # Width = 1000, height = 700
    def ball_move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bouncing_y(self):
        self.y_movement *= -1

    def bouncing_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.9

    def reset_ball_position(self):
        self.goto(0, 0)
        self.move_speed = 0.04
        self.bouncing_x()
        go_y = random.randint(-1, 1)

        if go_y < 0:
            self.bouncing_y()

    def get_move_speed(self):
        return self.move_speed