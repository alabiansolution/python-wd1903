class Employee():
	# This is a class variable
	pay_raise = 0.20

	# This is an instance variable
	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay
		self.full_email = self.last_name+'.'+self.first_name+'@'+'company.com'
		self.email = self.full_email.lower()

	def full_name(self):
		return self.first_name+' '+self.last_name

	def salary(self):
		increment = self.pay * self.pay_raise
		salary = self.pay + increment
		return salary


class Developer(Employee):

	def __init__(self, first_name, last_name, pay, prog_lang):
		super().__init__(first_name, last_name, pay)
		self.prog_lang = prog_lang


d1 = Developer('Shugbomi', 'Adewale', 1000, 'PHP')
d2 = Developer('Sam', 'Haruna', 1200, 'Python')
d3 = Developer('Demi', 'Akinwale', 1050, 'JavaScript')

class Manager(Developer):
	def __init__(self, first_name, last_name, pay, prog_lang, employee):
		super().__init__(first_name, last_name, pay, prog_lang)
		if employee is None:
			self.employee = []
		else:
			self.employee = employee

	def add_emp(self, emp):
		if emp not in self.employee:
			self.employee.append(emp)

	def remove_emp(self, emp):
		if emp in self.employee:
			self.employee.remove(emp)

	def show_employee(self):
		for emp in self.employee:
			print(emp.full_name())


m1 = Manager('Benedict', 'Uwazie', 5000, 'Python', [])
print(m1.salary())
m1.add_emp(d1)
m1.add_emp(d2)
m1.add_emp(d3)
m1.remove_emp(d2)
m1.show_employee()

m2 = Manager('Adebayo', 'Alabi', 10000, 'PHP', [d1, d2, d3])
print('Here are the Developers', m2.last_name, 'is Managing')
m2.show_employee()