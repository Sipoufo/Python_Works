from turtle import Turtle, Screen

pointer = Turtle()

for i in range(0,4):
    pointer.right(90)
    pointer.forward(200)

screen = Screen()
screen.exitonclick()