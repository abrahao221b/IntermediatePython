class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        position = self.question_number
        position -= 1
        current_question = self.question_list[position]
        print(f"Category: {current_question.category}")
        print(f"Difficulty: {current_question.difficulty}")
        user_answer = input(f"Q{self.question_number}: "
                            f"{current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, position)

    def check_answer(self, user_answer, position):
        question = self.question_list[position]
        if user_answer == question.answer.lower():
            self.user_score += 1
            print("You got it right!")
            print(f"The correct answer was: {question.answer}")
            print(f"Your current score is: {self.user_score}"
                  f"/{self.question_number}\n")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {question.answer}")
            print(f"Your current score is: {self.user_score}"
                  f"/{self.question_number}\n")
