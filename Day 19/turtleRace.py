import turtle as t, random

is_race_on = False
colors = ["green", "red", "violet", "blue", "pink", "orange"]
screen_width = 500
screen_height = 400
turtles = []
good_color = False
t.speed("slowest")

screen = t.Screen()
# Use for init a screen
screen.setup(screen_width, screen_height)

screen.listen()
turtle_position = [-60, -20, 20, 60]
all_turtle = []
for i in range(4):
    turtle = t.Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    # Use for move a turtle with X and Y
    turtle.goto(-230, turtle_position[i])
    all_turtle.append(turtle)

while not good_color:
    user_color = screen.textinput("Make your bet", "Which turtle will win the race? choose your good color [green, red, violet, blue]")
    for color in colors:
        if user_color == color:
            good_color = True
            
if good_color:
    while not is_race_on:
        for turtle_t in all_turtle:
            distance =  turtle_t.forward(random.randint(0, 20))
            if turtle_t.xcor() > 230:
                # Use for take a turtle color
                win_color = turtle_t.pencolor()
                if win_color == user_color:
                    print(f"You have won")
                    break
                else:
                    print("You haven't won")
                    is_race_on = True
                    break

screen.exitonclick()