# with open("./weather_data.csv", mode='r') as weather_data:
#     data = weather_data.readlines()
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# import pandas
# #
# # data = pandas.read_csv("weather_data.csv")
# # # data_dict = data.to_dict()
# # #
# # # print(data_dict)
# # #
# # # temp_list = data["temp"].tolist()
# # # print(data["temp"].mean())
# # # print(data["temp"].max())
# # #
# # # print(data.condition)
# # #
# # # # get data in row
# # # print(data[data.day == "Monday"])
# #
# # # print(data[data.temp == data["temp"].max()])
# # #
# # # monday = data[data.day == "Monday"]
# # # monday_temp = monday.temp
# # #
# #
# # # create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sqr = len(data[data["Primary Fur Color"] == "Gray"])
red_sqr = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sqr = len(data[data["Primary Fur Color"] == "Black"])
# fur_data = data["Primary Fur Color"]
# gray_sqr = 0
# cinnamon_sqr = 0
# black_sqr = 0
#
#
# for fur in fur_data:
#     if fur == "Gray":
#         gray_sqr += 1
#     elif fur == "Cinnamon":
#         red_sqr += 1
#     elif fur == "Black":
#         black_sqr += 1

fur_dict = {
    "fur": ["gray", "red", "black"],
    "count": [gray_sqr, red_sqr, black_sqr],
}

new_data = pandas.DataFrame(fur_dict)
new_data.to_csv("squirrel_count.csv")