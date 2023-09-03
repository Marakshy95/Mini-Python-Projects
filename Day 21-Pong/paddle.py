from turtle import Turtle
from ball import Ball



STARTING_POSITIONS = [(-580, 0), (-580, 20), (-580, 40), (-580, 60)]
ENEMY_POSITIONS = [(580, 0), (580, 20), (580, 40), (580, 60)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

ball = Ball



class Paddle:
    def __init__(self):
        self.segments = []
        self.enemy_segments = []
        self.create_paddle()
        self.create_enemy_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.speed("fast")
            self.segments.append(new_segment)

    def create_enemy_paddle(self):
        for position in ENEMY_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.speed("fast")
            self.enemy_segments.append(new_segment)


    def up(self):
        for segment in self.segments:
            segment.setheading(UP)
            segment.forward(20)

    def down(self):
        for segment in self.segments:
            segment.setheading(DOWN)
            segment.forward(20)

