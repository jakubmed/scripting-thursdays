#!/usr/bin/env python
from __future__ import division
import math
import sys
import matplotlib.pyplot as plt
import numpy as np

list=[int(elem) for elem in '4 3 1'.split()]
new_list=sorted(list)
print(*new_list,sep='\n')
print("Maximum je",new_list[-1])
print("Minimum je",new_list[0])
