
# -*- coding: utf-8 -*-

x = [1, 2, 3, 4, 5]
y = [] # fill y with each element in x ** 2

for element in x:
    y.append(element ** 2)

print('X = ', x)
print('Y = ', y)

# Condense that to one line using list comprehension

# first example

x = [1, 2, 3, 4, 5]
y = [(element ** 2) for element in x]

print('\nX = ', x)
print('Y = ', y)

# second example

x = [1, 2, 3, 4, 5]
y = [(element ** 2) for element in x]
z = [element for element in x if (element % 2 == 1)] # add an element to z if x[element] mod 2 == 1
