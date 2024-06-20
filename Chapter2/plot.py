import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 

v = np.array([1, -2, 5])
colV = np.array([[1], [-2], [5]])
rowV = np.array([[1, -2, 5]])
transposedv = colV.T # returns a row vector
plt.plot([0, v[0]], [0, v[1]])
plt.axis([-3, 3, -3, 3])
#plt.show()


v1 = np.array([[2], [6], [-12]])
v2 = np.array([[4], [-5], [10]])

v3 = v1 - v2
v4 = - (v2 - v1)

scalar = 2
v5 = v1*scalar

# CREATE A 3D PLOT
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# PLOT VECTORS
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='b', label='v1')
ax.quiver(0, 0, 0, v5[0], v5[1], v5[2], color='r', label='v5')

# SET THE PLOT LIMITS
ax.set_xlim([min(0, v1[0], v5[0]), max(0, v1[0], v5[0])])
ax.set_ylim([min(0, v1[1], v5[1]), max(0, v1[1], v5[1])])
ax.set_zlim([min(0, v1[2], v5[2]), max(0, v1[2], v5[2])])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.legend()
plt.show()
