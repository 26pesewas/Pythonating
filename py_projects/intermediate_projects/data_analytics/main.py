# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp_list = []
#     for row in data:
#         if row[1] != 'temp':
#             temp_list.append(int(row[1]))
#
#     print(temp_list)
import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].tolist()
#
# # maximum value in a series
# print(data["temp"].max())

# print row that has the max temp
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == 'Monday']
#
# monday_temp = monday.temp[0]
# print((monday_temp * 9/5) + 32)


#creating a data frame from scratch
data_dict = {
    "students":["Anna", "Frank", "Tyra"],
    "age": [10,25,40]
}

data = pandas.DataFrame(data_dict)
print(data)

#create a new csv file
data.to_csv("new_data.csv")