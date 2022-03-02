from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_Move = 10
        self.y_Move = 10
        self.moveSpeed = 0.1
    
    def move(self):
        xPosition = self.xcor() + self.x_Move
        yPosition = self.ycor() + self.y_Move
        self.goto(xPosition, yPosition)
    
    def bounceX(self):
        self.x_Move *= -1
    
    def bounceY(self):
        self.y_Move *= -1
        self.moveSpeed *= 0.9
    
    def restBallPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.bounceX()