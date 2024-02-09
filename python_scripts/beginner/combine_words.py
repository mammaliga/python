def combine_words(string, **kwargs):
	if "prefix" in kwargs.keys():
		return kwargs["prefix"] + string
	elif "suffix" in kwargs.keys():
		return string + kwargs["suffix"]
	return string


print(combine_words("child"))  #'child'

print(combine_words("child", prefix="man"))  #'manchild'

print(combine_words("child", suffix="ish"))  #'childish'

print(combine_words("work", suffix="er"))  #'worker'

print(combine_words("work", prefix="home"))  #'homework'


