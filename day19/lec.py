# even more turtle, instances, state and higher order functions
from turtle import Turtle as T, Screen as S

t = T()
screen = S()

# =========================================
# # higher order functions and event listeners

# # function that moves turtle
# def move_forward():
#     t.forward(10)

# # get hold of screen events
# screen.listen()

# # trigger event
# # NOTE: when passing functions as inputs, parenthesis are not included
# # turtle.onkey() is an example of a higher order python function
# screen.onkey(key = 'space', fun = move_forward)

# =========================================
# challenge - make an etch-a-sketch app

screen.listen()

def forward():
    t.forward(10)

def backward():
    t.backward(10)

def counter_clockwise():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def clockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home() 
    t.pendown()

screen.onkeypress(forward, 'w')
screen.onkeypress(backward, 's')
screen.onkeypress(counter_clockwise, 'a')
screen.onkeypress(clockwise, 'd')
screen.onkey(clear, 'c')

# =========================================
# # object state and instances
# a = T() # another instance of T
# b = T() # another instance of T

# =========================================
# understanding the turtle coordinate system
# go to turtle_project.py




# exit
screen.exitonclick()

