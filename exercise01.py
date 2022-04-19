# -*- coding: utf-8 -*-
import math

# 01
def checkAge(age):
	if (age >= 18):
		print('Allowed')
	elif (age > 0 and age < 18):
		print('Not Allowed')
	else:
		print('Invalid age')

age = int(input("Insert your age: "))
checkAge(age)

# 02

def checkGrade(grade):
	if (grade >= 6.0):
		return ('Good job')
	else:
		return ('Try next year')

def calcAvg(grade1, grade2):
	return ((grade1 + grade2/2))

first_grade = float(input("Insert your first grade: "))
second_grade = float(input("Insert your second grad: "))
result = calcAvg(first_grade, second_grade)
result = checkGrade(result)
print(result)

# 04 

arr = [3, 4, 2]
arr.sort()
print('Sorted by lesser array: ', arr)

# 05

print('Insert two numbers then a signal: ')
y = float(input('First number: '))
x = float(input('Second number: '))
signal = input('Signal: ')

if (signal == '+'):
	result = y + x
elif (signal == '-'):
	result = y - x
else:
	print('Invalid signal')

print(result)