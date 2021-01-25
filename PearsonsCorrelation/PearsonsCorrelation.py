import os
import numpy as np
from scipy.stats import pearsonr

dir_path = os.getcwd()

print("Pearson's Correlation Coefficient Equation: Covariance(X, Y) / (Standard Deviation of X * Standard Deviation of Y)")
print("Ensure data1.set & data2.set has correct values in program directory {1 2 3 4 5}")

d1 = np.loadtxt(dir_path + '\\data1.set')
d2 = np.loadtxt(dir_path + '\\data2.set')


pCorrelation, _ = pearsonr(d1, d2)

if pCorrelation > 0.5:
    print("Significant Positive Correlation Found: %.3f" % pCorrelation)
else:
    if pCorrelation < -0.5:
        print("Significant Negative Correlation Found: %.3f" % pCorrelation)
    else:
        print("No Significant Correlation Found: %.3f" % pCorrelation)