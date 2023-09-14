import pandas

squirrel_dict = {
    "color": [],
    "count": []
}

data_squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

for color in data_squirrel.color:
    has = False
    for squirrel_color in squirrel_dict["color"]:
        if pandas.isna(color) or color == squirrel_color:
            has = True
            break
    if not has:
        squirrel_dict["color"].append(color)

squirrel_dict["color"].reverse()
squirrel_dict["color"].pop()

full_squirrel_dict = {}

for color in squirrel_dict["color"]:
    full_squirrel_dict[color] = 0

for color in data_squirrel.color:
    if color in full_squirrel_dict:
        full_squirrel_dict[color] += 1

for color in squirrel_dict["color"]:
    squirrel_dict["count"].append(full_squirrel_dict[color])


squirrel_dataFrame = pandas.DataFrame(squirrel_dict)
squirrel_dataFrame.to_csv("squirrel_quantity_file")

