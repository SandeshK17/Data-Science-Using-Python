import pandas as pd
dict1 = {'Name':['sachin','Kohli','Hardik'],'Age':[50,34,29]}
df1 = pd.DataFrame(dict1)
dict2 ={'Name':['Rohit','Bumrah','Jadeja'],'Age':[38,34,35]}
df2 = pd.DataFrame(dict2)
df3 = pd.concat([df1,df2])
print("First Dictionary is :",df1)
print("Second Dictionary is :",df2)
print("Dictionary after Concatenation is :",df3)