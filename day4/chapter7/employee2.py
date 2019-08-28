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

# emp1 = Employee('Jack', 'Dorsey', 1000)
# emp2 = Employee('John', 'Doe', 2000)

# print(emp2.pay)
# print(emp2.salary())

class Developer(Employee):

	def __init__(self, first_name, last_name, pay, prog_lang):
		super().__init__(first_name, last_name, pay)
		self.prog_lang = prog_lang


d1 = Developer('Shugbomi', 'Adewale', 1000, 'PHP')
d2 = Developer('Sam', 'Haruna', 1200, 'Python')

print(d2.salary())
print(d2.full_name())