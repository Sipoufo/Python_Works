from turtle import Turtle
import time

start_Position = [(0,0), (-20,0), (-40, 0)]
Move = 20

class Snake(object):
    def __init__(self):
        # super()
        # Turtle square
        self.segments = []
        for position in start_Position:
            self.addSegment(position)
        self.head = self.segments[0]
        
    def addSegment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    
    def extend(self):
        self.addSegment(self.segments[-1].position())

    def move(self) :
        # for seg in segments:
        #     seg.forward(20)
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(Move)
    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)