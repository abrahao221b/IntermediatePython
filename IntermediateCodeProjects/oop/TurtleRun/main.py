from turtle import Screen
from race import Race

picked = input("Choose your player: (red, black, yellow, blue, green): ")
screen = Screen()

new_race = Race()

new_race.set_runners_position()
winner = new_race.start_race()

if picked == winner:
    print("You Win!!!")
else:
    print("You Loose!!!")
    print(f"The winner is: {winner}")

screen.exitonclick()

