player1 = input("Player 1: ")
player2 = input("Player 2: ")

if player1 and player2:
	if not (player1 == player2):
		if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock"):
			if player1 == "rock":
				print("SHOOT\n Player 1 wins")
			else:
				print("SHOOT\n Player 2 wins")
		elif (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "scissors"):
			if player1 == "scissors":
				print("SHOOT\n Player 1 wins")
			else:
				print("SHOOT\n Player 2 wins")
		elif (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "paper"):
			if player1 == "paper":
				print("SHOOT\n Player 1 wins")
			else:
				print("SHOOT\n Player 2 wins")			
	else:
		print("Draw!")
else:
	print("Something went wrong")


	# stoopid ass boah


