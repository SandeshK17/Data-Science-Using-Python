import pandas as pd
l = [{'Name':'Sachin','Surname':'Tendulkar'},{'Name':'Virat','Surname':'Kohli'},{'Name':'Hardik','Surname':'Pandya'}]
df = pd.DataFrame(l)
print(df)

for(row_index,row_value) in df.iterrows():
    print("\n Column index is :",row_index)
    print("\n Column Value is :",row_value)

for(col_index,col_value) in df.iterrows():
    print("\n Row index is :",col_index)
    print("\n Row Value is :",col_value)