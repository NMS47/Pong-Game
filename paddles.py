from turtle import Turtle

SCREEN_WIDTH = 1200

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(90)


    def player_up(self):
        if self.ycor() < 271:
            self.forward(20)

    def player_down(self):
        if self.ycor() > -271:
            self.backward(20)

