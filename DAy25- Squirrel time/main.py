import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_list = data["Primary Fur Color"].to_list()

data_dict = {
    "Fur color":["Gray", "Black", "Cinnamon"],
    "Count": []
}

color_list = ["Gray", "Black", "Cinnamon"]

for color in color_list:
    data_dict["Count"].append(data_list.count(color))


df = pandas.DataFrame(data_dict)

df.to_csv("Data squirrel count")


print(data_dict)