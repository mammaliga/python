class Vehicle:
	def __init__(self, make, model, year):
		self.model = model
		self.year = year

v1 = Vehicle("Honda", "Civic", 2017)
print(v1.make)