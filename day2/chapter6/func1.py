
def say_hello():
	print('Hello my people')

say_hello()

def say_hi(name):
	print('Hi mr', name)

say_hi('Benedict')
say_hi('Alabi')
say_hi('Ope')

# My name is Benedict, I am 40years old and I am Fair in complexion

def person(name, age, complexion):
	print('My name is ',name,'I am ',str(age),'years old and I am ',complexion,'in complexion')


person('Benedict', 40, 'Fair')
person('Alabi', 50, 'Dark')

def add(num1, num2):
	sum = num1 + num2
	print(sum)


add(20, 50)
add(30, 10)

def office(name, color='Yellow'):
	print('The name of my office is ', name, 'and the color is ', color)

office('MTN')
office('Alabian', 'Blue')

def add_range(start, stop=20):
	start = 1
	total = 0

	while start <= stop:
		total += start
		start += 1
	print(total)

add_range(5)
add_range(1, 30)
