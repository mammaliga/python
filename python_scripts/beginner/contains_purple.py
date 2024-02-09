def contains_purple(*args):
	if "Purple" in args:
		return True
	return False

print(contains_purple(25, "Purple"))  #True

print(contains_purple("green", False, 37, "blue", "hello world"))   #False

print(contains_purple("purple"))   #True

print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))   #True

print(contains_purple(1,2,3))  #False