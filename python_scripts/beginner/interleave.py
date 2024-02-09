def interleave(str1, str2):
	return "".join("".join(pair) for pair in zip(str1, str2))


print(interleave('hi','ha'))    # 'hhia'

print(interleave('aaa', 'zzz'))  # 'azazaz'

print(interleave('lzr','iad')) #  'lizard'

# str1 = "lzr"
# str2 = "iad"

# zipped = list(zip(str1, str2))

# word = ["".join(pair) for pair in zipped]

# print("".join(word))