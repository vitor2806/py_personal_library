# -*- coding: utf-8 -*-

x = 2

while x < 10:
	print("X = ", x)
	x += 1

arr1 = [1, 2, 3, 4, 5]
arr2 = ["Hello", "World", "!"]
arr3 = arr1 + arr2

print("")
for i in arr3:
	print("Valor = ", i)

print("")
# range(start, end, step)
for i in range(20, 10, -2):
	print(i)