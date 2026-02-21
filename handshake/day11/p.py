#Extract single column from 2D array.
import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
column=arr[:,1]
print("extracted column",column)