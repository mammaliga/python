menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def is_enough_resources(coffee):
    ingredients = menu.get(coffee).get("ingredients")
    if (resources["water"] - ingredients.get("water") > 0) and (resources["coffee"] - ingredients.get("coffee") > 0) and (resources["milk"] - ingredients.get("milk") > 0):
        return True
    return False

def is_enough_money(coffee, value):
    cost = menu.get(coffee).get("cost")
    if value - cost >= 0:
        return True
    return False

def make_coffee(coffee):
    ingredients = menu.get(coffee).get("ingredients")
    resources["water"] -= ingredients.get("water")
    resources["milk"] -= ingredients.get("milk")
    resources["coffee"] -= ingredients.get("coffee")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources.get('water')}\nMilk: {resources.get('milk')}\nCoffee:{resources.get('coffee')}\nMoney: {money}")
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        if is_enough_resources:
            print("Please insert coins")
            q = float(input("how many quarters? "))
            d = float(input("how many dimes? "))
            n = float(input("how many nickles? "))
            p = float(input("how many pennies? "))
            value = (q * quarters) + (d * dimes) + (n * nickles) + (p * pennies)
        else:
            print("sorry not enough water/milk/coffee")
            if is_enough_money(choice, value):
                money = round(money + value, 2)
                if money > menu.get(choice).get("cost"):
                    print(money)
                    print(menu.get(choice).get('cost'))
                    change = round(money - menu.get(choice).get('cost'), 2)
                    print(f"too much. money here is the change: {change}")
                    money -= change
                    make_coffee(choice)
                    print(f"here is your {choice}. enjoy!")
                else:
                    make_coffee(choice)
                    print(f"here is your {choice}. enjoy!")
            else:
                money = 0
                print("not enough money. money refunded")