# Bad way to read csv files!!
# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

# Good way to read csv files

# It's useful, but has created too many lines of code. It's best to use PANDAS!!
# import csv
#
# with open("weather_data.csv") as file:
#     # Creating a csv object
#     data = csv.reader(file)
#     temperature = []
#
#     # Taking the temperatures
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)
#     # To read the csv object, needs to be loop through it
#     for row in data:
#         print(row)

# Using PANDAS to analyse the data
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data[data.day == "Monday"].condition.any())