import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
df = pd.DataFrame([tips])
fg = seaborn.FacetGrid(df,col = 'time',row = "sex")
fg = fg.map(plt.hist,"tip", color  = "tomato")