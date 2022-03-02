from turtle import Turtle, goto

class Paddle (Turtle):
    paddle_width = 5
    paddle_len = 1
    initX = 350
    initY = 0
    
    def __init__(self, screen_height, postion):
        super().__init__()
        # Screen size
        self.screen_height = screen_height
        
        # Paddle definition
        self.shape("square")
        self.color("White")
        self.shapesize(self.paddle_width, self.paddle_len)
        self.penup()
        self.goto(postion)
        
    def moveUp(self):
        if self.ycor() < ((self.screen_height / 2) - 50):
            xPosition = self.xcor()
            yPosition = self.ycor() + 20
            self.goto(xPosition, yPosition)
    
    def moveDown(self):
        if self.ycor() > ((-self.screen_height / 2) + 50):
            xPosition = self.xcor()
            yPosition = self.ycor() - 20
            self.goto(xPosition, yPosition)