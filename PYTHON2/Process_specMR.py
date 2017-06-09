#!/usr/bin/env python3
import numpy as np
from numpy import histogram as hist
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit

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

x = h[1]
xdata = x[:-1]
ydata = h[0]

plt.plot(xdata, ydata, 'b-', label='data')
#plt.show()

def func(x, a1, b1, c1, a2, b2, c2, a3, b3, c3):
    return a1 * np.exp(-b1 *(x - c1)**2) + a2 * np.exp(-b2 *( x - c2)**2) + a3 * np.exp(-b3 * (x - c3)**2)

popt, pcov = curve_fit(func, xdata, ydata)

#plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')













#pyasl.instrBroadGaussFast(h[1], h[0], 10000, edgeHandling="firstlast", fullout=True)
#scipy.ndimage.filters.gaussian_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)
