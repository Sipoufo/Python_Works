import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard

screen = Screen()
screen_width = 800
screen_height = 600
game_On = True

screen.setup(screen_width, screen_height)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

# Creation of object
# Paddle
Right_paddle = Paddle(screen_height, (350, 0))
Left_Paddle = Paddle(screen_height, (-350, 0))
# ball
ball = Ball()
# Score
score = ScoreBoard()

screen.listen()
screen.onkey(Right_paddle.moveUp, "Up")
screen.onkey(Right_paddle.moveDown, "Down")
screen.onkey(Left_Paddle.moveUp, "z")
screen.onkey(Left_Paddle.moveDown, "s")

while game_On :
    screen.update()
    time.sleep(ball.moveSpeed)
    ball.move()
    
    if ball.ycor() > ((screen_height/2) - 20) or ball.ycor() < (-(screen_height/2) + 20) :
        ball.bounceY()
    
    if ball.distance(Right_paddle) < 52 and ball.xcor() > 320 or ball.distance(Left_Paddle) < 52 and ball.xcor() < -320:
        ball.bounceX()
    
    if ball.xcor() > 380:
        ball.restBallPosition()
        score.addLeftScore()
    
    elif ball.xcor() < -380:
        ball.restBallPosition()
        score.addRightScore()
    
screen.exitonclick()