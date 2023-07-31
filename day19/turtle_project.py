# turtle racing project

from turtle import Turtle as T, Screen as screen
import random

# initializing screen, screen dimensions
s = screen()
s.setup(500, 400)

# t1 = T(shape = 'turtle')
# t1.penup()
# t2 = T(shape = 'turtle')
# t2.penup()
# t3 = T(shape = 'turtle')
# t3.penup()
# t4 = T(shape = 'turtle')
# t4.penup()
# t5 = T(shape = 'turtle')
# t5.penup()
# t6 = T(shape = 'turtle')
# t6.penup()

# t1.goto(-230, -166.67)
# t2.goto(-230, -100)
# t3.goto(-230, -33.33)
# t4.goto(-230, 33.33)
# t5.goto(-230, 100)
# t6.goto(-230, 166.67)

# # initializing turtle colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# # turtle list
# turtles = [t1, t2, t3, t4, t5, t6]

# # # assigning colors to turtle
# i = 0
# for t in turtles:
#     t.color(colors[i])
#     i += 1

# turtle list
turtles = []
# shorter code - initializing race turtles, position, shape, color
y_pos = -166.67
for turtle in range (0, 6):
    t = T(shape = 'turtle')
    t.penup()
    t.color(colors[turtle])
    t.goto(x = -230, y = y_pos)
    y_pos += 66.67
    turtles.append(t)

# prompt user to pick a turtle to bet on
user_bet = s.textinput(title = 'Make your bet: ', prompt = 'Which turtle will win the race? Enter a color: ')

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        # check if a turtle reached the finish line
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            # check if user won/lost
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
        # keep the turtle moving until it reaches the finish line
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    



s.exitonclick()

