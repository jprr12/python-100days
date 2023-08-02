from turtle import Turtle as T

SB_ALIGN = 'center'
SB_FONT = ('Arial', 21, 'normal')

class Scoreboard(T):
    def __init__(self):
        '''initialize scoreboard properties'''
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        '''specific scoreboard property'''
        self.write(f"Score: {self.score}", align = SB_ALIGN, font = SB_FONT)

    def increase_score(self):
        '''call method to update scoreboard and increase score'''
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        '''call when snake collided with wall/tail'''
        self.goto(0,0)
        self.write("GAME OVER", align=SB_ALIGN, font=SB_FONT)

