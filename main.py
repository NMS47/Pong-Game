import time
from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import ScoreBoard

SCREEN_WIDTH = 1000
SCREEN_HIGHT = 1000


screen = Screen()

ball = Ball()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HIGHT)
screen.title("Pong Game")
screen.tracer(0)
#score = ScoreBoard()

paddle1 = Paddle()
paddle2 = Paddle()
paddle1.setx((-SCREEN_WIDTH/2) + 20)
paddle2.setx((SCREEN_WIDTH/2) - 25)
score = ScoreBoard()

screen.listen()
screen.onkey(paddle1.player_up, "w")
screen.onkey(paddle1.player_down, "s")
screen.onkey(paddle2.player_up, "Up")
screen.onkey(paddle2.player_down, "Down")

game_on = True
speed = 0.1
while game_on:
    screen.update()
    time.sleep(speed)
    ball.move_ball(SCREEN_HIGHT, SCREEN_WIDTH)

    if ball.distance(paddle2) < 50 and ball.xcor() > 460:
        if 90 > ball.heading():
            ball.turn_left()
        else:
            ball.turn_right()
    elif ball.distance(paddle1) < 50 and ball.xcor() < -460:
        if 180 < ball.heading():
            ball.turn_left()
        else:
            ball.turn_right()
    if ball.xcor() > 490:
        score.new_score_p1()
        ball.ball_reset_1()
        if speed < 0.03:
            speed -= 0.02

    elif ball.xcor() < -490:
        score.new_score_p2()
        ball.ball_reset_2()
        if speed < 0.03:
            speed -= 0.02
screen.exitonclick()
