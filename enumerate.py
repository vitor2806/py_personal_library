# -*- coding: utf-8 -*-

import enum


localist = ['cat', 'dog', 'whale']

# will print values
for animal in localist:
    print(animal)
print('')

# will print index + values
for animal in range(len(localist)):
    print(animal, localist[animal])
print('')

# this is the equivalent of previous code
for index, animal in enumerate(localist):
    print(index, animal)