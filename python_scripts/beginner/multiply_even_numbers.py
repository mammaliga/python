# def multiply_even_numbers(collection):
# 	for num in collection:
		
def multiply_even_numbers(arr):
	product = 1
	for num in arr:
		if num % 2 == 0:
			product *= num
	return product

print(multiply_even_numbers([2,3,4,5,6])) # 48
print(multiply_even_numbers([1,2,3,2,2,5,12,8,4,5,4,3,56,43,38])) # 48
