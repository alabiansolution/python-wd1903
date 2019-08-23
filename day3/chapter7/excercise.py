class Student():

	# Below is an instance variable
	def __init__(self, name):
		self.name = name
		self.mark = []
		print('Welcome {}'.format(self.name))

	def add_mark(self, ma):
		self.mark.append(ma)

	def get_avg(self):
		return sum(self.mark)/len(self.mark)

student1 = Student('Festus')
student1.add_mark(70)
student1.add_mark(80)
student1.add_mark(100)
student1.add_mark(120)

print(student1.get_avg())
	


	