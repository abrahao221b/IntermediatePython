from turtle import Turtle

# Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Snake class
class Snake:
    # Attributes
    snake_body = []

    def __init__(self):
        for part in range(3):
            self.link_part()
        self.head = self.snake_body[0]

    # Snake movement
    def move(self):
        for index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(x=new_x, y=new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    # Linking snake parts
    def link_part(self):
        body = Turtle(shape="square")
        body.color("white")
        body.penup()

        if not self.snake_body:
            body.goto(x=0, y=0)
        else:
            body_x = self.snake_body[len(self.snake_body) - 1].xcor()
            body_y = self.snake_body[len(self.snake_body) - 1].ycor()
            body.goto(x=(body_x - 20), y=body_y)

        self.snake_body.append(body)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Gets
    def get_snake_body(self):
        return self.snake_body
