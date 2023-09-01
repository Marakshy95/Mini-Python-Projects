from turtle import Turtle
from turtle import Screen
from random import randint
import random

turtle_guy = Turtle()
turtle_guy.shape("turtle")
turtle_guy.speed(100)
screen = Screen()
screen.colormode(255)

def draw_square():
    # i=0
    # while i < 4:
    #     turtle_guy.forward(100)
    #     turtle_guy.right(90)
    #     i+=1

    for i in range(4):
        turtle_guy.forward(100)
        turtle_guy.right(90)

def draw_jagged_line():

    for n in range(20):
        turtle_guy.forward(10)
        turtle_guy.penup()
        turtle_guy.forward(10)
        turtle_guy.pendown()
        



def draw_crazy_shapes():
    n = 0
    directions = [0, 90, 180, 270]
    while n < 100:
        for _ in range(100):
            steps = randint(0, 100)
            turtle_guy.setheading(random.choice(directions))
            turtle_guy.forward(steps)
            turtle_guy.pensize(steps)
            turtle_guy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        n += 1



def draw_spyrograph():
    for _ in range(200):       
        turtle_guy.circle(150)
        turtle_guy.forward(30)
        turt_head = turtle_guy.heading()
        turtle_guy.setheading(turt_head + 25)
        turtle_guy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))


draw_spyrograph()






screen.colormode()
screen.exitonclick()


