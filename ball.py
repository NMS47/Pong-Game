from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(30)
        self.speed(1)

    def turn_left(self):
        self.left(90)
        self.forward(15)

    def turn_right(self):
        self.right(90)
        self.forward(15)

    def move_ball(self, height, width):
        conditions = [
            ((height//2) - 170) > round(self.ycor()),
            ((-height//2) + 170) < round(self.ycor()),
        ]
        if all(conditions):
            self.forward(10)
        elif self.heading() < 90 or 180 < self.heading() < 270:
            self.turn_right()
        else:
            self.turn_left()

    def ball_reset_1(self):
        self.goto(0,0)
        self.setheading(210)

    def ball_reset_2(self):
        self.goto(0,0)
        self.setheading(30)



