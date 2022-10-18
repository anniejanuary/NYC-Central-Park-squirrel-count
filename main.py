import pandas

data_pandified = pandas.read_csv("squirrel_data.csv")
fur_color_column = data_pandified["Primary Fur Color"]

count_gray = len(data_pandified[data_pandified["Primary Fur Color"] == "Gray"])
count_red = len(data_pandified[data_pandified["Primary Fur Color"] == "Cinnamon"])
count_black = len(data_pandified[data_pandified["Primary Fur Color"] == "Black"])

color_stats_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [count_gray, count_red, count_black]
}

print(color_stats_dict)

df = pandas.DataFrame(color_stats_dict)
print(df)

df.to_csv("squirrels_count.csv")
