import turtle as t
import random as rm

my_turtle = t.Turtle()
t.colormode(255)

def random_color():
    ran1 = rm.randint(0, 256)
    ran2 = rm.randint(0, 256)
    ran3 = rm.randint(0, 256)
    return (ran1, ran2, ran3)

for _ in range(36):
    my_turtle.speed("fastest")
    my_turtle.color(random_color())
    my_turtle.circle(100)
    my_turtle.speed("slow")
    my_turtle.setheading(my_turtle.heading() + 10)

screen = t.Screen()
screen.exitonclick()