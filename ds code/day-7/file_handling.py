import pandas as pd

import openpyxl
import numpy as np
import seaborn as  sns

df = sns.load_dataset('titanic')
df.to_excel('titanic.xlsx', index=False)
df.to_csv('titanic.csv', index=False)

df =pd.read_csv('titanic.csv')
print(df.head())