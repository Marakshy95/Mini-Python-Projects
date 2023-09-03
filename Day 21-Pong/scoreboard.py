from turtle import Turtle

style = ("Courier", 30)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.enemy_points = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.write(f"{self.points}   {self.enemy_points} ", font = style , align = ("center"))
        self.hideturtle()

    def add_score(self):
        self.points += 1
        self.clear()
        self.write(f"{self.points}   {self.enemy_points} ", font = style , align = ("center"))

    def add_enemy_score(self):
        self.enemy_points += 1
        self.clear()
        self.write(f"{self.points}    {self.enemy_points} ", font = style , align = ("center"))       
