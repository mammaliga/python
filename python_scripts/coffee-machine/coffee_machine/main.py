from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while True:
	item = input(f"Choose coffee {menu.get_items()}: ")
	if item == "off":
		break
	elif item == "report":
		coffee.report()
		money.report()
	else:
		drink = menu.find_drink(item)
		if drink and coffee.is_resource_sufficient(drink) and  money.make_payment(drink.cost):
			coffee.make_coffee(drink)