from turtle import Turtle
import random



random_y = random.randint(-280, 280)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.goto(0, 0)
        self.setheading(180)
        self.speed("fastest")
        self.ball_movement()
        direction = self.heading()


    def ball_movement(self):
        self.forward(10)

    def random_direction(self):
        guess = random.randint(1,10)
        if guess < 5:
            self.left(30)
        else:
            self.right(30)

    def wall_mechanics(self):
        if self.ycor() > 380:
            new_direction = ( -self.heading())
            self.setheading(new_direction)


        elif self.ycor() < -380:
             new_direction = ( -self.heading())
             self.setheading(new_direction)

    def refresh(self):
        self.goto(0, 0)
        new_direction = (180 -self.heading())
        self.setheading(new_direction)