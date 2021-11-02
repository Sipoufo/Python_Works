# from turtle import Turtle, Screen

# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("red","green")
# my_turtle.forward(300)

# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable() 
table.add_column("Pokemon Name", ["Pikaku","Squirite","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align = "l"
print(table)