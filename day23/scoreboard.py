FONT = ("Courier", 21, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.lv = 1
        self.update_sb()
    
    def update_sb(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Level: {self.lv}", align='center', font=FONT)
    
    def lvl_up(self):
        self.lv += 1
        self.update_sb()
    
    def lvl_reset(self):
        self.lv = 1
        self.update_sb()

