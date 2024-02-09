
def single_letter_count(string, char):
	if not type(string) == str or not type(char) == str:
		return "Invalid arguments"
	return string.lower().count(char)


print(single_letter_count("Hello World", "h")) # 1
print(single_letter_count("Hello World", "z")) # 0
print(single_letter_count("HelLo World", "l")) # 3
print(single_letter_count(234234, 3)) # 3
