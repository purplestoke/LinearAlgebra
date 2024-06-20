import numpy as np


v1 = np.array([2, 3, 4, 5])
v2 = np.array([1, 0, 5, 7])

# DOT PRODUCT 
dp = np.dot(v1, v2)


# DISTRIBUTIVE PROPERTY OF DOT PRODUCT (SCALARS DISTRIBUTE INSIDE PARENTHESIS)
# NOT ENTIRELY ASSOCIATIVE (ABILITY TO MOVE THE PARENTHESIS)
scalar = 5
#print(scalar * (np.dot(v1, v2)))
#print(np.dot(scalar*v1, v2))

# CAUCHY-SCHWARZ INEQUALITY (UPPER BOUND FOR THE DOT PRODUCT)
# |v1 * v2| <= ||v1|| ||v2||

# GEOMETRIC REPRESENTATION OF DOT PRODUCT 
# v1 * v2 = |v1||v2|cos(theta)

# theta = cos^-1 ((v1 * v2)/ |v1||v2|)

# SIGN OF DOT PRODUCT TELLS US INFO ABOUT THE ANGLE
# If dot is +, the angle is acute
# If dot is -, the angle is obtuse
# If dot is 0, we have a right angle (Orthogonal)
# If theta is 0 or 180, we have a collinear relationship (vectors are on the same line)




