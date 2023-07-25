class QuizBrain():
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_question(self):
        return self.question_num < len(self.question_list)
    
    # check answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Current score: {self.score}/{self.question_num}")
        

