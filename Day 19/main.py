import turtle as t

my_turtle = t.Turtle()

def moveFoward():
    my_turtle.forward(50)

screen = t.Screen()
screen.listen()
screen.onkey(moveFoward, "space")
screen.exitonclick()