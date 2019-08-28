# Create a multiplication table function using while loop, this function should take 
# three argument the multiplication table number, the start value, the stop value. 
# The start value and stop value should take default values of your choice. 
# It will be done in such a way that when you pass one number the multiplication 
# table of that number will be generated along with the default start and
# stop values. These default start and stop values can also 
# be overwritten when you pass them as an argument when calling the function.


def multiplication(number, start=1, stop=12):
	while start <= stop:
		print(number, ' X ', start, ' = ', number*start)
		start += 1


multiplication(3)
multiplication(4, 5, 15)

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
num3 = int(input('Enter num3: '))

multiplication(num1, num2, num3)