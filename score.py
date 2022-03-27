# ((width // 2) - 20) > round(self.xcor()),
# ((-width / 2) + 20) < round(self.xcor()),

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(300)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_p1} - {self.score_p2}", align="center", font=("Arial", 40, "normal"))

    def new_score_p1(self):
        self.score_p1 += 1
        self.update_score()

    def new_score_p2(self):
        self.score_p2 += 1
        self.update_score()