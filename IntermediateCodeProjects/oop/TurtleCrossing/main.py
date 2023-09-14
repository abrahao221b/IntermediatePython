import time
from turtle import Screen
from turtleRunner import TurtleRunner
from gameboard import GameBoard
from traffic import Traffic

# Creating the game's screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Setting the screen sleep time
sleep_time = 0.05

# Creating the player
turtleRunner = TurtleRunner()

# Setting a screen's listener
screen.listen()

# Setting the commands
screen.onkey(fun=turtleRunner.up, key="Up")
screen.onkey(fun=turtleRunner.down, key="Down")
screen.onkey(fun=turtleRunner.left, key="Left")
screen.onkey(fun=turtleRunner.right, key="Right")

# Creating the game's board score
game_board_status = GameBoard()

# Creating the car's traffic
traffic = Traffic()

# Creating the game start variable
game_start = True

# Game loop
while game_start:
    # Setting the screen sleep
    time.sleep(sleep_time)
    # Setting the traffic movement
    traffic.move_traffic()
    # Updating the screen
    screen.update()

    # Game over boolean evaluation
    if traffic.touch(turtleRunner.get_turtle_runner()):
        game_start = False
        game_board_status.game_over()
        break

    # Level up evaluation
    if turtleRunner.get_turtle_runner().ycor() >= 280:
        game_board_status.level_up()
        turtleRunner.reset_position()
        traffic.level_up_traffic()

# Closing the screen on muse click
screen.exitonclick()
