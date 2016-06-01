class Animal(object):
	def __init__(self, name, health=100):
		print "Running init"
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Running displayHealth"
		print "Animal name: ", self.name
		print "Animal health: ", self.health

# animal = Animal("Missy")
# animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)   # use super to call the Animal __init__ method

	def pet(self):
		print "Petting"
		self.health += 5
		return self
dog = Dog("Ginger", 150)
dog.walk().walk().walk().run().run().pet().displayHealth()