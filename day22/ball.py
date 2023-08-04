from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        '''initializing ball physical properties'''
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        # randomizing ball direction to increase difficulty
        self.x_move = random.randint(7, 13)
        self.y_move = random.randint(7, 13)
        self.move_speed = 0.1

    def move(self):
        '''initializing ball movement animation'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def y_bounce(self):
        '''called when ball collides with wall'''
        self.y_move *= -1
    
    def x_bounce(self):
        '''called when ball collides with paddle'''
        self.x_move *= -1
        # increases speed to increase difficulty
        self.move_speed *= 0.9
        
    def reset(self):
        '''called when player scores; resets game state and reverses ball direction'''
        self.home()
        self.x_move *= -1
        self.move_speed = 0.1
        self.move()

