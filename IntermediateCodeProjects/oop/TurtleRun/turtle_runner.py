import turtle
from turtle import Turtle
import random


class TurtleRunner:

    def __init__(self, color):
        self.runner = Turtle()
        self.velocity = 0
        self.set_velocity()
        self.color = color
        self.set_runners_state()

    def set_runners_state(self):
        self.runner.color(self.color)
        self.runner.shape("turtle")
        self.runner.shapesize(2)
        self.runner.penup()

    def set_velocity(self):
        self.velocity = random.randint(10, 30)

    def get_runner(self):
        return self.runner

    def get_velocity(self):
        return self.velocity

    def get_color(self):
        return self.color
