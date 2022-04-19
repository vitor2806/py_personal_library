# -*- coding: utf-8 -*-
#relational operators
x = 2
y = 3.5

print("X equal to Y?", x == y)
print("X diff to Y?", x != y)
print("X less than Y?", x < y)
print("X great than Y?", x > y)
print("X less or equal to Y?", x <= y)
print("X great or equal to Y?", x >= y)
print("X plus Y equals to 5?", x + y == 5)

#logical operators

print("")
print("X equals to Y and X equals to X + Y?",
	x == y and x == x + y)
print("X differs to Y and X + Y equals to 5.5?",
	x != y and x + y == 5.5)
print("X equals to Y or X + Y equals to 5.5?",
	x == y or x + y == 5.5)