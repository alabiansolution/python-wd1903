# Write a program in python that tells if the name you supplied is in a list or the name is not in a list.
supply = input('Enter name: ')
name = supply.capitalize()
president = ['Atiku', 'Buhari', 'Sowore', 'Ezekwesili', 'Fela Durutoye']

if name in president:
	print(name, 'is contesting for President')
elif name not in president:
	print(name, 'is not contesting for President')
	print('Here are the list of contestant')
	for x in president:
		print(x)

