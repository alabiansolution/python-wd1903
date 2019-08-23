# Write a program in python that will print the lowest number among three numbers supplied

num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
num3 = int(input('Enter number3: '))


if num1 < num2 and num1 < num3:
	print(num1, 'is less than ',num2,'and ',num3)
elif num2 < num1 and num2 < num3:
	print(num2, 'is less than ',num1,'and ',num3)
elif num3 < num1 and num3 < num2:
	print(num3, 'is less than ',num1,'and ',num2)