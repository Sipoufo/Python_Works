import turtle as t
import random

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.pensize(15)
my_turtle.speed("slow")

def random_color():
    ran1 = random.randint(0, 256)
    ran2 = random.randint(0, 256)
    ran3 = random.randint(0, 256)
    return (ran1, ran2, ran3)


# color = ["deep sky blue", "green yellow", "hot pink", "purple", "yellow", "dark gray", "olive drab", "dark goldenrod"]
position = [0, 90, 180, 270]

for _ in range(400):
    my_turtle.pencolor(random_color())
    my_turtle.setheading(random.choice(position))
    my_turtle.forward(32)

screen = t.Screen()
screen.exitonclick()