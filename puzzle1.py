# -*- coding: utf-8 -*-
import random

# ** MY FIRST CODE

'''# Generates a number between 3 and 7
arr_size = random.randint(50, 100)

#Creates an empty array
arr_number = [] 

# Runs from 0 to number generated early
for i in range(0, arr_size):
	# For each position appends a random number into array
	arr_number.append(str(random.randint(5, 19)))

nineteen_count = 0;
five_count = 0;
arr_count = 0
for number in arr_number:
	arr_count += 1;
	if number == '19':
		nineteen_count += 1;
		arr_number[arr_count] = ('*' + number + '*')
	if number == '5':
		five_count += 1;
		arr_number[arr_count] = ('*' + number + '*')
print(arr_number)
if nineteen_count == 2 and five_count >= 3:
	print(True)
else:
	print(False)'''

# ** BETTER ONE

def check(arr):
	return arr.count(19) == 2 and arr.count(5) >= 3

# Generates a number between 3 and 7
arr_size = random.randint(5, 15)

#Creates an empty array
arr_number = [] 

# Runs from 0 to number generated early
for i in range(0, arr_size):
	# For each position appends a random number into array
	arr_number.append(random.randint(0, 19))

print(check(arr_number))
print(arr_number)

