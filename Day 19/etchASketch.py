import turtle as t

my_turtle = t.Turtle()

def moveFoward():
    my_turtle.forward(20)
def moveBackward():
    my_turtle.backward(20)
def moveCounterClockwise():
    my_turtle.left(10)
def moveClockwise():
    my_turtle.right(20)
def moveClearDrawing():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

screen = t.Screen()
screen.listen()
screen.onkey(moveFoward, "z")
screen.onkey(moveBackward, "s")
screen.onkey(moveCounterClockwise, "q")
screen.onkey(moveClockwise, "d")
screen.onkey(moveClearDrawing, "c")
screen.exitonclick()