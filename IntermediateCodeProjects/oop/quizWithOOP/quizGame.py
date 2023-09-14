import random
from quizRepository import questions


class Quiz:
    def __init__(self):
        self.questions = questions

    def initializing_question(self):
        for question in self.questions:
            question["picked"] = False

    def verifying_questions(self):
        total = 0
        for question in self.questions:
            if question["picked"]:
                total += 1
        if total == 10:
            return True
        return False

    def shuffle_question(self):
        while True:
            index = random.randint(0, 9)
            if not self.questions[index]["picked"]:
                self.questions[index]["picked"] = True
                return self.questions[index]["question"], self.questions[index]["answer"]
