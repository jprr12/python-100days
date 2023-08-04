# ping pong game project

# TODO 1: set up main screen NOTE: done
# TODO 2: create 2 paddles that responds to key press NOTE: done
# TODO 3: create ball that moves and bounces on screen NOTE: done
# TODO 4: detecting collision with paddle NOTE: done
# TODO 5: detecting when ball goes out of bounds NOTE: done
# TODO 6: set up scoreboard NOTE: done
# extra TODO: comment on each concepts, block of code that needs explanation

# import turtle and external modules
from turtle import Screen as S
import time
from paddle import Paddle as P
from ball import Ball
from scoreboard import Scoreboard

# essential constants
LP_POS = (-350, 0)
RP_POS = (350, 0)

# setting up main screen
screen = S()
screen.setup(800, 600) # set screen dimensions
screen.bgcolor('black') # set screen background color
screen.title('Ping Pong')
screen.tracer(0) # turns animation off

# # creating paddle no. 1
# # paddle physical properties
# paddle1 = T()
# paddle1.color('white')
# paddle1.penup()
# paddle1.shape('square')
# paddle1.shapesize(stretch_wid=5, stretch_len=1)
# paddle1.goto(350, 0)

# create 2 paddles from Paddle()
l_paddle = P(LP_POS)
r_paddle = P(RP_POS)

# create ball
ball = Ball()

# create scoreboard
score = Scoreboard()

# # paddle movement
# screen.listen()
# def go_up():
#     new_y = paddle1.ycor() + 20
#     paddle1.goto(paddle1.xcor(), new_y)

# def go_down():
#     new_y = paddle1.ycor() - 20
#     paddle1.goto(paddle1.xcor(), new_y)

# paddle movement with Paddle()
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

# game start
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update() # manually update screen if turtle.tracer(0)
    ball.move()

    # detecting collision with top/bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_bounce()

    # detecting collision with paddles
    # NOTE: coudn't quite get the right numbers for a perfect paddle bounce
    if ball.distance(r_paddle) < 40 and ball.xcor() > 330 or ball.distance(l_paddle) < 40 and ball.xcor() < -330:
        ball.x_bounce()
    # scoring the player
    elif ball.xcor() > 380:
        ball.reset()
        score.r_point()
    elif ball.xcor() < -380:
        ball.reset()
        score.l_point()
    
    # detecting game over when player reaches a certain score
    if score.l_score == 5:
        score.game_over("Left")
        game_on = False
    elif score.r_score == 5:
        score.game_over("Right")
        game_on = False

screen.exitonclick()

