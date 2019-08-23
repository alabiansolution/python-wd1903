class Student():

	school_name = 'Alabian Solutions'
	address = 'No 12, Oluakerele, Balogun'
	color = 'Blue'

	def school_detail(self):
		print('Here are the school detail {}, {} and color of {}'.format(self.school_name, self.address, self.color))



class Employee(Student):
	pass


emp1 = Employee()
print(emp1.school_name)
emp1.school_detail()

	


	