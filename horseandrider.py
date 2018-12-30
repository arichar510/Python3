class Horse:
	def __init__(self, color, age, rider):
		self.color = color
		self.age = age
		self.rider = rider

class Rider:
	def __init__(self, name):
		self.name = name

wayne = Rider("Wayne")

silver = Horse("silver", "4", wayne)

print(silver.rider.name)