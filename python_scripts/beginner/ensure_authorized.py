from functools import wraps

def ensure_authorized(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs.get("role") and kwargs.get("role") == "admin":
			return fn(*args, **kwargs)
		return "Unauthorized"
	return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody")) # "Unauthorized"
print(show_secrets(a="b")) # "Unauthorized"

