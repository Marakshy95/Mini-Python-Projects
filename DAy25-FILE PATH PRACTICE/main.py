import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

#to read all data
data = pandas.read_csv("50_states.csv")

#to get all states info in a list
all_states_list = data.state.to_list()

# to get a specific state information line!
state_info = data[data.state == "Iowa"]  #<<< important



# get to a row 

for (index, row) in data.iterrows():       #<<< even morfe important
    if row.student == "angela":
        print(row.score)




# is_on = True
# while is_on:
#     
#     for state in questiona.data_dict["State"]:
#         questiona.increment += 1
#         print(questiona.increment)
#         if answer_state.lower() == state.lower():
#             questiona.add_state(int(questiona.increment))
#             score.increase_score()
#             continue










screen.exitonclick()