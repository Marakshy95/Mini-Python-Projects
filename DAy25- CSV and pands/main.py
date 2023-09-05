# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv


# with open("./weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))
#     print(temperatures)
    
import pandas

data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])


# data_dict = data.to_dict()
# print(data_dict)


# data_list = data["temp"].to_list()
# print(data_list)



# avg_temp = int(sum(data_list)) / int(len(data_list))
# print(avg_temp)

# avg_temp = data["temp"].mean()
# print(avg_temp)

# max_value = data["temp"].max()
# print(max_value)

# new_max_vlue = data.temp.max()
# print(new_max_vlue)




#going thru rows
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp * (9/5) + 32
# print(monday_temp_f)


#Creating a dataframe from scratch
