import numpy as np
arr = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print("Order of Array :",arr.shape)

# We can reshape the array
# reshape(row, col)
arr = arr.reshape(12,1)
print(arr)
