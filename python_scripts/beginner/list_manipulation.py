def list_manipulation(array, command, location, value=None):
		if command == "remove" and location == "beginning":
			return array.pop(0)
		elif command == "remove" and location == "end":
			return array.pop()
		elif command == "add" and location == "beginning" and value:
			array.insert(0, value)
			return array
		elif command == "add" and location == "end" and value:
			array.append(value)
			return array
		return "Invalid arguments"

print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning")) 
print(list_manipulation([1,2,3], "add", "beginning", 20)) 
print(list_manipulation([1,2,3], "add", "end", 30))