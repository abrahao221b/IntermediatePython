from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto", 24, "normal")
POSITION = (0, 265)
POSITION_GAMEOVER = (0, 130)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def show_score(self):
        self.goto(POSITION)
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1

    def clear_core(self):
        self.clear()

    def gameover(self):
        self.penup()
        self.goto(POSITION_GAMEOVER)
        self.color("white")
        self.pendown()
        self.write(arg=f"Final Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.color("red")
        self.penup()
        self.goto(-1, 0)
        self.pendown()
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
