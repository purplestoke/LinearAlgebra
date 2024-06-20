import numpy as np

# ONLY WORKS WITH VECTORS OF 3RD DIMENSIONALITY

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

cp = np.cross(v1, v2)

print(cp)
