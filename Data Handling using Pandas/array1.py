import pandas as pd
s1 = pd.Series([10.5,20,30,40,50],index=['a','b','c','d','e'])
print(s1['b'])
s3 = s1 + 5
print(s3)