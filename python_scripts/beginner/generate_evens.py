def generate_evens(rng):
	return [num for num in range(1,rng) if num % 2 == 0]

print(generate_evens(50))	