# def max_magnitude(lst):
# 	return max(abs(num) for num in lst)
# 	# return max(list(map(lambda num: abs(num), lst)))

# print(max_magnitude([300, 20, -900]))
# print(max_magnitude([-5, -1, -89]))
# print(max_magnitude([10, 11, 12]))

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["nigyar", "kulebjaka", "jake"]

zipped = list(zip(midterms, finals))


final_grades = {max(pair) for pair in zipped}
print(final_grades)
