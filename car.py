# Create a class called  Car.  
class Car(object):
# In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage.
	def __init__(self, price=None, speed=None, fuel=None, mileage=None):
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 
		print "Running init"
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = .15
		else:
			self.tax= .12

	def displayInfo(self):
		print "Running displayInfo"
		print "Price: ", self.price
		print "Speed: ", self.speed
		print "Fuel: ", self.fuel
		print "Miles: ", self.mileage
		print "Tax: ", self.tax
# Create five different instances of the class Car.
car_one = Car()
car_two = Car()
car_three = Car()
car_four = Car()
car_five = Car()
 # In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

