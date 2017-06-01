#!/usr/bin/env python3
from numpy import histogram as hist
import matplotlib.pyplot as plt
import scipy

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

#pyasl.instrBroadGaussFast(h[1], h[0], 10000, edgeHandling="firstlast", fullout=True)
scipy.ndimage.filters.gaussian_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)
