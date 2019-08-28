
from package.module import Employee



class Developer(Employee):

	def __init__(self, first_name, last_name, pay, prog_lang):
		super().__init__(first_name, last_name, pay)
		self.prog_lang = prog_lang


d1 = Developer('Adebayo', 'Alabi', 3500, 'PHP')

print(d1.salary())
print(d1.full_name())