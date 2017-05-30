#!/usr/bin/env python3
from numpy import histogram as hist
import matplotlib.pyplot as plt

############################################
imp_file = "spectrum"
hist_bin = 0.05
############################################

#reading the imput file
with open (imp_file, "r") as f:
   dataset = []
   for line in f:
      num = float(line)
      dataset.append(num)

#making histogram with 500 bins (a tuple is created)
h = hist(dataset, bins=500, range=None, normed=False, weights=None, density=None)

print(h[1])

new_file = 'histogram.dat'

print(len(h[1]))

#plt.plot(h[0],h[1])
#plt.show()

with open(new_file,'w') as f:
   f.write(dataset)



