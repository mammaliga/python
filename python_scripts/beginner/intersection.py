def intersection(arr1, arr2):
	return [item for item in arr1 if item in arr2]

print(intersection([1,2,3], [2,3,4]))    #[2,3]
print(intersection(['a','b','z'], ['x','y','z']))   # ['z']