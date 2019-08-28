class Employee():
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
		print(salary)

emp1 = Employee('Benedict', 'Uwazie', 2000)
emp1.salary()
print(emp1.email)
