#!/usr/bin/env python
from __future__ import division
import math
import sys
import matplotlib.pyplot as plt
import numpy as np

print("Enter numbers")
inp=input()
list=inp.split()
for i in range(len(list)):
        list[i]=int.list[i]

new_list=sorted(list)
print(*new_list,sep='\n')
print("Maximum je",new_list[-1])
print("Minimum je",new_list[0])
