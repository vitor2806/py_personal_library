# -*- coding: utf-8 -*-

def double(number):
    return number*2

arg = 2
print(double(arg))

arg = [1, 2, 3, 4, 5]
print(double(arg)) # when i do list * 2 its only concatenated

print((map(double, arg))) # when i print a map its only returned it address
double_value = (map(double, arg))
double_value = list(double_value)
print(double_value)

for element in double_value: # to see each element mapped i need to store it on a variable then print it
    print(element)