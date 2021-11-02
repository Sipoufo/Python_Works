from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
i = 0
while i <= 50:
    timmy_the_turtle.forward(10*i)
    timmy_the_turtle.right(90)
    i += 1


screen = Screen()
screen.exitonclick()