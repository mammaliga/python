# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0) 
# total_donations = 0

# for v in donations.values():
# 	total_donations += v

# print(total_donations)

# This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# if food in bakery_stock:
# 	print(f"{food}: {bakery_stock.get(food)} left")
# else:
# 	print(f"We do not bake {food}")

# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# initial_game_state = {}.fromkeys(game_properties, 0)
# print(initial_game_state)


# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# stock_list = inventory.copy()
# stock_list["cookie"] = 18
# stock_list.pop("cake")
# print(stock_list)