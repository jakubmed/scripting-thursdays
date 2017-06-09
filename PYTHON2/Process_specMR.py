#!/usr/bin/env python3
import numpy as np
from numpy import histogram as hist
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit

############################################
imp_file = "spectrum"
bin_nums = 500
initial_guess = [51,1,11,25,1,13,15,1,17]
# hint [height1, width1, peak position1,height2, width2, peak position2, height3, width3, peak position3]
############################################

#read the imput file
with open (imp_file, "r") as f:
   dataset = []
   for line in f:
      num = float(line)
      dataset.append(num)

#make histogram with 500 bins (a tuple is created)
h = hist(dataset, bins=bin_nums, range=None, normed=False, weights=None, density=None)

#divide a tuple into separate strings
x = h[1]
xdata = x[:-1]
ydata = h[0]

#plot histogram
plt.plot(xdata, ydata, 'b-', label='data')

#define fitting function: 3 gaussians in this case
def func(x, a1, b1, c1, a2, b2, c2, a3, b3, c3):
    return a1 * np.exp(-b1 * (x - c1)**2) + a2 * np.exp(-b2 * (x - c2)**2) + a3 * np.exp(-b3 * (x - c3)**2)

#define initial guess
guess = np.array(initial_guess,dtype=float)

#curve fitting
popt, pcov = curve_fit(func, xdata, ydata, guess)

print(popt)

#plot the fitting function
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')
plt.show()












#pyasl.instrBroadGaussFast(h[1], h[0], 10000, edgeHandling="firstlast", fullout=True)
#scipy.ndimage.filters.gaussian_filter(input, sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)
