from turtle import Turtle


class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.goto(-100, 245)
        self.write(self.player1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 245)
        self.write(self.player2_score, align="center", font=("Courier", 80, "normal"))

    @staticmethod
    def draw_division_line():
        turtle = Turtle()
        turtle.color("white")
        turtle.pensize(4)
        turtle.penup()
        turtle.goto(x=0, y=330)
        turtle.setheading(270)
        distance = 20
        total_distance = 0
        while total_distance < 600:
            turtle.pendown()
            turtle.forward(distance)
            turtle.penup()
            turtle.forward(distance)
            total_distance += distance

    def draw_game_result(self, who_scored):
        self.clear()
        if who_scored == 1:
            self.player1_score += 1
        else:
            self.player2_score += 1

        self.goto(-100, 245)
        self.write(self.player1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 245)
        self.write(self.player2_score, align="center", font=("Courier", 80, "normal"))

    def player_win(self, player):
        self.goto(0, 0)
        self.color("green")
        self.write(f"PLAYER {player} WIN!!!!!", align="center", font=("Roboto", 20, "normal"))

    def get_player1_score(self):
        return self.player1_score

    def get_player2_score(self):
        return self.player2_score
