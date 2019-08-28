# Create a class called Bicycle list out the possible 
# class properties of this Bicycle, create a method
# that will display the details of this Bicycle, create a 
# method that will convert the weight in Kilogram
# (kg) to pounds (lbs) and another method that will 
# convert pounds to kilogram make sure that
# weights are floats and rounded accordingly you 
# can check the python documentation for some
# these functions. Where 1 kg = 2.20462 lbs
# a. Create an instance of this class
# b. Call the diiferent methods in this class


class Bicycle():

	wheels = 2
	color = 'Black'
	name = 'Mazda'

	def kg_pounds(self, kg):
		kilo = 2.20462 * kg
		result = round(kilo, 2)
		return str(result)+'lbs'

	def pounds_kg(self, pounds):
		pnd = pounds/2.20462
		result = round(pnd, 2)
		return str(result)+'kg'

	def detail(self):
		print('The name of the Bicycle is {} with the color of {} and {} wheels'.format(self.name, self.color, self.wheels))

b1 = Bicycle()

print(b1.kg_pounds(300))
print(b1.pounds_kg(300))






