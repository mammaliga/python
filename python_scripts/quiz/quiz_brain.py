from random import choice


class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.checked = 0
        self.count = 0

    def random_question(self):
        question = choice(self.questions)
        return question

    def ask_question(self):
        question = self.random_question()
        self.questions.remove(question)
        user_answer = input(f"Q.{self.count+1} {question} (True/False): ")
        if user_answer.lower() == question.answer.lower():
            self.checked += 1
            self.count += 1
            print(f"That's right! {self.checked}/{self.count}")
            print("\n")
        else:
            self.count += 1
            print(f"Wrong answer! {self.checked}/{self.count}")
            print("\n")
