import colorgram, random as ran
import turtle as t

t.colormode(255)
my_turtle = t.Turtle()
my_turtle.penup()

rgb_color = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    rgb_color.append((color.rgb.r, color.rgb.g, color.rgb.b))

for i in range(10):
    my_turtle.speed("fastest")
    my_turtle.sety(i * 30)
    for l in range(10):
        my_turtle.speed("slowest")
        my_turtle.setx(l * 30)
        my_turtle.dot(20, ran.choice(rgb_color))
    
screen = t.Screen()
screen.exitonclick()