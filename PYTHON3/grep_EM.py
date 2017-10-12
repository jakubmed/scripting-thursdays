#!/usr/bin/env python
import sys
import re,collections

myfile=open('jmena','r')
table = []

for line in myfile:
    contents = line.strip().split(':')
    table.append(contents)

#print(table)
dictionary = {}
for line in table:
    for jmeno in line:
        if jmeno in dictionary:
            dictionary[jmeno] += 1
        else:
            dictionary[jmeno] = 1

for jmeno, occurences in dictionary.items():
    print(jmeno, ':', occurences)
