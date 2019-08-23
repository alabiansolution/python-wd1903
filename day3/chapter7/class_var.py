class Student():

	# Below is a class variable
	company = "Alabian Solutions"
	address = 'No 12, Oluakere'

	# Below is an instance variable
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
		print('Your name is {} and age is {} with color {}'.format(self.name, self.age, self.color))

	def common_stuff(self):
		print('Our company name is {} and address is {}'.format(self.company, self.address))


student1 = Student('Vokna', 33, 'Dark')
student1.common_stuff()



	