# more turtle graphics, GUIs, importing modules
import random

from turtle import Turtle as T, Screen as S
# activate turtle pointer
t = T()
# activate turtle GUI
screen = S()
# initializing turtle characteristics
t.shape('arrow')
t.color('midnight blue')
# t.speed(3)
# t.pensize(10)

# movement
# t.forward(30)

# =====================================
# # turtle challenge 1 - draw a square
# for i in range(4):
#     t.forward(100)
#     t.left(90)

# =====================================
# # turtle challenge 2 - draw a dashed line
# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# =====================================
# # turtle challenge 3 - drawing different shapes
# colors = ['black', 'red', 'blue', 'yellow', 'chartreuse', 'magenta', 'dark violet', 'silver']
# sides = 3
# while sides < 11:
#     for _ in range(sides):
#         angle = 360 / sides
#         t.forward(40)
#         t.right(angle)
#     sides += 1
#     t.pencolor(random.choice(colors))

# =====================================
# # turtle challenge 4 - generate a random turtle walk
# directions = [0, 90, 180, 270]
# colors = ['black', 'red', 'blue', 'yellow', 'chartreuse', 'magenta', 'dark violet', 'silver']
# for _ in range(200):
#     t.color(random.choice(colors))
#     t.forward(40)
#     t.setheading(random.choice(directions))

# =====================================
# # tuples, how to generate random RGB colors
# # set colormode to use rgb
# screen.colormode(255)
# # randomizing rgb colors
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     # pencolor() function to use rgb tuple
#     t.pencolor(random_color())
#     t.forward(random.randint(20, 40))
#     t.setheading(random.choice(directions))

# =====================================
# turtle challenge 5 - draw a spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spiro(size):
    for _ in range(int(360 / size)):
        t.color(random_color())
        t.circle(50)
        t.setheading(t.heading() + size)
    return

screen.colormode(255)
t.speed(0)

draw_spiro(10)

# exit turtle GUI on click
screen.exitonclick()

