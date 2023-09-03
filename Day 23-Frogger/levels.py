from turtle import Turtle

style = ("Courier", 30)

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.color("white")
        self.penup()
        self.goto(-350,350)
        self.write(f"Level = {self.current_level} ", font = style , align = ("center"))
        self.hideturtle()

    def add_level(self):
        self.current_level += 1
        self.clear()
        self.write(f"Level = {self.current_level} ", font = style , align = ("center")) 

    def game_over(self):
        self.goto(0,0)
        self.write("GG", font = style , align = ("center")) 
