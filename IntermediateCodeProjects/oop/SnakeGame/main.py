import time
from turtle import Screen
import snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
sleep_time = 0.09

snake = snake.Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_start = True
while game_start:
    scoreboard.clear_core()
    scoreboard.show_score()
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.link_part()
        scoreboard.increase_score()
        sleep_time -= 0.001

    # Detecting collision with the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 \
            or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_start = False
        scoreboard.gameover()

    # Detecting collision with the tail
    for part in snake.get_snake_body()[1:]:
        if snake.head.distance(part) < 10:
            game_start = False
            scoreboard.gameover()

screen.exitonclick()
