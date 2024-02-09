def sum_even_values(*args):
	return sum(arg for arg in args if arg % 2 == 0)


print(sum_even_values(1,2,3,4,5,6)) # 12
print(sum_even_values(4,2,1,10)) # 16
print(sum_even_values(1, 13, 25)) # 0
