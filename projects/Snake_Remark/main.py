import time
from turtle import Screen
from food import Food
from snake import Snake

screen = Screen()
screen_width = 700
screen_height = 700
screen.bgcolor("#CCFF99")
screen.setup(screen_width, screen_height)
screen.title("SnakeGame")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

game_on = True

while game_on:
    if snake.head.distance(food) < 20:
        food.apparition()
        snake.addEndQueue()
    
    if  screen_width / 2 < snake.head.xcor() or -screen_width / 2 > snake.head.xcor() :
        snake.updateXPosition(-snake.head.xcor(), int(snake.head.ycor()))
    
    if  screen_width / 2 < snake.head.ycor() or -screen_width / 2 > snake.head.ycor() :
        snake.updateYPosition(-snake.head.ycor(), int(snake.head.xcor()))

    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()