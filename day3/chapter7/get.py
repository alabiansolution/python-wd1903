class Student():
	def __init__(self, name):
		self.name = name
		self.marks = []
		print('Welcome {} to school'.format(self.name))

	def add_marks(self, mark):
		self.marks.append(mark)

	def get_avg(self):
		return sum(self.marks)/len(self.marks)


student1 = Student('Benedict')
student1.add_marks(60)
student1.add_marks(70)
student1.add_marks(80)
print(student1.get_avg())
