# -*- coding: utf-8 -*-

def FASTA(string):
    string = string.upper()
    string = string.replace(" ", "") 
    return ('>HEADER\n' + string)

sequence = input('Insert a sentence: ')
print('\nIn FASTA mode:\n' + FASTA(sequence))
