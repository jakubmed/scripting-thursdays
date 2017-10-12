#!/usr/bin/env python
import sys

print("Enter numbers")
inp=input()
list=inp.split()
for i in range(len(list)):
        list[i]=int(list[i])
new_list=sorted(list)
print(*new_list,sep='\n')
print("Maximum je",new_list[-1])
print("Minimum je",new_list[0])
