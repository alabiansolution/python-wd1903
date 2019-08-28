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

class Developer(Employee):

	def __init__(self, first_name, last_name, pay, prog_lang):
		super().__init__(first_name, last_name, pay)
		self.prog_lang = prog_lang 

d1 = Developer('John', 'Doe', 2000, 'Python')
print(d1.email)
d1.full_name()
d1.salary()