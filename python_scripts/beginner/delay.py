from functools import wraps
from time import sleep

def delay(time):
	def decorator(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			print(f"The {fn.__name__} function will execute in {time} seconds")
			sleep(time)
			return fn(*args, **kwargs)
		return wrapper
	return decorator

@delay(10)
def say_hi():
    return "hi"

print(say_hi())