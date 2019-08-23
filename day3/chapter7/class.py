class Car():
	name = 'bmw_x6'
	color = 'red'
	wheels = 4

	def welcome(self):
		print('Welcome to our new car which is ', self.name)

	def car_detail(self):
		result = 'The name of the car is '+self.name+' and the color is '+self.color+' with '+str(self.wheels)+'s'
		return result

bmw = Car()
print(bmw.name)
print(bmw.color)
print(bmw.wheels)
print('ACESSING A METHOD')
bmw.welcome()
print(bmw.car_detail())