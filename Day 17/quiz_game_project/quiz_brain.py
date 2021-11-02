import random


class QuizBrain:

    # Constructor
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.question_answer = ["true", "false"]
        self.score = 0

    # Methode
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        valid_anwser = False
        # print(self.question_list[self.question_number].text)
        while not valid_anwser:
            user_answer = input(
                f"Q.{self.question_number} : {current_question.text} (True/False)?:").lower()
            if user_answer in self.question_answer:
                valid_anwser = True
                self.check_answer(user_answer, current_question.answer)
            else:
                print("Write a valid answer")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}\n")
