from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
POSITION = (0, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_hall.txt", mode="r") as file:
            self.high_score = int(file.read()) 
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_hall.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
        