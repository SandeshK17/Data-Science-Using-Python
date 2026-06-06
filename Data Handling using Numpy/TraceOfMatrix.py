# Trace of a given matrix is adding the diagonal elements of the matrix
import numpy as np
n = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Given Matrix A is : \n",n)
print("Trace of the given matrix :",n.trace())
print("Trace is also this:",sum(n.diagonal()))
