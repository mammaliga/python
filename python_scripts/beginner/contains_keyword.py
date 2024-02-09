from keyword import iskeyword

def conatins_keyword(*args):
	return any(iskeyword(arg) for arg in args)

