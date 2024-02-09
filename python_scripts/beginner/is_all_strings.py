
def is_all_strings(lst):
	return all(type(item) == str for item in lst) 


print(is_all_strings(['a', 'b', 'c']))  #True

print(is_all_strings([2,'a', 'b', 'c']))  #False

print(is_all_strings(('hello', 'goodbye')))  #True 