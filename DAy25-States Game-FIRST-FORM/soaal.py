from turtle import Turtle
# from main import data_dict

class Question(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.hideturtle()
        self.increment = -1
        self.data_dict = {
                "State":[],
                "Positionx": [],
                "Positiony": []
            }


    def add_state(self, i):
        self.goto(self.data_dict["Positionx"][i], self.data_dict["Positiony"][i] )
        self.write(self.data_dict["State"][i])
        print(i)
        self.clear()

    def clear(self):
        self.increment = -1