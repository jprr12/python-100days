# quiz game project

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# list containing the questions
question_bank = []
# loop to iterate through the question data
for i in question_data:
    question_txt = i['question']
    question_answer = i['correct_answer']
    new_question = Question(question_txt, question_answer)
    question_bank.append(new_question)
# program will start the quiz
quiz = QuizBrain(question_bank)
# continue asking questions until every question in list is asked
while quiz.still_has_question():
    quiz.next_question()

print("Well done!")
print(f"Your final score: {quiz.score}/{quiz.question_num}")

