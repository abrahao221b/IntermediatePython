import pandas

# Reading the CSV file with PANDAS
data = pandas.read_csv("weather_data.csv")

# Printing the data type of "data"
# print(type(data))

# Printing the second column of the CSV file
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# print(sum(data_list)/len(data_list))

# Printing the average with PANDAS
# print(data["temp"].mean())

# Printing the max value with PANDAS
# print(data["temp"].max())

# Another way of printing the columns using PANDAS
# print(data.condition)

# Printing the row
# print(data[data.day == "Monday"])

# Printing the day that has the biggest temperature
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

monday_temp_fahrenheit = (9*monday.temp) / 5 + 32


# Creating a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")