from csv import reader, DictReader

# with open("314 fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")


with open("314 fighters.csv") as file:
    csv_dict = DictReader(file)
    for fighter in csv_dict:
        print(fighter)
