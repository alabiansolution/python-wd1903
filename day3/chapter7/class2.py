class Car():
	name = 'bmw_x6'
	color = 'red'
	wheels = 4

	def welcome(self):
		print('Welcome to our new car which is ', self.name)

	def car_detail(self):
		result = 'The name of the car is '+self.name+' and the color is '+self.color+' with '+str(self.wheels)+'s'
		return result

	def __str__(self):
		return 'This is what you get when you print an Object'

bmw1 = Car()
bmw1.name='Mazda'
bmw1.color='Orange'
print(bmw1.car_detail())
bmw2 = Car()
# print(type(bmw2))
print(bmw2)
