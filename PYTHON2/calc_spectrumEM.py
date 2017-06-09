#!/usr/bin/env python
import math
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x,a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a1*np.exp(-a2*(x-a3)**2)+a4*np.exp(-a5*(x-a6)**2)+a7*np.exp(-a8*(x-a9)**2)

arr=np.loadtxt('spectrum')

histogram=np.histogram(arr,bins=400)
plt.hist(arr,bins=400)
plt.show()

xdata=histogram[1]
ydata=histogram[0]

i=0
while (i < len(xdata)-1):
    print(xdata[i],ydata[i])
    i=i+1

init_vals=[50,1,10,30,1,14,20,1,17]
best_vals,covar=curve_fit(func,xdata,ydata,p0=init_vals,bounds=(0, 40),method=None,jac=None)
print (best_vals)
