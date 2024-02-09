
def extremes(items):
	"""
	>>> extremes([1, 2, 3, 4, 5])
	(1, 5)
	>>> extremes('alcatraz')
	('a', 'z')
	"""
	return (min(items), max(items))

# print(extremes([1,2,3,4,5]))  # (1, 5)

# print(extremes((99,25,30,-7)))  # (-7, 99)

# print(extremes("alcatraz"))  #( 'a', 'z')