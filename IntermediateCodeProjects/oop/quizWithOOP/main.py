from quizGame import Quiz
from quizRepository import logo
import os


def main():
    play = True
    while play:
        logo()
        choice = input("Do you want to play a quiz game? (y / n): ").lower()
        if choice == "y":
            # os.system("clear")
            quiz = Quiz()
            quiz.initializing_question()
            score = 0
            user_score = 0
            while not quiz.verifying_questions():
                question, answer = quiz.shuffle_question()
                user_answer = input(f"{question} (True/False): ").lower()
                score += 1
                if user_answer == answer:
                    print("You got it right!")
                    user_score += 1
                else:
                    print("That's wrong.")
                print(f"The correct answer was: {answer}")
                print(f"Your current score is: {user_score}/{score}")
        else:
            break


main()
