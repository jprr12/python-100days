from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        '''initializing scoreboard physical properties'''
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_sb()

    def update_sb(self):
        '''updating scoreboard properties'''
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal') )
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal') )
    
    def l_point(self):
        '''updating left player score'''
        self.l_score += 1
        self.update_sb()
    
    def r_point(self):
        '''updating right player score'''
        self.r_score += 1
        self.update_sb()
    
    def game_over(self, player):
        '''called when player reaches a certain score'''
        self.goto(0, 0)
        self.write(f"GAME OVER! {player.upper()} PLAYER WINS!", align='center', font=('Courier', 20, 'normal'))

