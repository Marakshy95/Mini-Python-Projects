import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

from soaal import Question
from score import Scoreboard
data = pandas.read_csv("50_states.csv")

questiona = Question()
score = Scoreboard()


state_list = data["state"].to_list()
xpos_list = data["x"].to_list()
ypos_list = data["y"].to_list()

for state in state_list:
    questiona.data_dict["State"].append(state)
for x in xpos_list:
    questiona.data_dict["Positionx"].append(x)
for y in ypos_list:
    questiona.data_dict["Positiony"].append(y)



is_on = True
while is_on:
    questiona.clear()
    answer_state = screen.textinput(title="Guess a state name", prompt="Whats another state name?")
    for state in questiona.data_dict["State"]:
        questiona.increment += 1
        print(questiona.increment)
        if answer_state.lower() == state.lower():
            questiona.add_state(int(questiona.increment))
            score.increase_score()
            continue










screen.exitonclick()