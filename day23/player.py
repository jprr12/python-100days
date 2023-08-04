STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        '''turtle properties'''
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.setheading(90)
        self.penup()
        self.reset()
    
    # movement
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    # resets turtle position
    def reset(self):
        self.goto(STARTING_POSITION)

