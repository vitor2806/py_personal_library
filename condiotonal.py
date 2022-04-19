# -*- coding: utf-8 -*-

x = 2
y = 3
z = 4

## x == 2 ? x += y : x += z equals to:
(x := x + y) if (x == 2) else (x := x + z)
print(x)

if(z > y):
	print("x + z = ", x + z)
else:
	print("x + y = ", x + y)

if(z < y):
	print("x + y = ", x + y)
elif(z > y):
	print("x - y = ", x - y)
else:
	print("z + y = ", z + y)