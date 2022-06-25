from question_model import QuestionFormat
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = QuestionFormat(question['text'], question['answer'])
    question_bank.append(new_question)

obj = QuizBrain(question_bank)

while QuizBrain.questions_left(obj):
    user_answer=obj.ask_qn()

