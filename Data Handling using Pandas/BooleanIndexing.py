# Boolean Indexing in Data Frame
import pandas as pd
dic = {'Name':['sachin','Kohli','Hardik'],'Age':[50,34,29]}
df = pd.DataFrame(dic,index=[True,False,True])
print(df)
print(df.loc[True])
print(df.loc[False])