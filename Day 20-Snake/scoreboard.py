from turtle import Turtle

style = ("Courier", 30)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.write(f"Score = {self.points} ", font = style , align = ("center"))
        self.hideturtle()

    def add_score(self):
        self.points += 1
        self.clear()
        self.write(f"Score = {self.points} ", font = style , align = ("center"))    

    def game_over(self):
        self.goto(0,0)
        self.write("GG", font = style , align = ("center")) 
