import pandas
data = pandas.read_csv("squirrells.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
red = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

squirrells_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [len(gray), len(red), len(black)]
}
new_data = pandas.DataFrame(squirrells_dict)
new_csv = new_data.to_csv("squirrel_count.csv")
