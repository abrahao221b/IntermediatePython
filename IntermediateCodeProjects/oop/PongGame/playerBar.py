from turtle import Turtle

# Constants
UP = 90
DOWN = 270
MOVE_DISTANCE = 30


# Player's Bar class
class PlayerBar:
    # Attributes
    bar_size = 4

    def __init__(self, mode):
        self.player = []
        self.mode = mode
        self.players_start_position = 0
        self.x = 0
        self.link_part()
        self.set_position()

    def link_part(self):
        for i in range(self.bar_size):
            bar = Turtle(shape="square")
            bar.color("white")
            bar.shapesize(stretch_wid=1.5, stretch_len=1.5)
            bar.penup()
            self.player.append(bar)

    def set_position(self):
        if self.mode == 1:
            self.x = -460
        else:
            self.x = 450

        for i in range(self.bar_size):
            self.player[i].goto(x=self.x, y=self.players_start_position)
            self.players_start_position += 30

    def move(self, movement):
        if movement == 1:
            for index in range(0, len(self.player) - 1, 1):
                new_x = self.player[index + 1].xcor()
                new_y = self.player[index + 1].ycor()
                self.player[index].goto(x=new_x, y=new_y)
            self.player[len(self.player) - 1].forward(MOVE_DISTANCE)
        else:
            for index in range(len(self.player) - 1, 0, -1):
                new_x = self.player[index - 1].xcor()
                new_y = self.player[index - 1].ycor()
                self.player[index].goto(x=new_x, y=new_y)
            self.player[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.player[len(self.player) - 1].ycor() < 330:
            self.player[len(self.player) - 1].setheading(UP)
            self.move(1)

    def down(self):
        if self.player[0].ycor() > -330:
            self.player[0].setheading(DOWN)
            self.move(2)

    def touch(self, ball):
        for i in self.player:
            if i.distance(ball) < 28:
                return True

    def get_player(self):
        return self.player
