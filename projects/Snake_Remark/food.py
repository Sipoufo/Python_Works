from turtle import Turtle
import random

xMax = 330
yMax = 330

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color("blue")
        self.apparition()

    def apparition(self):
        xrand = random.randint(-xMax, xMax)
        yrand = random.randint(-yMax, yMax)
        self.goto(xrand, yrand)