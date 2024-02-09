from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.questions:
    quiz.ask_question()
print(f"That's all! Your score is {quiz.checked}/{quiz.count}")
