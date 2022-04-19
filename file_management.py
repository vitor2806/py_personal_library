# -*- coding: utf-8 -*-

"""
r = readonly
w = write (if files already exists it will be deleted then create a new one)
a = create or update a new archive

"""

file = open('test.txt')
print(file)

"""
lines = file.readlines()
print(lines)
"""

unique = file.read()
print(unique)

w = open("test2.txt", "w") #w method
w.write("This is a file")
w.close()

w = open("test.txt", "a")
w.write("This is a file\n")
w.close()
