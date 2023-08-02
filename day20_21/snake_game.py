# snake game part 1 - creating snake body and movement, controling snake

from turtle import Screen as S
import time
from snake_body import Snake
from food import Food
from scoreboard import Scoreboard

# screen setup
screen = S()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snek")
screen.tracer(0)

# TODO 1: add comments explaining code bits until end of project NOTE: ongoing
# TODO 2: create a Snake class that creates the snake segments NOTE: done
# TODO 3: create a class that controls the snake NOTE: done
# TODO 4: create food and detect collision with it NOTE: done
# TODO 5: create a scoreboard that updates everytime the snake hits a food NOTE: done
# TODO 6: detect collision with wall/tail NOTE: ongoing

# create snake body, food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# initialize snake controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
# initialize snake movement to right when game starts
while game_on:
    # refresh screen for smoother animation transition
    screen.update()
    time.sleep(0.075)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        # remove current food and create another random food
        food.refresh()
        # update score
        scoreboard.increase_score()
        # add length to snake
        snake.extend()
    
    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        game_on = False
        scoreboard.game_over()

    # detect collision with tail
    # looping through all segments (except head, through slicing) to detect collision
    for seg in snake.segments[1:]: # notice the head segment is sliced
        if snake.head.distance(seg) < 15:
            game_on = False
            scoreboard.game_over()

print(f"GAME OVER! Final Score: {scoreboard.score}")

# exit GUI
screen.exitonclick()

