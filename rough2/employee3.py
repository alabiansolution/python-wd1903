class Employee():
	pay_raise = 0.20

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay
		self.form_email = last_name+'.'+first_name+'@'+'company.com'
		self.email = self.form_email.lower()


	def full_name(self):
		return self.first_name+' '+self.last_name

	def salary(self):
		increment = self.pay*self.pay_raise
		salary = increment+self.pay
		print(salary)

class Developer(Employee):

	def __init__(self, first_name, last_name, pay, prog_lang):
		super().__init__(first_name, last_name, pay)
		self.prog_lang = prog_lang 

d1 = Developer('John', 'Doe', 2000, 'Python')
d2 = Developer('James', 'Wick', 4000, 'Java')
d3 = Developer('Peter', 'Pan', 6000, 'PHP')

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

	def print_emp(self):
		print('Here are list of employee')
		for emp in self.employee:
			print(emp.full_name())


m1 = Manager('Alabi', 'Adebayo', 3000, 'PHP', [])

m1.add_emp(d1)
m1.add_emp(d2)
m1.add_emp(d3)
m1.print_emp()




