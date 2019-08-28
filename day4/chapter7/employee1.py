class Employee():

	pay_raise = 0.10

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

emp1 = Employee('Jack', 'Dorsey', 1000)

print(emp1.email)
print(emp1.full_name())
print(emp1.salary())