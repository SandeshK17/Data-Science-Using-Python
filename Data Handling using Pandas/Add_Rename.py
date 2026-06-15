# Add, Rename and Delete a column
import pandas as pd
s = pd.Series([10,15,20,25])
df = pd.DataFrame(s)
df.columns = ['List 1']
df['List 2'] = 20
df['List 3'] = df['List 1'] + df['List 2']
# del df['List 3']
df.pop('List 3')
print(df)

df1 = df.drop(index=[1],axis=0)
print(df1)
