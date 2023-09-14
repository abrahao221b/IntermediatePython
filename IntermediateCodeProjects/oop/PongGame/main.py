import time
from turtle import Turtle, Screen
from playerBar import PlayerBar
from gameBoard import GameBoard
from ball import Ball

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
sleep_time = 0.01

player1 = PlayerBar(1)
player2 = PlayerBar(2)

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")


gameBoard = GameBoard()
gameBoard.draw_division_line()


ball = Ball()


game_start = True
max_score = 0

while game_start:
    time.sleep(ball.get_move_speed())
    screen.update()
    ball.ball_move()

    if ball.xcor() > 470:
        gameBoard.draw_game_result(1)
        ball.reset_ball_position()

    if ball.xcor() < -470:
        gameBoard.draw_game_result(2)
        ball.reset_ball_position()

    if ball.ycor() > 330 or ball.ycor() < -320:
        ball.bouncing_y()

    if player1.touch(ball) or player2.touch(ball):
        ball.bouncing_x()

    if gameBoard.player1_score > 5 or gameBoard.player2_score > 5:
        game_start = False

if gameBoard.player1_score > gameBoard.player2_score:
    gameBoard.player_win("player1".upper())
else:
    gameBoard.player_win("player2".upper())

screen.exitonclick()