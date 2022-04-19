# -*- coding: utf-8 -*-

arr1 = [1, 2, 3, 4, 5]
arr2 = ['pine', 'car', 'tree', 'dog', 'cat']

for number, word in zip(arr1, arr2): # for each element in two arrays zip function will concatenate each one
    print(number, word)

arr2 = [2, 3, 4, 5, 6]

for number, base in zip(arr1, arr2):
    print(number + base)

arr3 = zip(arr1, arr2)
arr3 = list(arr3)
print(arr3)

word = ['money', 'beauty', 'pineapple', 'away', 'keyboard']

for x,y,z in zip(arr1, arr2, word):
    print(x + y, z)