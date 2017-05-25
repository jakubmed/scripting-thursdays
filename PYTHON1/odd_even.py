#!/usr/bin/env python
from __future__ import division
import math
import sys
import matplotlib.pyplot as plt
import numpy as np

print("Zadej cislo:")
cislo=0
#print(cislo)
while True:
    try:
        cislo=int(input())
    except ValueError:
        print("To neni integer!")
        quit()
    else:
        print("V pohode")
        break
mod=cislo%2
#print(mod)
if mod > 0:
    print(cislo,"je liche cislo")
else:
    print(cislo,"je sude cislo")
