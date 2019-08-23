class Student():

	# Instance variable are below
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color

	def detail(self):
		result='My name is {} and my age is {} and my color is {}'.format(self.name, self.age, self.color)
		return result

print('STUDENT1 DATA')
student1 = Student('Benedict', 22, 'Fair')
print(student1.name)
print(student1.age)
print(student1.color)

print('STUDENT2 DATA')
student2 = Student('Tomiwa', 23, 'Fair')
print(student2.name)
print(student2.age)
print(student2.color)
print(student2.detail())


	