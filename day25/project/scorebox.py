from turtle import Turtle as T
from turtle import Screen
screen = Screen()

class Scorebox(T):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.hideturtle()
    
    def show_state(self, state, x, y):
        self.goto(x, y)
        self.write(state)
    def update_score(self):
        self.score += 1

