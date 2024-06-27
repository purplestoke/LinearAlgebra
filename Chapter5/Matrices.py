import numpy as np

A = np.array([[3,5,6],
             [0,4,8],
             [12, 6,9]])
# TRANSPOSE WITH .T
At1 = A.T
# TRANSPOSE WITH NP.TRANSPOSE()
At2 = np.transpose(A)
#print(A)
#print(At1)
#print(At2)

# SYMMETRIC MATRIX, THE TRANSPOSE = THE ORIGINAL --------------------------------------
# IF THE TOP RIGHT OF THE MATRIX = THE LOWER LEFT

B = np.array([[1,4,7],
              [4,7,2],
              [7,2,0]])
#print(B, "\n")
#print(B.T)

# SKEW SYMMETRIC MATRIX --------------------------------------
# LOWER TRIANGLE IS THE SIGN FLIPPED OF THE UPPER
# MUST HAVE A DIAGONAL OF 0, B/C 0 = -0
# C = -C^T
C = np.array([[0,1,2],
                [-1,0,3],
                [-2,-3,0]])
#print(C, "\n")
#print(-C.T)

# IDENTITY MATRIX --------------------------------------
I = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

# NUMPY FUNCTIONS FOR SOME MATRICES --------------------------------------
I = np.eye(4)
O = np.ones(4)
Z = np.zeros((4,4))
#print(I)
#print(O)
#print(Z)

# DIAGONAL MATRIX -------------------------
D = np.diag([1,4,6,8])
#print(D)
F = np.array([[3,4,5],
              [0,7,8],
              [2,6,7]])
#print(np.diag(F))

# AUGMENTED MATRIX
# CONCATENATING MATRICES MUST HAVE SAME NUMBER OF ROWS
G = np.array([[3,4,5],
             [1,1,1],
             [0,6,8]])
FG = np.concatenate((F,G), axis=1)
#print(FG)

# TRIANGLE MATRIX, UPPER AND LOWER
T = np.array([[1,2,3],
              [0,2,4],
              [0,0,6]])
#print("This is an Upper Triangle Matrix:\n", T)

# MATRIX ADDITION----------------------
#print(G + T)
# SCALAR-MATRIX MULTIPLCATION------------------
scalar = 2
#print(T*2)


# SHIFTING A MATRIX ---------------------
I = np.eye(4)
A = np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]])
l = .01
As = A + l*I
print(As)
# TRACE OF A MATRIX = SUM OF THE DIAGONAL
print(np.trace(A))