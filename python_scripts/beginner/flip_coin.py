from random import choice

def flip_coin():
	coin = choice(("Heads", "Tails"))
	return coin

coin = flip_coin()
print(coin)