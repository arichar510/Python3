class Apple:
	def __init__(self, color, weight, age, seeds):
		self.color = color
		self.weight = weight
		self.age = age
		self.seeds = seeds

	def query(self, color, weight, age, seeds):
		color = input("Color? ")
		weight = input("Weight? ")
		age = input("Age? ")
		seeds = input("Seeds? ")

apple1 = Apple("Green", "8 oz", "2 weeks", "Yes")
apple2 = Apple("Red", "12 oz", "4 weeks", "No")
apple3 = Apple("Yellow", "9 oz", "3 days", "Maybe")
apple4 = Apple("Blue", "44 oz", "4 days", "Definitely")

apple1.query()
apple2.query()
apple3.query()
apple4.query()

