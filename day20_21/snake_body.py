from turtle import Turtle as T

# initialize snake starting position, movement per instance, direction for setheading()
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        '''initialize starting snake body and movement'''
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''insert snake segments for each starting position'''
        for position in START_POS:
            self.add_segment(position)
    
    def add_segment(self, position):
        '''add a snake segment tied to the snake body'''
        new_segment = T('square')
        new_segment.penup()
        new_segment.color('green')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        '''call when snake collides with food, adds a new segment in front of head'''
        self.add_segment(self.segments[-1].position())
    
    def move(self):
            '''animate snake segments to move to the position of the segment in front'''
            '''head movement excluded (see movement controls below)'''
            for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)

# movement control
# control snake movement while preventing movement to direction opposite of current snake head heading
# only moves the head segment
    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
         if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

