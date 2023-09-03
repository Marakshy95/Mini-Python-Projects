from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")



is_on = True

while is_on == True:
    screen.update()
    ball.ball_movement()
    time.sleep(0.01)
    ball.wall_mechanics()

    for segment in paddle.segments:
        if segment.distance(ball) < 20:
            ball.setheading(0)
            ball.random_direction()
    for segment in paddle.enemy_segments:
        if segment.distance(ball) < 20:
            ball.setheading(180)
            ball.random_direction()

    for segment in paddle.enemy_segments:
        segment.sety(ball.ycor())

    if ball.xcor() > 590:
        ball.refresh()
        scoreboard.add_score()
    elif ball.xcor() < -590:
        ball.refresh()
        scoreboard.add_enemy_score()

screen.exitonclick()