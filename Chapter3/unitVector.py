import numpy as np

v = np.array([2, 5, 4, 7])
vMag = np.linalg.norm(v)
vUnit = v / vMag
print(vMag)
print(vUnit)