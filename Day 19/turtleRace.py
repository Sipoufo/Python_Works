import turtle as t, random

colors = ["green", "red", "yellow", "blue"]
screen_width = 500
screen_height = 400
turtles = []
t.speed("slowest")

screen = t.Screen()
screen.setup(screen_width, screen_height)
user_color = screen.textinput("Make your bet", "Which turtle will win the race? choose your color [green, red, yellow, blue, pink]")
screen.listen()
turtle_position = [-120, -40, 40, 120]

for i in range(4):
    turtle = t.Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(-230, turtle_position[i])

screen.exitonclick()