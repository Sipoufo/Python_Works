from turtle import Turtle, Screen
import random

my_turtle = Turtle()
i = 0
size_line = 40
color = ["deep sky blue", "green yellow", "hot pink", "purple", "yellow", "dark gray", "olive drab", "dark goldenrod"]

while i < 5:
    my_turtle.color(random.choice(color))
    for line in range(i+3):
        my_turtle.forward(size_line + 50)
        my_turtle.right(360 / (i + 3))
    i += 1

screen = Screen()
screen.exitonclick()