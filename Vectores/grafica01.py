import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(-3, 3, 10)
y = np.linspace(-3, 3, 10)
z = np.linspace(-1, 1, 3)

xmesh, ymesh, zmesh = np.meshgrid(x, y, z)

# Campo vectorial
def F(x, y, z):
    u = x 
    v = -y
    w = z*2
    return np.array([u, v, w])
umesh, vmesh, wmesh = F(xmesh, ymesh, zmesh)

# gráfica
fig = plt.figure('Campo Vectorial')
ax = fig.add_subplot(projection='3d')
#ax.scatter(xmesh, ymesh, zmesh)
ax.quiver(xmesh, ymesh, zmesh,
          umesh, vmesh, wmesh, length = 0.1)

plt.show()