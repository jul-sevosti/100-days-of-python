from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x= 0, y = 280)
        self.hideturtle()

    def refresh(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=('Arial', 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 12, "normal"))