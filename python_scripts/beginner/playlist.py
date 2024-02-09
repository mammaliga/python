playlist = []
song = {}.fromkeys(["title", "authors", "duration", "album"], "unknown")
song["authors"] = []
print("Add new song:")
song["title"] = input("title: ")
add_authors = input("authors (press q to go to the next step): ")
while True:
	while add_authors != "q":
		song["authors"].append(add_authors)
		add_authors = input("author: ")
	song["album"] = input("album: ")
	song["duration"] = input("duration: ")
	msg = input("Add another song? (y/n) ")
	if msg == "y":
		song["title"] = input("title: ")
		add_authors = input("authors (press q to go to the next step): ")
		while add_authors != "q":
			song["authors"].append(add_authors)
			add_authors = input("author: ")
		song["album"] = input("album: ")
		song["duration"] = input("duration: ")
		break
	else:
		print(song)
		break
