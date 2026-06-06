import pandas as pd
import numpy as np
arr = np.array([10,30,30,40,10])
index = ['a','b','c','d','e']
print(arr)
s = pd.Series(arr,index)
print(s)

# Finding the number of elements in a series
print("Size of the series :",s.size)


# Finding the average of elements in a series
print("Mean of the series :",s.mean())

# Finding the maximum of elements in a series
print("Maximum Number is :",s.max())

# Finding the minimum of elements in a series
print("Minimum Number is :",s.min())

# Sorting a series
print("Sorted Series :",s.sort_values())

# Displaying unique values in a series
print(s.unique())
print(s.nunique())