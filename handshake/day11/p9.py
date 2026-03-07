#Multiply two matrices using np.dot().
import numpy as np
A=np.array([
    [1,2,3],
    [4,5,6]

])
B=np.array([
    [12,13,14],
    [14,15,16],
    [17,70,27]
])
multilpy=np.dot(A,B)
print("matrix A:\n",A)
print("matrix B:\n",B)
print("matrix dot product A.B:\n",multilpy)