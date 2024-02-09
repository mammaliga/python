def is_palindrome(string):
	if "".join(string.lower().split()) == "".join(string[::-1].lower().split()):
		return True
	return False


print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalPanama')) # True
