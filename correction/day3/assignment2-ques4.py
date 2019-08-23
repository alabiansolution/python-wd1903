# Write a program that sums all the numbers in a list 10, 20, 30, 40, 70, 200, 300 and also determine
# the average.

numbers = [10, 20, 30, 40, 70, 200, 300]

total = 0

for number in numbers:
	total += number

print('The Total is ', total)
average = total/len(numbers)
print('The Average is ', average)