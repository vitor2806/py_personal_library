import math

#calc sqrt root from B²-4AC
def delta(a, b, c):
	return math.sqrt((b ** 2) - (4 * a * c))

#uses delta result to do (-B +- delta)/2A
def bhaskar(a, b, c):
	st_x = (-b + delta(a, b, c))/(2 * a)
	nd_x = (-b - delta(a, b, c))/(2 * a)
	return (st_x, nd_x)

print("Insert a, b and c")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
# get values same order as bhaskar return
try:
	result_st_x, result_nd_x = bhaskar(a, b, c)
	print("X' = ", result_st_x)
	print('X" = ', result_nd_x)
except:
	print('Delta value less than 0')