from turtle import Turtle as T
import random

class Food(T):
    '''create Food() that inherits from Turtle()'''
    def __init__(self):
        '''initialize food attributes'''
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.75, 0.75)
        self.color('red')
        self.speed(0)
        # initialize food position at random area on GUI at game start
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


