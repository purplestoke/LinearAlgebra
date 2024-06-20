import numpy as np

v1 = np.array([1, 5, 4, 7])
v2 = np.array([4, 1, 0, 2])

op = np.outer(v1, v2)
print(op)


# ELEMENT WISE VECTOR PRODUCT (OFTEN NOT USED)
v3 = v1 * v2
print(v3)