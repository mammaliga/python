from functools import wraps

def double_return(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		result = fn(*args, **kwargs)
		return [result, result]
	return wrapper



@double_return 
def add(x, y):
    return x + y
    
print(add(1, 2)) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]