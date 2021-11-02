from turtle import Turtle, Screen

my_turtle = Turtle()
i = 0

# while i <= 20:
#     my_turtle.forward(5)
#     my_turtle.color("white")
#     my_turtle.forward(5)
#     my_turtle.color("black")
#     i += 1

# Order solution
for _ in range(21):
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()

screen = Screen()
screen.exitonclick()
