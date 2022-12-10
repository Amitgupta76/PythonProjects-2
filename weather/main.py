import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# temp_list = data["temp"].to_list()
# print(data["temp"].max())
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# colors = data["Primary Fur Color"]
# count = []
# for color in colors[2:]:
#     count = color.count()
# print(colors)
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(gray)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")