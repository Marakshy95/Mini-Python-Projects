from turtle import Turtle


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.goto(0, -380)
        self.setheading(90)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(0, -380)

    def increase_size(self):
        self.shapesize(2,2)