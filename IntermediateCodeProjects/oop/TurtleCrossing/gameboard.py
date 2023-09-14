from turtle import Turtle

# Constants
FONT = ("Roboto", 20, "normal")


# Class GameBoard. It is the game score board
class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.round = 1
        self.goto(x=-250, y=260)
        self.write(f"Level: {self.round}", align="center", font=FONT)
        self.hideturtle()

    # Increasing the level number
    def level_up(self):
        self.clear()
        self.round += 1
        self.write(f"Level: {self.round}", align="center", font=FONT)

    # Printing the phrase game over
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

    # Gets
    def get_round(self):
        return self.round
