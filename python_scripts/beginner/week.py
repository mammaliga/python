def week():
    week = ["monday", "tuesday",
            "wednesday", "thursday", "friday", "saturday", "sunday", ]
    for day in week:
       yield day


day = week()

try:
	print(next(day))
except StopIteration:
	break