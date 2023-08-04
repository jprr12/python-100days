# day 23 - turtle crossing capstone

# import modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# set GUI
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initialize turtle
p = Player()

# initialize cars
car = CarManager()

# initialize scoreboard
score = Scoreboard()

# turtle controls
screen.listen()
screen.onkey(p.go_up, 'Up')

# game start
game_on = True
carspeed = 0.1
while game_on:
    time.sleep(carspeed)
    screen.update()
    # cars start moving when game starts
    car.create_car()
    car.move()

    # collision with finish line
    if p.ycor() > 280:
        # reset turtle position
        p.reset()
        # increase car speed
        carspeed *= 0.5
        # increase scoreboard level
        score.lvl_up()

    # collision with car
    for cars in car.all_cars:
        if p.distance(cars) < 30:
            # game_on = False
            p.reset()
            carspeed = 0.1
            score.lvl_reset()


screen.exitonclick()

