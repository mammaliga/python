def current_beat():
	beats = ("1", "2", "3", "4")
	while True:
		for beat in beats:
			yield beat

beat = current_beat()

