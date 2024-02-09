def copy(f1, f2):
	with open(f1) as orig:
		read = orig.read()

	with open(f2, "w") as copy:
		write = copy.write(read[::-1])
		print(write)



print(copy('text.txt', 'text_copy.txt')) # None
# expect the contents of story.txt and story_copy.txt to be the same