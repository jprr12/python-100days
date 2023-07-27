# day 18 project - painting

# import colorgram as C
# colors = C.extract('image.jpg', 30)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)

import random
from turtle import Turtle as T, Screen as S

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

# initializing turtle + GUI
t = T()
t.hideturtle()
t.speed(0)
t.penup()
screen = S()
screen.colormode(255)
# setting initial direction
t.setheading(225)
t.forward(300)
t.setheading(180)
t.forward(30)
t.setheading(0)

dot_num = 100
for i in range(1, dot_num + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)





# exit GUI on click
screen.exitonclick()

