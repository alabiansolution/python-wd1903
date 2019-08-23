states = ['Imo', 'Enugu', 'Abia', 'Ebonyi', 'Anambra']

for item in states:
	print(item)

# print(range(6))
for x in range(6):
	print(x)

# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# .
# .
# .
# .
# 2 X 12 = 24

for x in range(1, 13):
	print('3 X ',x, ' = ', 3*x)

number = int(input('Enter number: '))

for x in range(1, 13):
	print(number, ' X ',x, ' = ', number*x)

states = {
	'Imo':'Owerri',
	'Abia':'Umuahia',
	'Enugu':'Enugu',
	'Jigawa':'Dutse',
}

for ky in states:
	print(ky)