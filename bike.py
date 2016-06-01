class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		print 'Running init'
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
	def displayInfo(self):
		print "Running displayInfo"
		print "Price: ", self.price
		print "Max Speed: ", self.max_speed
		print "Miles: ", self.miles
	
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
 # have it display "Riding" on the screen and increase the total miles ridden by 10
 	
	def reverse(self):
		print "Reversing"
		if self.mile >= 5:  # What would you do to prevent the instance from having negative miles?
			self.miles -= 5
			return self
# have it display "Reversing" on the screen and decrease the total miles ridden by 5.


# Create 3 instances of the Bike class.
bike_one = Bike(200)
bike_two = Bike(1500)
bike_three = Bike(750)

# Try chaining methods here
bike_one.ride().ride().ride().reverse().displayInfo()

# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
bike_two.ride().ride().reverse().reverse().displayInfo()

bike_three.reverse().reverse().reverse().displayInfo()



