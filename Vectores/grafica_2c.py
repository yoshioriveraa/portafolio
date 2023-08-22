import matplotlib.pyplot as plt
import numpy as np
from pylab import *

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(16 - X*2 - Y*2)
cs = ax.contour(X, Y, Z, 20, cmap = cm.coolwarm)
ax.clabel(cs, fontsize = 6)
plt.colorbar(cs)
plt.show()