class Chicken:
	total_eggs = 0
	def __init__(self, species, name, eggs=0):
		self.species = species
		self.name = name
		self.eggs = eggs

	def __repr__(self):
		return f"{self.name}"	

	def lay_egg(self):
		self.eggs += 1
		Chicken.total_eggs += 1
		return self.eggs

c1 = Chicken("Partridge Silkie", "Alice")
c2 = Chicken("Speckled Sussex", "Amelia")

# print(Chicken.total_eggs)
# print(c1.lay_egg())
# print(Chicken.total_eggs)
# print(c2.lay_egg())
# print(c2.lay_egg())
# print(Chicken.total_eggs)
print(c1)



