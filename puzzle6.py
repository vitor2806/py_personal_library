# -*- coding: utf-8 -*-

file_name = input('Insert file name: ')

try:
    file_find = open(file_name)
    file_text = file_find.read()
    print(file_text)
    file_find.close()
except:
    print("File doesn't exist")