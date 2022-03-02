from turtle import Turtle

class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score} High Score = {self.read_Score()}", align= "center", font = ("Arial", 20, "normal"))
        self.hideturtle()

    def read_Score(self):
        with open('data.txt') as file:
            return file.read()

    def write_Score(self, high_Score):
        with open('data.txt', 'w') as file:
            file.write(str(high_Score))

    def update_Screen(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.read_Score()}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.write_Score(self.score)
        self.score = 0
        self.update_Screen()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align= "center", font = ("Arial", 20, "normal"))
        
    def changeScore(self):
        self.score += 1
        self.update_Screen()