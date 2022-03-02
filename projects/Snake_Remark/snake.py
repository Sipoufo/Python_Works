from turtle import Turtle

speed = "fastest"
snake_size_width = 1
snake_size_height = 1
positions = [(0,0),(-20,0)]

class Snake(Turtle):
    def __init__(self):
        self.parts = []
        for position in positions:
            self.addQueue(position)
        self.head = self.parts[0]

    def addQueue(self, position):
        part = Turtle()
        part.shape("square")
        part.color("#5EAF0E")
        part.penup()
        part.shapesize(snake_size_width, snake_size_height)
        part.goto(position)
        self.parts.append(part)
    
    def addEndQueue(self):
        self.addQueue(self.parts[-1].position())

    def move(self):
        for part in range(len(self.parts)- 1, 0, -1):
            XPosition = self.parts[part - 1].xcor()
            YPosition = self.parts[part - 1].ycor()
            self.parts[part].goto(XPosition, YPosition)
        self.parts[0].forward(20)

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 270 and self.head.heading() != 90:
            self.head.setheading(270)

    def updateYPosition(self, screenY, xPosition):
        self.head.goto(xPosition, screenY)
    
    def updateXPosition(self, screenX, yPosition):
        self.head.goto(screenX, yPosition)