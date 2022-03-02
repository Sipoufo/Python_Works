# # with open('./weather_data.csv') as weather:
# #     data = weather.readlines()
# # print(data)
#
# # import csv
# # with open('./weather_data.csv') as weather:
# #     data = csv.reader(weather, delimiter=';')
# #     temperatures = []
# #     i = 0
# #     for row in data:
# #         # print(row)
# #         if i > 0:
# #             temperatures.append(int(row[1]))
# #         i += 1
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv('./weather_data.csv', delimiter=';')
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# # average
# # average = sum(data_list) / len(data_list)
# # print(average )
# average = data["temp"].mean()
# print(average)
#
# # Maximum
# max = data["temp"].max()
# print(max)
#
# # Get Data which had the highest temperature
# print(data[data["temp"] == max])
#
# # condition to a particular day
# monday = data[data["day"] == "Monday"]
# temp = monday["temp"].to_list()
# to_Fahrenheit = (temp[0] * 1.8) + 32
# print(to_Fahrenheit)
#
# # Create dataFrame from scratch
# data_list_new = {
#     "Students" : ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_list_new)
# data.to_csv("new_data.csv")
# print(new_data)
import pandas

central_Park_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = ["Gray", "Cinnamon", "Black"]
new_data = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : []
}

i = 0
for color in colors:
    color_count = central_Park_data[central_Park_data["Primary Fur Color"] == color].count()
    new_data["Count"].append(color_count["Primary Fur Color"])
    i += 1
new_data_frame = pandas.DataFrame(new_data)
new_data_frame.to_csv("./squirrel.count.csv")