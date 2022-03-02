from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        randX = random.randint(-280, 280)
        randY = random.randint(-280, 280)
        self.goto(randX, randY)