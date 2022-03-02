from turtle import Screen
import time
from snake import Snake
from food import food
from scoreBoard import scoreBoard

# screen
screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = food()

score = scoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    snake.move()
    
    # Collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.changeScore()
    
    # Collision with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # score.gameOver()
        score.reset()
        snake.reset()
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()