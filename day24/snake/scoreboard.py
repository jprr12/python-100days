from turtle import Turtle as T

SB_ALIGN = 'center'
SB_FONT = ('Arial', 21, 'normal')

# file = open('data.txt', 'w+')

class Scoreboard(T):
    def __init__(self):
        '''initialize scoreboard properties'''
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
        # self.high_score = int(high_score)
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        '''specific scoreboard property'''
        self.clear()
        self.write(f"Your Score: {self.score} Highest Score: {self.high_score}", align = SB_ALIGN, font = SB_FONT)

    def increase_score(self):
        '''call method to update scoreboard and increase score'''
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

