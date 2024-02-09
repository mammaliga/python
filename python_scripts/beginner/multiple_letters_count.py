
def multiple_letter_count(string):
	return {char:string.count(char) for char in string}

print(multiple_letter_count("awesome")) # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

