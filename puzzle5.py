# -*- coding: utf-8 -*-
def checkStr(str1, str2):
    return (str1 == str2)

first_sentence = input('Insert a sentence: ')
second_sentence = input('Another one: ')

print("Is these two sentences equals?\n", checkStr(first_sentence, second_sentence))

