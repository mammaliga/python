

def last_element(list):
	if not list:
		return None
	return list.pop()

print(last_element([1,2,3])) # 3
print(last_element([])) # None