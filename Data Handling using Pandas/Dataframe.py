import pandas as pd
df = pd.DataFrame()
name = pd.Series(['Rohit Sharma','Virat Kohli','MS Dhoni'])
team = pd.Series(['MI','RCB','CSK'])
dic = {'Name':name,'Team':team}
df = pd.DataFrame(dic)
print(df)
