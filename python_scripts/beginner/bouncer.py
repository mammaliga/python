age = int(input("What is your age? "))

if age:
	if age >= 18 and age <= 21:
		print("entry but with wristband")
	elif age > 21:
		print("normal entry")
	else:
		print("too young")
else:
	print("enter an age!")