def find_and_replace(file_name, search_word, replace_word):
	with open(file_name, "r+") as file:
		text = file.read().split()
		file.write(" ".join([replace_word if word == search_word else word for word in text]))



find_and_replace('text.txt', 'nigga', 'mamaliga')