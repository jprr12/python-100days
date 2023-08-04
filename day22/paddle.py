from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        '''initializing paddle physical properties'''
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    
    # paddle movement
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

