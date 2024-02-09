class Comment:
	def __init__(self, username, text, likes=0):
		self.username = username
		self.text = text
		self.likes = likes

angela = Comment("angelaYu", "aprreciate it bro", 24)

print(angela.text)