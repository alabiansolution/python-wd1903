def add_range(start, stop=20):
	start = 1
	total = 0

	while start <= stop:
		total += start
		start += 1
	print(total)

states = {
	'Imo':'Owerri',
	'Abia':'Umuahia',
	'Enugu':'Enugu',
	'Jigawa':'Dutse',
}

class Employee():
	'''
	This class have a couple of things
	That we cannot explain
	'''
	pay_raise = 0.10

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay
		self.form_email = last_name+'.'+first_name+'@'+'company.com'
		self.email = self.form_email.lower()


	def full_name(self):
		print(self.first_name, self.last_name)

	def salary(self):
		increment = self.pay*self.pay_raise
		salary = increment+self.pay
		return salary 

