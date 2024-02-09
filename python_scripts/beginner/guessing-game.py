from random import randint

random_num = randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while True:
	if guess < random_num:
		guess = int(input("Too low. Try again: "))
	elif guess > random_num:
		guess = int(input("Too high. Try again: "))
	else:
		print(f"you won\n the number was {random_num}")
		restart = input("Do want to keep playing? (y/n) ")
		if restart == "y":
			random_num = randint(1, 10)
			guess = int(input("Guess a number between 1 and 10: "))
		elif restart == "n":
			print("Thanks for playing! Bye.")
			break

