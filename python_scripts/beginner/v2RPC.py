from random import randint 

score1 = 0
score2 = 0
rounds = 1
winning_score = 5
while score1 < winning_score and score2 < winning_score:
	print(f"You: {score1}  Computer: {score2}")
	print(f"Round {rounds}")
	p1 = input("(Choose your move:): ").lower()
	rand = randint(0, 2)
	if p1 == "q" or p1 == "quit":
		break
	if rand == 0:
		p2 = "rock"
	elif rand == 1:
		p2 = "paper"
	else:
		p2 = "scissors"

	if p1 == p2:
		print("It's a tie!")
	elif p1 == "rock":
		if p2 == "scissors":
			print("you win")
			score1 += 1
		else:
			print("computer wins")
			score2 += 1
	elif p1 == "scissors":
		if p2 == "paper":
			print("you win")
			score1 += 1
		else:
			print("computer wins")
			score2 += 1
	elif p1 == "paper":
		if p2 == "rock":
			print("you win")
			score1 += 1
		else:
			print("computer wins")
			score2 += 1
	else:
		print("please enter a valid move")
	rounds += 1
print(f"computer - {score2} \n you - {score1}")