# -*- coding: utf-8 -*-

# reduce = receives a list then return an unique value for it
from functools import reduce

def sum(x, y):
    return x + y

arr = [1, 9, 182, 345, 6] # i want to sum it all

# not eficient way
sum_value = 0
for number in arr:
    sum_value += number
print(sum_value)

# eficient way
sum_value = reduce(sum, arr)
print(sum_value)
