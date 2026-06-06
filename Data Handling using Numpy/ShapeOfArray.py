import numpy as np
Arr = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print("Order of Array :",Arr.shape)

#We can reshape the array
# reshape(row, col)
Arr = Arr.reshape(12,1)
print(Arr)