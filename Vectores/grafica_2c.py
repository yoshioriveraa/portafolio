import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative

def f(x):
    return np.cos(x**2) + np.exp(np.sqrt(x))

def df(f, x):
    return derivative(f, x, dx = 1e-8)

print(df(f, 1))




