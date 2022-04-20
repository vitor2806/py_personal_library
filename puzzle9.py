# -*- coding: utf-8 -*-

name = input('Insert multi-fast file name: ')
archive = open(name)
archive_content = archive.readlines()

fasta = {}

for line in archive_content: #check line by line
    if line[0] == '>': #if line first char is a ">" then
        seq = line[1:].strip() #seq receives line without ">" \n
        fasta[seq] = '' # key 'line' receives ''
    else:
        fasta[seq] = fasta[seq]+line.strip() #if there isnt a ">" on first char, then key 'line' receives last line + line without \n

print(fasta)