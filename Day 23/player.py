from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_To_Start()
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        # self.forward(MOVE_DISTANCE)

    def down():
        pass

    def left():
        pass

    def right():
        pass
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def go_To_Start(self):
        self.goto(STARTING_POSITION)