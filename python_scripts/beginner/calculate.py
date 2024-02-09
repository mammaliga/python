def calculate(message="The result is", **kwargs):	
	if kwargs["operation"] == "add":
		result = kwargs.get("first", 0) + kwargs.get("second", 0)
	elif kwargs["operation"] == "multiply":
		result = kwargs.get("first", 0) * kwargs.get("second", 1)
	elif kwargs["operation"] == "divide":
		result = kwargs.get("first", 0) / kwargs.get("second", 1)
	elif kwargs["operation"] == "subtract":
		result = kwargs.get("first", 0) - kwargs.get("second", 0)

	if not kwargs.get("make_float"):
		return f"{message} {int(result)}"
	return f"{message} {result}"

print(calculate(make_float=False, message="your product is", operation="multiply", first=8))	

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"