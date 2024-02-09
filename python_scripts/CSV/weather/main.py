import pandas as pd

data = pd.read_csv("weather_data.csv")

temperatures = data["temp"].to_list()
avg_temp = data["temp"].mean()
# print(avg_temp)
max_temp = data["temp"].max()
# print(max_temp)

# print(data[data["day"] == "Tuesday"])
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = (monday_temp * (9/5)) + 32
print(monday_temp_F)
