class Vehicle:
	def __init__(self, name, speed, direction):
		self.speed = speed
		self.direction = direction
		self.name = name
		
		
		
	def print_info(self):
		print("Vehicle Info:")
		print("  Name: " +str(self.name))
		print("  Speed: "+ str(self.speed))
		print("  Direction: "+(self.direction))


class Car(Vehicle):
	def __init__(self, name, speed, direction, mpg, mileage, fuel_level = 0):
		self.speed = speed
		self.direction = direction
		self.name = name
		self.mpg = mpg
		self.fuel_level = fuel_level
		self.mileage = mileage

	def drive(self, distance):
		self.mileage += distance
		self.fuel_level -= (float(distance/self.mpg))
		self.speed = 0
		
	def fill_up(self, gallons):
		self.fuel_level += gallons
	
	def print_info(self):
		print("Vehicle Info:")
		print("  Name: " +str(self.name))
		print("  Speed: "+ str(self.speed))
		print("  Direction: "+ str(self.direction))
		#print ("  Mpg: " + str(self.mpg))
		print("  Fuel level: "+ str(self.fuel_level))
		print("  Milage: "+ str(self.mileage))
		
		
	def xyz(self):
		print("XYZ")
		