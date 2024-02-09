def triple_and_filter(*args):
	return tuple(num * 3 for num in args if num % 4 == 0)



# tuple(map(lambda num: num * 3, filter(lambda num: num % 4 == 0, args)))
# list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

print(triple_and_filter(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))